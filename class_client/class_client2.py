from threading import *
from socket import *

# import socket
# _SERVER_IP = '10.10.20.109'
_SERVER_IP = gethostbyname(gethostname())
_SERVER_PORT = 5050
BUFFER = 50000
FORMAT = "utf-8"
_CONNECT = (_SERVER_IP, _SERVER_PORT)

header_split = chr(1)
list_split_1 = chr(2)
list_split_2 = chr(3)


class ClientApp2:
    def __init__(self, client_controller=None):
        super().__init__()
        self.client_controller = client_controller
        self.client_socket = None
        self._connected = None

        self.connect_server()

        self.listeningThread = Thread(target=self.check_server_response, daemon=True)
        self.listeningThread.start()
        # client 로그인 유저 정보 저장
        self.user_no = None
        self.user_id = None
        self.user_name = None
        self.user_pw = None
        self.user_nickname = None
        self.user_message = None
        self.user_create_date = None
        self.user_team = None
        self.team_no = 1
    def connect_server(self):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(_CONNECT)
        message = f"{f'enter{header_split}접속한다':{BUFFER}}".encode(FORMAT)
        self.client_send_message(message)
        self._connected = True

    def client_send_message(self, message):
        self.client_socket.send(message)

    def client_send_chat_message(self, input_chat):
        team_no = 1
        message = f"{f'send_chat{header_split}{self.user_no}{list_split_1}{team_no}{list_split_1}{self.user_name}{list_split_1}{input_chat}':{BUFFER}}".encode(
            FORMAT)
        self.client_socket.send(message)

    def client_send_get_todolist(self):
        message = f"{f'get_todolist{header_split}{self.user_no}{list_split_1}{self.team_no}':{BUFFER}}".encode(
            FORMAT)
        self.client_socket.send(message)

    def client_send_json_message(self, message):
        self.client_socket.send((bytes(message, "UTF-8")))

    def check_server_response(self):
        while self._connected:
            try:
                response = self.client_socket.recv(BUFFER).decode(FORMAT).strip()
                self._parse_packet(response)

            except Exception as e:
                pass

    def _parse_packet(self, p: str):
        parsed = p.split(header_split)
        header = parsed[0].strip()

        if header == 'login':
            result = parsed[1]


            if result == 'False':
                self.client_controller.emit_login(False)
            else:
                result = eval(result)
                result = result[0]
                self.user_no, self.user_name, self.user_id, self.user_pw, self.user_nickname, self.user_message, self.user_create_date, self.user_team = result
                self.client_controller.emit_login(True)

        elif header == 'duple':
            result = parsed[1]
            if result == 'False':
                self.client_controller.emit_duple(False)
            else:
                self.client_controller.emit_duple(True)

        elif header == 'insertuser':
            result = parsed[1]
            if result == 'False':
                self.client_controller.emit_insertuser(False)
            else:
                self.client_controller.emit_insertuser(True)

        if header == 'recv_chat':
            result = parsed[1]
            result = result.split(list_split_1)
            self.client_controller.emit_recv_chat(result)

        elif header == 'recv_get_notice':
            result = parsed[1]
            result = eval(result)
            self.client_controller.emit_recv_get_notice(result)

        elif header == 'recv_get_todolist':
            result = parsed[1]
            result = eval(result)
            self.client_controller.emit_recv_get_todolist(result)

        elif header == 'recv_get_member_todo_list_for_admin':
            result = parsed[1]
            result = result.split(list_split_1)
            todo_list, user_id, user_name = result
            todo_list = eval(todo_list)
            result = todo_list, user_id, user_name
            self.client_controller.emit_member_todo_list_for_admin(result)

        elif header == 'recv_get_member_todo_list_for_admin2':
            result = parsed[1]
            todo_list = eval(result)
            self.client_controller.emit_member_todo_list_for_admin2(todo_list)

        elif header == 'update_user_message':
            result = parsed[1]
            self.user_message = result
            self.client_controller.emit_update_user_message()


        elif header == 'recv_insert_todo':
            result = parsed[1]
            self.client_controller.emit_refresh_todolist()

        elif header == 'recv_insert_notice':
            result = parsed[1]
            self.client_controller.emit_refresh_notice()

        elif header == 'recv_get_team_name_list':
            result = parsed[1]
            result = eval(result)
            self.client_controller.emit_admin_login(result)

        elif header == 'recv_get_team_name_list2':
            result = parsed[1]
            result = eval(result)
            self.client_controller.emit_set_combobox(result)

        elif header == 'recv_get_team_member':
            result = parsed[1]
            result = eval(result)
            self.client_controller.emit_get_team_member(result)

        elif header == 'get_matplotlib':
            result = parsed[1]
            result = eval(result)
            self.client_controller.emit_set_matplotlib(result)

        elif header == 'recv_get_chatin_log':
            result = parsed[1]
            result = eval(result)
            self.client_controller.emit_get_chatin_log(result)
