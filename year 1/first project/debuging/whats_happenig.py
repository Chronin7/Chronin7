#defining stuff 

class BankAccount:
	#initioation?
	def __init__(self, account_number, balance=0):
		self.account_number = account_number
		self.balance = balance
#dposit check valid num
	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			return True
		return False
	#withdraw cheack forvalid num
	def withdraw(self, amount):
		if 0 < amount <= self.balance:
			self.balance -= amount
			return True
		return False
#show the balence of person
	def get_balance(self):
		return self.balance
#creates acount and adds initial balance
def create_account():
	account_number = input("Enter account number: ")
	initial_balance = float(input("Enter initial balance: "))
	return BankAccount(account_number, initial_balance)
#where the meet of the code
def main():
	accounts = {}
	while True:
		#show options
		print("\n1. Create Account")
		print("2. Deposit")
		print("3. Withdraw")
		print("4. Check Balance")
		print("5. Exit")
		
		choice = input("Enter your choice (1-5): ")
		#makes acount and apendids it to a list
		if choice == '1':
			account = create_account()
			accounts[account.account_number] = account
			print(f"Account {account.account_number} created successfully!")
		#the other options
		elif choice in ['2', '3', '4']:
			#ascs for acount num
			account_number = input("Enter account number: ")
			#cheacks if acount exists
			if account_number in accounts:
				account = accounts[account_number]
				#adds munny
				if choice == '2':
					amount = float(input("Enter deposit amount: "))
					#checks if it is a valid num
					if account.deposit(amount):
						print(f"Deposited ${amount:.2f} successfully!")
					else:
						print("Invalid deposit amount.")
				#withdraws monny
				elif choice == '3':
					amount = float(input("Enter withdrawal amount: "))
					#cheacks that it is valid num
					if account.withdraw(amount):
						print(f"Withdrawn ${amount:.2f} successfully!")
					else:
						print("Invalid withdrawal amount or insufficient funds.")
				else:
					#prints curint balance with formationg
					print(f"Current balance: ${account.get_balance():.2f}")
			else:
				print("Account not found.")
		
		elif choice == '5':
			#quits
			print("Thank you for using our banking system. Goodbye!")
			break
		
		else:
			print("Invalid choice. Please try again.")

if __name__ == "__main__":
	main()