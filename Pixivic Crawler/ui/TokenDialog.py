# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TokenDialogUi.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_token_Dialog(object):
    def setupUi(self, token_Dialog):
        token_Dialog.setObjectName("token_Dialog")
        token_Dialog.resize(418, 249)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(13)
        token_Dialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(token_Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.msg_label = QtWidgets.QLabel(token_Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.msg_label.setFont(font)
        self.msg_label.setObjectName("msg_label")
        self.horizontalLayout_2.addWidget(self.msg_label)
        self.refresh_button = QtWidgets.QPushButton(token_Dialog)
        self.refresh_button.setObjectName("refresh_button")
        self.horizontalLayout_2.addWidget(self.refresh_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.code_pic_label = QtWidgets.QLabel(token_Dialog)
        self.code_pic_label.setMinimumSize(QtCore.QSize(400, 150))
        self.code_pic_label.setText("")
        self.code_pic_label.setObjectName("code_pic_label")
        self.verticalLayout.addWidget(self.code_pic_label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.code_lineEdit = QtWidgets.QLineEdit(token_Dialog)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.code_lineEdit.setFont(font)
        self.code_lineEdit.setObjectName("code_lineEdit")
        self.horizontalLayout.addWidget(self.code_lineEdit)
        self.buttonBox = QtWidgets.QDialogButtonBox(token_Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout.addWidget(self.buttonBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(token_Dialog)
        self.buttonBox.accepted.connect(token_Dialog.accept)
        self.buttonBox.rejected.connect(token_Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(token_Dialog)

    def retranslateUi(self, token_Dialog):
        _translate = QtCore.QCoreApplication.translate
        token_Dialog.setWindowTitle(_translate("token_Dialog", "Dialog"))
        self.msg_label.setText(_translate("token_Dialog", "请输入验证码"))
        self.refresh_button.setText(_translate("token_Dialog", "看不清？换一张"))
