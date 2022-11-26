from controller.controller import Controller
from view.pyqtiu.ChangeRecordEnterWindow import Ui_ChangeRecordEnterScreenUI
from PyQt5.QtWidgets import QMainWindow


class ChangeRecordEnterScreen(QMainWindow):
    controller = Controller()
    
    def __init__(self):
        super(ChangeRecordEnterScreen, self).__init__()
        self.ui = Ui_ChangeRecordEnterScreenUI(self)
    
    def open_user_screen(self, user):
        self.user_screen.open(user)
        
    def open_change_record_screen(self):
        self.change_record_screen.open()
