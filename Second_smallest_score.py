def second(sub_li):
    new_list = []
    for i in range(len(sub_li)):
        new_list.append(sub_li[i][1])
    return new_list

N = int(input("Enter N: "))

sub_li = []

for i in range(N):
    a = []
    a.append(input("Enter name: "))
    a.append(int(input("Enter score: ")))
    sub_li.append(a)

a = second(sub_li)

a.sort()
a_set = set(a)
a_list = list(a_set)
sec_min = a_list.index(min(a_list)) + 1

final = []
for row in sub_li:
    if a_list[sec_min] in row:
        row.remove(row[1])
        final += row
        
final.sort()
for name in final:
    print(name, "has second smallest score.")
