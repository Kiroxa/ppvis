from controller.controller import Controller
from model.budget_manager import BudgetManager
from view.pyqtiu.SelectCabinetWindow import Ui_SelfCabinetUI
from PyQt5.QtWidgets import QMainWindow


class SelfCabinet(QMainWindow):
    controller = Controller()
    budget_manager = BudgetManager()
    
    def __init__(self):
        super(SelfCabinet, self).__init__()
        self.ui = Ui_SelfCabinetUI(self)
    
    def view(self, model, controller):
        self.view.show(model, controller)
        
    def show_user_screen(self, user):
        self.screen.show(user)