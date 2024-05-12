import time 

input("Insert Your Card: ")
time.sleep(3)

password  = 2580
pin = int(input("Enter Your Pin: "))
 
Amount = 1000
transaction_history = []

if pin == password:
    while True:
        print('''
                1. Check Balance  
                2. Transactions History  
                3. Withdraw  
                4. Deposit  
                5. Transfer  
                6. Quit
                ''')
        
        try:
            choice = int(input("Enter your Choice: "))
        except:
            print("You entered an invalid choice. Try again")
            continue
        
        if choice == 1:
            print("Your Balance is ", Amount, "/-")
            
        elif choice == 2:
            print("\nTransaction History:")
            for transaction in transaction_history:
                print(transaction)
                
        elif choice == 3:
            withdraw = int(input("Enter Withdraw Amount: "))
            
            if withdraw <= Amount:
                Amount = Amount - withdraw
                transaction_history.append(f"Withdrawn: {withdraw}")
                
                print("Successfully.....")
                print(f"{withdraw}/- is debited from your account.")
                print(f"Now your amount is {Amount}")
            else:
                print(f"Insufficient balance.")
            
        elif choice == 4:
            deposit = int(input("Enter Deposit Amount: "))
            Amount = Amount + deposit
            transaction_history.append(f"Deposited: {deposit}")
            
            print("Successfully.....")
            print(f"{deposit}/- is credited to your account.")
            print(f"Now your amount is {Amount}")
            
        elif choice == 5:
            transfer_amount = int(input("Enter the amount for transfer: "))
            
            if transfer_amount <= Amount:
                transfer_to = input("Enter recipient's account number: ")
                Amount -= transfer_amount
                transaction_history.append(f"Transfer: {transfer_amount} to {transfer_to}")
                
                print("Successfully.....")
                print(f"{transfer_amount}/- is transferred to {transfer_to}")
                print(f"Now your Balance {Amount}")
            else:
                print(f"Insufficient balance.")
        
        elif choice == 6:
            print("Thank you")
            print("Best of Luck....")
            break
        
else:
    print(f"Your {pin} pin is wrong..... Try again")
