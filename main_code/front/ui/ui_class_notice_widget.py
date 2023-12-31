# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'notice_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Notice_widget(object):
    def setupUi(self, Notice_widget):
        Notice_widget.setObjectName("Notice_widget")
        Notice_widget.resize(772, 185)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(Notice_widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.main_frame = QtWidgets.QFrame(Notice_widget)
        self.main_frame.setMinimumSize(QtCore.QSize(750, 163))
        self.main_frame.setMaximumSize(QtCore.QSize(16777215, 163))
        self.main_frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:20px;")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.h_lay = QtWidgets.QHBoxLayout()
        self.h_lay.setContentsMargins(10, -1, -1, -1)
        self.h_lay.setSpacing(0)
        self.h_lay.setObjectName("h_lay")
        self.label = QtWidgets.QLabel(self.main_frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.h_lay.addWidget(self.label)
        self.del_btn = QtWidgets.QPushButton(self.main_frame)
        self.del_btn.setMaximumSize(QtCore.QSize(50, 50))
        self.del_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.del_btn.setIcon(icon)
        self.del_btn.setIconSize(QtCore.QSize(20, 20))
        self.del_btn.setObjectName("del_btn")
        self.h_lay.addWidget(self.del_btn)
        self.verticalLayout.addLayout(self.h_lay)
        self.line = QtWidgets.QFrame(self.main_frame)
        self.line.setStyleSheet("background-color: #E4EAEE;")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.frame = QtWidgets.QFrame(self.main_frame)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(10, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.detail_lab = QtWidgets.QLabel(self.frame)
        self.detail_lab.setWordWrap(True)
        self.detail_lab.setObjectName("detail_lab")
        self.horizontalLayout.addWidget(self.detail_lab)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_3.addWidget(self.main_frame)

        self.retranslateUi(Notice_widget)
        QtCore.QMetaObject.connectSlotsByName(Notice_widget)

    def retranslateUi(self, Notice_widget):
        _translate = QtCore.QCoreApplication.translate
        Notice_widget.setWindowTitle(_translate("Notice_widget", "Form"))
        self.label.setText(_translate("Notice_widget", "공지 제목 공지 제목"))
        self.detail_lab.setText(_translate("Notice_widget", "공지 내용이 이러쿵 저러쿵"))
from main_code.front.ui import my_qrc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Notice_widget = QtWidgets.QWidget()
    ui = Ui_Notice_widget()
    ui.setupUi(Notice_widget)
    Notice_widget.show()
    sys.exit(app.exec_())
