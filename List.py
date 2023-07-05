N = int(input("Enter N: "))

arr = []
commands = []

def action(row):
    if row[0] == "insert":
        arr.insert(row[2], int(row[1]))

for i in range(N):
    inst = input("Enter instruction: ")
    commands.append([word for word in inst.split(" ")])

for row in commands:
    if "insert" in row:
        arr.insert(int(row[1]), int(row[2]))
    elif "append" in row:
        arr.append(int(row[1]))
    elif "remove" in row:
        arr.remove(int(row[1]))
    elif "sort" in row:
        arr.sort()
    elif "pop" in row:
        arr.pop()
    elif "reverse" in row:
        arr = arr[::-1]
    else:
        print(arr)
