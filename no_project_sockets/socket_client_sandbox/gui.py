from PyQt5.QtWidgets import QWidget, QPushButton, QTextBrowser


class ClientGUI(QWidget):

    def __init__(self) -> None:
        super().__init__()
        self.initUI()


    def initUI(self):
        self.setFixedSize(300, 400)
        self.setWindowTitle("Depth of Market")
        self.textField()
        self.createButtons()
        self.show()


    def textField(self):
        self.content = QTextBrowser(self)
        self.content.setGeometry(10, 10, 280, 150)


    def createButtons(self):
        self.button = QPushButton("Send", self)
        self.button.setGeometry(40, 170, 100, 50) #(aw=100, ah=50)
