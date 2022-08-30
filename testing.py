def get_string(m, _min=2, _max=15):
    """
    Validate string

    :param m: string
    :param _min: integer
    :param _max: integer
    :return: string
    """
    getting_answer = True
    while getting_answer is True:
        # getting input
        my_string = input(m)
        # checking length of input
        if len(my_string) < _min:
            output = "You string is too short. Please re-enter"
            print(output)
        elif len(my_string) > _max:
            output = "You string is too long. Please re-enter"
            print(output)
        else:
            return my_string


def yes_no(m):
    """
    Validate Y or N

    :param m: string
    :return: boolean
    """
    getting_answer = True
    while getting_answer is True:
        # getting input
        output = input(m).upper()
        if output == "Y":
            delivery = False
        elif output == "N":
            delivery = True
        else:
            print("Unrecognised entry")


def get_integer(m, _min=0, _max=10):
    """
    Validate integer

    :param m: string
    :param _min: integer
    :param _max: integer
    :return: integer
    """
    # assume it is wrong
    have_correct_value = False
    while have_correct_value is False:
        try:
            my_integer = int(input(m))
        except ValueError:
            print("You have not entered an integer")
            # immediate jump back to top of loop
            continue
        # we have an integer
        if my_integer < _min:
            output = "Your value is too small, please re-enter"
            print(output)
            continue
        elif my_integer >= _max:
            output = "Your value is too big, please re-enter"
            print(output)
            continue
        # have the correct value so end loop
        return my_integer


def print_pasta(l):
    """
    Print pasta list

    :param l: list
    :return:
    """
    for x in l:
        output = "{} : {} : ${}".format(x[0], x[2], x[1])
        print(output)


def print_with_indexes(l):
    """
    Print pasta list with indexes

    :param l: list
    :return:
    """
    for i in range(0, len(l)):
        output = "{:3} : {:10} : {} : ${} ".format(i, l[i][0], l[i][2], l[i][1])
        print(output)


def print_order_with_indexes(l):
    """
    Print order with indexes

    :param l: list
    :return:
    """
    for i in range(0, len(l)):
        output = "{:3} : {:3} : Quantity = {:1}".format(i, l[i][0], l[i][2])
        print(output)


def review_order(o, t):
    """
    Review order

    :param t: integer
    :param o: list
    :return:
    """
    print("Your order -> ")
    for x in o:
        output = "{:3} : ${:3} : Quantity = {:1}".format(x[0], x[1], x[2])
        # calculating the total
        t += x[2] * x[1]
        print(output)
    print("Total price: ${}".format(t))
    print("-" * 80)
    return t


def add_pasta(l, o):
    """
    Add pasta to order

    :param l:
    :param o:
    :return:
    """
    # print pasta list
    print_with_indexes(l)
    print("-" * 80)
    # start loop
    add_pasta_loop = True
    while add_pasta_loop is True:
        user_choice = get_integer("Which pasta would you like to add to your order? (Please enter the index number) -> ", 0, len(l))
        # get the quantity the user would like to add of the chosen pasta
        quantity = get_integer("How many {} would you like to add? -> ".format(l[user_choice][0]), 1, 6)
        name = l[user_choice][0]
        price = l[user_choice][1]
        # adding the name, price and quantity to the order list
        o.append([name, price, quantity])
        confirmation = "You have added {} {} to your order".format(quantity, l[user_choice][0])
        print(confirmation)
        add_pasta_loop = False


def remove_pasta(o):
    """
    Remove pasta from the user's order

    :param o: list
    :return:
    """
    # print order list
    print_order_with_indexes(o)
    # making sure there is something in the users order
    if len(o) == 0:
        print("Sorry, you have not added anything to your order yet")
        print("-" * 80)
    else:
        print("-" * 80)
        user_choice = get_integer("PLease enter the index number of the pasta you would like to delete from you order -> ", 0, len(o))
        confirmation = "{} has been removed from your order".format(o[user_choice][0])
        print(confirmation)
        # remove item from order
        del o[user_choice]


def edit_order(o):
    """
    Edit user's order

    :param o: list
    :return:
    """
    # print order list
    print_order_with_indexes(o)
    # making sure there is something in the users order
    if len(o) == 0:
        print("Sorry, you have not added anything to your order yet")
        print("-" * 80)
    else:
        print("-" * 80)
        user_choice = get_integer("What pasta would you like to edit? (Please enter the index number) -> ", 0, len(o))
        quantity = get_integer("What would you like to change the quantity of {} to? The current quantity is {} -> ".format(o[user_choice][0], o[user_choice][2]), 1, 6)
        # changing the original quantity to the new quantity
        o[user_choice][2] = quantity
        confirmation = "You now have {} {}".format(o[user_choice][2], o[user_choice][0])
        print(confirmation)


def customer_details(c, total):
    """
    Enter customer details

    :param total: integer
    :param c: list
    :return:
    """
    name = get_string("Can you please enter your name -> ", 0, 50)
    phone_number = get_string("Can you please enter your phone number -> ", 7, 15)
    print("-"*80)
    # starting loop
    choice = True
    while choice is True:
        options = ["D : Delivery (There is an extra $3 charge for delivery)", "P : Pickup"]
        for x in options:
            print(x)
        user_choice = get_string("Please enter your choice -> ", 0, 1).upper()
        if user_choice == "D":
            delivery = True
            while delivery is True:
                total += 3
                number = get_string("You have selected Delivery. Can you please enter your address. Number -> ", 0, 5)
                street = get_string("Street -> ", 0, 50)
                suburb = get_string("Suburb -> ", 0, 50)
                city = get_string("City -> ", 0, 50)
                postcode = get_string("Postcode -> ", 0, 4)
                address = "{} {}, {} {} {}".format(number, street, suburb, city, postcode)
                confirmation = get_string("Your address is {}. Is this correct? (Please enter Y or N) -> ".format(address), 0, 1)
                if confirmation == "Y":
                    delivery = False
                elif confirmation == "N":
                    total -= 3
                    delivery = True
                else:
                    print("Sorry, you have entered an invalid input. Please try again")
                output = "Name : {} \nAddress : {} \nPhone Number : {}\nTotal Cost : ${}".format(address, phone_number, name, total)
            # adding information to customer details list
            c.extend([name, phone_number, address])
            print(output)
            choice = False
        elif user_choice == "P":
            print("You have selected Pickup")
            output = "Name : {} \nPhone Number : {}\nTotal Cost : ${}".format(phone_number, name, total)
            # adding information to customer details list
            c.extend([name, phone_number, "N/A"])
            print(output)
            # finishing loop
            choice = False
        else:
            print("Unrecognised entry")
            # jumping back to top of loop
            continue


def finalising_order(o, c, t):
    """
    Finalising the user's order

    :param t: integer
    :param o: list
    :param c: list
    :return: boolean
    """
    # making sure there is something in the users order
    if len(o) == 0:
        print("Sorry, you have not added anything to your order yet")
        print("-" * 80)
        return True
    else:
        # calling the review order function
        total = review_order(o, t)
        # starting loop
        correcting_order = True
        while correcting_order is True:
            order = get_string("Is this order correct? Please enter Yes (Y) or No (No) -> ", 0, 1).upper()
            if order == "Y":
                # calling the customer details function
                customer_details(c, total)
                # final confirmation
                # is all good?
                confirmation = True
                while confirmation is True:
                    final_confirmation = get_string("Do you want to finalise this order? Please enter Yes (Y) or No (N) -> ", 0, 1)
                    if final_confirmation == "Y":
                        o.clear()
                        c.clear()
                        # calling the order again function and returning the boolean (T or F) it already returned
                        order_or_quit = order_again()
                        return order_or_quit
                    elif final_confirmation == "N":
                        c.clear()
                        return True
                    else:
                        print("Unrecognised entry")
                        confirmation = True
                # if not good, clear the customer details and return to main menu
                # clearing the lists so if they would like to place another order, they can start again
            elif order == "N":
                # returning True so that the main program does not stop and goes back to the options menu
                return True
            else:
                print("Unrecognised entry")
                # going back to the top of the loop
                correcting_order = True


def order_again():
    """
    Ask the user if they would like to order again

    :return: boolean
    """
    # starting loop
    another_order = True
    while another_order is True:
        output = get_string("Would you like to place another order? Please enter Yes (Y) or No (N) -> ", 0, 1).upper()
        if output == "Y":
            # returning True so that the program returns to the main menu
            return True
        elif output == "N":
            print("Thank you for ordering your meal. The program will terminate")
            # return False so that the run loop in the main menu stops and the program terminates
            return False
        else:
            print("Unrecognised entry")


def main():
    """
    The main menu program

    :return:
    """
    pasta_list = [["Linguine Gamberi", 23, "Long flat pasta. Tomato, garlic and chilli sauce, prawns anchovies, capers, olives, parmesan"],
                  ["Fusilli Pesto", 19, "Short, spiral pasta. Kale and cashew pesto and cream sauce, olives, parmesan"],
                  ["Conchilglie alla Bolognese", 22, "Small, shell pasta. Northern italian beef and pork sauce, parmesan"],
                  ["Rigatoni alla Caponata", 21, "Short, tube pasta. Agrodolce tomato sauce, eggplant, ricotta salata, pine nut"],
                  ["Fettuccine Carbonara", 20, "Long, flat pasta. Creamy egg and pepper sauce, bacon, parmesan"],
                  ["Spaghetti Pomodoro", 16, "Long, thin pasta. Classic tomato and basil sauce, parmesan"],
                  ["Pappardelle Ricci D’Angello", 26, "Short, frizzy pasta. Slow cooked lamb ragu, rosemary, olives, sweet garlic, parmesan"],
                  ["Raviolo di Salsiccia", 22, "Filled pasta. Red wine vinegar and tomato sauce, sausage, green capsicum, three cheese (filled) parmesan"],
                  ["Ravioli di Ricotta", 20, "Spinach and ricotta (filled) pasta, brown butter sauce, sage, hazelnuts, parmesan"]]
    order_list = []
    details_list = []
    total = 0
    options = ["P : Print Menu", "Q : Quit", "R : Review Order", "A : Add To Your Order", "D : Delete from Order", "E : Edit order", "F : Finalising Order"]
    run = True
    while run is True:
        # print the options list
        for x in options:
            print(x)
        print("-" * 80)
        user_choice = get_string("Please enter your choice -> ", 0, 1).upper()
        print("-" * 80)
        if user_choice == "P":
            print_pasta(pasta_list)
            print("-" * 80)
        elif user_choice == "A":
            # calling the add pasta function
            add_pasta(pasta_list, order_list)
        elif user_choice == "R":
            # calling the review order function
            review_order(order_list, total)
        elif user_choice == "D":
            # calling the remove pasta function
            remove_pasta(order_list)
        elif user_choice == "E":
            # calling the edit order function
            edit_order(order_list)
        elif user_choice == "F":
            # calling the finalising order function
            run = finalising_order(order_list, details_list, total)
        elif user_choice == "Q":
            # stopping the loop and therefore ending the program
            run = False
            print("Thank you for looking through my program")
        else:
            print("Unrecognised entry, please re-enter")


main()

