from PyQt5.QtWidgets import QStackedWidget
from PyQt5.QtWidgets import QMessageBox

from view.screens.add_record_screen import AddRecordScreen
from view.screens.change_record_enter_screen import ChangeRecordEnterScreen
from view.screens.change_account_screen import ChangeAccountScreen
from view.screens.change_record_scree import ChangeRecordScreen
from view.screens.delete_record_screen import DeleteRecordScreen
from view.screens.my_account_screen import MyAccountScreen
from view.screens.registration_screen import RegistrationScreen
from view.screens.self_cabinet import SelfCabinet
from view.screens.show_record_screen import ShowRecordScreen
from view.screens.user_screen import UserScreen


class UI:
    def __init__(self):
        self.widgets = QStackedWidget()
        
        self.current_view = None
        self.error = QMessageBox()
        
        self.add_record_view = AddRecordScreen()
        self.change_record_enter_view = ChangeRecordEnterScreen()
        self.change_account_view = ChangeAccountScreen()
        self.change_record_view = ChangeRecordScreen()
        self.delete_record_view = DeleteRecordScreen()
        self.my_accout_view = MyAccountScreen()
        self.registration_view = RegistrationScreen()
        self.self_cabinet_view = SelfCabinet()
        self.show_record_view = ShowRecordScreen()
        self.user_screen_view = UserScreen()
        
        self.init_view()
        self.init_buttons()
    
    def init_buttons(self):
        self.user_screen_view.ui.registration_pushButton.clicked.connect(self.enter_registration)
        self.user_screen_view.ui.enter_pushButton.clicked.connect(self.enter_account)
        
        self.registration_view.ui.crete_account_pushButton.clicked.connect(self.enter_account)
        
        self.my_accout_view.ui.delete_account_pushButton.clicked.connect(self.delete_account)
        self.my_accout_view.ui.leave_account_pushButton.clicked.connect(self.leave_account)
        self.my_accout_view.ui.change_account_pushButton.clicked.connect(self.change_account)
        self.my_accout_view.ui.back_pushButton.clicked.connect(self.back_self_cabinet)
        
        self.change_account_view.ui.back_pushButton.clicked.connect(self.confirm_account_change)
        self.change_account_view.ui.save_pushButton.clicked.connect(self.confirm_account_change)
        
        self.self_cabinet_view.ui.my_account_pushButton.clicked.connect(self.confirm_account_change)
        self.self_cabinet_view.ui.add_record_pushButton.clicked.connect(self.enter_add_record)
        self.self_cabinet_view.ui.show_record_pushButton.clicked.connect(self.enter_show_record)
        self.self_cabinet_view.ui.delete_record_pushButton.clicked.connect(self.enter_delete_record)
        self.self_cabinet_view.ui.edit_record_pushButton.clicked.connect(self.enter_edit_record)
        
        self.show_record_view.ui.back_pushButton.clicked.connect(self.back_self_cabinet)
        self.add_record_view.ui.back_pushButton.clicked.connect(self.back_self_cabinet)
        self.delete_record_view.ui.back_pushButton.clicked.connect(self.back_self_cabinet)
        self.change_record_view.ui.back_pushButton.clicked.connect(self.back_self_cabinet)
        
        self.add_record_view.ui.add_pushButton.clicked.connect(self.back_self_cabinet)
        self.delete_record_view.ui.delete_pushButton.clicked.connect(self.back_self_cabinet)
        self.change_record_view.ui.change_pushButton.clicked.connect(self.back_self_cabinet)
        
    def enter_add_record(self):
        self.current_view = self.add_record_view
        self.widgets.setCurrentWidget(self.current_view)
        
    def enter_show_record(self):
        self.current_view = self.show_record_view
        self.widgets.setCurrentWidget(self.current_view)
        
    def enter_delete_record(self):
        self.current_view = self.delete_record_view
        self.widgets.setCurrentWidget(self.current_view)
    
    def enter_edit_record(self):
        self.current_view = self.change_record_view
        self.widgets.setCurrentWidget(self.current_view)
    
    def enter_registration(self):
        self.current_view = self.registration_view
        self.widgets.setCurrentWidget(self.current_view)
        
    def enter_account(self):
        self.current_view = self.my_accout_view
        self.widgets.setCurrentWidget(self.current_view)
        
    def delete_account(self):
        self.error.setWindowTitle("АККАУНТ УДАЛЕН")
        self.error.setText("ВАШ АККАУНТ УДАЛЕН")
        self.error.setIcon(QMessageBox.Information)
        self.error.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        self.error.exec_()
        
    def leave_account(self):
        self.error.setWindowTitle("ВЫХОД ИЗ АККАУНТА")
        self.error.setText("ВЫ ВЫШЛИ ИЗ АККАУНТА")
        self.error.setIcon(QMessageBox.Information)
        self.error.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        self.error.exec_()
        
    def change_account(self):
        self.current_view = self.change_account_view
        self.widgets.setCurrentWidget(self.current_view)
        
    def back_self_cabinet(self):
        self.current_view = self.self_cabinet_view
        self.widgets.setCurrentWidget(self.current_view)
        
    def confirm_account_change(self):
        self.current_view = self.my_accout_view
        self.widgets.setCurrentWidget(self.current_view)
        
    def init_view(self):
        # add widgets
        self.widgets.addWidget(self.add_record_view)
        self.widgets.addWidget(self.change_record_enter_view)
        self.widgets.addWidget(self.change_account_view)
        self.widgets.addWidget(self.change_record_view)
        self.widgets.addWidget(self.delete_record_view)
        self.widgets.addWidget(self.my_accout_view)
        self.widgets.addWidget(self.registration_view)
        self.widgets.addWidget(self.self_cabinet_view)
        self.widgets.addWidget(self.show_record_view)
        self.widgets.addWidget(self.user_screen_view)
        
        self.widgets.setCurrentWidget(self.user_screen_view)
        
        
    def init_app(self):
        # sizes
        self.widgets.setFixedWidth(840)
        self.widgets.setFixedHeight(620)
        
        self.show_windows()
        
    def show_windows(self):
        self.widgets.show()

    def view(self, model, controller):
        self.view.show()
    
    def show_user_view(self):
        self.user_view.show()
    
    def show_registratin_view(self):
        self.registration_view.show()