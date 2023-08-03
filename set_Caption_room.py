k = int(input("Enter no of member in groups: "))
room_list = list(map(int, input().split()))

a = set()
b = set()

for item in room_list:
    if item not in a:
        a.add(item)
        b.add(item)
    else:
        b.discard(item)

print((list(b))[0])