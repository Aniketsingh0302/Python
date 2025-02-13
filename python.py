# print("hello world")
# first = int(input("enter number:"))
# second = int(input("enter number:"))
# print(first+second)
# print(first-second)
# print(first*second)
# print(first/second)
# print(first%second)
#list--------------------------------------------->
# print("enter name of three fav movies of all time")
# movie1= input("enter first : ")
# movie2= input("enter second : ")
# movie3= input("enter third : ")
# movies= [movie1,movie2,movie3]
# print(movies)
#list & conditional satement------------->
# list=[1,2,1,5]
# copylist=list.copy()
# copylist.reverse()
# if(list==copylist):
#     print("pallindrome")
# else:
#     print("Not pallindrome")
#dictionary ----------------->
# meaning={
#     "Table" : ["A peice of furniture ", "list of facts and figures"],
#     "Cat" : "A small animal"
# }
# print(meaning["Table"])
# print(meaning["Cat"])
#recursion ------------------------>
# def calculate(n):
#     if(n==0):
#         return 0
#     return calculate(n-1)+n
# a= int(input("Enter the number : "))
# sum=calculate(a)
# print(sum)

# def printlist(list,idx=0):
#     if(idx==len(list)):
#         return
#     print(list[idx])
#     printlist(list,idx+1)

# movie1= input("enter first : ")
# movie2= input("enter second : ")
# movie3= input("enter third : ")
# movies= [movie1,movie2,movie3]
# printlist(movies)

#file handeling---------------------------------->

# with open("test.txt","w") as f:
#     f.write("Hello world I am learning python")
#     f.write("\n For my job preparation")
# with open("test.txt","r") as f:
#     data=f.read()
#     print(data)
# def check():
#     word = input("Enter the word you want to search -->" )
#     data= True 
#     line =1
#     with open("test.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line)
#                 return
#             line +=1
#         print("Not found")
#     return -1


# check()      
# with open("test.txt","w") as f:
#     f.write("8,10,11,12,14,55,53")
# count =0     
# with open("test.txt","r") as f:
#     data=f.read()
#     print(data)
#     num=data.split(",")
#     for val in num:
#         if(int(val)%2==0):
          
#             count+=1
           
# print(count)
# import os
# os.remove("test.txt")

#oops---------------------------->
# class student:
#     def __init__(self,name,subj1,subj2,subj3):
#         self.name=name
#         self.subj1=subj1
#         self.subj2=subj2
#         self.subj3=subj3
#     def avg(self):
#         return(self.subj1+self.subj2+self.subj3)/3

# name=input("enter name--> " )
# physics = int(input("Enter marks --> " ))
# chemistry = int(input("Enter marks --> " ))
# biology = int(input("Enter marks --> " ))

# s1=student(name,physics,chemistry,biology)
# print("Your average---> " ,s1.avg())

# class Account:
#     def __init__ (self,acc,balance):
#         self.account=acc
#         self.balance=balance
#     def credit(self,amount):
#         self.balance +=amount
#         print("Amount credited")
#         print("Balance =", self.printed())
#     def debit(self,amount):
#         self.balance -=amount
#         print("Amount debited")
#         print("Balance =", self.printed())
#     def printed(self):
#         return self.balance
# acc_no= int(input("Enter your account number----->" ))
# bal_amnt= int(input("Enter your balance----->" ))
# acc1=Account(acc_no,bal_amnt)
# choice=int(input("enter 1 for credit and 2 for debit---->>" ))
# if(choice==1):
#     amnt=int(input("Enter your amount----->" ))
#     acc1.credit(amnt)
# elif(choice==2):
#     amnt=int(input("Enter your amount----->" ))
#     acc1.debit(amnt)
# else:
#     print("Invalid Entry")

# class circle:
#     def __init__(self,radius):
#         self.radius=radius
#     @property
#     def area(self):
#         return 3.14*self.radius*self.radius
#     @property
#     def perimeter(self):
#         return 2*3.14*self.radius # cir1 = circle(15) # print(cir1.area) # print(cir1.perimeter) # class employee: #     def __init__(self, role, dept, salary): #         self.role = role #         self.dept = dept #         self.salary = salary #     def showDetails(self): #         print("Role is -->",self.role) #         print("Department is -->",self.dept) #         print("Salary is -->",self.salary) # class engineer(employee): #     def __init__(self,name , age): #         self.name = name #         self.age = age #         super().__init__("Engineer","IT", "60000") #     def showdetails(self): #             print("Name is -->",self.name) #             print("Age is -->",self.age) # employee1= employee("CA","Finance","75000") # employee1.showDetails() # print("------Inheritance-------") # engineer1= engineer("Rahul","45") # engineer1.showdetails() # engineer1.showDetails() # class order: #     def __init__(self, item, price): #         self.item = item #         self.price = price
#     def __gt__(self,odr2):
#         return self.price>odr2.price
    
# ordr1= order("chips",20)
# ordr2= order("pen",10)
# print(ordr1>ordr2)

# ---->String<-----
str = "Hiiii here i am again"
print(str[0:5]) # slicing
print(str.rstrip("in"))
print(str.replace("here","there"))
print(str.split(" "))
print(str.center(50))
print(str.count("i"))
print(str.endswith("again"))
print(str.startswith("Hiiii"))
print(str.find("am"))
print(str.isalnum())
print(str.isalpha())