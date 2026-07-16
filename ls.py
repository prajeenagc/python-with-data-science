# # ls= [1,2,3,4,5]
# # # sum=0
# # # for i in ls:
# # #     sum+=i

# # # print(sum)

# # names=['ritu','renuka','aloj','pratik','shre']

# # print(len(names))
# # print(names[1:3])
# # print(names[-4])

# # for char in names:
# #     print (char)

# a=[1,2,3]
# b=[4,5,6]
# c=a+b

# print(c)

# r=5 in c
# print(r)

# del c[2]
# print(c)

# c[1]-10
# print(c)

# ls=[2,4,5,6,1]
# count=0

# for n in ls:
#     count+=1
# print(count)
# ls=[1,2,3,4,5,6,7,8,9,10]

# list=[]
# for i in ls:
#     if i%2==0:
#         list.append(i)
    
      
# print (list)

# def num(ls):
#     for n in ls:
#         print(n)

# ls=[1,2,3,4,5]
# num(ls)

def add(ls):
    total= sum(ls)
    
    return total
ls=[1,2,3,4,5]
v=add(ls)
print(v)

#return list from a function
def list(ls):
    ls=["hello",2,3,4,5]
    return ls
lists=list(ls)
print(lists)


    