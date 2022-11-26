from controller.controller import Controller
from model.record import Record
from view.pyqtiu.ShowScreenWindow import Ui_ShowRecordScreenUI
from PyQt5.QtWidgets import QMainWindow


class ShowRecordScreen(QMainWindow):
    record = Record()
    controller = Controller()
    
    def __init__(self):
        super(ShowRecordScreen, self).__init__()
        self.ui = Ui_ShowRecordScreenUI(self)
    
    def open_user_screen(self, user):
        self.user_screen.open(user)