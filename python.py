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