"""
Description: Total sales graph using matplotlib library for QAP 4 project 1

Author: Nathaniel Lane
Date: March 17th, 2023
"""

#Comment like a pro

#Import matplotlib library as plt
import matplotlib.pyplot as plt

#Create an empty list called Y_Values
Y_Values = []

#Create a for loop to ask the user for total sales for each month of the year
Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']\

#Tell user what the program is
print()
print("==================================")
print("----Total sales for each month----")
print("==================================")

#Create the for loop to gather all sales for each month and add them to the Y_Values list
for month in Months:
    while True:
        print()
        try:
            Sales = float(input(f"Enter total sales for {month}: "))
            if Sales < 0:
                print()
                print("Sales amount must not be a negative number - please reenter")
        except:
            print()
            print("Invalid input - please enter a number")
        else:
            Y_Values.append(Sales)
            break

#Create a list of abbreviated month names to use as x-axis labels
X_Values = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Create a figure and axis object
fig, ax = plt.subplots()

#Create a bar plot with the Y_Values as the heights and the lsit of abbreviated months as the x-axis labels
ax.bar(X_Values, Y_Values)

# Set the title and axis labels
ax.set_title('Total Sales by Month')
ax.set_xlabel('Month')
ax.set_ylabel('Total Sales ($)')

#Show the plot
plt.show()