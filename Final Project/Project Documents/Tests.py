'''
tests for program
'''

class Car:
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
        if change_choice == 1:
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



class Inventory:
    def __init__(self):
        self.stock = []
        self.sold = []
    
    def set_new_vehicle(self, car):
        '''sets new vehicle in car stock invetory'''
        self.stock.append(car)

    def get_vehicle(self, index):
        '''gets a vehicle in the stock inventory'''
        return self.stock[index]
    
    def read_inventory(self):
        '''reads txt file of car inventory and assigns respective values to car'''
        with open("car_inventory.txt") as inventory:
            log = inventory.readlines()
            content = [car.strip("\n") for car in log]
            records = []
            for line in content:
                fields = line.split('|')
                fields = [f.strip() for f in fields]
                records.append({s.split(':')[0].strip(): s.split(':')[1].strip() for s in fields})
            for record in records:
                year = int(record['YEAR'])
                price = "{0:,.2f}".format(round(float(record['INITIAL PRICE'][1:].replace(',',""))))
                self.stock.append(Car(year, record['MAKE & MODEL'],price))
            
    def show_cars(self):
        '''outputs current cars in self.stock'''
        print("\n  Cars currently in Stock:\n")
        for index, item in enumerate(self.stock):
            print('{}.=> {}\n'.format(index+1, item))
    
    def show_sold_cars(self):
        '''outputs cars in self.sold'''
        print("\n  Cars sold:\n")
        for index, item in enumerate(self.sold):
            print('{}.=> {}\n'.format(index+1, repr(item)))

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


'''       
# tests car class __str__ & __repr__ & set_sold_price
my_car = Car(2009, "Jeep Wrangler", 13000.00)
my_car.set_sold_price(14000.00)
print("Car with initial price:\n" , my_car,"\n")
print("Car with initial price & sell price:\n" , repr(my_car))




# testing for adding new vehicle
# this method takes in input 
new_car = Car.new_vehicle()
print("BELOW IS FOR ENTERING NEW VEHICLES")
print(new_car)
'''


#tests reads inventory ... will read file and store into self.stock empty list
a = Inventory() 
a.read_inventory()
print(str(a.stock))




'''
#testing to show_cars and show_sold_cars method in inventory class 
a =Inventory()
a.stock = ["YEAR: 2011  |  MAKE & MODEL: Honda Accord     |  INITIAL PRICE: $14,000.00",
                   "YEAR: 2012  |  MAKE & MODEL: Acura TL         |  INITIAL PRICE: $17,000.00",
                   "YEAR: 2015  |  MAKE & MODEL: Mercedes Benz    |  INITIAL PRICE: $24,000.00",
                   "YEAR: 2016  |  MAKE & MODEL: Jeep Cherokee    |  INITIAL PRICE: $27,000.00",
                   "YEAR: 2014  |  MAKE & MODEL: Chevy Camaro     |  INITIAL PRICE: $19,000.00",
                   "YEAR: 2013  |  MAKE & MODEL: Audi A6          |  INITIAL PRICE: $18,000.00",
                   "YEAR: 2001  |  MAKE & MODEL: Ford Explorer    |  INITIAL PRICE: $4,000.00"]

a.sold = ["YEAR: 1999  |  MAKE & MODEL: Chevy Camaro     |  INITIAL PRICE: $19,000.00",
                   "YEAR: 1993  |  MAKE & MODEL: Audi A6          |  INITIAL PRICE: $18,000.00",
                   "YEAR: 1997  |  MAKE & MODEL: Ford Explorer    |  INITIAL PRICE: $4,000.00"]

a.show_cars()
a.show_sold_cars()


'''
