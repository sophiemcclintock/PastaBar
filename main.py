def get_string(m):
    my_string = input(m)
    return my_string


def get_integer(m):
    my_integer = int(input(m))
    return my_integer


def print_pasta(l):
    for x in l:
        output = "{} costs ${}".format(x[0], x[1])
        print(output)


def main():
    pasta_list = [["Linguine Gamberi", 23],
                  ["Fusilli Pesto", 19],
                  ["Conchilglie alla Bolognese", 22]]
    options = ["P: Print", "Q: Quit"]
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
        elif user_choice == "Q":
            run = False
            print("Thank you for looking through my program")
        else:
            print("Unrecognised entry")


main()
