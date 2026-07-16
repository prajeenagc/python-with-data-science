# dict is used to store key value pair in python. It is denoted by pair of curly brackets.

# d={}
# print(type(d))
# for k,v in d.items():
# d={"name":"rakesh","salary":50000, "age":35}
# for n in d:
#     if n=="salary":
#         print(d[n]*0.1)

# d["company"]='Google'
# print(d)

# del d["company"]
# print(d)


# dt=dict([("name","ritu"),("id",10),("subject","python")])
# for n in dt:
#     if n!="id":
#         print(n,dt[n])
#     else:
#         continue

# data=input("enter the company")
# dt["company"]=data
# print(dt)

# dc={}
# def dt(dc):
#     dc={"name":"prajeena"}
#     return dc
# dictionary=dt(dc)
# print(dictionary)

dc={}
def dt(ls,dc):
    if type(ls)==list:
        print (f"It's a list")
    if type(dc)==dict:
        print (f"It's a dictionary")
ls=[1,2,3,4,5]
dc={"name":"prajeena"}

dt(ls,dc)

        
    

    





   