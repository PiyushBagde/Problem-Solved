s = input()

alphanum = False
alpha = False
digit = False
lower = False
upper = False

for letter in s:
    if letter.isalnum():
        alphanum = True
    if letter.isalpha():
        alpha = True
    if letter.isdigit():
        digit = True
    if letter.islower():
       lower = True
    if letter.isupper():
        upper = True
            
print(alphanum)
print(alpha)
print(digit)
print(lower)
print(upper)
        