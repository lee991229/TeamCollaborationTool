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


class ClientApp:
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

    def connect_server(self):
        self.client_socket = socket(AF_INET, SOCK_STREAM)
        self.client_socket.connect(_CONNECT)
        message = f"{f'enter{header_split}접속한다':{BUFFER}}".encode(FORMAT)
        self.client_send_message(message)
        self._connected = True

    def client_send_message(self, message):
        print('메세지 잘보내?', message.split())
        self.client_socket.send(message)

    def client_send_chat_message(self, input_chat):
        team_no = 1
        print('클라우드까지와?')
        message = f"{f'send_chat{header_split}{self.user_no}{list_split_1}{team_no}{list_split_1}{self.user_name}{list_split_1}{input_chat}':{BUFFER}}".encode(
            FORMAT)
        self.client_socket.send(message)

    def client_send_json_message(self, message):
        self.client_socket.send((bytes(message, "UTF-8")))

    def check_server_response(self):
        while self._connected:
            # if not self.client_socket == None:
            try:
                response = self.client_socket.recv(BUFFER).decode(FORMAT).strip()
                # print("메인 레스폰스", response)
                self._parse_packet(response)

            except Exception as e:
                print(e)
                pass

    def _parse_packet(self, p: str):
        parsed = p.split(header_split)
        header = parsed[0].strip()

        if header == 'login':
            result = parsed[1]
            print(result)

            if result == 'False':
                self.client_controller.emit_login('로긴 실패')
            else:
                result = eval(result)
                print(result)
                self.client_controller.emit_login('로긴성공')
                self.user_id, self.username, self.user_pw, self.user_nickname, _, _ = result

        if header == 'duple':
            result = parsed[1]
            if result == 'False':
                self.client_controller.emit_duple(False)
            else:
                self.client_controller.emit_duple(True)
                # self.user_id, self.username, self.user_pw, self.user_nickname = result

        if header == 'insertuser':
            result = parsed[1]
            if result == 'False':
                self.client_controller.emit_insertuser(False)
            else:
                self.client_controller.emit_insertuser(True)
                # self.user_id, self.username, self.user_pw, self.user_nickname = result

        if header == 'recv_chat':
            result = parsed[1]
            result = result.split(list_split_1)
            # print(result)
            for i in result:
                print(i)
            # result = eval(result)
            # print(result, '채팅 받아온거')
            self.client_controller.emit_recv_chat(result)
                # self.user_id, self.username, self.user_pw, self.user_nickname = result
