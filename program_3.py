# Program #3: Average Rainfall
# Write a program that uses nested loops to collect data and calculate the average 
# rainfall over a period of years.  
# The program should first ask for the number of years.  
# The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month.  
# Each iteration of the inner loop will ask the user for inches of rainfall for each month.  
# After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.

def main():
    ######################
    number_years = int(input("Enter the number of years: "))
    total = 0


    for years in range(number_years):
        for months in range(12):
            inches = int(input("Enter the number of inches of rainfall for this month: "))
            total = total + inches

    number_months = number_years * 12
    average_rainfall = total / number_months

    print("Number of months: ", number_months)
    print("Total inches of rainfall: ", total)
    print("Average rainfall per month in inches: ", average_rainfall)
    ######################    


if __name__ == '__main__':
    main()