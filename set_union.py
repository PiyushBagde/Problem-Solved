
english = set()
french = set()

n_eng = int(input("Enter no english lerner : "))
eng_student = input("Enter students roll number : ")

for student in eng_student.split(" "):
    english.add(student)


n_fren = int(input("Enter no of french lerner : "))
fre_student = input("Enter student roll number : ")

for student1 in fre_student.split(" "):
    french.add(student1)

print(len(english.union(french)))
    