class Transaction:
    def __init__(self, amount, txn_type):
        self.amount = amount
        self.txn_type = txn_type

class AccountHolder:
    def __init__(self, citizen_num, first_name, last_name, age):
        self.citizen_num = citizen_num
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.transactions = []
        self.balance = 0

    def client_info(self):
        print(f"\n--- Account Info ---")
        print(f"Citizen Number: {self.citizen_num}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Current Balance: ${self.balance:.2f}")

    def verify_user(self):
        search_num = input("Enter your citizen number to verify: ")
        return search_num == self.citizen_num

    def deposit(self, amount): 
        if self.verify_user():
            self.balance += amount
            self.transactions.append(Transaction(amount, "deposit"))
            print(f"Deposit of ${amount} successful! New balance: ${self.balance}")
        else:
            print("Verification failed!")

    def withdraw(self, amount):
        if self.verify_user():
            if amount <= self.balance:
                self.balance -= amount
                self.transactions.append(Transaction(amount, "withdrawal"))
                print(f"Withdrawal of ${amount} successful! New balance: ${self.balance}")
            else:
                print("Insufficient funds!")
        else:
            print("Verification failed!")

def main():
    c_num = input("Enter your citizen number: ")
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    age = int(input("Enter your age: "))
    
    user_account = AccountHolder(c_num, f_name, l_name, age)
    
    while True:
        user_account.client_info()
        choice = input("\nEnter 1 to deposit, 2 to withdraw, or 'q' to quit: ")
        
        if choice == '1':
            amt = float(input("Enter deposit amount: "))
            user_account.deposit(amt)
        elif choice == '2':
            amt = float(input("Enter withdrawal amount: "))
            user_account.withdraw(amt)
        elif choice.lower() == 'q':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()