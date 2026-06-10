from abc import ABC, abstractmethod

class CalculationStrategy(ABC):

    @abstractmethod
    def calculate(self, current_balance: float, amount: float) -> float:
        pass

class IncomeStrategy(CalculationStrategy):

    def calculate(self, current_balance: float, amount: float) -> float:
        return current_balance + amount
    
class ExpenseStrategy(CalculationStrategy):
    def calculate(self, current_balance: float, amount: float) -> float:
        return current_balance - amount