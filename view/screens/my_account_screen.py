from view.pyqtiu.MyAccountWindow import Ui_MyAccountScreenUI
from PyQt5.QtWidgets import QMainWindow


class MyAccountScreen(QMainWindow):
    def __init__(self):
        super(MyAccountScreen, self).__init__()
        self.ui = Ui_MyAccountScreenUI(self)