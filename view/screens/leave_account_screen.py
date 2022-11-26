from model.user import User
from PyQt5.QtWidgets import QMainWindow


class LeaveAccountScreen(QMainWindow):
    user = User()
    
    def open_registration_screen(self):
        self.registration_screen.open()