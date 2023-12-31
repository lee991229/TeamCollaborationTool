# 모듈
import json
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.font_manager as fm
from PyQt5.QtWidgets import QMainWindow, QLayout, QLabel, QPushButton, QLineEdit, QTextEdit, QGraphicsDropShadowEffect, \
    QApplication
from PyQt5.QtCore import Qt, pyqtSignal, QSize, QTimer
from PyQt5.QtGui import QFontDatabase, QIcon, QColor, QPixmap

# UI
from main_code.front.message import YourMsg, MyMsg  # 메세지
# from main_code.front.client_controller import ClientController
from main_code.front.ui.ui_class_notice_board import Ui_NoticeBoard  # 메인 화면
from main_code.front.profile_widget import ProFile  # 프로필 변경
from main_code.front.category_list import CtgList  # 카테고리 리스트
from main_code.front.Warning_dialog import DialogWarning  # 경고창
from main_code.front.Font import Font  # 폰트 클래스
from main_code.front.notice import Notice  # 공지 캐러셀
from main_code.front.todolist import TodoList  # 투두리스트 캐러셀
from main_code.front.notice_dialog import DialogNoticeAdd, DialogToDoAdd  # 공지 다이얼로그, 투두리스트 다이얼로그
from main_code.front.team_process_list import MemberList  # 관리자 창에서 보이는 멤버 리스트 캐럿셀

from main_code.front.admin_todo_edit_dialog import AdminTodoAdd  # 관리자가 개인별 투두리스트 조회 및 추가하는 창

# 전역변수
header_split = chr(1)
list_split_1 = chr(2)
list_split_2 = chr(3)
BUFFER = 50000
FORMAT = "utf-8"


# def character_page_event(img):
#     mywindow2 = AdminTodoAdd(img)  # 캐릭터 버튼 프래스 이밴트 다이얼 로그
#     mywindow2.exec()

class NoticeBorad(QMainWindow, Ui_NoticeBoard):
    # 시그널 선언
    reg_id_lab_signal = pyqtSignal(bool)
    recv_emit_insertuser = pyqtSignal(bool)
    emit_signal_my_chat = pyqtSignal(list)
    emit_signal_chat = pyqtSignal(list)
    recv_login_signal = pyqtSignal(bool)
    recv_get_notice_signal = pyqtSignal(list)
    recv_get_todolist_signal = pyqtSignal(list)
    member_todo_list_for_admin_signal = pyqtSignal(tuple)
    member_todo_list_for_admin_signal2 = pyqtSignal(list)
    refresh_todolist_signal = pyqtSignal()
    refresh_notice_signal = pyqtSignal()
    admin_login_signal = pyqtSignal(list)
    set_combobox_signal = pyqtSignal(list)
    update_user_message_signal = pyqtSignal()
    get_team_member_signal = pyqtSignal(list)
    set_matplotlib_signal = pyqtSignal(list)

    def __init__(self, client_controller):
        super().__init__()
        self.adminadd = None
        self.ctg_clicked = None
        self.user_role = None  # 로그인한 유저의 역할

        self.setupUi(self)
        self.client_controller = client_controller
        self.Warn = DialogWarning()
        self.font = Font()
        self.team_list = None
        self.Notice_add = None
        self.Todo_add = None

        # window frame 설정
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # 변수
        self.init_var()

        # 버튼 트리거 함수 호출
        self.set_btn_trigger()
        self.init_func()

    def create_donut_chart(self, todo_people: list, todo_cnt: list):
        sizes = todo_cnt
        labels = todo_people

        colors = ['#0F9B58', '#0FBC74', '#53B83A', '#3EC56B', '#1AA867', '#0FAF52', '#0FAF6B', '#53AF37']

        # 비율에 따라 도넛 모양으로 그래프 그리기
        plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.4))

        # 도넛 모양으로 그래프 그리기
        centre_circle = plt.Circle((0, 0), 0.70, fc='white')
        fig = plt.gcf()
        fig.gca().add_artist(centre_circle)

        # 모두 동일한 비율로 그리기
        plt.axis('equal')
        plt.tight_layout()

    # 변수
    def init_var(self):
        self.ctg_clicked = None  # 카테고리 버튼 클릭 확인(공지, 투두리스트)
        self.update_timer = QTimer(self)
        self.update_timer.setInterval(10)
        self.vsb = self.chat_scrollarea.verticalScrollBar()

    # widget 이동 함수=======================================================================
    def mousePressEvent(self, event):
        self.client_controller.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        self.client_controller.mouseMoveEvent(self, event)

    # 시그널======================================================================
    def init_func(self):
        """클라이언트 - 서버 받는 시그널"""
        self.reg_id_lab_signal.connect(self.set_reg_id_lab)
        self.recv_emit_insertuser.connect(self.insertuser)
        self.emit_signal_my_chat.connect(self.recv_my_chat)
        self.emit_signal_chat.connect(self.recv_chat)
        self.recv_login_signal.connect(self.login)
        self.recv_get_notice_signal.connect(self.set_notice)
        self.recv_get_todolist_signal.connect(self.set_todolist)
        self.member_todo_list_for_admin_signal.connect(self.show_member_todo_list_for_admin2)
        self.member_todo_list_for_admin_signal2.connect(self.show_member_todo_list_for_admin3)
        self.refresh_todolist_signal.connect(self.get_todolist)
        self.refresh_notice_signal.connect(self.get_notice)
        self.admin_login_signal.connect(self.set_admin_ctg)
        self.update_timer.timeout.connect(self.set_scrollbar)
        self.set_combobox_signal.connect(self.set_combobox)
        self.update_user_message_signal.connect(self.set_user_message)
        self.get_team_member_signal.connect(self.set_team_member)
        self.set_matplotlib_signal.connect(self.set_matplotlib)
        self.update_timer.start()

    def set_main_page_profil(self):
        user_team = self.client_controller.client_app.user_name
        user_name = self.client_controller.client_app.user_team
        self.user_team.setText(user_team)
        self.user_name.setText(user_name)

    def set_user_message(self):
        state = self.client_controller.client_app.user_message
        self.user_state.setText(state)

    def set_scrollbar(self):
        if self.vsb.value() != self.vsb.maximum():
            self.vsb.setValue(self.vsb.maximum())

    def set_btn_trigger(self):
        """UI 버튼 시그널 연결"""

        self.login_btn.clicked.connect(lambda state: self.click_login_btn())  # 로긴 버튼
        self.register_btn.clicked.connect(lambda state: self.click_register_btn())  # 회원가입 화면 이동 버튼
        self.reg_register_btn.clicked.connect(lambda state: self.click_reg_register_btn())  # 회원가입 버튼
        self.send_btn.clicked.connect(lambda state: self.click_send_btn())  # 채팅 전송 버튼
        self.chat_edit.returnPressed.connect(self.click_send_btn)
        self.plus_button.clicked.connect(lambda state: self.click_plus_button())

    def set_font(self):
        """기본 폰트 적용하는 부분"""
        # 로그인 창
        self.login_title_lab.setFont(Font.title(1))
        self.login_id_lab.setFont(Font.text(3))
        self.login_pw_lab.setFont(Font.text(3))
        self.login_id_edit.setFont(Font.text(3, False))
        self.login_pw_edit.setFont(Font.text(3, False))
        self.login_btn.setFont(Font.button(2))
        self.register_btn.setFont(Font.button(2))

        # 회원가입 창
        reg_lab = self.register_page.findChildren(QLabel)
        reg_edit = self.register_page.findChildren(QLineEdit)
        [lab.setFont(Font.text(3)) for lab in reg_lab]
        self.comboBox.setFont(Font.text(3))
        [edit.setFont(Font.text(3, False)) for edit in reg_edit]
        self.reg_title_lab.setFont(Font.title(2))
        self.reg_sub_title.setFont(Font.text(3))
        self.reg_register_btn.setFont(Font.button(1))

        # -- 메인창
        # 프로필창
        profile_lab = self.profile_widget.findChildren(QLabel)
        [lab.setFont(Font.text(3)) for lab in profile_lab]

        # 채팅
        self.chat_edit.setFont(Font.text(2))

        # 관리자 페이지창
        self.team_process_lab.setFont(Font.text(1))
        self.team_todo_label.setFont(Font.text(1))
        self.label.setFont(Font.title(3))

    def ctg_list_show(self):
        """카테고리 넣어주기"""
        self.ctg_dict = {
            '프로필 수정': ['user.png', None],
            '채팅': ['send_black.png', self.chat_page],
            '공지': ['bell.png', self.notice_page],
            '투두리스트': ['heart.png', self.notice_page],
            '로그아웃': ['out.png', self.notice_page]
        }

        self.ctg_list = list(self.ctg_dict.keys())
        self.event_dict = {'채팅': [None, self.pass_, self.plus_button.hide],
                           '공지': [self.notice_v_lay, self.get_notice, self.plus_button.hide],
                           '투두리스트': [self.notice_v_lay, self.get_todolist, self.plus_button.show],
                           '로그아웃': [None, self.logout_, self.plus_button.show],
                           '....': [self.team_mem_v_lay, self.plus_button.hide]

                           }

        for ctg in self.ctg_list:  # 카테고리 이미지, 카테고리 이름 넣어주기
            img_name = self.ctg_dict[ctg][0]
            ctg_ = CtgList(img_name=img_name, c_name=ctg, parent=self, role=self.user_role)
            self.category_v_lay.addWidget(ctg_)

    def pass_(self):
        pass

    def click_plus_button(self):
        actions = {
            '공지': self.Notice_add.exec_,
            '투두리스트': self.Todo_add.exec_
        }
        action = actions.get(self.ctg_clicked)
        if action:
            action()

    def ctg_list_trigger(self, ctg_name):
        """카테고리에 따라 페이지 변경 혹은 창 띄우기"""
        name = self.client_controller.client_app.user_name
        state = self.client_controller.client_app.user_message
        self.ctg_clicked = ctg_name
        for c in self.ctg_list:
            if ctg_name == '프로필 수정':
                img_path = 'user_green.png'
                p_ = ProFile(self, img=img_path, name=name, state=state)
                p_.show_dialog()
                break
            elif ctg_name == c:
                self.clear_layout(self.event_dict[ctg_name][0])  # 레이아웃 비우기
                self.event_dict[ctg_name][1]()
                self.event_dict[ctg_name][2]()
                self.inner_stackedWidget.setCurrentWidget(self.ctg_dict[c][1])

    def admin_ctg_list_show(self, result):
        """카테고리 넣어주기"""
        self.admin_ctg_dict = {
            '프로필 수정': ['user.png', None],
            '채팅': ['send_black.png', self.chat_page],
            '공지': ['bell.png', self.notice_page],
        }
        # 팀카테고리 이미지, 화면 딕셔너리에 저장
        for i in result:
            self.admin_ctg_dict[i] = ['user.png', self.team_page]

        self.admin_ctg_dict['로그아웃'] = ['out.png', self.notice_page]

        self.admin_ctg_list = list(self.admin_ctg_dict.keys())
        self.adminevent_dict = {'채팅': [None, self.pass_, self.plus_button.hide],
                                '공지': [self.notice_v_lay, self.get_notice, self.plus_button.show],
                                '투두리스트': [self.notice_v_lay, self.get_todolist, self.plus_button.show],
                                '로그아웃': [None, self.logout_, self.plus_button.show]
                                }
        # 팀카테고리별 클릭 이벤트 설정
        for i in result:
            self.adminevent_dict[i] = [None, self.get_team_member, self.plus_button.hide]

        for ctg in self.admin_ctg_list:  # 카테고리 이미지, 카테고리 이름 넣어주기
            img_name = self.admin_ctg_dict[ctg][0]
            ctg_ = CtgList(img_name=img_name, c_name=ctg, parent=self, role=self.user_role)
            self.category_v_lay.addWidget(ctg_)

    def logout_(self):
        self.close()
        self.client_controller.re_()
        # self.stackedWidget.setCurrentWidget(self.login_page)

    def admin_ctg_list_trigger(self, ctg_name):
        """카테고리에 따라 페이지 변경 혹은 창 띄우기(관리자)"""
        name = self.client_controller.client_app.user_name
        state = self.client_controller.client_app.user_message

        self.ctg_clicked = ctg_name
        for c in self.admin_ctg_list:
            if ctg_name == '프로필 수정':
                p_ = ProFile(self, img=None, name=name, state=state)
                p_.show_dialog()
                break
            # 클릭한 카테고리의 이름이 팀이름중 하나이면
            if ctg_name in self.team_list:
                self.get_matplotlib(ctg_name)
                self.get_team_member(ctg_name)
                break
            elif ctg_name == c:
                self.clear_layout(self.adminevent_dict[ctg_name][0])  # 레이아웃 비우기
                self.adminevent_dict[ctg_name][1]()
                self.adminevent_dict[ctg_name][2]()
                self.inner_stackedWidget.setCurrentWidget(self.admin_ctg_dict[c][1])

    def get_matplotlib(self, ctg_name):
        message = f"{f'get_matplotlib{header_split}{ctg_name}':{BUFFER}}".encode(
            FORMAT)
        self.client_controller.controller_send_message(message)
        # people, cnt = self.data.return_todo_list_dict('개발부')  # db에서 값 가져오기(서버에서 연결하는 부분으로 추가 예정)

    def set_matplotlib(self, result):
        # 캔버스 만들어서 그래프 그리기
        self.clear_layout(self.v_lay_graph)
        canvas = FigureCanvas(plt.figure())
        self.v_lay_graph.addWidget(canvas)
        people, cnt = result
        self.create_donut_chart(people, cnt)

    def set_admin_ctg(self, result):
        self.admin_ctg_list_show(result)

    def show_member_todo_list_for_admin(self, user_id, user_no, user_name):
        message = f"{f'get_todolist2{header_split}{user_id}{list_split_1}{user_name}{list_split_1}{user_no}':{BUFFER}}".encode(
            FORMAT)
        self.client_controller.controller_send_message(message)

    def show_member_todo_list_for_admin2(self, result):
        self.adminadd = AdminTodoAdd(self, result)
        self.adminadd.exec_()

    def show_member_todo_list_for_admin3(self, result):
        self.adminadd.test(result)

    # 유저 프로필 상메 업데이트
    def update_user_message(self, user_message):
        message = f"{f'update_user_message{header_split}{self.client_controller.client_app.user_no}{list_split_1}{user_message}':{BUFFER}}".encode(
            FORMAT)
        self.client_controller.controller_send_message(message)

    # 레이아웃 비우기
    def clear_layout(self, layout: QLayout):
        """레이아웃 안의 모든 객체를 지웁니다."""
        if layout is None or not layout.count():
            return
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()

            if widget is not None:
                widget.setParent(None)
            # 아이템이 레이아웃일 경우 재귀 호출로 레이아웃 내의 위젯 삭제
            else:
                self.clear_layout(item.layout())

    # 팀 화면============================================
    # 팀이름을 인자로 멤버들 반환요청
    def get_team_member(self, ctg_name):
        self.label.setText(ctg_name)
        message = f"{f'get_team_member{header_split}{ctg_name}':{BUFFER}}".encode(
            FORMAT)
        self.client_controller.controller_send_message(message)

    # 팀원 목록 반환받음
    def set_team_member(self, result):
        self.inner_stackedWidget.setCurrentWidget(self.team_page)
        self.clear_layout(self.team_mem_v_lay)
        members = result
        for i in members:
            user = MemberList(self, i)
            self.team_mem_v_lay.addWidget(user)

    def admin_del_todo_list_send2(self, todo_title):
        message = f"{f'admin_del_todo_list_send{header_split}{todo_title}':{BUFFER}}".encode(
            FORMAT)
        self.client_controller.controller_send_message(message)

    def admin_todo_checked_send2(self, todo_id, checked):
        message = f"{f'admin_todo_checked_send{header_split}{todo_id}{list_split_1}{checked}':{BUFFER}}".encode(
            FORMAT)
        self.client_controller.controller_send_message(message)

    def admin_todo_list_plus2(self, title, contents, user_id):
        message = f"{f'admin_todo_list_plus{header_split}{title}{list_split_1}{contents}{list_split_1}{user_id}':{BUFFER}}".encode(
            FORMAT)
        self.client_controller.controller_send_message(message)
        pass

    # 투루리스트==========================================
    def insert_todo_list(self, title, contents):
        msg = title, contents, self.client_controller.client_app.user_no
        message = f"{f'insert_todo{header_split}{msg}':{BUFFER}}".encode(
            FORMAT)
        self.client_controller.controller_send_message(message)

    def get_todolist(self):
        self.clear_layout(self.notice_v_lay)  # 레이아웃 비우기
        self.client_controller.controller_send_get_todolist()

    def set_todolist(self, result):
        """
        받아온 유저의 투두리스트들을 캐러셀로 만들어 집어넣는다
        :param result:
        :return:
        """
        people_lab = result[1]

        if len(people_lab) == 0:
            people_lab = None
        else:
            pass
        for i in result[0]:
            todo = TodoList(self, i, people_lab, self.user_role)
            self.notice_v_lay.addWidget(todo)

    def send_todo_list_checked(self, todo_id, btn_checked):
        message = f"{f'update_todo_checked{header_split}{todo_id}{list_split_1}{btn_checked}':{BUFFER}}".encode(
            FORMAT)
        self.client_controller.controller_send_message(message)

    # 공지 화면 =====================================================================================
    def insert_notice(self, title, contents, team):
        msg = title, contents, team
        message = f"{f'insert_notice{header_split}{msg}':{BUFFER}}".encode(
            FORMAT)
        self.client_controller.controller_send_message(message)

    def set_notice(self, result):
        for i in result:
            notice = Notice(self, i, self.user_role)
            self.notice_v_lay.addWidget(notice)

    def del_notice(self, title):
        msg = title
        message = f"{f'delete_notice{header_split}{msg}':{BUFFER}}".encode(FORMAT)
        self.client_controller.controller_send_message(message)

    # 공지를 db에요청 함수
    def get_notice(self):
        self.clear_layout(self.notice_v_lay)  # 레이아웃 비우기
        # 유저가 입력한 로그인 정보 encode
        user_no = self.client_controller.client_app.user_no
        user_nn = self.client_controller.client_app.user_nickname
        message = f"{f'get_notice{header_split}{user_no}{list_split_1}{user_nn}':{BUFFER}}".encode(
            FORMAT)
        self.client_controller.controller_send_message(message)

    # window widget show=======================================================================
    def show(self):
        message = f"{f'get_team_name_list2{header_split}':{BUFFER}}".encode(
            FORMAT)
        self.client_controller.controller_send_message(message)
        self.stackedWidget.setCurrentWidget(self.login_page)
        self.inner_stackedWidget.setCurrentWidget(self.chat_page)
        self.set_font()  # 폰트 설정
        self.style_init()  # ui 설정
        super().show()

    def style_init(self):
        # 카테고리 바 그림자 넣기
        self.set_background_color(self.category_bar)

    def set_background_color(self, obj):
        effect = QGraphicsDropShadowEffect()
        effect.setColor(QColor(0, 0, 0, 150))
        effect.setBlurRadius(5)
        effect.setOffset(5, 5)  # 객체와 그림자 사이의 거리 또는 변위
        obj.setGraphicsEffect(effect)

    # 채팅 =========================================================================================
    # 전송버튼 클릭시 채팅을 서버에 보내는 함수
    def get_chat(self):  # 로그인 할때 채팅 기록 불러오기
        user_id = self.client_controller.client_app.user_id
        message = f"{f'get_chatin_log{header_split}{user_id}':{BUFFER}}".encode(
            FORMAT)
        self.client_controller.controller_send_message(message)

    def click_send_btn(self):

        if len(self.chat_edit.text()) >= 1:
            input_chat = self.chat_edit.text()
            self.chat_edit.clear()  # 채팅바 클리어
            self.client_controller.controller_send_chat_message(input_chat)  # 입력된 채팅 client_controller에 보내기

    # 서버에서 채팅 메시지 받는 함수
    def recv_my_chat(self, result):  # 본인이 보낸 메시지라면
        user_no, team_no, name, chat = result
        message_widget = MyMsg(name, chat)
        self.chat_v_lay.addWidget(message_widget)

    def recv_chat(self, result):  # 다른 사람이 보낸 메시지라면
        if len(result) > 2:
            user_no, team_no, name, chat = result
        else:
            name, chat = result
        message_widget = YourMsg(name, chat)
        self.chat_v_lay.addWidget(message_widget)

    # 채팅방 입장시 db에 저장된 채팅 요청
    def send_det_chat(self):
        message = f"{f'get_chat{header_split}{user_input_id}':{BUFFER}}".encode(FORMAT)
        self.client_controller.controller_send_message(message)

    # 로그인 함수=======================================================================
    def click_login_btn(self):
        user_input_id = self.login_id_edit.text()  # 유저가 입력한 id
        user_input_pw = self.login_pw_edit.text()  # 유저가 입력한 pw
        self.login_id_edit.clear()
        self.login_pw_edit.clear()
        # 유저가 입력한 로그인 정보 encode
        message = f"{f'login{header_split}{user_input_id}{list_split_1}{user_input_pw}':{BUFFER}}".encode(
            FORMAT)
        self.client_controller.controller_send_message(message)

    # 로그인 결과 알림 및 화면 전환
    def login(self, result):
        self.user_role = self.client_controller.client_app.user_nickname
        if result:
            if '관리자' in self.client_controller.client_app.user_nickname:
                # db에 있는 팀명 리스트 요청 리스트 받아올때 카테고리 집어넣기
                # 유저가 입력한 로그인 정보 encode
                message = f"{f'get_team_name_list{header_split}':{BUFFER}}".encode(
                    FORMAT)
                self.client_controller.controller_send_message(message)
            else:
                self.ctg_list_show()  # 카테고리 넣어주기

            self.set_main_page_profil()
            self.set_user_message()
            self.get_chat()
            self.Warn.set_dialog_type(bt_cnt=1, t_type='login_cmplt')  # 알림창 띄우기
            self.Warn.show_dialog()
            self.user_role = self.client_controller.client_app.user_nickname
            # self.login_user_role(user_role)
            self.stackedWidget.setCurrentWidget(self.main_page)  # 화면전환
        else:
            self.Warn.set_dialog_type(bt_cnt=1, t_type='loginfailed')  # 알림창 띄우기

    # 회원 가입 함수=======================================================================

    def insertuser(self, result):
        if result:
            self.Warn.set_dialog_type(bt_cnt=1, t_type='register_cmplt')
            self.Warn.show_dialog()
            self.stackedWidget.setCurrentWidget(self.login_page)
        else:
            self.Warn.set_dialog_type(bt_cnt=1, t_type='register_failed')
            self.Warn.show_dialog()

    def set_combobox(self, result):
        self.team_list = result
        self.Notice_add = DialogNoticeAdd(self, self.team_list)
        self.Todo_add = DialogToDoAdd(self, self.team_list)
        for i in result:
            self.comboBox.addItem(i)

    # 회원 가입 화면 으로 이동 하는 함수
    def click_register_btn(self):
        self.stackedWidget.setCurrentWidget(self.register_page)

    # 아이디 중복 검사
    def click_reg_register_btn(self):
        self.send_duple()

    # 아이디 중복검사후 pw name nickname 검사
    def click_reg_register_btn2(self):
        if self.register_check():
            self.register_user()

    # 유저가 입력한 아이디 server에 보내서 중복확인
    def send_duple(self):
        input_reg_id = self.reg_id_edit.text()
        message = f"{f'duple{header_split}{input_reg_id}':{BUFFER}}".encode(
            FORMAT)
        self.client_controller.controller_send_message(message)

    # 조건 충족 회원가입 진행
    def register_user(self):
        input_reg_id = self.reg_id_edit.text()
        input_reg_pw = self.reg_pw_edit.text()
        input_reg_name = self.reg_name_edit.text()
        input_reg_nn = self.reg_nn_edit.text()
        input_reg_team = self.comboBox.currentText()
        result = [input_reg_id, input_reg_pw, input_reg_name, input_reg_nn, input_reg_team]

        user_info = json.dumps(result)
        message = f"{f'insertuser{header_split}{user_info}'}"
        self.client_controller.controller_send_json_message(message)

    # 아이디 중복검사 결과에따른 이벤트
    def set_reg_id_lab(self, result):
        if result is True:
            self.reg_id_lab.setText('ID 사용가능')
            self.reg_id_lab.setStyleSheet('color:blue;')
            self.click_reg_register_btn2()
        else:
            self.reg_id_lab.setText('ID 사용불가')
            self.reg_id_lab.setStyleSheet('color:red;')

    def set_reg_name_lab(self):
        self.reg_name_lab.setText('이름은 두 글자 이상이여야 합니다.')
        self.reg_name_lab_lab.setStyleSheet('color:red;')

    def set_reg_nn_lab(self):
        self.reg_nn_lab.setText('닉네임은 두 글자 이상이여야 합니다.')
        self.reg_nn_lab.setStyleSheet('color:red;')

    def set_reg_pw_lab(self):
        self.reg_pw_lab.setText('비밀번호가 같지 않습니다.')
        self.reg_pw_lab.setStyleSheet('color:red;')

    def set_reg_pw_lab2(self):
        self.reg_pw_lab.setText('비밀번호를 6자리 이상 적어주세요.')
        self.reg_pw_lab.setStyleSheet('color:red;')

    # 유저가 입력한 회원가입조건 검사
    def register_check(self):
        self.reg_name_lab.setText('이름')
        self.reg_nn_lab.setText('닉네임')
        self.reg_pw_lab.setText('비밀번호')

        if len(self.reg_name_edit.text()) < 2:
            self.set_reg_name_lab()
            return False
        else:
            self.reg_name_lab.setStyleSheet('color:black;')

        if len(self.reg_nn_edit.text()) < 2:
            self.set_reg_nn_lab()
            return False
        else:
            self.reg_nn_lab.setStyleSheet('color:black;')

        if len(self.reg_pw_edit.text()) < 6:
            self.set_reg_pw_lab2()
            return False
        else:
            self.reg_pw_lab.setStyleSheet('color:black;')

        if self.reg_pw_edit.text() != self.reg_pw_check_edit.text():
            self.set_reg_pw_lab()
            return False

        if self.reg_id_lab.text() != 'ID 사용가능':
            return False
        return True

    def log_out(self):
        """로그아웃 함수"""
        self.user_role = None
        self.stackedWidget.setCurrentWidget(self.login_page)
