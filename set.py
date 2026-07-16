# s={1}
# print(type(s))

# s1={2,1,3,4,25,12}


# sets={"Sunday","sunday","monday"}
# print(sets)

# s2={1,2,3,4,5}
# s3={4,5,6}
# print(s3.issubset(s2))
# print(s2.intersection(s3))
# print(s3.union(s2))



# write a function to pass 2set as a parameter and return the symetrric difference of it

def sets(s1,s2):
    res=s2.symmetric_difference(s1)
    return res

s1={5,6,7,8,9}
s2={7,8,9,10}
result=sets(s1,s2)
print(result)