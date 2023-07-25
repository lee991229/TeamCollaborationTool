import json
import sqlite3
import select
from socket import *
from threading import *
from code.domain.class_db_connector import DBConnector

from  code.domain.class_db_connector import DBConnector
# 사용할 구분자
header_split = chr(1)
list_split_1 = chr(2)
list_split_2 = chr(3)


class Server():
    HOST = gethostbyname(gethostname())

    PORT = 5050
    BUFFER = 50000
    FORMAT = 'utf-8'

    connected_member = list()

    def __init__(self, db_conn: DBConnector):
        self._serverSocket = socket(AF_INET, SOCK_STREAM)
        self.db_conn = db_conn
        # print(self.db_conn.log_in('123', '142'))
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
        print(f"Server SENDED: ({result})".split())
        client_socket.send(result)

    def receive_message(self, client_socket: socket):
        try:
            recv_message = client_socket.recv(self.BUFFER)
            decode_msg = recv_message.decode(self.FORMAT).strip() # recv 메시지
            header = decode_msg.split(header_split)[0] # recv 메시지의 header

            if header == 'login':  # client에서 유저 id pw를 받아와 db에서 조회후 client에 결과값을 보낸다
                substance = decode_msg.split(header_split)[1]
                data = substance.split(list_split_1)
                id, pw = data

                print( id, pw, '잘 받니?')
                print(self.db_conn)
                result = self.db_conn.log_in(id, pw) #todo: db에서 아이디 비번 조회
                # result = ['유저 고유번호','유저아이디', '유저닉네임', '유저 이름']
                print('통과?')
                if result is False: # 아이디와 비밀번호가 없으면 False를 보낸다
                    response_header = f"{f'login{header_split}{False}':{self.BUFFER}}".encode(self.FORMAT)
                    self.send_message(client_socket, response_header)

                else: # 아이디와 비밀번호가 맞으면 유저정보를 보내준다
                    user_info = json.dumps(result)
                    response_header = f"{f'login{header_split}{user_info}':{self.BUFFER}}".encode(
                        self.FORMAT)
                    # self.send_message(client_socket, response_header)
                    client_socket.send(bytes(message, "UTF-8"))

            elif header == 'duple': # 회원가입 아이디 중복확인
                substance = decode_msg.split(header_split)[1]
                join_username = substance
                result = self.db_conn.duple_reg_id(join_username)
                if result is True:
                    response_header = f"{f'duple{header_split}{True}':{self.BUFFER}}".encode(self.FORMAT)
                    self.send_message(client_socket, response_header)
                elif result is False:
                    response_header = f"{f'duple{header_split}{False}':{self.BUFFER}}".encode(self.FORMAT)
                    self.send_message(client_socket, response_header)

            elif header == 'insertuser': # 회원가입
                register_user_info = decode_msg.split(header_split)[1]
                result = self.db_conn.insert_user(register_user_info)

                if result is True:
                    response_header = f"{f'insertuser{header_split}{True}':{self.BUFFER}}".encode(self.FORMAT)
                    self.send_message(client_socket, response_header)
                elif result is False:
                    response_header = f"{f'insertuser{header_split}{False}':{self.BUFFER}}".encode(self.FORMAT)
                    self.send_message(client_socket, response_header)
            # elif header == 'duple':
            #     substance = decode_msg.split(header_split)[1]
            #     data = substance.split(list_split_1)
            #     result = self.db_conn.

        except:
            pass