from controller.controller import Controller
from view.pyqtiu.AddRecordScreenWindow import Ui_AddRecordScreenUI
from PyQt5.QtWidgets import QMainWindow


class AddRecordScreen(QMainWindow):
    controller = Controller()
    
    def __init__(self):
        super(AddRecordScreen, self).__init__()
        self.ui = Ui_AddRecordScreenUI(self)
    
    def open_user_screen(self, user):
        self.user_screen.open(user)