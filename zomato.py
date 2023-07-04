
dishes = {}
orders = {}
orderIdCounter = 1
# ANSI escape codes for colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
MAGENTA = '\033[95m'
RESET = '\033[0m'

orderIdGenerator = 1
def add_dish_to_menu(dishes, dish_id, dish_name, price):
    dish = {
        "dish_id" : dish_id,
        "dish name" : dish_name,
        "price" : price,
        "availability": "yes" # at the time of adding new dish it would be in available state
    }
    if dish_id in dishes:
        print("Dish with this Id is already available in the list")
    else:
        dishes[dish_id] = dish
        print(GREEN+"\nDish added successfully\n"+RESET)

def update_availability_of_dish_by_id(id):
    if id in dishes:

        currentStatus = dishes[id]["availability"]
        print("Current availability Status :", currentStatus)
        print()
        updatedStatus = input("Enter new availavility status (yes/no) : ").lower()
        # to make sure availability is either yes or no
        if updatedStatus=="no" or updatedStatus=="yes":
            dishes[id]["availability"] = updatedStatus
            print(GREEN+"\navailability status changed successfully\n"+RESET)
        else:
            print(RED+"\n availability must be either yes OR no\n"+RESET)
    else:
        print(RED+"\n Invalid dish id\n")


def remove_dish_by_Id(id):
    if id in dishes:
        dishes.__delitem__(id)
        print(GREEN+"\nDish with Id ", id, "deleted successfully\n"+RESET)
    else:
        print(RED+"Invalid dish_id\n"+RESET)

def place_order(dish_id):
    global orderIdCounter  # Declare orderIdCounter as global
    if dish_id in dishes:
        # if availability is no then not purchase
        if dishes[dish_id]["availability"]=="no":
            print(RED+"\nSorry! This item is currently unavailable\n")
        else:
            customerName = input("Please enter your name : ")
            order = {
                "customer name" : customerName,
                "Dish name" : dishes[dish_id]["dish name"],
                "price": dishes[dish_id]["price"],
                "status": "placed"

            }
            orders[orderIdCounter] = order
            orderIdCounter += 1
            print(GREEN+"\nOrder placed successfully\n"+RESET)
    else:
        print(RED+"Invalid dish_id\n"+RESET)

# updating order status
def update_order_status(order_id):
    if order_id in orders:

        currentStatus = orders[order_id]["status"]
        print("Current Status :", currentStatus)
        print()
        updatedStatus = input("Enter new status : ").lower()
        
        orders[order_id]["status"] = updatedStatus
        print(GREEN+"\nOrder status changed successfully\n"+RESET)
    else:
        print(RED+"\nInvalid order id\n"+RESET)
    

def display_menu():
    if len(dishes) == 0:
        print(YELLOW+"No any order yet"+RESET)

    for key in dishes:
        print("dish_id :", key, "| Dish name :", dishes[key]["dish name"], "| price :", dishes[key]["price"], "| Availability :", dishes[key]["availability"])


def review_all_orders():
    if len(orders) == 0:
        print("No any order yet")

    for key in orders:
        print("Customer name : ", orders[key]["customer name"],"| order_id :", key, "| Dish name :", orders[key]["Dish name"], "| price :", orders[key]["price"], "| status :", orders[key]["status"])


print(YELLOW+"welcome to zesty zomato\n"+RESET)
while True:
    print("1. admin")
    print("2. customer")
    print("0. "+RED+"Exit"+RESET)
    try:
        choice = int(input(YELLOW+"\nplease enter your preference 0 to 2\n"+RESET))
    

        if choice == 1:
            
            username = input("Enter username : ")
            password = input("Enter password : ")

            if username == "admin" and password == "admin":
                print(YELLOW+"\nLogged In successfully\n"+RESET)
                print(MAGENTA+"\nWelcome Admin\n"+RESET)
                while True:
                    print("1. to add new dish")
                    print("2. to update availability status")
                    print("3. to remove dish")
                    print("4. to review all orders")
                    print("5. to see menu")
                    print("6. to update order status")
                    print("0. "+RED+"back"+RESET)

                    admin_choice = 0
                    try:
                        admin_choice = int(input(YELLOW+"\nplease enter your preference 0 to 6\n"+RESET))

                        if admin_choice==1:
                            dish_id = input("Enter dish id : ")
                            dish_name = input("Enter dish name : ")
                            price = input("Enter price : ")
                            add_dish_to_menu(dishes, dish_id, dish_name, price)

                        elif admin_choice==2:
                            dish_id = input("enter dish id to update : ")
                            update_availability_of_dish_by_id(dish_id)
                        elif admin_choice==3:
                            dish_id = input("enter dish id to remove : ")
                            remove_dish_by_Id(dish_id)
                        elif admin_choice==4:
                            print(GREEN+"\n-------------------------ORDERS---------------------------\n"+RESET)
                            review_all_orders()
                            print(GREEN+"\n-------------------------END-----------------------------\n"+RESET)
                        elif admin_choice==5:
                            print(GREEN+"\n-------------------------MENU-----------------------------\n"+RESET)
                            display_menu()
                            print(GREEN+"\n-------------------------END------------------------------\n"+RESET)
                        elif admin_choice==6:
                            order_id = int(input("Enter order Id to update : "))
                            update_order_status(order_id)
                            
                        elif admin_choice==0:
                            print("\Exiting from Admin module...\n")
                            break
                        else:
                            print(RED+"Invalid choice. please try again...\n"+RESET)


                    except ValueError:
                        print(RED+"Invalid input! Please enter a valid integer."+RESET)
            else:
                print(RED+"Invalid credentials. please try again...\n"+RESET)
        elif choice == 2:
            print(GREEN+"\nWelcome to customer module\n"+RESET)
            while True:
                print("1. to display Menu")
                print("2. to purchase item")
                print("0. "+RED+"back"+RESET)

                customerChoice = -1
                try:
                    customerChoice = int(input(YELLOW+"\nplease enter your preference 0 to 2\n"+RESET))
                    if customerChoice==1:
                        print(GREEN+"\n-------------------------MENU-----------------------------\n"+RESET)
                        display_menu()
                        print(GREEN+"\n-------------------------END------------------------------\n"+RESET)
                    elif customerChoice == 2:
                        dish_id = input("Enter dish id to purchase : ")
                        place_order(dish_id)
                    elif customerChoice == 0:
                        break
                    else:
                        print(RED+"Invalid dish Id\n"+RESET)

                except ValueError:
                    print("Invalid input! Please enter a valid integer.")
        elif choice == 0:
            print(GREEN+"\nThank you for using Zesty Zomato. Have a great day!\n"+RESET)
            break
        else:
            print(RED+"Invalid choice. Please try again."+RESET)
    except ValueError:
        print(RED+"Invalid input! Please enter a valid integer."+RESET)

                
                
                    



