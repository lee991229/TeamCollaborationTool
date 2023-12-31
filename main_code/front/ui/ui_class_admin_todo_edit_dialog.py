# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_todo_edit_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminTodoDialog(object):
    def setupUi(self, AdminTodoDialog):
        AdminTodoDialog.setObjectName("AdminTodoDialog")
        AdminTodoDialog.resize(430, 550)
        AdminTodoDialog.setStyleSheet("\n"
"QWidget#profile_widget{\n"
"background-color: rgb(228, 234, 238);\n"
"border-top-left-radius: 20px;\n"
"    border-top-right-radius: 20px;\n"
"}\n"
"QWidget#scrollAreaWidgetContents{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QDialog#AdminTodoDialog{\n"
"    background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"QFrame#frame{\n"
"border: 0.5px solid gray;\n"
"border-radius: 20px;\n"
"background-color: rgb(255, 255, 255);}")
        self.verticalLayout = QtWidgets.QVBoxLayout(AdminTodoDialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(AdminTodoDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 20)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.profile_widget = QtWidgets.QWidget(self.frame)
        self.profile_widget.setMinimumSize(QtCore.QSize(0, 100))
        self.profile_widget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.profile_widget.setStyleSheet("")
        self.profile_widget.setObjectName("profile_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.profile_widget)
        self.horizontalLayout.setContentsMargins(25, 30, 25, 30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.photo_lab = QtWidgets.QLabel(self.profile_widget)
        self.photo_lab.setMinimumSize(QtCore.QSize(45, 45))
        self.photo_lab.setMaximumSize(QtCore.QSize(45, 45))
        self.photo_lab.setText("")
        self.photo_lab.setPixmap(QtGui.QPixmap(":/newPrefix/user_green.png"))
        self.photo_lab.setScaledContents(True)
        self.photo_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.photo_lab.setObjectName("photo_lab")
        self.horizontalLayout.addWidget(self.photo_lab)
        self.name_lab = QtWidgets.QLabel(self.profile_widget)
        self.name_lab.setMinimumSize(QtCore.QSize(100, 45))
        self.name_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.name_lab.setObjectName("name_lab")
        self.horizontalLayout.addWidget(self.name_lab)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancel_lab = QtWidgets.QPushButton(self.profile_widget)
        self.cancel_lab.setMinimumSize(QtCore.QSize(30, 30))
        self.cancel_lab.setMaximumSize(QtCore.QSize(24, 16777215))
        self.cancel_lab.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.cancel_lab.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cancel_lab.setIcon(icon)
        self.cancel_lab.setIconSize(QtCore.QSize(20, 20))
        self.cancel_lab.setObjectName("cancel_lab")
        self.horizontalLayout.addWidget(self.cancel_lab)
        self.verticalLayout_2.addWidget(self.profile_widget)
        self.scrollArea = QtWidgets.QScrollArea(self.frame)
        self.scrollArea.setStyleSheet("\n"
"            QScrollBar:vertical {\n"
"                border: none;\n"
"                background: #E4EAEE;\n"
"                width: 10px;\n"
"                margin: 0px;\n"
"            }\n"
"\n"
"            QScrollBar::handle:vertical {\n"
"                background: #14C871;\n"
"                min-height: 20px;\n"
"                border-radius: 5px;\n"
"            }\n"
"\n"
"            QScrollBar::handle:vertical:hover {\n"
"                background: #0F9B58;\n"
"            }\n"
"\n"
"            QScrollBar::sub-line:vertical,\n"
"            QScrollBar::add-line:vertical {\n"
"                border: none;\n"
"                height: 0px;\n"
"            }\n"
"")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 428, 240))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.admin_todo_lay = QtWidgets.QVBoxLayout()
        self.admin_todo_lay.setObjectName("admin_todo_lay")
        self.verticalLayout_3.addLayout(self.admin_todo_lay)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setStyleSheet("background-color: #E4EAEE;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.todo_add_frame = QtWidgets.QFrame(self.frame)
        self.todo_add_frame.setMaximumSize(QtCore.QSize(16777215, 125))
        self.todo_add_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.todo_add_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.todo_add_frame.setObjectName("todo_add_frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.todo_add_frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(6, -1, 6, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.todo_title_textedit = QtWidgets.QTextEdit(self.todo_add_frame)
        self.todo_title_textedit.setMinimumSize(QtCore.QSize(0, 20))
        self.todo_title_textedit.setMaximumSize(QtCore.QSize(16777215, 30))
        self.todo_title_textedit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.todo_title_textedit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.todo_title_textedit.setObjectName("todo_title_textedit")
        self.gridLayout.addWidget(self.todo_title_textedit, 1, 1, 1, 1)
        self.todo_contents_lab = QtWidgets.QLabel(self.todo_add_frame)
        self.todo_contents_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.todo_contents_lab.setObjectName("todo_contents_lab")
        self.gridLayout.addWidget(self.todo_contents_lab, 2, 0, 1, 1)
        self.todo_contents_plain = QtWidgets.QPlainTextEdit(self.todo_add_frame)
        self.todo_contents_plain.setMaximumSize(QtCore.QSize(16777215, 40))
        self.todo_contents_plain.setObjectName("todo_contents_plain")
        self.gridLayout.addWidget(self.todo_contents_plain, 2, 1, 1, 1)
        self.todo_add_title_lab = QtWidgets.QLabel(self.todo_add_frame)
        self.todo_add_title_lab.setMaximumSize(QtCore.QSize(16777215, 20))
        self.todo_add_title_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.todo_add_title_lab.setObjectName("todo_add_title_lab")
        self.gridLayout.addWidget(self.todo_add_title_lab, 0, 0, 1, 4)
        self.todo_title_lab = QtWidgets.QLabel(self.todo_add_frame)
        self.todo_title_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.todo_title_lab.setObjectName("todo_title_lab")
        self.gridLayout.addWidget(self.todo_title_lab, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.todo_add_frame)
        self.pushButton.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.pushButton.setStyleSheet("background-color: rgb(20, 200, 113);\n"
"border-radius: 20px;\n"
"")
        self.pushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(25, 25))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 2, 1)
        self.verticalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.todo_add_frame)
        spacerItem2 = QtWidgets.QSpacerItem(5, 8, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem2)
        self.h_bottom_lay = QtWidgets.QHBoxLayout()
        self.h_bottom_lay.setObjectName("h_bottom_lay")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_bottom_lay.addItem(spacerItem3)
        self.admit_btn = QtWidgets.QPushButton(self.frame)
        self.admit_btn.setMinimumSize(QtCore.QSize(132, 50))
        self.admit_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.admit_btn.setStyleSheet("background-color: rgb(20, 200, 113);\n"
"border-radius:5px;\n"
"color:white;")
        self.admit_btn.setObjectName("admit_btn")
        self.h_bottom_lay.addWidget(self.admit_btn)
        spacerItem4 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.h_bottom_lay.addItem(spacerItem4)
        self.cancel_btn = QtWidgets.QPushButton(self.frame)
        self.cancel_btn.setMinimumSize(QtCore.QSize(132, 50))
        self.cancel_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        self.cancel_btn.setStyleSheet("\n"
"border-radius:5px;\n"
"border: 0.5px solid gray;")
        self.cancel_btn.setObjectName("cancel_btn")
        self.h_bottom_lay.addWidget(self.cancel_btn)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.h_bottom_lay.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.h_bottom_lay)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(AdminTodoDialog)
        QtCore.QMetaObject.connectSlotsByName(AdminTodoDialog)

    def retranslateUi(self, AdminTodoDialog):
        _translate = QtCore.QCoreApplication.translate
        AdminTodoDialog.setWindowTitle(_translate("AdminTodoDialog", "Dialog"))
        self.name_lab.setText(_translate("AdminTodoDialog", "이름"))
        self.todo_contents_lab.setText(_translate("AdminTodoDialog", "내용"))
        self.todo_add_title_lab.setText(_translate("AdminTodoDialog", "투두리스트 추가"))
        self.todo_title_lab.setText(_translate("AdminTodoDialog", "제목"))
        self.admit_btn.setText(_translate("AdminTodoDialog", "확인"))
        self.cancel_btn.setText(_translate("AdminTodoDialog", "취소"))
from main_code.front.ui import my_qrc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminTodoDialog = QtWidgets.QDialog()
    ui = Ui_AdminTodoDialog()
    ui.setupUi(AdminTodoDialog)
    AdminTodoDialog.show()
    sys.exit(app.exec_())
