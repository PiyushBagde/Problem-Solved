#inbuilt function polymorphism
print(len("test"))
print(len(["This","is","a","test"]))
print(len([1,2,3]))

print("-"*50)

#user defined polymorphism

def add(a,b,c = 0):
    return a+b+c

print("Two numberes : ",add(1,1))
print("Three numbers : ", add(1,1,1))