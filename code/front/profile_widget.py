from PyQt5.QtWidgets import *
from code.front.ui.ui_class_profile_dialog import Ui_ProfileDialog
from PyQt5.QtGui import *

'''
프로필 변경 다이얼로그
'''

class ProFile(QDialog, Ui_ProfileDialog):
    """프로필 변경 다이얼로그"""
    def __init__(self, img, name, state):
        super().__init__()
        self.setupUi(self)

        # 값 넣어주기
        self.profile_img.setPixmap(QPixmap(img))
        self.name_lab.setText(name)
        self.state_edit.setText(state)

        # 버튼 누를 때 시그널 연결
        self.admit_btn.clicked.connect(self.change_profile)


    def change_profile(self):
        """여기에서 프로필 상태메세지를 변경합니다."""
        self.state_edit.text()
        self.close()

    def show_dialog(self):
        return self.exec_()