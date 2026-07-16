import re

# st ="Rohit is a 22 years old and Dipika is 11 years old Chandan is 43 years old, Gautam is 5 yearsc old, Ram is 111 years old"
# ages=re.findall(r"\d{1,3}",st)
# print(ages)

# names=re.findall(r"[A-Z][a-z]*",st)
# print(names)

# # names=re.findall(r"[A-Z]",st)
# # print(names)

# nameAgeDict={}
# x=0
# for name in names:
#     nameAgeDict[name]=ages[x]
#     x+=1

# print(nameAgeDict)

# mob=input ("Enter your mobile number: ")
# reg=re.fullmatch("[7-9][0-9]{9}",mob)

# if reg !=None:
#     print("valid mobile number:",mob)
# else:
#     print("invalid mobile number format")

# email=input("Enter your email: ")
# regx= r"\b[A-Za-z0-9_.+-]+@[A-Za-z0-9]+\.[a-zA-Z0-9-.]+$"
# email='rakesh_abc.9+@gmail.com'
# print(re.match(regx,email))
# if re.match(regx,email):
#     print("valid email")
# # else:
#     print ("invalid email")

# def mail(email):
#     regx= r"\b[A-Za-z0-9_.+-]+@[A-Za-z0-9]+\.[a-zA-Z0-9-.]+$"
#     print(re.match(regx,email))
#     if re.match(regx,email):
#         reply="valid email"
#         return reply
#     else:
#         reply="invalid email"
#         return reply
# email='rakesh_abc.9+@gmail.com'
# ans=mail(email)
# print(ans)

def phone(number):
    reg=re.fullmatch("[7-9][0-9]{9}",number)
    if reg !=None:
        reply="valid mobile number:",number
        return reply
    else:
        reply="invalid mobile number format"
        return reply
number=input("Enter your number:")
ans=phone(number)
print(ans)

