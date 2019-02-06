'''
Jesus Medina 
CS - 521
Final Project



NOTES: 
car_inventory.txt is a list of vehicles
the bussiness would owner the vehicle would have in their lot 

the txt format is critical for reading the values and connecting 
it to the database
'''


class Car():
    
    def __init__(self, year, make_model, price, sold_price = 0):
        self.year       = year
        self.make_model = make_model
        self.price      = price
        self.sold_price = sold_price
    
    @staticmethod
    def new_vehicle(): # new vehicle
        '''create a new vehicle to system'''
        year       = int(input("- Enter Vehicle Year: "))
        make_model = input("- Enter Make & Model: ")
        price      = "{0:,.2f}".format(float(input("- Enter Initial Price: ")))
        
        with open('car_inventory.txt', 'a') as log:
            log.write("\n" + str(Car(year, make_model, price)) + "\n")            
            log.close
        
        return Car(year, make_model, price)
    
    def change_attributes(self):
        '''allows user to change particular attribute of a car in the in stock inventory'''
        change_choice = int(input("- What would you like to change?\n\n\t" +
                              "1. Year \n\t" +
                              "2. Make & Model\n\t" +
                              "3. Initial Price\n\n" +
                              "- Enter option [1-3]: "))
        if change_choice   == 1:
            self.year       = int(input("- Enter Vehicle Year: "))
        elif change_choice == 2:
            self.make_model = input("- Enter Make & Model: ")
        elif change_choice == 3:
            self.price      = "{0:,.2f}".format(float(input("- Enter Initial Price: ")))
        
    def set_sold_price(self, sold_price):
        '''sets a sold price for a particular car'''
        self.sold_price = sold_price
        
    def __str__(self):
        '''shows car with initial price'''
        return 'YEAR: {}  |  MAKE & MODEL: {:15}  |  INITIAL PRICE: ${}'.format(self.year, self.make_model, self.price)

    def __repr__(self):
        '''to show car with sold price'''
        return '{}  |  SELL PRICE: ${:,.2f}'.format(str(self), self.sold_price)



class Inventory():
    
    def __init__(self):
        self.stock = []
        self.sold  = []
    
    def set_new_vehicle(self, car):
        '''sets new vehicle in car stock invetory'''
        self.stock.append(car)

    def get_vehicle(self, index):
        '''gets a vehicle  the stock inventory'''
        index -= 1 # to match index to selections on screen
        return self.stock[index]
    
    def read_inventory(self):
        '''reads txt file of car inventory and assigns respective values to car'''
        with open("car_inventory.txt") as inventory:
            log = inventory.readlines()
            content = [car.strip("\n") for car in log]
            records = []
            for line in content:
                fields = line.split('|') # removes the character ... in the txt file to seperate 
                fields = [f.strip() for f in fields]
                records.append({s.split(':')[0].strip(): s.split(':')[1].strip() for s in fields}) # creating dictionary of 
            for record in records:
                year = int(record['YEAR'])
                price = "{0:,.2f}".format(round(float(record['INITIAL PRICE'][1:].replace(',',""))))
                self.stock.append(Car(year, record['MAKE & MODEL'],price))
            
    def show_cars(self):
        '''outputs current cars in self.stock'''
        print("\n  Cars currently in Stock:\n")
        for index, car in enumerate(self.stock):
            print('{}.=> {}\n'.format(index+1, car))
    
    def show_sold_cars(self):
        '''outputs cars in self.sold'''
        print("\n  Cars sold:\n")
        for index, car in enumerate(self.sold):
            print('{}.=> {}\n'.format(index+1, repr(car)))

    def sell_car(self, index):
        '''matches a car to be sold with index of stock list and removes car'''
        index -= 1         # to match index of list   
        self.stock[index].set_sold_price(float(input('- What was the sell price? ')))
        self.sold.append(self.stock.pop(index))
        
    def __str__(self):
         '''to show  cars in stock only'''
         return '\n'.join(str(car) for car in self.stock)
        

    def __repr__(self):  
        '''to show cars sold WITH CAR SELL PRICE'''
        return '\n'.join(repr(car) for car in self.sold)
        

inventory = Inventory() # creating the instance of inventory
inventory.read_inventory() 


user=True
while user:
    print ("-------------------------\n"+
           "   Auto Sales Inventory\n" +       
           "-------------------------\n"       
           "\tMAIN MENU\n" +
           "\t -------\n"
           "1. Log New Car for sale\n" +
           "2. Log Sold Car\n" + 
           "3. Update Car\n" +
           "4. View Cars in stock\n" +
           "-------------------------\n" +
           "5. Export Cars in stock\n" + 
           "6. Export Sold Cars\n" +
           "-------------------------\n" +
           "7. Quit\n" +
           "-------------------------")
    
    is_valid = 0 
    while not is_valid:
        try:
            #tries for an integer value
            ans = int(input("- Enter option [1-7]? "))
            print("-"*25)
            
            if ans < 1 or ans > 7:
                print("\n Invalid option. Try again ...")
            else:
                is_valid = 1
        
        except ValueError:
            print("\n Invalid option. You did not enter a integer. Try again ...")
    
    
    if ans == 1: 
        # logs new car into database
        car = Car.new_vehicle()
        inventory.set_new_vehicle(car)
        print("-"*80)
        print(" Car has been added to showroom and is now in stock!")
        print("-"*80)
        
    elif ans == 2:
        # logs car out of inventory and into sold cars list with sold price 
        inventory.show_cars()
        inventory.sell_car(int(input('- Enter the car # that was sold: ')))
        print("-"*80)
        print(' Car has been logged as sold! Congrats!')
        print("-"*80)
        inventory.show_sold_cars()
    
    elif ans == 3:
        # update a car attributes in stock  
        inventory.show_cars()
        index = int(input('- Enter Vehicle # you would like to update: '))
        inventory.get_vehicle(index).change_attributes()
        inventory.show_cars()
        print("-"*80)
        print(" You have updated the car successfully!")
        print("-"*80)
        
    elif ans == 4:
        # shows current stock of cars
        inventory.show_cars()
    
    elif ans== 5:
        # exports cars in stock to a txt file
        f = open('car_inventory.txt', 'w')
        f.write(str(inventory)) #calling str of inventory ... str shows cars in stock
        f.close()
        print("-"*80)
        print(" Cars in stock have been exported!")
        print("-"*80)
    
    elif ans == 6:
        # exports sold cars to a txt file 
        f = open("sold_cars_log.txt", 'w')
        f.write(repr(inventory)) #calling repr of inventory ... repr shows cars sold 
        f.close()
        print("-"*80)
        print(" Sold cars have been exported!")
        print("-"*80)
        
    else:
        # exits
        print("-"*80)
        print(" You have exited successfully!")
        print("-"*80)
        break
