class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f'Your current balance is: Rs {self.balance}')  
    def deposit(self, amount):
        if amount <= 0:
            print('Error: Deposit amount should be greater than zero')
        else:
            self.balance = self.balance + amount  
            print(f'Rs. {amount} has been deposited successfully')
            self.check_balance()

    def withdraw(self, amount):
        if amount <= 0:
            print('Withdrawal amount must be greater than zero')
        elif amount > self.balance:
            print('Insufficient Balance')
        else:
            self.balance = self.balance - amount
            print(f'Rs. {amount} has been withdrawn successfully')
            self.check_balance()

def main():
    atm = ATM(balance=1000)
    while True:
        print('\nWelcome to NMB Bank ATM')
        print('1. Check Balance')
        print('2. Deposit Money')
        print('3. Withdraw Money')
        print('4. Exit')

        choice = input('Enter your choice (1-4): ')

        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            try:
                amount = float(input('Enter amount to deposit: '))
                atm.deposit(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '3':
            try:
                amount = float(input('Enter amount to withdraw: '))
                atm.withdraw(amount)
            except ValueError:
                print("Invalid amount. Please enter a number.")
        elif choice == '4':
            print('Goodbye! Have a nice day.')
            break
        else:
            print('Invalid choice. Please try again.')

if __name__ == '__main__':
    main()
