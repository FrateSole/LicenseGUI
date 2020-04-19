from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setupUi(self)
        self.show()
        self.offset = None

    def setupUi(self, MainWindow):
        MainWindow.setMinimumSize(QtCore.QSize(370, 323))
        MainWindow.setMaximumSize(QtCore.QSize(370, 323))
        MainWindow.setStyleSheet("background-color: rgb(20, 0, 104);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 110, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(13)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("border-radius: 15px;\n"
                                    "background-color: rgb(255, 255, 255)")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(120, 200, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: green;\n"
                                      "border-radius: 15px;\n"
                                      "color: white")
        self.pushButton.clicked.connect(self.validate)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 30, 272, 30))
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)


        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 170, 150, 16))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("""
        color: red;
        font-family:Verdana;""")
        self.label_4.setObjectName("label_4")


        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:green;\n"
                                 "background: transparent;")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;\n"
                                   "background: transparent;")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:red;\n"
                                   "background: transparent;")
        self.horizontalLayout.addWidget(self.label_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 370, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.close_btn = QtWidgets.QPushButton(self.centralwidget)
        self.close_btn.setGeometry(QtCore.QRect(350, 5, 15, 15))
        self.close_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.close_btn.setStyleSheet("""
        background-color:#e4685d;
        border-radius:7px;
        font-family:Verdana;
        font-size:12px;""")
        self.close_btn.setText("X")
        self.close_btn.clicked.connect(QtWidgets.qApp.quit)

        self.resize_btn = QtWidgets.QPushButton(self.centralwidget)
        self.resize_btn.setGeometry(QtCore.QRect(320, 5, 15, 15))
        self.resize_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.resize_btn.setStyleSheet("""
        background-color:#FFFF00;
        border-radius:7px;
        font-family:Verdana;
        font-size:12px;""")
        self.resize_btn.setText("-")
        self.resize_btn.clicked.connect(self.resize)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "XXX-XXX-XXX-XXX"))
        self.pushButton.setText(_translate("MainWindow", "ACTIVATE"))
        self.label.setText(_translate("MainWindow", "Activate "))
        self.label_2.setText(_translate("MainWindow", "License"))
        self.label_3.setText(_translate("MainWindow", "Key"))
        self.label_4.setText(_translate("MainWindow", ""))

    def resize(self):
        self.showMinimized()
        return
    def validate(self):
        key = self.lineEdit.text()
        if key == "FrateSole":          #DO WHATEVER YOU WANT IN THIS FUNCTION TO VALIDATE THE KEY!
            self.label_4.setStyleSheet("color:green; background: transparent;")
            self.label_4.setText("Key ACTIVATED!")
        else:
            self.label_4.setStyleSheet("color:red; background: transparent;")
            self.label_4.setText("Invalid KEY")

    def mousePressEvent(self, event):
        if event.y() < 35:
            if event.button() == QtCore.Qt.LeftButton:
                self.offset = event.pos()
            else:
                super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.offset is not None and event.buttons() == QtCore.Qt.LeftButton:
            self.move(self.pos() + event.pos() - self.offset)
        else:
            super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        self.offset = None
        super().mouseReleaseEvent(event)

if __name__ == "__main__":
    ui_app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    os._exit(ui_app.exec_())

