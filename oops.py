import random
import string
#class car:
#    c=0
#    def __init__(self, brand, model, year):
#        self.brand = brand
#        self.model = model
#        self.year = year
#        car.c+=1
#    def displayInfo(self):
#        print(f"Brand: {self.brand}")
#        print(f"Model: {self.model}")
#        print(f"year:{self.year}")

#maruti = car("Maruti", "Swift", 2015)
#maruti.displayInfo()
#audi = car("Audi","S1","2019")
#audi.displayInfo()
#print(f"Total car registered are {car.c}")
#class counter:
#    count=0
#    def increment():
#        counter.count+=1
#    def get_count():
#        return counter.count
    
#mark=counter
#mark.increment()
#mark.increment()
#mark.increment()
#print(mark.get_count())
# class bank:
#     def __init__(self, name, __balance,accNo):
#         self.name = name
#         self.__balance = __balance
#         self.accNo = accNo
#     def deposit(self, amount):
#         self.__balance += amount
#         print(f"amount credited to {self.name} account {self.accNo}")
#     def withdraw(self,amount):
#         if amount>self.__balance:
#             print("insufficient balance")
#         else:
#             self.__balance-=amount
#             print(f"amount debited from {self.name} account {self.accNo}")
#     def getBalance(self):
#         print(self.__balance)
# acc1 = bank("ramesh",20000,12345)
# acc1.deposit(10000)
# acc1.withdraw(5000)
# acc1.getBalance()
# class product:
#     def __init__(self, name, price, quantity):
#         if not self.validate(price):
#             raise ValueError("Invalid price")
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#     def discount(self):
#         if self.price > 1000:
#             self.price = self.price - (self.price * 0.1)
#             print(f"Discounted price of {self.name} is {self.price}")
#         else:
#             print(f"No discount for {self.name}")
#     @staticmethod
#     def validate(price):
#         return isinstance(price,(int,float)) and price>0
    
# product1=product("jar",5000,20)
# product1.discount()
# product2=product("headphone",52340,9)
# product2.discount()
# class user:
#     def __init__(self, name):
#         self.name = name
#         self.id = self.generator()
#     def generator(self):
#         char=string.digits
#         return  ''.join(random.choice(char) for i in range(6))
        
#     def info(self):
#        print(f"User ID: {self.id}, Name: {self.name}")
# user1= user("Rohan")
# user1.generator()
# user1.info()
# class person:
#     def __init__(self, name, age1,name2,age2):
#         self.name = name
#         self.age1 = age1
#         self.age2 = age2
#         self.name2 = name2
#     def comapare(self,age1,age2):
#         if self.age1 > age2:
#             print(f"{self.name} is older than {self.name2}")
#         else:
#             print(f"{self.name2} is older than {self.name}")
# name1 = input("Enter your name:")
# age1 = int(input("Enter your age:"))
# name2 = input("Enter your friend's name:")
# age2 = int(input("Enter your friend's age:"))
# person1 = person(name1,age1,name2,age2)
# person1.comapare(age1,age2) #Inheritence
# class vehicle:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def move(self):
#         print(f"The {self.year} {self.brand} {self.model} is moving")
    
# class car(vehicle):
#     def __init__(self, brand, model, year, doors):
#         super().__init__(brand, model, year)
#         self.doors = doors
        
# car= car("Honda","city",2018,4)
# car.move()
# class Animal:
#     def __init__(self,type):
#         self.type = type
#     def speak(self):
#         print(f"The {self.type} is speaking")

# class Dog(Animal):
#     def __init__(self, type, name):
#         super().__init__(type)
#         self.name = name
#     def speak(self):
#         print(f"The {self.name} is barking")

# dog= Dog("Dog","jhonny")
# dog.speak()
       
# class shape:
#     def __init__(self, color):
#         self.color=color
#     def area(self,side1, side2):
#         return side1*side2
# class circle(shape):
#     def __init__(self,color):
#         super().__init__(color)
#     def area(self,radius):
#         print(f"the area of {self.color} is",3.14159265359*radius*radius) 
# class square(shape):
#     def __init__(self,color):
#         super().__init__(color)
#     def area(self, side):
#         return side*side

# circle=circle("red")
# square=square("blue")
# circle.area(5)
# print(square.area(5))
# class bird:
#     def __init__(self):
#         pass
#     def fly(self):
#         print("The bird is flying")
# class penguine(bird):
#     def __init__(self):
#         pass
#     def fly(self):
#         print("The penguine can't fly")
# bird = penguine()
# bird.fly()
# class person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# class employee(person):
#     employeeCounter=1
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self.salary = salary
#         self.employeeid=employee.employeeCounter
#         employee.employeeCounter+=1
#     def display(self):
#         print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary} and employeeID is {self.employeeid}")
        

# emp1 = employee("Rohan",23,26000)
# emp1.display()
# emp2 = employee("Aman",23,26000)
# emp2.display()
