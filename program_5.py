# Program #5: Bank Balance
# Write a program that asks the user to enter the amount that he or she has budgeted for a month.
# A loop should then prompt the user to enter each of his or her expenses for the 
# month and keep a running total. (Enter 0 to exit the loop)  
# When the loop finishes, the program should display the amount that the 
# user is over or under budget.

def main():
    budget = 0.0
difference = 0.0
spent = 1.0         #initialize for while loop
total = 0.0

    ###################
budget = int(input('Enter the amount of money you budgeted for the month: '))
while spent != 0:
    spent = int(input("Enter the cost of your expense (enter 0 to end): "))
    total = total + spent

if total > budget:
    difference = total - budget
    print("You are over budget by $", difference)
else:
    difference = budget - total
    print("You are under budget by $", difference)


if __name__ == '__main__':
    main()