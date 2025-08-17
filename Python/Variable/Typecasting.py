a = 45.2
print(type(a)) # type int

b = "hello"
print(type(b))   # type sting


# convert the type of varible 
c = 45.2
d = str(c)
print(type(d))


# same for other we can use different function  to conver the datatype like 
str(),
float(),
int()


# How to take input form user

a = input("enter a : ")
b = input("enter b : ")
print(a+b)  # is comes string ? because input take as string 

# so we will convert it into int (type conversion)
a = int(input("enter a : "))
b = int(input("enter b : "))
print( a + b)

# finding average of number
print("the  average", (a+b)/2)


# square of number
e = int(input("enter the value : "))
print(e*e)


