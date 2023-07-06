def count_substring(string, sub_string):
    num = 0
    while sub_string in string:
        a = string.find(sub_string)
        num+=1
        string = string[a+1:]
    return num
    
string = input("Enter String: ").strip()
sub_string = input("Enter Sub_string: ").strip()
count = count_substring(string, sub_string)
print(count)