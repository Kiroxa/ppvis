from model.record import Record 
from view.pyqtiu.ChangeRecordWindow import Ui_ChangeRecordScreenUI
from PyQt5.QtWidgets import QMainWindow


class ChangeRecordScreen(QMainWindow):
    record = Record()
    
    def __init__(self):
        super(ChangeRecordScreen, self).__init__()
        self.ui = Ui_ChangeRecordScreenUI(self)
    
    def show_user_screen(self, user):
        self.user_screen.show(user)
        
    def open_change_record_screen(self):
        self.change_record_screen.open()