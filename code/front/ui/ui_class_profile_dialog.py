# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'profile_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProfileDialog(object):
    def setupUi(self, ProfileDialog):
        ProfileDialog.setObjectName("ProfileDialog")
        ProfileDialog.resize(430, 460)
        ProfileDialog.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ProfileDialog)
        self.verticalLayout_2.setContentsMargins(15, 70, 15, 70)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main_frame = QtWidgets.QFrame(ProfileDialog)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.h_lay = QtWidgets.QHBoxLayout()
        self.h_lay.setObjectName("h_lay")
        self.profile_img = QtWidgets.QLabel(self.main_frame)
        self.profile_img.setMinimumSize(QtCore.QSize(150, 150))
        self.profile_img.setMaximumSize(QtCore.QSize(158, 158))
        self.profile_img.setStyleSheet("background-color: rgb(213, 213, 213);")
        self.profile_img.setObjectName("profile_img")
        self.h_lay.addWidget(self.profile_img)
        self.verticalLayout.addLayout(self.h_lay)
        self.name_lab = QtWidgets.QLabel(self.main_frame)
        self.name_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.name_lab.setObjectName("name_lab")
        self.verticalLayout.addWidget(self.name_lab)
        self.state_lab = QtWidgets.QLabel(self.main_frame)
        self.state_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.state_lab.setObjectName("state_lab")
        self.verticalLayout.addWidget(self.state_lab)
        self.admit_btn = QtWidgets.QPushButton(self.main_frame)
        self.admit_btn.setMinimumSize(QtCore.QSize(0, 56))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.admit_btn.setFont(font)
        self.admit_btn.setStyleSheet("border-radius:5px;\n"
"background-color: rgb(20, 200, 113);\n"
"color:white;")
        self.admit_btn.setObjectName("admit_btn")
        self.verticalLayout.addWidget(self.admit_btn)
        self.verticalLayout_2.addWidget(self.main_frame)

        self.retranslateUi(ProfileDialog)
        QtCore.QMetaObject.connectSlotsByName(ProfileDialog)

    def retranslateUi(self, ProfileDialog):
        _translate = QtCore.QCoreApplication.translate
        ProfileDialog.setWindowTitle(_translate("ProfileDialog", "Dialog"))
        self.profile_img.setText(_translate("ProfileDialog", "여기에 프로필 사진"))
        self.name_lab.setText(_translate("ProfileDialog", "이름이름"))
        self.state_lab.setText(_translate("ProfileDialog", "상태메세지 상태메세지"))
        self.admit_btn.setText(_translate("ProfileDialog", "확인"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ProfileDialog = QtWidgets.QDialog()
    ui = Ui_ProfileDialog()
    ui.setupUi(ProfileDialog)
    ProfileDialog.show()
    sys.exit(app.exec_())