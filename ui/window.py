# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'F:\Python\MAP\ui\window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.resize(450, 480)
        MainWindow.setMinimumSize(QtCore.QSize(450, 460))
        MainWindow.setMaximumSize(QtCore.QSize(450, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logo/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 150))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.deleteNote = QtWidgets.QCheckBox(self.groupBox)
        self.deleteNote.setObjectName("deleteNote")
        self.gridLayout.addWidget(self.deleteNote, 1, 0, 1, 1)
        self.createVcut = QtWidgets.QCheckBox(self.groupBox)
        self.createVcut.setObjectName("createVcut")
        self.gridLayout.addWidget(self.createVcut, 2, 0, 1, 1)
        self.selBoardThick = QtWidgets.QLineEdit(self.groupBox)
        self.selBoardThick.setMaximumSize(QtCore.QSize(150, 16777215))
        self.selBoardThick.setObjectName("selBoardThick")
        self.gridLayout.addWidget(self.selBoardThick, 0, 1, 1, 1)
        self.vcut2pdf = QtWidgets.QCheckBox(self.groupBox)
        self.vcut2pdf.setObjectName("vcut2pdf")
        self.gridLayout.addWidget(self.vcut2pdf, 2, 1, 1, 1)
        self.map2pdf = QtWidgets.QCheckBox(self.groupBox)
        self.map2pdf.setObjectName("map2pdf")
        self.gridLayout.addWidget(self.map2pdf, 1, 1, 1, 1)
        self.createMap = QtWidgets.QCheckBox(self.groupBox)
        self.createMap.setObjectName("createMap")
        self.gridLayout.addWidget(self.createMap, 1, 2, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.selAuthor = QtWidgets.QLineEdit(self.groupBox_2)
        self.selAuthor.setObjectName("selAuthor")
        self.gridLayout_2.addWidget(self.selAuthor, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 1, 2, 1, 1)
        self.residualThickness = QtWidgets.QLineEdit(self.groupBox_2)
        self.residualThickness.setObjectName("residualThickness")
        self.gridLayout_2.addWidget(self.residualThickness, 1, 3, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.routTol = QtWidgets.QLineEdit(self.groupBox_2)
        self.routTol.setObjectName("routTol")
        self.gridLayout_2.addWidget(self.routTol, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 2, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_2.addWidget(self.comboBox_2, 2, 3, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.selPath = QtWidgets.QPushButton(self.centralwidget)
        self.selPath.setMinimumSize(QtCore.QSize(0, 30))
        self.selPath.setObjectName("selPath")
        self.horizontalLayout_2.addWidget(self.selPath)
        self.outputPath = QtWidgets.QLineEdit(self.centralwidget)
        self.outputPath.setMinimumSize(QtCore.QSize(0, 30))
        self.outputPath.setObjectName("outputPath")
        self.horizontalLayout_2.addWidget(self.outputPath)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.runProgram = QtWidgets.QPushButton(self.centralwidget)
        self.runProgram.setMinimumSize(QtCore.QSize(0, 30))
        self.runProgram.setToolTip("")
        self.runProgram.setObjectName("runProgram")
        self.horizontalLayout.addWidget(self.runProgram)
        self.exitProgram = QtWidgets.QPushButton(self.centralwidget)
        self.exitProgram.setMinimumSize(QtCore.QSize(0, 30))
        self.exitProgram.setObjectName("exitProgram")
        self.horizontalLayout.addWidget(self.exitProgram)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setEnabled(False)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 40))
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_3.addWidget(self.textBrowser)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 450, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "工程自动化标注"))
        self.label_2.setText(_translate("MainWindow", "自动标注坐标程序"))
        self.groupBox.setTitle(_translate("MainWindow", "基本信息"))
        self.label.setText(_translate("MainWindow", "板厚："))
        self.deleteNote.setText(_translate("MainWindow", "删除标注"))
        self.createVcut.setText(_translate("MainWindow", "大板V-Cut"))
        self.selBoardThick.setToolTip(_translate("MainWindow", "输入板厚"))
        self.selBoardThick.setStatusTip(_translate("MainWindow", "请输入板厚..."))
        self.selBoardThick.setText(_translate("MainWindow", "1.0"))
        self.vcut2pdf.setText(_translate("MainWindow", "V-Cut生成PDF"))
        self.map2pdf.setText(_translate("MainWindow", "图纸生成PDF"))
        self.createMap.setText(_translate("MainWindow", "制作分孔图"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Vcut信息"))
        self.label_3.setText(_translate("MainWindow", "制作人："))
        self.label_4.setText(_translate("MainWindow", "成型方式："))
        self.label_7.setText(_translate("MainWindow", "V-cut余厚："))
        self.label_5.setText(_translate("MainWindow", "成型公差："))
        self.routTol.setText(_translate("MainWindow", "+/-0.13"))
        self.label_6.setText(_translate("MainWindow", "V-cut角度："))
        self.comboBox.setItemText(0, _translate("MainWindow", "CNC+VCUT"))
        self.comboBox.setItemText(1, _translate("MainWindow", "VCUT"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "30"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "45"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "60"))
        self.selPath.setText(_translate("MainWindow", "输出路径："))
        self.runProgram.setStatusTip(_translate("MainWindow", "点击运行脚本..."))
        self.runProgram.setText(_translate("MainWindow", "运行"))
        self.exitProgram.setStatusTip(_translate("MainWindow", "点击退出脚本..."))
        self.exitProgram.setText(_translate("MainWindow", "退出"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">有任何需求请联系-&gt;Robot QQ:502614708,微信号:Robot_0101 </p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">版本信息：Copyright (C) 2022.12.12 V1.01</p></body></html>"))
# import icon_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())