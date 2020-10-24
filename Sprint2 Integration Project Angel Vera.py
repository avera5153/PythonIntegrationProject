# Angel Vera
# Integration project
# This Integration Project will focus shopping in a convenience store setting.
# Individual who helped greatly (Thank you very much!): Jairo Garciga
#Notable contributions: product_list line #45, function locations at top

#Function to begin the introduction message of the program.
def intro_message():
    print("Welcome to the Interproject convenience store! ")
    print("Please enter required information below...")
#Function to easily print forty dashes for a more readable receipt look.
def receipt_cutoff():
    print("-" * 40)
def calculate_points(new_money):
    # Exponent gives compound interest for points every purchase.
    points = (new_money // 1) ** 1.005
    return points
intro_message()
# Name of person
name = input("What is your name? ")
print("Hello", name + "!", "Glad you are with us!")

money = float(input(
    "How much money have you brought?"))  # How much money the person brought

# Too little money asks for money again in order to not pay the customer.
while money < 1.56:
    print(
        "Unfortunately we would be giving you money, and that "
        "would be illegal. Please find just a bit more cash.")
    money = float(input("How much money have you brought?"))
print("\n")
if money > 0 and money < 100:
    print("You have brought $", format(money, "0.2f"), sep='')
else:  # Exclaims about how the customer brought a large amount of money.
    print(
        "Wow! You sure have brought quite a lot of money! "
        "We hope that you spend it with us!")

print("\n")

# Variables for each of the items as well as discounts or tax rates.
wrench = 5.49
churro = 3.49
energy_drink = 2.99
soda = 1.99
chips = 1.49

# Printing the total list of items.
print(
    "Choose what items to buy! Please choose how many "
    "items you would like as it progresses!")
product_list = ["Wrench $5.49", "Churro $3.49", "Energy Drink $2.99",
                "Soda $1.99", "Chips $1.49 "]
for x in range (0, len(product_list))  :
    print(product_list[x])

receipt_cutoff()
print("\n")

num_wrench = int(input("How many wrenches would you like? "))
num_churro = int(input("How many churros would you like? "))
num_energy_drink = int(input("How many energy drinks would you like?"))
num_soda = int(input("How many sodas would you like?"))
num_chips = int(input("How many chips would you like?"))
# subTotal is total price of every item before tax, added with + operator.
# Also multiplied by the * operator.

sub_total = (wrench * num_wrench) + (churro * num_churro) + (
        energy_drink * num_energy_drink) + (soda * num_soda) + (
                    chips * num_chips)
total_items = num_wrench + num_churro + num_energy_drink + num_soda + num_chips  # Adds the total number of products together.

if total_items == 0:
    print(
        "Perhaps next time you would be willing to pick a selection! "
        "In any case, we will write up this total.")

elif total_items >= 10:
    print(
        "Thank you for buying so many of our items,"
        " we really appreciate it greatly!")
if num_wrench >= 1 and num_churro >= 1 and num_energy_drink >= 1 and num_soda >= 1 and num_chips >= 1:
    sub_total -= 5
    print(
        "You have bought at least one of every of our "
        "products which has earned you five dollars off!")
    print("Your discounted subtotal is: $", format(sub_total, "0.2f"), sep='')
else:
    print("Your subtotal will be ", format(sub_total, "0.2f"), sep='')

# The final total of all materials bought, multiplied by tax.
final_total = sub_total * 1.07  # 1.07 is the tax rate.
# Prints if you have enough money and if you don't, to try again.
new_money = money - final_total  # Money left over from transaction.

# Average of all item costs, divided by the / operator.
total_average = (final_total / total_items)

if final_total == money:
    print("A nice and clean zero, no change involved at all!")
elif final_total > money:
    print(
"Sorry! You did not bring enough to complete a transaction. Please try again!")
else:
    print("The total amount after tax is: $", format(final_total, "0.2f"),
          sep='')
    print("Your remaining amount of cash is $", format(new_money, "0.2f"),
          sep='')
receipt_cutoff()

print("The products in your basket now number", total_items, sep=' ')

print("The average amount of cash you spent for each item was $",
    format(total_average, "0.2f"), sep='')
# Charity to give at the end of a transaction

give_donation = True
total_donation_amount = 0
while give_donation:
    spare_change = int(input("Please donate spare dollars if you would like!"))

    print("You now have, $", format(new_money - spare_change, "0.2f"),
          sep='')  # The spare change is subtracted by the - operator
                   # To get a new dollar amount after donating.
    total_donation_amount += spare_change
    new_money -= spare_change
    give_more_charity = input("Would you like to give more to charity? Y/N")
    # Checks if the input is not Y or N, giving an individual the ability to
    # Quit donating.
    if give_more_charity != 'Y' or give_more_charity == 'N':
        give_donation = False

print("Thank you for your contribution to the betterment of society!")
new_money -= total_donation_amount
print("The whole number dollar amount you have is: $",
      format(new_money // 1, "0.0f"),
      sep='')  # Floor division returns integer
               # Amount of dollars after transaction.
print("And your cent amount will be: $", format(new_money % 1, "0.2f"),
      sep='')  # Modulus operator returns the cents in your money left over.

receipt_cutoff()
print("\n")

total_points = calculate_points(new_money)
print("You have now earned: ", format(total_points, "0.0f"), sep='')
print("points today.")

print ("\n")
#Prompts a message by means of the not function to see if it is not less
# than 100.
if not(new_money < 100):
    print("We can see that you have room for more spending, and we hope that"
          "you will be able to come around again to spend here!")
print("As always, we thank you for your patronage and have a nice day!")