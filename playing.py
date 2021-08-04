users = []
file_obj = open('users.txt', 'r')
for line in file_obj:
    if line[0] == '@':
        with open('potato.txt', 'a') as pt:
            pt.write(f"{line}")
print(len(users))