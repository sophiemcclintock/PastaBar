def get_string(m):
    my_string = input(m)
    return my_string


def get_integer(m):
    my_integer = int(input(m))
    return my_integer


def print_pasta(l):
    for x in l:
        output = "{} : ${}".format(x[0], x[1])
        print(output)


def review_order(l):
    print("Your order -> ")
    total = 0
    for x in l:
        output = "{} : {} : ${}".format(x[2], x[0], x[1])
        total += x[2] * x[1]
        print(output)
    print("Total price: ${}".format(total))
    print("-" * 80)


def print_with_indexes(l):
    for i in range(0, len(l)):
        output = "{:3} : {:10} : ${}".format(i, l[i][0], l[i][1])
        print(output)


def print_order_with_indexes(l):
    for i in range(0, len(l)):
        output = "{:3} : {:3} : Quantity = {:3}".format(i, l[i][0], l[i][2])
        print(output)


def add_pasta(l, o):
    print_with_indexes(l)
    print("-" * 80)
    add_pasta_loop = True
    while add_pasta_loop is True:
        user_choice = get_integer(
            "Which pasta would you like to add to your order? (Please enter the index number) -> ")
        quantity = get_integer("How many {} would you like to add? -> ".format(l[user_choice][0]))
        l[user_choice][2] += quantity
        o.append(l[user_choice])
        confirmation = "You have added {} {} to your order".format(l[user_choice][2], l[user_choice][0])
        print(confirmation)
        add_pasta_loop = False


def remove_pasta(l, o):
    print_order_with_indexes(o)
    print("-" * 80)
    user_choice = get_integer("PLease enter the index number of the pasta you would like to delete from you order -> ")
    confirmation = "{} has been removed from your order".format(o[user_choice][0])
    print(confirmation)
    l[user_choice][2] = 0
    del o[user_choice]


def main():
    pasta_list = [["Linguine Gamberi", 23, 0],
                  ["Fusilli Pesto", 19, 0],
                  ["Conchilglie alla Bolognese", 22, 0]]
    order_list = []
    options = ["P : Print", "Q : Quit", "R : Review", "A : Add To Your Order", "D : Delete from Order"]
    run = True
    while run is True:
        for x in options:
            print(x)
        print("-" * 80)
        user_choice = get_string("Please enter your choice -> ")
        print("-" * 80)
        if user_choice == "P":
            print_pasta(pasta_list)
            print("-" * 80)
        elif user_choice == "A":
            add_pasta(pasta_list, order_list)
        elif user_choice == "R":
            review_order(order_list)
        elif user_choice == "D":
            remove_pasta(pasta_list, order_list)
        elif user_choice == "Q":
            run = False
            print("Thank you for looking through my program")
        else:
            print("Unrecognised entry")


main()
