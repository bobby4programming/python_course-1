class Person:
    def __init__( self, first_name, last_name, age, address, phone, email = "", marital_status = "single", middle_name = ""):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.age = age
        self.address = address
        self.phone = phone
        self.email = email
        self.marital_status = marital_status

    def get_person_attribute(self, attribute):
        return getattr(Person, attribute)

class Account(object):
        customers = 0

        def __init__(self, person, bvn,  acct_num, interest_rate = 0, acct_type = "savings", acct_bal = 0):
            self.person = person
            self.bvn = bvn
            self.acct_num = acct_num
            self.acct_type = acct_type
            self.amount = float(acct_bal)
            self.interest_rate = interest_rate
            Account.customers += 1

        @ staticmethod
        def get_num_of_customers():
            return Account.customers

        def deposit(self, amount):
            self.amount += float(amount)
            return self.amount

        def withdraw(self, amount_to_withdraw):
            if (amount_to_withdraw > self.amount) or (amount_to_withdraw - self.amount <= 0):
                return "You don't have enough money on this account"
            self.amount -= float(amount_to_withdraw)
            return self.amount
        
        def balance(self):
            return self.amount
        
        def __calculate_interest(self):
            return float(self.interest_rate / 100) 
        
        def get_customer_interest(self):
            return self.__calculate_interest()
        
class Savings(Account):
    def __init__(self, bonus, max_daily_widthdrawal = 3):
        self.bonus = bonus
        self.max_daily_widthdrawal = max_daily_widthdrawal

class Current(Account):
    def __init__(self, cheque_book, acct_bal = 50000, interest_rate = 3.5):
        self.cheque_book = cheque_book
        self.acct_bal = float(acct_bal)
        self.interest_rate = interest_rate
