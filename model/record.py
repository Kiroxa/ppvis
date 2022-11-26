from model.income import Income
from model.outcome import Outcome
from model.user import User


class Record:
    incomes = Income()
    outcomes = Outcome()
    user = User()
    
    def add_income(self, income):
        self.incomes.add_income(income)
        
    def add_outcome(self, outcome):
        self.outcomes.add_outcome(outcome)
        
    def change_income(self, income):
        self.incomes.change_income(income)
        
    def change_outcome(self, outcome):
        self.outcomes.change_outcome(outcome)
        
    def show_income(self, income):
        return self.incomes.show_income(income)
    
    def show_outcome(self, outcome):
        return self.outcomes.show_outcome(outcome)
    
    def delete_income(self, income):
        self.incomes.delete_income(income)
        
    def delete_outcome(self, outcome):
        self.outcomes.delete_outcome(outcome)
    
    