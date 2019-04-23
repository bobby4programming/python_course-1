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
            if (amount_to_withdraw > self.amount) or (self.amount - amount_to_withdraw  <= 0):
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
    def __init__(self, person, bvn,  acct_num, bonus, interest_rate = 1.2, acct_type = "savings", acct_bal = 0, max_daily_widthdrawal = 3):
        self.person = person
        self.bvn = bvn
        self.acct_num = acct_num
        self.amount = bonus
        self.acct_type = acct_type
        self.amount = float(acct_bal)
        self.interest_rate = interest_rate
        self.max_daily_widthdrawal = max_daily_widthdrawal
        Account.customers += 1

class Current(Account):
    def __init__(self, person, bvn,  acct_num, cheque_book, acct_type = "current", acct_bal = 10000, interest_rate = 3.5, min_acct_bal=25000, closedBal=5000, close_the_account=False):
        self.person = person
        self.bvn = bvn
        self.acct_num = acct_num
        self.acct_type = acct_type
        self.amount = float(acct_bal)
        self.cheque_book = cheque_book
        self.acct_bal = float(acct_bal)
        self.interest_rate = interest_rate
        self.min_acct_bal = min_acct_bal
        self.closedBal = closedBal
        self.close_the_account = close_the_account
        Account.customers += 1
    
    def deactivate_the_accounnt(self):
        self.close_the_account = True
        #activate disable mode for the accout
    
    # def withdraw(self, amount_to_withdraw, emergency=False, close_the_account=False):
    #     if (emergency) and self.amount - amount_to_withdraw  <= 10000:
    #         self.amount -= float(amount_to_withdraw

    #     if (close_the_account): # FIX LATER
    #         self.amount -= self.closedBal
    #         self.close_the_account = close_the_account
    #         self.deactivate_the_accounnt()

    #     if (amount_to_withdraw > self.amount) or (self.amount - amount_to_withdraw  <= self.min_acct_bal):
    #         return "You don't have enough money on this account"
    #         self.amount -= float(amount_to_withdraw)
    #     return self.amount

jimmy = Person('Jimmy', 'Kliff', 30, '15 Admun Cresent Wuse II, Abuja', '1809090929', 'jimmy.klliff@gmail.com')
jimm_account = Savings(jimmy, '1092029029', '1003998745', 2500, acct_bal=10000)
# print('withdrawal by Jimmy',jimm_account.withdraw(8000))
# print('Jimmy\'s account balance',jimm_account.balance())
# print(Account.get_num_of_customers())

sandra = Person('Sandra', 'Ayodele', 47, '309 Adetokunbo Ademola Cresent Wuse II, Abuja', '1809890929', 'ayodele.sandra@gmail.com')
sandra_account = Current(sandra, '901234578', "ZX201234567", "current", acct_bal=120000, interest_rate = 3.9)
# print('withdrawal by Sandra',sandra_account.withdraw(78993))
# print('Sandra\'s account balance',sandra_account.balance())
# print(Account.get_num_of_customers())