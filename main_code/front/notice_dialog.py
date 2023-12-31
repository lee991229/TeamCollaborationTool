from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap, QIcon
import sys
from main_code.front.ui.ui_class_notice_dialog import Ui_NoticeDialog
from main_code.front.Font import Font


class DialogNoticeAdd(QDialog, Ui_NoticeDialog):
    """공지를 추가하는 창"""

    def __init__(self, main_window, team_list):
        super().__init__()
        self.setupUi(self)
        self.team_list = team_list
        self.main_window = main_window
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.connect_event()
        self.set_ui()
        self.set_combobox()

    def set_combobox(self):
        for i in self.team_list:
            self.team.addItem(i)

    def set_ui(self):
        self.title_lab.setText('공지작성창')
        self.title_edit.setPlaceholderText("공지 제목을 작성하세요")
        self.contents_edit.setPlaceholderText("공지 내용을 작성하세요")
        self.close_btn.setIcon(QIcon('./src_img/close.png'))
        self.title_lab.setFont(Font.title(2))
        self.title_edit.setFont(Font.text(2))
        self.contents_edit.setFont(Font.text(2))
        self.ok_btn.setFont(Font.button(1))

    def connect_event(self):
        self.ok_btn.clicked.connect(self.add_notice)
        self.close_btn.clicked.connect(self.close)

    def add_notice(self):
        """여기서 공지를 서버에 넘깁니다."""

        title = self.title_edit.text()
        contents = self.contents_edit.toPlainText()
        team = self.team.currentText()
        self.main_window.insert_notice(title, contents, team)
        self.close()

    def close(self):
        self.title_edit.clear()
        self.contents_edit.clear()
        self.team.setCurrentIndex(0)
        super().close()


class DialogToDoAdd(QDialog, Ui_NoticeDialog):
    """투두리스트 추가하는 다이얼로그"""

    def __init__(self, main_window, team_list):
        super().__init__()
        self.setupUi(self)
        self.team_list = team_list
        self.main_window = main_window
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.connect_event()
        self.set_ui()

    def set_ui(self):
        self.title_lab.setText('투두리스트 작성창')
        self.title_edit.setPlaceholderText("투두리스트 제목을 작성하세요")
        self.contents_edit.setPlaceholderText("투두리스트 내용을 작성하세요")
        self.close_btn.setIcon(QIcon('./src_img/close.png'))
        self.title_lab.setFont(Font.title(2))
        self.title_edit.setFont(Font.text(2))
        self.contents_edit.setFont(Font.text(2))
        self.ok_btn.setFont(Font.button(1))
        self.team.setVisible(False)  # 투두리스트는 팀명 안보임
        self.set_combobox()

    def set_combobox(self):
        for i in self.team_list:
            self.team.addItem(i)

    def connect_event(self):
        self.ok_btn.clicked.connect(self.add_todo)
        self.close_btn.clicked.connect(self.close)

    def add_todo(self):
        """여기서 투두리스트를 서버에 넘깁니다."""

        title = self.title_edit.text()
        contents = self.contents_edit.toPlainText()
        self.main_window.insert_todo_list(title, contents)
        self.close()

    def close(self):
        self.title_edit.clear()
        self.contents_edit.clear()
        super().close()
