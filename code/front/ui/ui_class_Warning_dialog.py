# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Warning_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WarnDialog(object):
    def setupUi(self, WarnDialog):
        WarnDialog.setObjectName("WarnDialog")
        WarnDialog.resize(428, 510)
        WarnDialog.setStyleSheet("QFrame#frame{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"border: 0.5px solid gray;\n"
"\n"
"}\n"
"QDialog#WarnDialog{\n"
"background-color:rgb(255, 255, 255, 0)\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(WarnDialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(WarnDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.warn_title_widget = QtWidgets.QWidget(self.frame)
        self.warn_title_widget.setMinimumSize(QtCore.QSize(0, 100))
        self.warn_title_widget.setMaximumSize(QtCore.QSize(16777215, 100))
        self.warn_title_widget.setStyleSheet("background-color: rgb(228, 234, 238);\n"
"border-top-left-radius: 20px;\n"
"    border-top-right-radius: 20px;")
        self.warn_title_widget.setObjectName("warn_title_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.warn_title_widget)
        self.horizontalLayout.setContentsMargins(25, 30, 25, 30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.close_btn = QtWidgets.QPushButton(self.warn_title_widget)
        self.close_btn.setMinimumSize(QtCore.QSize(45, 45))
        self.close_btn.setMaximumSize(QtCore.QSize(45, 45))
        self.close_btn.setText("")
        self.close_btn.setObjectName("close_btn")
        self.horizontalLayout.addWidget(self.close_btn)
        self.verticalLayout_3.addWidget(self.warn_title_widget)
        self.contents = QtWidgets.QWidget(self.frame)
        self.contents.setMinimumSize(QtCore.QSize(0, 240))
        self.contents.setObjectName("contents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.contents)
        self.verticalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.warning_lab = QtWidgets.QLabel(self.contents)
        self.warning_lab.setMinimumSize(QtCore.QSize(0, 220))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.warning_lab.setFont(font)
        self.warning_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.warning_lab.setWordWrap(True)
        self.warning_lab.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByMouse)
        self.warning_lab.setObjectName("warning_lab")
        self.verticalLayout_2.addWidget(self.warning_lab)
        self.verticalLayout_3.addWidget(self.contents)
        self.widget_1 = QtWidgets.QWidget(self.frame)
        self.widget_1.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_1.setObjectName("widget_1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(138, 47, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.ok_btn = QtWidgets.QPushButton(self.widget_1)
        self.ok_btn.setMinimumSize(QtCore.QSize(132, 50))
        self.ok_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ok_btn.setFont(font)
        self.ok_btn.setStyleSheet("background-color: rgb(20, 200, 113);\n"
"border-radius:5px;\n"
"color:white;")
        self.ok_btn.setObjectName("ok_btn")
        self.horizontalLayout_2.addWidget(self.ok_btn)
        spacerItem2 = QtWidgets.QSpacerItem(138, 47, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.verticalLayout_3.addWidget(self.widget_1)
        self.widget_2 = QtWidgets.QWidget(self.frame)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.accept_btn = QtWidgets.QPushButton(self.widget_2)
        self.accept_btn.setMinimumSize(QtCore.QSize(132, 50))
        self.accept_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.accept_btn.setFont(font)
        self.accept_btn.setStyleSheet("background-color: rgb(20, 200, 113);\n"
"border-radius:5px;\n"
"color:white;")
        self.accept_btn.setObjectName("accept_btn")
        self.horizontalLayout_3.addWidget(self.accept_btn)
        self.cancel_btn = QtWidgets.QPushButton(self.widget_2)
        self.cancel_btn.setMinimumSize(QtCore.QSize(132, 50))
        self.cancel_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cancel_btn.setFont(font)
        self.cancel_btn.setStyleSheet("\n"
"border-radius:5px;\n"
"border: 0.5px solid gray;")
        self.cancel_btn.setObjectName("cancel_btn")
        self.horizontalLayout_3.addWidget(self.cancel_btn)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_3.addWidget(self.widget_2)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem5)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(WarnDialog)
        QtCore.QMetaObject.connectSlotsByName(WarnDialog)

    def retranslateUi(self, WarnDialog):
        _translate = QtCore.QCoreApplication.translate
        WarnDialog.setWindowTitle(_translate("WarnDialog", "Dialog"))
        self.warning_lab.setText(_translate("WarnDialog", "여기에 경고문구 경고문구 경고문구"))
        self.ok_btn.setText(_translate("WarnDialog", "확인"))
        self.accept_btn.setText(_translate("WarnDialog", "확인"))
        self.cancel_btn.setText(_translate("WarnDialog", "취소"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    WarnDialog = QtWidgets.QDialog()
    ui = Ui_WarnDialog()
    ui.setupUi(WarnDialog)
    WarnDialog.show()
    sys.exit(app.exec_())
