from controller.controller import Controller
from view.pyqtiu.RegistrationWindow import Ui_RegistrationScreenUI
from PyQt5.QtWidgets import QMainWindow


class RegistrationScreen(QMainWindow):
    controller = Controller()
    
    def __init__(self):
        super(RegistrationScreen, self).__init__()
        self.ui = Ui_RegistrationScreenUI(self)
    
    def open_user_screen(self, user):
        self.user_screen.open(user)