import json
import sqlite3
import select
from socket import *
from threading import *
from main_code.domain.class_db_connector import DBConnector

from main_code.domain.class_db_connector import DBConnector

# 사용할 구분자
header_split = chr(1)
list_split_1 = chr(2)
list_split_2 = chr(3)


class Server():
    '''
    실습실 소연: 10.10.20.103
    실습실 종혁: 10.10.20.109
    기숙사 독서실 : 192.168.0.88
    '''
    # HOST = '10.10.20.103'#gethostbyname(gethostname())
    HOST = gethostbyname(gethostname())
    PORT = 5050
    BUFFER = 50000
    FORMAT = 'utf-8'

    connected_member = list()

    def __init__(self, db_conn: DBConnector):
        self._serverSocket = socket(AF_INET, SOCK_STREAM)
        self.db_conn = db_conn
        self.server_socket = None
        self.config = None
        self.sockets_list = list()
        self.clients = dict()
        self.thread_for_run = None
        self.run_signal = True

    def start(self):
        if self.thread_for_run is not None:  # 실행중이면 종료 시키기
            return
        self.server_socket = socket(AF_INET, SOCK_STREAM)  # AF_INET(ipv4를 의미)
        self.server_socket.bind((self.HOST, self.PORT))  # 바인딩
        self.server_socket.listen()  # 리슨 시작
        self.sockets_list.clear()  # 소켓리스트 클리어
        self.sockets_list.append(self.server_socket)
        self.run_signal = True
        self.thread_for_run = Thread(target=self.run)
        self.thread_for_run.start()

    def stop(self):
        self.run_signal = False
        if self.thread_for_run is not None:
            self.thread_for_run.join()
        self.server_socket.close()
        self.thread_for_run = None

    def run(self):
        while True:
            if self.run_signal is False:
                break
            try:
                read_sockets, _, exception_sockets = select.select(self.sockets_list, [], self.sockets_list, 0.1)
            except Exception:
                continue
            for notified_socket in read_sockets:
                if notified_socket == self.server_socket:
                    client_socket, client_address = self.server_socket.accept()
                    user = self.receive_message(client_socket)
                    if user is False:
                        continue
                    self.sockets_list.append(client_socket)
                    self.clients[client_socket] = user

                else:
                    message = self.receive_message(notified_socket)
                    if message is False:
                        self.sockets_list.remove(notified_socket)
                        del self.clients[notified_socket]
                        continue

            for notified_socket in exception_sockets:
                self.sockets_list.remove(notified_socket)
                del self.clients[notified_socket]

    def send_message(self, client_socket: socket, result):
        client_socket.send(result)

    def receive_message(self, client_socket: socket):
        try:
            recv_message = client_socket.recv(self.BUFFER)
            decode_msg = recv_message.decode(self.FORMAT).strip()  # recv 메시지
            header = decode_msg.split(header_split)[0]  # recv 메시지의 header
            if header == 'login':  # client에서 유저 id pw를 받아와 db에서 조회후 client에 결과값을 보낸다
                substance = decode_msg.split(header_split)[1]
                data = substance.split(list_split_1)
                id, pw = data
                result = self.db_conn.log_in(id, pw)
                if result is False:  # 아이디와 비밀번호가 없으면 False를 보낸다
                    response_header = f"{f'login{header_split}{False}':{self.BUFFER}}".encode(self.FORMAT)
                    self.send_message(client_socket, response_header)

                else:  # 아이디와 비밀번호가 맞으면 유저정보를 보내준다
                    user_info = json.dumps(result)

                    self.db_conn.insert_login_log(login_id=id) # 로그인 기록 저장

                    response_header = f"{f'login{header_split}{user_info}'}"

                    client_socket.send(bytes(response_header, "UTF-8"))

            elif header == 'duple':  # 회원가입 아이디 중복확인
                substance = decode_msg.split(header_split)[1]
                join_username = substance
                result = self.db_conn.duple_reg_id(join_username) # DB에 연결해 아이디 중복확인
                if result: # 사용 가능한 아이디일 때
                    response_header = f"{f'duple{header_split}{True}':{self.BUFFER}}".encode(self.FORMAT)
                    self.send_message(client_socket, response_header)
                else: # 사용 불가능한 아이디일 때 (중복일 때)
                    response_header = f"{f'duple{header_split}{False}':{self.BUFFER}}".encode(self.FORMAT)
                    self.send_message(client_socket, response_header)

            elif header == 'insertuser':  # 회원가입
                register_user_info = decode_msg.split(header_split)[1]
                register_user_info =eval(register_user_info)
                result = self.db_conn.insert_user(register_user_info)

                if result is True:
                    response_header = f"{f'insertuser{header_split}{True}':{self.BUFFER}}".encode(self.FORMAT)
                    self.send_message(client_socket, response_header)
                elif result is False:
                    response_header = f"{f'insertuser{header_split}{False}':{self.BUFFER}}".encode(self.FORMAT)
                    self.send_message(client_socket, response_header)

            elif header == 'send_chat':  # 채팅 받기
                send_chat = decode_msg.split(header_split)[1] # 데이터 받아오기
                send_chat2 = send_chat.split(list_split_1)
                user_no, team_no, name, chat = send_chat2
                result = self.db_conn.insert_chat_log(user_no, chat)
                response_header = f"{f'recv_chat{header_split}{user_no}{list_split_1}{team_no}{list_split_1}{name}{list_split_1}{chat}'}"   # 헤더만들기

                clients = self.clients.copy()
                for i in clients:
                    try:
                        i.send(bytes(response_header, "UTF-8"))
                    except:
                        continue

            elif header == 'get_notice':  # 공지 client에 보내주기
                recv_msg = decode_msg.split(header_split)[1]
                recv_msg = recv_msg.split(list_split_1)
                user_no, user_nn = recv_msg

                if '관리자' in user_nn:
                    result = self.db_conn.return_notice_all_data()
                else:
                    result = self.db_conn.get_notice_list(user_no)

                result = json.dumps(result)
                response_header = f"{f'recv_get_notice{header_split}{result}'}"
                client_socket.send(bytes(response_header, "UTF-8"))

            elif header == 'get_todolist':  #
                todolist_info = decode_msg.split(header_split)[1] # 데이터 받아오기
                todolist_info = todolist_info.split(list_split_1)
                user_no, team_name = todolist_info
                # 투두 리스트 받아오기
                todo_result = self.db_conn.get_todo_list(user_no)
                # 멤버 받아오기
                member_result = self.db_conn.return_team_members(user_no)
                # 합치기
                result = todo_result ,member_result
                result = json.dumps(result)

                response_header = f"{f'recv_get_todolist{header_split}{result}'}"
                client_socket.send(bytes(response_header, "UTF-8"))

            elif header == 'get_todolist2':  #
                todolist_info = decode_msg.split(header_split)[1] # 데이터 받아오기
                todolist_info = todolist_info.split(list_split_1)
                user_id, user_name, user_no = todolist_info
                # 투두 리스트 받아오기
                result = self.db_conn.get_todo_list(user_no)
                # 합치기
                result = json.dumps(result)
                response_header = f"{f'recv_get_member_todo_list_for_admin{header_split}{result}{list_split_1}{user_id}{list_split_1}{user_name}'}"
                client_socket.send(bytes(response_header, "UTF-8"))

            elif header == 'update_user_message':
                proflie_message = decode_msg.split(header_split)[1]
                proflie_message = proflie_message.split(list_split_1)
                user_no, user_message = proflie_message
                self.db_conn.update_profile_message(user_no, user_message)
                response_header = f"{f'update_user_message{header_split}{user_message}':{self.BUFFER}}".encode(self.FORMAT)
                self.send_message(client_socket, response_header)

            elif header == 'update_todo_checked':
                proflie_message = decode_msg.split(header_split)[1]
                proflie_message = proflie_message.split(list_split_1)
                todo_id, checked = proflie_message
                self.db_conn.update_todo_list(todo_id, int(checked))

            elif header == 'insert_todo':
                proflie_message = decode_msg.split(header_split)[1]
                proflie_message = eval(proflie_message)

                title, contents, user_no = proflie_message
                self.db_conn.insert_todo_list(user_no, title, contents)
                response_header = f"{f'recv_insert_todo{header_split}':{self.BUFFER}}".encode(self.FORMAT)
                self.send_message(client_socket, response_header)

            elif header == 'insert_notice':
                proflie_message = decode_msg.split(header_split)[1]
                proflie_message = eval(proflie_message)
                title, contents, team = proflie_message
                title_no = self.db_conn.return_team_num(team)

                self.db_conn.insert_notice_data(title_no, title, contents)

                response_header = f"{f'recv_insert_notice{header_split}':{self.BUFFER}}".encode(self.FORMAT)
                self.send_message(client_socket, response_header)

            # 팀목록 요청받음
            elif header == 'get_team_name_list':
                result = self.db_conn.return_team_name()
                response_header = f"{f'recv_get_team_name_list{header_split}{result}':{self.BUFFER}}".encode(self.FORMAT)
                self.send_message(client_socket, response_header)

            elif header == 'get_team_name_list2':
                result = self.db_conn.return_team_name()
                response_header = f"{f'recv_get_team_name_list2{header_split}{result}':{self.BUFFER}}".encode(self.FORMAT)
                self.send_message(client_socket, response_header)

            # 팀이름을 인자로 멤버들 받아오기
            elif header == 'get_team_member':
                team_name = decode_msg.split(header_split)[1]
                result = self.db_conn.return_team_members_for_admin(team_name)
                result = json.dumps(result)
                response_header = f"{f'recv_get_team_member{header_split}{result}'}"
                client_socket.send(bytes(response_header, "UTF-8"))

            elif header == 'delete_notice':
                notice_title = decode_msg.split(header_split)[1]
                result = self.db_conn.delete_notice_data(notice_title)

            elif header == 'admin_del_todo_list_send':
                result = decode_msg.split(header_split)[1]
                self.db_conn.delete_todo_data(result)

            elif header == 'admin_todo_checked_send':
                result = decode_msg.split(header_split)[1]
                todo_id, checked = result.split(list_split_1)
                result = self.db_conn.update_todo_list(todo_id, checked)

            # 그래프 만드는 값 보내기
            elif header == 'get_matplotlib':
                result = decode_msg.split(header_split)[1]
                result = self.db_conn.return_todo_list_dict(result)
                result = json.dumps(result)
                response_header = f"{f'get_matplotlib{header_split}{result}'}"
                client_socket.send(bytes(response_header, "UTF-8"))




            elif header == 'admin_todo_list_plus':
                result = decode_msg.split(header_split)[1]
                title, contents, user_id = result.split(list_split_1)
                user_no = self.db_conn.return_user_no(user_id)

                self.db_conn.insert_admin_todo_list(user_no, title, contents)

                result = self.db_conn.return_todo_list_by_title(title)

                result = json.dumps(result)

                response_header = f"{f'recv_get_member_todo_list_for_admin2{header_split}{result}'}"
                client_socket.send(bytes(response_header, "UTF-8"))

            elif header == 'get_chatin_log':
                result = decode_msg.split(header_split)[1]
                user_id = result
                chat_log = self.db_conn.return_chat_log(user_id)
                result = json.dumps(chat_log)

                response_header = f"{f'recv_get_chatin_log{header_split}{result}'}"
                client_socket.send(bytes(response_header, "UTF-8"))



        except:
            pass
