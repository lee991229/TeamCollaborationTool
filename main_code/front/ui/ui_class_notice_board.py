# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notice_board.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_NoticeBoard(object):
    def setupUi(self, NoticeBoard):
        NoticeBoard.setObjectName("NoticeBoard")
        NoticeBoard.resize(1120, 630)
        NoticeBoard.setMinimumSize(QtCore.QSize(1120, 630))
        self.centralwidget = QtWidgets.QWidget(NoticeBoard)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.login_page = QtWidgets.QWidget()
        self.login_page.setStyleSheet("QLineEdit{\n"
"background-color: rgb(242, 245, 253);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton#login_btn{\n"
"border-radius:5px;\n"
"background-color:#14C871;\n"
"color:white;\n"
"}\n"
"QPushButton#register_btn{\n"
"border-radius:5px;\n"
"background-color:white;\n"
"border: 0.5px solid gray;\n"
"}\n"
"QWidget#login_page{\n"
"background-color: white;}")
        self.login_page.setObjectName("login_page")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.login_page)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(329, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.v_lay_login = QtWidgets.QVBoxLayout()
        self.v_lay_login.setObjectName("v_lay_login")
        spacerItem1 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.v_lay_login.addItem(spacerItem1)
        self.login_title_lab = QtWidgets.QLabel(self.login_page)
        self.login_title_lab.setMaximumSize(QtCore.QSize(16777215, 47))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.login_title_lab.setFont(font)
        self.login_title_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.login_title_lab.setObjectName("login_title_lab")
        self.v_lay_login.addWidget(self.login_title_lab)
        self.login_id_lab = QtWidgets.QLabel(self.login_page)
        self.login_id_lab.setMinimumSize(QtCore.QSize(0, 40))
        self.login_id_lab.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.login_id_lab.setObjectName("login_id_lab")
        self.v_lay_login.addWidget(self.login_id_lab)
        self.login_id_edit = QtWidgets.QLineEdit(self.login_page)
        self.login_id_edit.setMinimumSize(QtCore.QSize(0, 70))
        self.login_id_edit.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.login_id_edit.setFont(font)
        self.login_id_edit.setStyleSheet("")
        self.login_id_edit.setText("")
        self.login_id_edit.setObjectName("login_id_edit")
        self.v_lay_login.addWidget(self.login_id_edit)
        self.login_pw_lab = QtWidgets.QLabel(self.login_page)
        self.login_pw_lab.setMinimumSize(QtCore.QSize(0, 40))
        self.login_pw_lab.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.login_pw_lab.setObjectName("login_pw_lab")
        self.v_lay_login.addWidget(self.login_pw_lab)
        self.login_pw_edit = QtWidgets.QLineEdit(self.login_page)
        self.login_pw_edit.setMinimumSize(QtCore.QSize(0, 70))
        self.login_pw_edit.setMaximumSize(QtCore.QSize(16777215, 70))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.login_pw_edit.setFont(font)
        self.login_pw_edit.setStyleSheet("")
        self.login_pw_edit.setText("")
        self.login_pw_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_pw_edit.setObjectName("login_pw_edit")
        self.v_lay_login.addWidget(self.login_pw_edit)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.v_lay_login.addItem(spacerItem2)
        self.widget = QtWidgets.QWidget(self.login_page)
        self.widget.setMinimumSize(QtCore.QSize(440, 52))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 120))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.login_btn = QtWidgets.QPushButton(self.widget)
        self.login_btn.setMinimumSize(QtCore.QSize(210, 50))
        self.login_btn.setMaximumSize(QtCore.QSize(210, 16777215))
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout.addWidget(self.login_btn)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.register_btn = QtWidgets.QPushButton(self.widget)
        self.register_btn.setMinimumSize(QtCore.QSize(210, 50))
        self.register_btn.setMaximumSize(QtCore.QSize(210, 16777215))
        self.register_btn.setObjectName("register_btn")
        self.horizontalLayout.addWidget(self.register_btn)
        self.v_lay_login.addWidget(self.widget)
        spacerItem4 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.v_lay_login.addItem(spacerItem4)
        self.horizontalLayout_2.addLayout(self.v_lay_login)
        spacerItem5 = QtWidgets.QSpacerItem(329, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.stackedWidget.addWidget(self.login_page)
        self.register_page = QtWidgets.QWidget()
        self.register_page.setStyleSheet("QLineEdit{\n"
"background-color: rgb(242, 245, 253);\n"
"border-radius:5px;\n"
"}\n"
"QPushButton{\n"
"border-radius:5px;\n"
"background-color:#14C871;\n"
"color:white;\n"
"}\n"
"QWidget#register_page{\n"
"background-color: white;}")
        self.register_page.setObjectName("register_page")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.register_page)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem6 = QtWidgets.QSpacerItem(349, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6)
        self.reg_v_lay = QtWidgets.QVBoxLayout()
        self.reg_v_lay.setObjectName("reg_v_lay")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.reg_v_lay.addItem(spacerItem7)
        self.reg_title_lab = QtWidgets.QLabel(self.register_page)
        self.reg_title_lab.setMinimumSize(QtCore.QSize(400, 0))
        self.reg_title_lab.setMaximumSize(QtCore.QSize(16777215, 47))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.reg_title_lab.setFont(font)
        self.reg_title_lab.setObjectName("reg_title_lab")
        self.reg_v_lay.addWidget(self.reg_title_lab)
        self.reg_sub_title = QtWidgets.QLabel(self.register_page)
        self.reg_sub_title.setObjectName("reg_sub_title")
        self.reg_v_lay.addWidget(self.reg_sub_title)
        self.reg_id_lab = QtWidgets.QLabel(self.register_page)
        self.reg_id_lab.setMinimumSize(QtCore.QSize(0, 25))
        self.reg_id_lab.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.reg_id_lab.setObjectName("reg_id_lab")
        self.reg_v_lay.addWidget(self.reg_id_lab)
        self.reg_id_edit = QtWidgets.QLineEdit(self.register_page)
        self.reg_id_edit.setMinimumSize(QtCore.QSize(400, 45))
        self.reg_id_edit.setMaximumSize(QtCore.QSize(16777215, 45))
        self.reg_id_edit.setStyleSheet("")
        self.reg_id_edit.setObjectName("reg_id_edit")
        self.reg_v_lay.addWidget(self.reg_id_edit)
        self.reg_name_lab = QtWidgets.QLabel(self.register_page)
        self.reg_name_lab.setMinimumSize(QtCore.QSize(0, 25))
        self.reg_name_lab.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.reg_name_lab.setObjectName("reg_name_lab")
        self.reg_v_lay.addWidget(self.reg_name_lab)
        self.reg_name_edit = QtWidgets.QLineEdit(self.register_page)
        self.reg_name_edit.setMinimumSize(QtCore.QSize(400, 45))
        self.reg_name_edit.setMaximumSize(QtCore.QSize(16777215, 45))
        self.reg_name_edit.setStyleSheet("")
        self.reg_name_edit.setText("")
        self.reg_name_edit.setObjectName("reg_name_edit")
        self.reg_v_lay.addWidget(self.reg_name_edit)
        self.reg_nn_lab = QtWidgets.QLabel(self.register_page)
        self.reg_nn_lab.setMinimumSize(QtCore.QSize(0, 25))
        self.reg_nn_lab.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.reg_nn_lab.setObjectName("reg_nn_lab")
        self.reg_v_lay.addWidget(self.reg_nn_lab)
        self.reg_nn_edit = QtWidgets.QLineEdit(self.register_page)
        self.reg_nn_edit.setMinimumSize(QtCore.QSize(400, 45))
        self.reg_nn_edit.setMaximumSize(QtCore.QSize(16777215, 45))
        self.reg_nn_edit.setStyleSheet("")
        self.reg_nn_edit.setObjectName("reg_nn_edit")
        self.reg_v_lay.addWidget(self.reg_nn_edit)
        self.reg_nn_lab_2 = QtWidgets.QLabel(self.register_page)
        self.reg_nn_lab_2.setMinimumSize(QtCore.QSize(0, 25))
        self.reg_nn_lab_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.reg_nn_lab_2.setObjectName("reg_nn_lab_2")
        self.reg_v_lay.addWidget(self.reg_nn_lab_2)
        self.comboBox = QtWidgets.QComboBox(self.register_page)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 45))
        self.comboBox.setStyleSheet("background-color: rgb(242, 245, 253);\n"
"border-radius:5px;")
        self.comboBox.setObjectName("comboBox")
        self.reg_v_lay.addWidget(self.comboBox)
        self.reg_pw_lab = QtWidgets.QLabel(self.register_page)
        self.reg_pw_lab.setMinimumSize(QtCore.QSize(0, 25))
        self.reg_pw_lab.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.reg_pw_lab.setObjectName("reg_pw_lab")
        self.reg_v_lay.addWidget(self.reg_pw_lab)
        self.reg_pw_edit = QtWidgets.QLineEdit(self.register_page)
        self.reg_pw_edit.setMinimumSize(QtCore.QSize(400, 45))
        self.reg_pw_edit.setMaximumSize(QtCore.QSize(16777215, 45))
        self.reg_pw_edit.setStyleSheet("")
        self.reg_pw_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.reg_pw_edit.setObjectName("reg_pw_edit")
        self.reg_v_lay.addWidget(self.reg_pw_edit)
        self.reg_pw_check_lab = QtWidgets.QLabel(self.register_page)
        self.reg_pw_check_lab.setMinimumSize(QtCore.QSize(0, 25))
        self.reg_pw_check_lab.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.reg_pw_check_lab.setObjectName("reg_pw_check_lab")
        self.reg_v_lay.addWidget(self.reg_pw_check_lab)
        self.reg_pw_check_edit = QtWidgets.QLineEdit(self.register_page)
        self.reg_pw_check_edit.setMinimumSize(QtCore.QSize(400, 45))
        self.reg_pw_check_edit.setMaximumSize(QtCore.QSize(16777215, 45))
        self.reg_pw_check_edit.setStyleSheet("")
        self.reg_pw_check_edit.setEchoMode(QtWidgets.QLineEdit.Password)
        self.reg_pw_check_edit.setObjectName("reg_pw_check_edit")
        self.reg_v_lay.addWidget(self.reg_pw_check_edit)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.reg_v_lay.addItem(spacerItem8)
        self.reg_register_btn = QtWidgets.QPushButton(self.register_page)
        self.reg_register_btn.setMinimumSize(QtCore.QSize(400, 45))
        self.reg_register_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.reg_register_btn.setObjectName("reg_register_btn")
        self.reg_v_lay.addWidget(self.reg_register_btn)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.reg_v_lay.addItem(spacerItem9)
        self.horizontalLayout_6.addLayout(self.reg_v_lay)
        spacerItem10 = QtWidgets.QSpacerItem(349, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10)
        self.stackedWidget.addWidget(self.register_page)
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.main_page)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.category_bar = QtWidgets.QWidget(self.main_page)
        self.category_bar.setMinimumSize(QtCore.QSize(270, 0))
        self.category_bar.setMaximumSize(QtCore.QSize(270, 16777215))
        self.category_bar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.category_bar.setObjectName("category_bar")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.category_bar)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.profile_widget = QtWidgets.QWidget(self.category_bar)
        self.profile_widget.setObjectName("profile_widget")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.profile_widget)
        self.horizontalLayout_8.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.profile_h_lay = QtWidgets.QHBoxLayout()
        self.profile_h_lay.setObjectName("profile_h_lay")
        self.profile_img = QtWidgets.QLabel(self.profile_widget)
        self.profile_img.setMinimumSize(QtCore.QSize(90, 90))
        self.profile_img.setMaximumSize(QtCore.QSize(90, 90))
        self.profile_img.setText("")
        self.profile_img.setPixmap(QtGui.QPixmap(":/newPrefix/user_green.png"))
        self.profile_img.setScaledContents(True)
        self.profile_img.setAlignment(QtCore.Qt.AlignCenter)
        self.profile_img.setObjectName("profile_img")
        self.profile_h_lay.addWidget(self.profile_img)
        self.profile_v_lay = QtWidgets.QVBoxLayout()
        self.profile_v_lay.setObjectName("profile_v_lay")
        self.user_name = QtWidgets.QLabel(self.profile_widget)
        self.user_name.setMinimumSize(QtCore.QSize(110, 0))
        self.user_name.setMaximumSize(QtCore.QSize(16777215, 25))
        self.user_name.setObjectName("user_name")
        self.profile_v_lay.addWidget(self.user_name)
        self.user_team = QtWidgets.QLabel(self.profile_widget)
        self.user_team.setMaximumSize(QtCore.QSize(16777215, 25))
        self.user_team.setObjectName("user_team")
        self.profile_v_lay.addWidget(self.user_team)
        self.user_state = QtWidgets.QLabel(self.profile_widget)
        self.user_state.setObjectName("user_state")
        self.profile_v_lay.addWidget(self.user_state)
        self.profile_h_lay.addLayout(self.profile_v_lay)
        self.horizontalLayout_8.addLayout(self.profile_h_lay)
        self.verticalLayout_6.addWidget(self.profile_widget)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_6.addItem(spacerItem11)
        self.category_v_lay = QtWidgets.QVBoxLayout()
        self.category_v_lay.setObjectName("category_v_lay")
        self.verticalLayout_6.addLayout(self.category_v_lay)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem12)
        self.horizontalLayout_5.addWidget(self.category_bar)
        self.inner_stackedWidget = QtWidgets.QStackedWidget(self.main_page)
        self.inner_stackedWidget.setObjectName("inner_stackedWidget")
        self.notice_page = QtWidgets.QWidget()
        self.notice_page.setStyleSheet("background-color: rgb(228, 234, 238);")
        self.notice_page.setObjectName("notice_page")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.notice_page)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.notice_widget = QtWidgets.QWidget(self.notice_page)
        self.notice_widget.setObjectName("notice_widget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.notice_widget)
        self.verticalLayout_5.setSpacing(7)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.notice_scrollarea = QtWidgets.QScrollArea(self.notice_widget)
        self.notice_scrollarea.setStyleSheet("\n"
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
        self.notice_scrollarea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.notice_scrollarea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.notice_scrollarea.setWidgetResizable(True)
        self.notice_scrollarea.setObjectName("notice_scrollarea")
        self.notice_scrollAreaWidgetContents = QtWidgets.QWidget()
        self.notice_scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 832, 565))
        self.notice_scrollAreaWidgetContents.setMinimumSize(QtCore.QSize(826, 0))
        self.notice_scrollAreaWidgetContents.setObjectName("notice_scrollAreaWidgetContents")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.notice_scrollAreaWidgetContents)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.notice_v_lay = QtWidgets.QVBoxLayout()
        self.notice_v_lay.setObjectName("notice_v_lay")
        self.verticalLayout_4.addLayout(self.notice_v_lay)
        spacerItem13 = QtWidgets.QSpacerItem(825, 483, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem13)
        self.notice_scrollarea.setWidget(self.notice_scrollAreaWidgetContents)
        self.verticalLayout_5.addWidget(self.notice_scrollarea)
        self.bottom_widget = QtWidgets.QWidget(self.notice_widget)
        self.bottom_widget.setMinimumSize(QtCore.QSize(0, 40))
        self.bottom_widget.setObjectName("bottom_widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.bottom_widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem14 = QtWidgets.QSpacerItem(789, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem14)
        self.plus_button = QtWidgets.QPushButton(self.bottom_widget)
        self.plus_button.setMinimumSize(QtCore.QSize(40, 40))
        self.plus_button.setMaximumSize(QtCore.QSize(30, 16777215))
        self.plus_button.setStyleSheet("border-radius:20px;\n"
"background-color: rgb(20, 200, 113);")
        self.plus_button.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/plus-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.plus_button.setIcon(icon)
        self.plus_button.setIconSize(QtCore.QSize(30, 30))
        self.plus_button.setObjectName("plus_button")
        self.horizontalLayout_3.addWidget(self.plus_button)
        self.verticalLayout_5.addWidget(self.bottom_widget)
        self.horizontalLayout_7.addWidget(self.notice_widget)
        self.inner_stackedWidget.addWidget(self.notice_page)
        self.chat_page = QtWidgets.QWidget()
        self.chat_page.setStyleSheet("background-color: rgb(228, 234, 238);")
        self.chat_page.setObjectName("chat_page")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.chat_page)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.chat_widget = QtWidgets.QWidget(self.chat_page)
        self.chat_widget.setObjectName("chat_widget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.chat_widget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.chat_scrollarea = QtWidgets.QScrollArea(self.chat_widget)
        self.chat_scrollarea.setStyleSheet("\n"
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
        self.chat_scrollarea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.chat_scrollarea.setWidgetResizable(True)
        self.chat_scrollarea.setObjectName("chat_scrollarea")
        self.chat_scrollarea_contents = QtWidgets.QWidget()
        self.chat_scrollarea_contents.setGeometry(QtCore.QRect(0, 0, 829, 16))
        self.chat_scrollarea_contents.setObjectName("chat_scrollarea_contents")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.chat_scrollarea_contents)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.chat_v_lay = QtWidgets.QVBoxLayout()
        self.chat_v_lay.setObjectName("chat_v_lay")
        self.verticalLayout_7.addLayout(self.chat_v_lay)
        spacerItem15 = QtWidgets.QSpacerItem(829, 533, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem15)
        self.chat_scrollarea.setWidget(self.chat_scrollarea_contents)
        self.verticalLayout_8.addWidget(self.chat_scrollarea)
        self.verticalLayout_2.addWidget(self.chat_widget)
        self.chat_line_widget = QtWidgets.QWidget(self.chat_page)
        self.chat_line_widget.setMinimumSize(QtCore.QSize(0, 80))
        self.chat_line_widget.setMaximumSize(QtCore.QSize(16777215, 80))
        self.chat_line_widget.setStyleSheet("QWidget#chat_line_widget{\n"
"background-color: rgb(255, 255, 255);\n"
"border-top-left-radius: 20px;\n"
"border-top-right-radius: 20px;}\n"
"QLineEdit#chat_edit{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border: transparent;\n"
"}\n"
"QPushButton#send_btn{\n"
"    background-color: rgb(255, 255, 255, 0);\n"
"}")
        self.chat_line_widget.setObjectName("chat_line_widget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.chat_line_widget)
        self.horizontalLayout_10.setContentsMargins(-1, -1, 20, -1)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.chat_edit = QtWidgets.QLineEdit(self.chat_line_widget)
        self.chat_edit.setMinimumSize(QtCore.QSize(0, 35))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.chat_edit.setFont(font)
        self.chat_edit.setObjectName("chat_edit")
        self.horizontalLayout_10.addWidget(self.chat_edit)
        self.send_btn = QtWidgets.QPushButton(self.chat_line_widget)
        self.send_btn.setMinimumSize(QtCore.QSize(40, 40))
        self.send_btn.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.send_btn.setFont(font)
        self.send_btn.setStyleSheet("")
        self.send_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/newPrefix/send_green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.send_btn.setIcon(icon1)
        self.send_btn.setIconSize(QtCore.QSize(40, 40))
        self.send_btn.setObjectName("send_btn")
        self.horizontalLayout_10.addWidget(self.send_btn)
        self.verticalLayout_2.addWidget(self.chat_line_widget)
        self.inner_stackedWidget.addWidget(self.chat_page)
        self.team_page = QtWidgets.QWidget()
        self.team_page.setStyleSheet("background-color: rgb(228, 234, 238);")
        self.team_page.setObjectName("team_page")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.team_page)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.team_title_widget = QtWidgets.QWidget(self.team_page)
        self.team_title_widget.setMinimumSize(QtCore.QSize(0, 50))
        self.team_title_widget.setMaximumSize(QtCore.QSize(16777215, 50))
        self.team_title_widget.setStyleSheet("background-color: rgb(15, 155, 88);")
        self.team_title_widget.setObjectName("team_title_widget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.team_title_widget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.team_title_widget)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        spacerItem16 = QtWidgets.QSpacerItem(819, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem16)
        self.verticalLayout_3.addWidget(self.team_title_widget)
        self.scrollArea = QtWidgets.QScrollArea(self.team_page)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 753, 367))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.team_h_lay = QtWidgets.QHBoxLayout()
        self.team_h_lay.setObjectName("team_h_lay")
        spacerItem17 = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.team_h_lay.addItem(spacerItem17)
        self.team_v_lay = QtWidgets.QVBoxLayout()
        self.team_v_lay.setObjectName("team_v_lay")
        self.team_process_widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.team_process_widget.setMaximumSize(QtCore.QSize(737, 16777215))
        self.team_process_widget.setObjectName("team_process_widget")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.team_process_widget)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.team_process_lab = QtWidgets.QLabel(self.team_process_widget)
        self.team_process_lab.setMinimumSize(QtCore.QSize(0, 25))
        self.team_process_lab.setMaximumSize(QtCore.QSize(16777215, 25))
        self.team_process_lab.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.team_process_lab.setObjectName("team_process_lab")
        self.verticalLayout_10.addWidget(self.team_process_lab)
        self.team_process_widget_2 = QtWidgets.QWidget(self.team_process_widget)
        self.team_process_widget_2.setMinimumSize(QtCore.QSize(737, 287))
        self.team_process_widget_2.setMaximumSize(QtCore.QSize(16777215, 287))
        self.team_process_widget_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.team_process_widget_2.setObjectName("team_process_widget_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.team_process_widget_2)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.v_lay_graph = QtWidgets.QVBoxLayout()
        self.v_lay_graph.setObjectName("v_lay_graph")
        self.verticalLayout_11.addLayout(self.v_lay_graph)
        self.verticalLayout_10.addWidget(self.team_process_widget_2)
        self.team_v_lay.addWidget(self.team_process_widget)
        self.team_todo_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.team_todo_label.setMinimumSize(QtCore.QSize(0, 25))
        self.team_todo_label.setMaximumSize(QtCore.QSize(16777215, 25))
        self.team_todo_label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.team_todo_label.setObjectName("team_todo_label")
        self.team_v_lay.addWidget(self.team_todo_label)
        self.team_mem_v_lay = QtWidgets.QVBoxLayout()
        self.team_mem_v_lay.setObjectName("team_mem_v_lay")
        self.team_v_lay.addLayout(self.team_mem_v_lay)
        spacerItem18 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.team_v_lay.addItem(spacerItem18)
        self.team_h_lay.addLayout(self.team_v_lay)
        spacerItem19 = QtWidgets.QSpacerItem(55, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.team_h_lay.addItem(spacerItem19)
        self.verticalLayout_9.addLayout(self.team_h_lay)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.inner_stackedWidget.addWidget(self.team_page)
        self.horizontalLayout_5.addWidget(self.inner_stackedWidget)
        self.stackedWidget.addWidget(self.main_page)
        self.verticalLayout.addWidget(self.stackedWidget)
        NoticeBoard.setCentralWidget(self.centralwidget)

        self.retranslateUi(NoticeBoard)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(NoticeBoard)

    def retranslateUi(self, NoticeBoard):
        _translate = QtCore.QCoreApplication.translate
        NoticeBoard.setWindowTitle(_translate("NoticeBoard", "MainWindow"))
        self.login_title_lab.setText(_translate("NoticeBoard", "로그인"))
        self.login_id_lab.setText(_translate("NoticeBoard", "ID"))
        self.login_id_edit.setPlaceholderText(_translate("NoticeBoard", "아이디를 입력하세요"))
        self.login_pw_lab.setText(_translate("NoticeBoard", "PASSWORD"))
        self.login_pw_edit.setPlaceholderText(_translate("NoticeBoard", "비밀번호를 입력하세요"))
        self.login_btn.setText(_translate("NoticeBoard", "로그인"))
        self.register_btn.setText(_translate("NoticeBoard", "회원가입하러가기"))
        self.reg_title_lab.setText(_translate("NoticeBoard", "회원가입"))
        self.reg_sub_title.setText(_translate("NoticeBoard", "쉬운 일정관리에 함께하세요."))
        self.reg_id_lab.setText(_translate("NoticeBoard", "ID"))
        self.reg_id_edit.setPlaceholderText(_translate("NoticeBoard", "아이디를 입력하세요"))
        self.reg_name_lab.setText(_translate("NoticeBoard", "이름"))
        self.reg_name_edit.setPlaceholderText(_translate("NoticeBoard", "이름을 입력하세요"))
        self.reg_nn_lab.setText(_translate("NoticeBoard", "닉네임"))
        self.reg_nn_edit.setPlaceholderText(_translate("NoticeBoard", "닉네임을 입력하세요"))
        self.reg_nn_lab_2.setText(_translate("NoticeBoard", "팀명"))
        self.reg_pw_lab.setText(_translate("NoticeBoard", "비밀번호"))
        self.reg_pw_edit.setPlaceholderText(_translate("NoticeBoard", "비밀번호를 입력하세요"))
        self.reg_pw_check_lab.setText(_translate("NoticeBoard", "비밀번호 확인"))
        self.reg_pw_check_edit.setPlaceholderText(_translate("NoticeBoard", "비밀번호를 다시 입력해 주세요"))
        self.reg_register_btn.setText(_translate("NoticeBoard", "가입하기"))
        self.user_name.setText(_translate("NoticeBoard", "이름"))
        self.user_team.setText(_translate("NoticeBoard", "팀이름"))
        self.user_state.setText(_translate("NoticeBoard", "상태메세지"))
        self.chat_edit.setPlaceholderText(_translate("NoticeBoard", "메세지를 작성하세요."))
        self.team_process_lab.setText(_translate("NoticeBoard", "팀업무진행도"))
        self.team_todo_label.setText(_translate("NoticeBoard", "팀원별 투두리스트"))
from main_code.front.ui import my_qrc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    NoticeBoard = QtWidgets.QMainWindow()
    ui = Ui_NoticeBoard()
    ui.setupUi(NoticeBoard)
    NoticeBoard.show()
    sys.exit(app.exec_())
