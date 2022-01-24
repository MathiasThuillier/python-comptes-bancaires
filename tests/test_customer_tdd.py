"""
    Unit testing for Customer
"""
from pytest_bdd import scenario, given, when, then, parsers, scenarios
import pytest
from src.account import CurrentAccount, SavingsAccount
from src.bank import Bank
from src.customer import Customer
scenarios('./features')
@pytest.mark.cc
class TestCustomer():
    @pytest.fixture
    def customer(self):
        """ Generate a default Customer """
        return Customer("Customer", self.bank(), [self.currentAccount(), self.savingsAccount()])

    def bank(self):
        return Bank("Caisse d'épargne")

    def currentAccount(self):
        return CurrentAccount("Compte courant",max_limit=1000, agios=0.1)

    def savingsAccount(self):
        return SavingsAccount("Livret A")

    def test_bank_customer_name(self, customer
    :Customer) -> None:
        """If bank of customer have name is Caisse d'épargne"""
        assert customer.bank.name == "Caisse d'épargne"

    def test_customer_have_one_account(self, customer
    :Customer) -> None:
        """If customer have one account with money"""
        pass
       #TODO


    #def test_customer_inner_transfert_cc_to_ce(self, customer:Customer) -> None:
    #   """If customer transfert money from cc to ce"""
    #  assert customer.inner_transfert(customer.current_account, customer.saving_account) == True