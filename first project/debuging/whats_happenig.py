class BankAccount:
	def __init__(self, account_number, balance=0):
		self.account_number = account_number
		self.balance = balance

	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			return True
		return False

	def withdraw(self, amount):
		if 0 < amount <= self.balance:
			self.balance -= amount
			return True
		return False

	def get_balance(self):
		return self.balance

def create_account():
	account_number = input("Enter account number: ")
	initial_balance = float(input("Enter initial balance: "))
	return BankAccount(account_number, initial_balance)

def main():
	accounts = {}
	while True:
		print("\n1. Create Account")
		print("2. Deposit")
		print("3. Withdraw")
		print("4. Check Balance")
		print("5. Exit")
		
		choice = input("Enter your choice (1-5): ")
		
		if choice == '1':
			account = create_account()
			accounts[account.account_number] = account
			print(f"Account {account.account_number} created successfully!")
		
		elif choice in ['2', '3', '4']:
			account_number = input("Enter account number: ")
			if account_number in accounts:
				account = accounts[account_number]
				if choice == '2':
					amount = float(input("Enter deposit amount: "))
					if account.deposit(amount):
						print(f"Deposited ${amount:.2f} successfully!")
					else:
						print("Invalid deposit amount.")
				elif choice == '3':
					amount = float(input("Enter withdrawal amount: "))
					if account.withdraw(amount):
						print(f"Withdrawn ${amount:.2f} successfully!")
					else:
						print("Invalid withdrawal amount or insufficient funds.")
				else:
					print(f"Current balance: ${account.get_balance():.2f}")
			else:
				print("Account not found.")
		
		elif choice == '5':
			print("Thank you for using our banking system. Goodbye!")
			break
		
		else:
			print("Invalid choice. Please try again.")

if __name__ == "__main__":
	main()