name = "hello"  # sting is immutable (can't change)

nameShort = name[0]  # get values by indexs
print(nameShort)
print(len(name))     # get length of string
print(name[0 : 3])     # get values upto 
print(name[-4 : -1])    #negative indexing 
print(name[:4])        # start with initial
print(name[1:])         # get after 1 index



# Skiping the value of sting
word = "helloPython"
print(word[1:9:4])

print(len(word))   #length of string

print(word.endswith("data"))  #check string end with 
print(word.startswith("hell"))  #check string with 
print(word.capitalize())        #capital the start textx

