#Data Structures and Algorithm
#Obial & De La Peña

import calendar
from datetime import datetime
import time

Reservation = {}
Food_Selection = ["Americano", "Latte sa Hingapi", "Caramel Macchiato", "Choco Almond", "Spanish Latte", "Salted Caramel", "French Vanilla"]
Available_sizes = ["Medium-109", "Large-119", "Litro-229"]
Sizes_Price = [109, 119, 229]
Available_times = ["10:00", "12:00", "14:00"]
Counter = 0  # Initialize Counter variable
size = 0

def Selected_Food():
    print("Food Selection: ")
    for i, data in enumerate(Food_Selection, 1):
        print(f'{i}. {data}')
    while True:
        try:
            food = int(input("Enter the food you want to order (number between 1 and {}): ".format(len(Food_Selection))))
            if 1 <= food <= len(Food_Selection):
                return Food_Selection[food - 1]
            else:
                print("Invalid Input. Please enter a number between 1 and {}.".format(len(Food_Selection)))
        except ValueError:
            print("Input Number Only")

def Available_Sizes():
    print("Available sizes: ")
    for i, data in enumerate(Available_sizes, 1):
        print(f'{i}. {data}')
    while True:
        try:
            global size
            size = int(input("Enter the size you want to order (number between 1 and {}): ".format(len(Available_sizes))))
            if 1 <= size <= len(Available_sizes):
                return Available_sizes[size - 1]
            else:
                print("Invalid Input. Please enter a number between 1 and {}.".format(len(Available_sizes)))
        except ValueError:
            print("Input Number Only")

def Size_Pricing():
    price =  size
    if 1 <= price <= len(Sizes_Price):
        return Sizes_Price[size - 1]

def Amount_Food():
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            if quantity > 0:
                return quantity
            else:
                print("Invalid Input. Please enter a positive number.")
        except ValueError:
            print("Input Number Only.")

def Selected_Date():
    while True:
        date = input("Enter the date (MM-DD-YYYY): ")
        try:
            date_obj = datetime.strptime(date, "%m-%d-%Y")
            if date_obj > datetime.now():
                return date
            else:
                print("Date must be in the future.")
        except ValueError:
            print("Invalid date format. Please use DD-MM-YYYY.")

def Selected_Time():
    while True:
        print("Reservation Time: ")
        for i, data in enumerate(Available_times, 1):
            print(f'{i}. {data}')
        try:
            time = int(input("Enter the time you want to reserve (number between 1 and {}): ".format(len(Available_times))))
            if 1 <= time <= len(Available_times):
                return Available_times[time - 1]
            else:
                print("Invalid Input. Please enter a number between 1 and {}.".format(len(Available_times)))
        except ValueError:
            print("Invalid Input. Please enter a number between 1 and {}.".format(len(Available_times)))

def add():
    while True:
        name = input("\nEnter your name: ")
        global Counter
        Counter += 1
        try:
            if name in Reservation:                
                Order_Number = f'{Counter:03}'
                Ordered_Food = Selected_Food()
                Ordered_Size = Available_Sizes()
                Ordered_Price = Size_Pricing()
                Ordered_Quantity = Amount_Food()
                Ordered_Date = Selected_Date()
                Ordered_Time = Selected_Time() 
                time_created = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
                Reservation[name].append({
                    "order_number": Order_Number,
                    "food": Ordered_Food,
                    "size" : Ordered_Size,
                    "quantity": Ordered_Quantity,
                    "price": Ordered_Price * Ordered_Quantity,
                    "date": Ordered_Date,
                    "time": Ordered_Time,
                    "time_created": time_created
                })
            else:            
                Order_Number = f'{Counter:03}'
                Ordered_Food = Selected_Food()
                Ordered_Size = Available_Sizes()
                Ordered_Quantity = Amount_Food()
                Ordered_Price = Size_Pricing()
                Ordered_Date = Selected_Date()
                Ordered_Time = Selected_Time() 
                time_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                Reservation[name] = [{
                    "order_number": Order_Number,
                    "food": Ordered_Food,
                    "size": Ordered_Size,
                    "quantity": Ordered_Quantity,
                    "price": Ordered_Price * Ordered_Quantity,
                    "date": Ordered_Date,
                    "time": Ordered_Time,
                    "time_created": time_created
                }]
        except ValueError:
            print("Invalid Input")
        print(f'Added reservation for {name}')
        break
    
def edit():
    print("\nEdit Reservation")
    Name = input("Enter Name: ")
    found = False
    for key, value in Reservation.items():
        if Name == key:
            for j, reserve in enumerate(Reservation[key], 1):
                print(f'   {j}. Order Number: {reserve["order_number"]}')
                print(f'      Food: {reserve["food"]}')
                print(f'      Size: {reserve["size"]}')
                print(f'      Quantity: {reserve["quantity"]}')
                print(f'      Price: {reserve["price"]}')
                print(f'      Date: {reserve["date"]}')
                print(f'      Time: {reserve["time"]}')
                print(f'      Time Reserved: {reserve["time_created"]}')
            while True:    
                Choice = input("Do you want to edit? (Y/N): ").upper()
                if Choice == 'Y':
                    if len(Reservation[key])==1:
                        print("\n")
                        Ordered_Food = Selected_Food()
                        Ordered_Size = Available_Sizes()
                        Ordered_Quantity = Amount_Food()
                        Ordered_Price = Size_Pricing()
                        Ordered_Date = Selected_Date()
                        Ordered_Time = Selected_Time() 
                        time_created = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
                        Reservation[key][0]["food"] = Ordered_Food
                        Reservation[key][0]["size"] = Ordered_Size
                        Reservation[key][0]["quantity"] = Ordered_Quantity
                        Reservation[key][0]["price"] = Ordered_Price * Ordered_Quantity
                        Reservation[key][0]["date"] = Ordered_Date
                        Reservation[key][0]["time"] = Ordered_Time
                        Reservation[key][0]["time_created"] = time_created
                        print("\n Updated Reservation")
                        break   
                    else:
                        try:
                            choice = int(input("Enter Order Number to Edit (number between 1 and {}): ".format(len(Reservation[key]))))
                            if 1 <=choice <= len(Reservation[key]):
                                print("\n")
                                Ordered_Food = Selected_Food()
                                Ordered_Size = Available_Sizes()
                                Ordered_Quantity = Amount_Food()
                                Ordered_Price = Size_Pricing()
                                Ordered_Date = Selected_Date()
                                Ordered_Time = Selected_Time() 
                                time_created = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
                                Reservation[key][choice -1]["food"] = Ordered_Food
                                Reservation[key][choice -1]["size"] = Ordered_Size
                                Reservation[key][choice -1]["quantity"] = Ordered_Quantity
                                Reservation[key][choice -1]["price"] = Ordered_Price * Ordered_Quantity
                                Reservation[key][choice -1]["date"] = Ordered_Date
                                Reservation[key][choice -1]["time"] = Ordered_Time
                                Reservation[key][choice -1]["time_created"] = time_created
                                print("Reservation Updated")
                                break
                            else:
                                print("Invalid choice. Enter number between 1 and {}: ".format(len(Reservation[key])))
                        except ValueError:
                            print("Input Numbers Only")
                elif Choice == 'B':
                    return
                else:
                    print("Invalid Input, Enter 'Y' or 'N' only")
        found = True
    if not found:
        print(f"{Name} not found")
        
def display(Name):
    for key, value in Reservation.items():
        if Name == key:      
        
def find():
    print("\nFind Reservation")
    Name = input("Enter Name: ")
    found = False
    for key, value in Reservation.items():
        if Name == key:
            for reservation in value:
                print(f'Order Number: {reservation["order_number"]}')
                print(f'Name: {key}')
                print(f'Food: {reservation["food"]}')
                print(f'Size: {reservation["size"]}')
                print(f'Quantity: {reservation["quantity"]}')
                print(f'Price: {reservation["price"]}')
                print(f'Date: {reservation["date"]}')
                print(f'Time: {reservation["time"]}')
                print(f'Time Reserved: {reservation["time_created"]}\n')
        found = True
    if not found:
        print(f"{Name} not found")

def delete():
    print("\nDelete Reservation")
    Name = input("Enter Name: ")
    found = False
    for key, value in Reservation.items():
        if Name == key:
            for j, reserve in enumerate(Reservation[key], 1):
                print(f'   {j}. Order Number: {reserve["order_number"]}')
                print(f'      Food: {reserve["food"]}')
                print(f'      Size: {reserve["size"]}')
                print(f'      Quantity: {reserve["quantity"]}')
                print(f'      Price: {reserve["price"]}')
                print(f'      Date: {reserve["date"]}')
                print(f'      Time: {reserve["time"]}')
                print(f'      Time Reserved: {reserve["time_created"]}')
            while True:
                try:
                    choice = int(input("Enter Order Number to Delete (number between 1 and {}): ".format(len(Reservation[key]))))
                    if 1 <= choice <= len(Reservation[key]):
                        del Reservation[key][choice-1]
                        print("Reservation removed")
                        break
                    else:
                        print("Invalid choice. Enter number between 1 and {}: ".format(len(Reservation[key])))
                except ValueError:
                    print("Input Numbers Only")
        found = True
    if not found:
        print(f"{Name} not found")

def all():
    if not Reservation:
        print("No reservations to display")
        return
    else:
        print("\nCurrent Reservations")
        for i, key in enumerate(Reservation.keys(), 1):
            print(f'{i}). {key}')
            for j, reservation in enumerate(Reservation[key], 1):
                print(f'   {j}. Order Number: {reservation["order_number"]}')
                print(f'      Food: {reservation["food"]}')
                print(f'      Size: {reservation["size"]}')
                print(f'      Quantity: {reservation["quantity"]}')
                print(f'      Price: {reservation["price"]}')
                print(f'      Date: {reservation["date"]}')
                print(f'      Time: {reservation["time"]}')
                print(f'      Time Reserved: {reservation["time_created"]}')
        while True:        
            Choice = input("\nEnter'b' to go back to the main menu: ").lower()
            if Choice == 'b':
                return
            
def main():
    while True:
        try:
            print("\n\tMenu")
            print("1. Add Reservation")
            print("2. Edit Reservation")
            print("3. Find Reservation")
            print("4. Delete Reservation")
            print("5. Display All")
            print("6. Exit")
            Selection = int(input("Enter your choice: "))

            if Selection == 1:
                add()
            elif Selection == 2:
                edit()
            elif Selection == 3:
                find()
            elif Selection == 4:
                delete()
            elif Selection == 5:
                all()
            elif Selection == 6:
                break
            else:
                print("Invalid choice. Please Select from 1-6.\n")
        except ValueError:
            print("Enter Number only.\n")

main()