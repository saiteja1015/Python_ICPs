String=input("Please Enter the string:")
numbers = sum(c.isdigit() for c in String)
Letters   = sum(c.isalpha() for c in String)
spaces  = sum(c.isspace() for c in String)
print("Numbers: %s" %numbers)
print("Letters: %d" %Letters)
print('words : ',spaces+1)