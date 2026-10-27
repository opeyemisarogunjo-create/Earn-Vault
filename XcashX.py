import json
import os
import pyfiglet


gen_pin = "5775"
available_balance = 5000000000000
unit = "💲"
savings_balance = 0.0
auto_save_percent = 0
pending_savings = 0.0

data_file = "xcashx.json"

def save_data():
    data = {
        "available_balance": available_balance,
        "savings_balance": savings_balance,
        "auto_save_percent": auto_save_percent,
        "pending_savings": pending_savings,
    }

    with open(data_file, "w") as file:
        json.dump(data, file, indent=4)

#DEFINITIONS

#Account Balance
def acct_bal(balance):
    if pin():
        print(f"You have {unit}{balance} left in your account!")
    return balance

#Loan Section

#Loan Section
def loan_section(balance):
    print(pyfiglet.figlet_format("LOAN SECTION", font="small"))
    print("Fill in the information below:")

    try:
        loan_amount = int(input("LOAN AMOUNT: "))
    except ValueError:
        print("Please enter a valid whole number.")
        return balance

    if loan_amount <= 0 or loan_amount >= 1000:
        print("Sorry, you can only borrow below $1000.")
    else:
        balance = balance + loan_amount
        print(f"Loan successful. Your account has been credited with {unit}{loan_amount}.")

    return balance


#Savings Section
def savings(balance):
    print(pyfiglet.figlet_format("SAVINGS", font = "small"))
    print("Below are options for different forms of savings.")
    print("1. Deposit.")
    print("2. Auto-Save.")
    print("3. Exit")

    
    while True:
            try:
                savings_option = int(input("> "))
            except ValueError:
                print("Please enter a valid option.")
                continue

            if savings_option == 1:
                balance = deposit(balance)
            
            elif savings_option == 2:
                balance = auto_save_menu(balance)
            
            elif savings_option == 3:
                return

            return balance


#Deposit

#Deposit
def deposit(balance):
    print(pyfiglet.figlet_format("DEPOSIT", font="small"))
    print("Type in amount you want to deposit:")

    try:
        deposit_amount = int(input("> "))
    except ValueError:
        print("Please enter a valid whole number.")
        return balance

    if deposit_amount <= 0:
        print("Error! Amount must be greater than zero!")
        return balance

    if deposit_amount > balance:
        print("Error! Amount is more than your balance!")
        return balance

    print(f"{first_name}, are you sure you want to proceed? yes or no.")
    dep_confirmation = input("> ").lower()

    if dep_confirmation == "yes":
        balancex = balance - deposit_amount
        global savings_balance
        savings_balance += deposit_amount
        print(f"{middle_name}, {unit}{deposit_amount} has successfully been deposited into your savings.")
        print(f"Savings balance: {unit}{deposit_amount}")
        print(f"Account balance: {unit}{balancex}")
        return balancex

    elif dep_confirmation == "no":
        print("Operation cancelled!")

    elif dep_confirmation != "yes" or "no":
        print("Error! Invalid Input !")

    print("Deposit cancelled!")
    return balance





#Auto Save
def auto_save_menu(balance):
    print(pyfiglet.figlet_format("AUTO SAVE", font="small"))
    print("With this feature, you can set a fixed percentage or amount to be deducted from your account and saved.")
    print("Type in how you want the money to be saved:")
    print("1. Fixed Percent.")
    print("2. Fixed Amount.")
    print("3. Exit")

    try:
        auto_save_option = int(input("> "))
    except ValueError:
        print("Please enter a valid option.")
        return balance

    if auto_save_option == 1:
        balance = fixed_percent(balance)

    elif auto_save_option == 2:
        print("Fixed Amount: Coming Soon...")

    elif auto_save_option == 3:
        return

    else:
        print("Invalid option.")

    return balance

# Auto Save
def auto_save(amount):
    global savings_balannce

    savings_amount = round(amount * auto_save_percent / 100, 2)
    savings_balance = round(pending_savings + savings_amount, 2)

    return savings_amount        




#Fixed Percent

def fixed_percent(balance):
    global auto_save_percent

    print("Type in the percent you want to auto save.")
    print("NOTE: Choice is from 1 to 100.")

    try:
        fixed_percent_choice = int(input("> "))
    except ValueError:
        print("Please enter a valid whole number.")
        return balance

    if fixed_percent_choice < 1 or fixed_percent_choice > 100:
        print("Invalid percentage. Choose between 1 and 100.")
        return balance

    auto_save_percent = fixed_percent_choice

    print(f"{first_name}, Auto Save is now set to {auto_save_percent}%.")

    return balance



# Process Pending Savings
def process_pending_savings(balance):
    global pending_savings, savings_balance

    if pending_savings <= 0 or balance <= 0:
        return balance

    savings_transfer = min(balance, pending_savings)

    balance = balance - savings_transfer
    savings_balance = round(savings_balance + savings_transfer, 2)
    pending_savings = round(pending_savings - savings_transfer, 2)

    print(f"Transferred to savings: {unit}{savings_transfer:.2f}")
    print(f"Pending savings: {unit}{pending_savings:.2f}")

    return balance

    

#Fixed Amount


# PIN Checker
def pin():
    print("Enter your PIN below:")
    enter_pin = input("> ")

    if enter_pin == gen_pin:
        return True
    else:
        print("Wrong PIN! Try Again! You have 4 trials left!")

    pin_trial = 4
    
    while pin_trial > 0:
        print("Try again")
        enter_pin = input("> ")
        pin_trial = pin_trial - 1    
        if enter_pin == gen_pin:
            return True

    return False

# Account Zone
def account(balance):
    print(pyfiglet.figlet_format("ACCOUNT STATUS", font="small"))
    print("Select your options from below:")
    print("1. Account Balance.")
    print("2. Loan Section.")
    print("3. Savings.")
    print("4. Exit")

    while True:
        try:
            account_selection = int(input("> "))

        except ValueError:
            print("Invalid Input!")
            continue    
    
        if account_selection == 1:
            balance = acct_bal(balance)

        elif account_selection == 2:
            balance = loan_section(balance)

        elif account_selection == 3:
            balance = savings(balance)

        elif account_selection == 4:
            return

        else:
            print("This selection is Invalid!!!")
            continue

        return balance


#Food Market
def food_market(balance):
    print(pyfiglet.figlet_format("FOOD MARKET", font="small"))
    print("Welcome to the Market, here you will be able to purchase items for use:")
    print("Use numbers to select the item(s) you want starting from 0")
    
    items = [
    ["Bottled Water", 19.99],
    ["Jam", 29.99],
    ["Bread", 39.99],
    ["Sugar", 35.99],
    ["Butter", 30]
    ]
    print(items)


    # Food Market Selection
    
    while True:
        try:
            food_market_selection1 = int(input("Item: "))

        except ValueError:
            print("Invalid Input! Try Again")
            continue
    
        while True:
            try:
                food_market_selection2 = int(input("Quantity: "))

            except ValueError:
                print("Invalid Input Try Again!")
                continue
    
            item = items[food_market_selection1][0]
            price = items[food_market_selection1][1]

            total_price = price * food_market_selection2
    
            print(f"{food_market_selection2} {item}, {unit}{total_price} will be deducted from your money")
    
            if pin():
                if balance < total_price:
                    print("Insufficient Balance!!!")

                else:
                    balance = balance - total_price
                    round(balance)
                    print(f"Transaction Successful. You have {unit}{balance:.2f}.")
                    savings_amount = auto_save(total_price)

                    global_placeholder = None  
                    
                    print("Do you want to buy more products? yes/no")

                    sel = input("> ").strip().lower()

                    if sel.lower() == "yes":
                        return balance

                    elif sel.lower() == "no":
                        break

                    else:
                        print("Invalid selection!")
                        continue
    
            return balance


#Automobile Market
def automobile_market(balance):
    print("AUTOMOBILE MARKET")
    print("Select a vehicle from below:")
    print("Use numbers to select the item(s) you want starting from 0")

    cars = [["Toyota corolla", 25000],
            ["Honda Civic", 28000],
            ["Toyota Camry", 32000],
            ["BMW 3 Series", 45000],
            ["Mercedes-Benz C-Class", 50000]
            ]
    print(cars)

    
    #Automobile Market Selection
    automobile_market_selection1 = int(input("Item "))
    automobile_market_selection2 = int(input("Quantity "))

    car = cars[automobile_market_selection1][0]
    price = cars[automobile_market_selection1][1]

    total_price_mobile = price * automobile_market_selection2

    print(f"{automobile_market_selection2} {car}, {unit}{total_price_mobile} will be deducted from your money.")
    
    if pin():
        if balance < total_price_mobile:
            print("Insufficient Balance!!!." \
            " If you wish to proceed, you can take loan from the Loan Section")

        else:    
            balance = balance - total_price_mobile
            print(f"Transaction Successful. You have {unit}{balance}.")
            
        
    return balance






# Market Section
def market(balance):
    print(pyfiglet.figlet_format("MARKET", font="small"))
    print("Select the category of Market you will like to visit:")
    print("1. Food Market")
    print("2. Automobile Market")
    print("3. Exit")
    
    while True:        
        try:    
            market_selection = int(input("> "))

        except ValueError:
            print("Invalid Input! Try Again!")
            continue

        if market_selection == 1:
            balance = food_market(balance)

        elif market_selection == 2:
            balance = automobile_market(balance) 

        elif market_selection == 3:
            return

        else:
            print("Feature unavailable! Try Again!")
            continue
        
        return balance


# Jobs Zone

# Job1
def job1(balance):
    if job == 1:
        print(pyfiglet.figlet_format("RESTAURANT X", font="small"))
        print(f"Congratulations {middle_name.upper()} you got the job!.")
        print("Fill in the of hours you can work below. " \
        "NOTE: Hours of work is between 1 to 7 hours!.")
        job1_duration = int(input("> "))

        if job1_duration < 1 or job1_duration > 7:
            print("Error! " \
            "Reason: Duration Out of Range!")
            return balance
        
        else:
            print("Successful!!!")
            print("Time is counting ;)")

        total_salary1 = j1 * job1_duration
        


        time = job1_duration

        while time > 0:
            print("Working")
            time = time - 1

        print(f"Job complete and your account has been credited with {unit}{total_salary1:.2f}.")

        savings_amount = auto_save(total_salary1)

        saved_amount = auto_save(total_salary1)

        balance = balance + total_salary1 - saved_amount

        print(f"Auto Save: {unit}{saved_amount:.2f} added to savings.")

        balance = process_pending_savings(balance)

        print(f"New balance is {unit}{balance}.")
        print("Select what you want to do next from below:")
        print("1. Continue Job")#done*
        print("2. Main Menu")#done*
        print("3. Market")#done*
        print("4. Exit")#done*

        # FINISHED: s3 options have been coded
        
        while True:
            try:    
                job1_selection = int(input("> "))
            except ValueError:
                print("Invalid Input! Try Again!")
                continue
        
        
            if job1_selection == 1:
                balance = job1(balance)
        
            elif job1_selection == 3:
                balance = market(balance)

            elif job1_selection == 4:
                return

            #returns balance    
            return balance


# Job2
def job2(balance):
    if job == 2:
        print(pyfiglet.figlet_format("MR. BEAN COFFEE SHOP", font="small"))
        print(f"Congratulations {middle_name.upper()}. You are now the Receptionist at Mr. Bean, work has started.")
        print("Fill in the hours you'll be able to work with:" \
        "Note: The minimum timing is 3 and max is 10.")
        
        while True:
            try:
                job2_duration = int(input("> "))

            except ValueError:
                print("Invalid Input! Try Again!")
                continue


            if job2_duration <3 or job2_duration > 10:
                print("Error! \nReason: Out of Range!")
                return balance

            else:
                print("Successful!!! work starts now!")
                print("Time is counting ;)")

            total_salary2 = j2 * job2_duration

            timei = job2_duration

            while timei > 0:
                print("Working")
                timei = timei - 1

            print(f"Job complete and your account has been credited with {unit}{total_salary2:.2f}.")

            savings_amount = auto_save(total_salary2)
            saved_amount = auto_save(total_salary2)
            balance = balance + total_salary2 - saved_amount
            print(f"Auto Save: {unit}{saved_amount:.2f} added to savings.")
            balance = process_pending_savings(balance)  

            print(f"New balance is {unit}{balance}.")
            print("You can now use the money.")
            print("Select your option from below:")
            print("1. Continue Job")#done*
            print("2. Main Menu")#done*
            print("3. Market")#done*
            print("4. Exit")#done*
            break
            
            #FINISHED: s3 options have been coded
        
        while True:
            try:
                job2_selection = int(input("> "))
            except ValueError:
                print("Invalid Input! Try Again!")
                continue
        
            if job2_selection == 1:
                balance = job2(balance)
        
            elif job2_selection == 3:
                balance = market(balance)

            elif job2_selection == 4:
                return

            #returns balance
            return balance


# Title
print(pyfiglet.figlet_format("EARN VAULT", font="small"))

# greeting
print("Welcome to EARN VAULT")

# filling of info
print("Fill in the details below respectively to continue:")


#personal info
first_name = input("FIRST NAME: ")
middle_name = input("MIDDLE NAME: ")
last_name = input("LASTNAME: ")

while True:
    try:
        age = int(input("AGE: "))

    except ValueError:
        print("Invalid Input! Try Again")
        continue

# condition for info
    if age < 18:
        print("You are below 18 years of age access denied!")
        exit()

# else
    else:
        print("Enter Phone Number below")
        phone_number = input("PHONE NUMBER: ")
        address = input("ADDRESS: ")

        print("Account Creation Successful.")

        print(f"Your pin is, {gen_pin} don't forget it")

        # initial balance
        print(f"Dear {first_name} {middle_name} {last_name} You have been credited with {unit}{available_balance}.")
        break
    




while True:

    # MAIN MENU
    print(pyfiglet.figlet_format("MAIN MENU", font="small"))
    #Options
    print("Choose from the options below:")
    print("1. Job.")
    print("2. Market.")
    print("3. Account.")
    print("4. Exit.")
    print("\n")
    

    try:    
        main_menu = int(input("> "))

    except ValueError:
        print("Invalid selection! Try Again!")
        continue

    if main_menu == 1:

        print("1. Work as a Waiter at a Food restaurant: ~ $20/hour for hours")
        j1 = int(20)
          

        print("2. Receptionist at a Coffee shop names Mr. Bean. ~ $15/hour for hours")
        j2 = int(15)

    elif main_menu == 2:
    
            # Market
        available_balance = market(available_balance)
    
    elif main_menu == 3:
    
        #Account Status
        available_balance = account(available_balance)
    
    
    
    elif main_menu == 4:
        print(f"Your balance still remains {unit}{available_balance}")
        exit()
    
    
    while True:  
        try:
            job = int(input("> "))

        except ValueError:
            print("Invalid selection! Try again")
            continue

        # Job1
        if job == 1:
            available_balance = job1(available_balance)

        # Job2
        elif job == 2:
            available_balance = job2(available_balance)