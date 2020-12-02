# Angel Vera Integration project This Integration Project will focus
# shopping in a convenience store setting. Individual who helped greatly (
# Thank you very much!): Jairo Garciga Resource(s) utilized during creation
# of items: Stackoverflow Function of check_valid_input:
# https://stackoverflow.com/questions/23294658/asking-the-user-for-input
# -until-they-give-a-valid-response
# Notable contributions: product_list line
# #45, function locations at top Function to begin the introduction message
# of the program.

"""The Interproject Convenience Store"""
__author__ = "Angel Vera"


def intro_message():
    """A simpler way to insert the introductory message into the main
    function."""
    print("Welcome to the Interproject convenience store! ")
    print("Please enter required information below...")
    print("\n")


def receipt_cutoff():
    """The function allows for a simplification of printing lines that mimic
    the appearance of receipt cutoffs and improves readability of lines in
    the main function."""
    print("-" * 40)


def calculate_points(new_money):
    """A convenient function to  calculate and recalculate points as needed
    when an individual progresses through the store."""
    if new_money < 0:
        points = (new_money // -1) ** 1.005
    else:
        points = (new_money // 1) ** 1.005
    return points


def check_valid_input(number_prompt):
    """Function to check the validity of inputs."""
    while True:
        try:
            item_number = int(input(number_prompt))
        except ValueError:
            print("Invalid integer. Please input without alphabetical "
                  "numbers or special characters. ")
            continue

        if item_number <= 0:
            print("Invalid Integer input. Please enter a non-negative "
                  "integer when prompted.")
            continue
        else:
            break
    return item_number


def main():
    """The main housing of all the calculations of the store, which calls on
    all on other defined functions as needed and houses all required
    information to call on. """

    intro_message()
    # Name of person
    name = input("What is your name? ")
    print("Hello", name + "!", "Glad you are with us!")
    # How much money the person brought, input.
    money = check_valid_input("How much money have you brought?")

    # Too little money asks for money again in order to not pay the customer.
    while money < 1.56:
        print(
            "Unfortunately we would be giving you money, and that "
            "would be illegal. Please find just a bit more cash.")
        money = check_valid_input("How much money have you brought?")
    print("\n")
    if 0 < money < 100:
        print("You have brought $", format(money, "0.2f"), sep='')
    else:  # Exclaims about how the customer brought a large amount of money.
        print(
            "Wow! You sure have brought quite a lot of money! "
            "We hope that you spend it with us!")

    print("\n")

    # Variables for each of the items as well as discounts or tax rates.

    # Printing the total list of items.
    print(
        "Choose what items to buy! Please choose how many "
        "items you would like as it progresses!")
    product_list = ["Wrench $5.49", "Churro $3.49", "Energy Drink $2.99",
                    "Soda $1.99", "Chips $1.49 "]
    for x in range(0, len(product_list)):
        print(product_list[x])

    receipt_cutoff()
    print("\n")

    # subTotal is total price of every item before tax, added with + operator.
    # Also multiplied by the * operator.

    wrench = 5.49
    churro = 3.49
    energy_drink = 2.99
    soda = 1.99
    chips = 1.49
    num_wrench = check_valid_input("How many wrenches would you like?")
    num_churro = check_valid_input("How many churros would you like? ")
    num_energy_drink = check_valid_input("How many energy drinks would you "
                                         "like?")
    num_soda = check_valid_input("How many sodas would you like?")
    num_chips = check_valid_input("How many chips would you like?")
    sub_total = (wrench * num_wrench) + (churro * num_churro) + (
            energy_drink * num_energy_drink) + (soda * num_soda) + (
                        chips * num_chips)
    # Adds the total number of products together.
    total_items = num_wrench + num_churro + num_energy_drink + \
        num_soda + num_chips

    # This while loop checks to see if the sub total of all you wished to
    # purchase is greater than the money you have brought, and will ask you
    # to input a combination of items where it is equal or less to the money
    # you have brought.
    positive_sub_total = True
    while positive_sub_total:
        if sub_total > money:
            print("You do not have the ability to purchase these products, "
                  "please purchase fewer products.")
            num_wrench = check_valid_input("How many wrenches would you like?")
            num_churro = check_valid_input("How many churros would you like? ")
            num_energy_drink = check_valid_input(
                "How many energy drinks would you "
                "like?")
            num_soda = check_valid_input("How many sodas would you like?")
            num_chips = check_valid_input("How many chips would you like?")
            sub_total = (wrench * num_wrench) + (churro * num_churro) + (
                    energy_drink * num_energy_drink) + (soda * num_soda) + (
                                chips * num_chips)
            total_items = num_wrench + num_churro + num_energy_drink + \
                num_soda + num_chips

        else:
            positive_sub_total = False

    if total_items == 0:
        print(
            "Perhaps next time you would be willing to pick a selection! "
            "In any case, we will write up this total.")

    elif total_items >= 10:
        print(
            "Thank you for buying so many of our items,"
            " we really appreciate it greatly!")
    if num_wrench >= 1 and num_churro >= 1 and \
            num_energy_drink >= 1 and num_soda >= 1 and num_chips >= 1:
        sub_total -= 5
        print(
            "You have bought at least one of every of our "
            "products which has earned you five dollars off!")
        print("Your discounted subtotal is: $", format(sub_total, "0.2f"),
              sep='')
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
            "Sorry! You did not bring enough to complete a transaction. "
            "Please try again!")

    else:
        print("The total amount after tax is: $", format(final_total, "0.2f"),
              sep='')
        print("Your remaining amount of cash is $", format(new_money, "0.2f"),
              sep='')
    receipt_cutoff()

    print("The products in your basket now number: ", total_items)

    print("The average amount of cash you spent for each item was $",
          format(total_average, "0.2f"), sep='')
    # Charity to give at the end of a transaction

    give_donation = True
    while give_donation:
        spare_change = check_valid_input(
            "Please donate spare dollars if you would like!")
        new_money -= spare_change

        print("Your balance is, $", format(new_money, "0.2f"),
              sep='')  # The spare change is subtracted by the - operator
        # To get a new dollar amount after donating.
        give_more_charity = str(input("Would you like to donate more? Press"
                                      " any other key than Y to cancel."))
        # Checks if the input is not Y or N, giving a person the ability to
        # Quit donating.
        if give_more_charity != 'Y':
            give_donation = False

    print("Thank you for your contribution to the betterment of society!")
    if new_money < 0:
        print("You now owe the store: $", format(new_money, "0.2f"), sep='')
    else:
        print("The whole number dollar amount you have is: $",
              format(new_money // 1, "0.0f"),
              sep='')  # Floor division returns integer
        # Amount of dollars after transaction.
        print("And your cent amount will be: $", format(new_money % 1, "0.2f"),
              sep='')  # Modulus operator returns the cents in your money left
        # over.

    receipt_cutoff()
    print("\n")

    total_points = calculate_points(new_money)
    print("You have now earned: ", format(total_points, "0.0f"), sep='')
    print("points today.")

    receipt_cutoff()
    print("\n")

    record_data = True
    while record_data:
        record_customer_data = str(input("Is there data that you would like "
                                         "to record with our store? Press "
                                         "any key other than Y to cancel."))
        if record_customer_data != 'Y':
            print(("If you ever wish to ever record your information "
                   "with us in a future purchase please do so at the next "
                   "checkout! You are free to do so whenever! "))
            record_data = False
        else:
            last_name = input("Enter your last name: ")
            first_name = input("Enter your first name: ")
            phone_number = input("Enter your phone number without dashes: ")
            contact_information = open("customer_information.txt", 'a')
            contact_information.write("Name: " + first_name + " " + last_name)
            contact_information.write("\nPhone Number: " + phone_number)
            contact_information.write("\n")
            contact_information.close()
            print("Your information as input is that your first name is " +
                  first_name + ", your last name is " + last_name +
                  " and your phone number is " + phone_number + ".")
            print("Information input has been recorded and saved in our "
                  "database, thank you for staying with us!")

    print("\n")
    # Prompts a message by means of the not function to see if it is not less
    # than 100.
    if new_money > 1.56:
        print("We can see that you have room for more spending, and we hope "
              "that you will be able to come around again to "
              " spend here!")
    else:
        print(
            "As always, we thank you for your patronage and have a nice day!")


########## CALL TO MAIN ##########
main()
