from model.record import Record
from controller.controller import Controller
from view.pyqtiu.DeleteRecordWindow import Ui_DeleteRecordScreenUI
from PyQt5.QtWidgets import QMainWindow


class DeleteRecordScreen(QMainWindow):
    record = Record()
    controller = Controller()
    
    def __init__(self):
        super(DeleteRecordScreen, self).__init__()
        self.ui = Ui_DeleteRecordScreenUI(self)
    
    def open_user_screen(self, user):
        self.user_screen.open(user)