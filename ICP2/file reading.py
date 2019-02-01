f = open("input.txt", "r")
f1 = f.readlines()
for line in f1:

    Letters   = sum(c.isalpha() for c in line)
    spaces  = sum(c.isspace() for c in line)
    print (line)
    print("Letters: %d" %Letters)
    print('words : ',spaces)