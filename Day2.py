'''*************Tip calculator with the Bill Split*********'''

print("Welcome to the tip calculator\n")

bill = float(input("What was the total Bill $$ \n"))

tip = int(input("Enter the what percent of tip would you like to give? 5 , 10 , 12 , or 15?\n "))
person = int(input("Enter the number of people to split the bill?\n"))

bill_with_tip = tip/100 * bill + bill

final_bill = bill_with_tip / person

print(f"Each person should pay {final_bill} ")