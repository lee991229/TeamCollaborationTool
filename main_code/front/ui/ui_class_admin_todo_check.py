# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_todo_check.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MemberWidget(object):
    def setupUi(self, MemberWidget):
        MemberWidget.setObjectName("MemberWidget")
        MemberWidget.resize(723, 58)
        MemberWidget.setStyleSheet("")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(MemberWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(MemberWidget)
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(35, -1, 35, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.name_lab = QtWidgets.QLabel(self.frame)
        self.name_lab.setObjectName("name_lab")
        self.horizontalLayout.addWidget(self.name_lab)
        self.role_lab = QtWidgets.QLabel(self.frame)
        self.role_lab.setObjectName("role_lab")
        self.horizontalLayout.addWidget(self.role_lab)
        spacerItem = QtWidgets.QSpacerItem(574, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.show_btn = QtWidgets.QPushButton(self.frame)
        self.show_btn.setMinimumSize(QtCore.QSize(20, 30))
        self.show_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/right_green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.show_btn.setIcon(icon)
        self.show_btn.setIconSize(QtCore.QSize(20, 30))
        self.show_btn.setObjectName("show_btn")
        self.horizontalLayout.addWidget(self.show_btn)
        self.horizontalLayout_2.addWidget(self.frame)

        self.retranslateUi(MemberWidget)
        QtCore.QMetaObject.connectSlotsByName(MemberWidget)

    def retranslateUi(self, MemberWidget):
        _translate = QtCore.QCoreApplication.translate
        MemberWidget.setWindowTitle(_translate("MemberWidget", "Form"))
        self.name_lab.setText(_translate("MemberWidget", "이름"))
        self.role_lab.setText(_translate("MemberWidget", "직급"))
from main_code.front.ui import my_qrc_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MemberWidget = QtWidgets.QWidget()
    ui = Ui_MemberWidget()
    ui.setupUi(MemberWidget)
    MemberWidget.show()
    sys.exit(app.exec_())
