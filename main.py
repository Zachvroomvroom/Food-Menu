def menu():
    print("MENU")
    food_menu = {'Burger':'10.99','Drink':'12.99','Fries':'13.99'}
    while True:
        print("1. Display\n2. Add\n3. Modify\n4. Delete\n5. Quit")
        insert = input("What would you like to do? ")
        if insert == '1':
            print("-----------------------")
            for i in food_menu:
                print(i,end=' $')
                print(food_menu[i])
            print("-----------------------")
        elif insert == '2':
            print("-----------------------")
            insert = input("What do you want to add? ")
            price = input("How expensive is it? ")
            food_menu[insert] = price
            print("-----------------------")
        elif insert == '3':
            print("-----------------------")
            for i in food_menu:
                print(i)
            insert = input("What do you want to modify? ")
            price = input("How expensive is it now? ")
            food_menu[insert] = price
        elif insert == '4':
            print("-----------------------")
            for i in food_menu:
                print(i)
            insert = input("What would you like to delete? ")
            del food_menu[insert]
            print("-----------------------")
        elif insert == '5':
            break

menu()