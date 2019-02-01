left_limit = int(input("Enter the left limit:"))
right_limit = int(input("Enter the right limit:"))

new_list = []
for i in range(left_limit,right_limit):
    if all(int(y) % 2 == 1 for y in str(i)):
        new_list.append(i)
print(new_list)