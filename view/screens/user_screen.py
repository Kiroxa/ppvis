from controller.controller import Controller
from view.pyqtiu.UserWindow import Ui_UserScreenUI
from PyQt5.QtWidgets import QMainWindow


class UserScreen(QMainWindow):
    controller = Controller()
    
    def __init__(self):
        super(UserScreen, self).__init__()
        self.ui = Ui_UserScreenUI(self)
    
    def open_show_record_screen(self):
        self.show_record_screen.open()
        
    def open_delete_record_screen(self):
        self.delete_record_screen.open()
        
    def open_edit_record_screen(self):
        self.edit_record_screen.open()    