# Tech With Tim Slot Betting Project
# Input Deposit amount from User - Done
# Input Number of Lines to Bet on from User - Done
# Input Amount for each Line from User. Minimum and Maximum Bet 
# Calculate Total Bet using Number of Lines TIMES Amount

# Maximum Number of Lines available to bet on
MAX_LINES=3
# Minimum and Maximum amount that can be used for betting 
MIN_BET=10
MAX_BET=100

# Function that asks User to enter their Deposit
def acceptDeposit():

    while True:
        amount = input("Enter the total amount of money you wish to deposit in Slot machine: ")

        if amount.isdigit():
              deposit = int(amount);
              if deposit>0:
                  break
              else:
                  print("You need to deposit some money in order to use Slot machine. Please enter an amount greater than zero.");
        else:
            print("Please deposit money, not alphabets.");

    return deposit;
# End of Function

# Function that asks User to enter Number of Lines to Bet On
def acceptNoOfLines():

    while True:
        numberL = input("Enter the exact number of Lines you wish to make bets on. Min: 1, Max: " + str(MAX_LINES) + " : ")

        if numberL.isdigit():
            no_Of_Lines = int(numberL);
            if  1 <= no_Of_Lines <= MAX_LINES:
#                no_Of_Lines >= 1 and no_Of_Lines <= MAX_LINES:
                break
            else:
                print("Number of Lines should be between 1 and " + str(MAX_LINES))
        else:
            print("Betting Lines are numeric, not alphabetical.");

    return no_Of_Lines;
# End of Function



#deposit = acceptDeposit();

no_Of_Lines = acceptNoOfLines();

#print("Total Deposit: ", deposit);

print("Number of Lines: ", no_Of_Lines);

