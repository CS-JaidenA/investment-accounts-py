#!/usr/bin/env python

import random

# generate accounts

accounts: list[float] = list(range(20))

for account in accounts:
	accounts[account] = float(random.randint(0, 5000))

def addToAccount(index, amount):
	accounts[index] += amount
	return accounts[index]

# menu loop

while True:
	print()

	print("MAIN MENU")
	print("1: Print Accounts")
	print("2: Deposit")
	print("3: Withdrawal")
	print("4: Count Under $2000")
	print("5: Generous Donor")
	print("6: Hacker Attack")
	print("7: Exit")

	option: str = input("Enter Option #: ")

	print()

	match option:
		case '1':
			print("ACCOUNT BALANCES")
			for i in range(len(accounts)):
				print(f"Account {i}: ${accounts[i]}")
		case '2':
			print("DEPOSIT")
			index: int = int(input("Enter account #: "))
			amount: float = float(input("Enter amount to deposit: $"))

			print(f"Account {index} Previous Balance: {accounts[index]}")
			print(f"Account {index} New Balance: ${addToAccount(index, amount)}")
		case '3':
			print("WITHDRAWAL")
			index: int = int(input("Enter account #: "))
			amount: float = float(input("Enter amount to withdraw: $"))

			if accounts[index] - amount >= 0:
				print(f"Account {index} Previous Balance: ${accounts[index]}")
				print(f"Account {index} New Balance: ${addToAccount(index, -amount)}")
			else:
				print("Sorry, insufficient funds.")
		case '4':
			print("COUNT UNDER $2000")

			count: int = 0

			for i in range(len(accounts)):
				if accounts[i] <= 2000:
					print(f"Account {i}: ${accounts[i]}")
					count += 1

			print(f"Accounts with less than $2000: {count}")
		case '5':
			print("GENEROUS DONOR")

			for i in range(len(accounts)):
				if accounts[i] < 2000:
					print(f"Account {i} Previous Balance: ${accounts[i]}")
					print(f"Accounts {i} New Balance: ${addToAccount(i, 500)}")
		case '6':
			print("HACKAER ATTACK")

			total: float = 0

			# for account in accounts would create a copy of, not a reference to the account

			for i in range(len(accounts)):
				total += 0.05 * accounts[i]
				accounts[i] *= 0.95

			print(f"Total stolen is: ${total}")
		case '7':
			break
		case _:
			print("Invalid option. Try again...")
