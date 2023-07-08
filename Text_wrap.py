import textwrap

def wrap(string, max_width):
    while len(string)> max_width:
        print(string[0:max_width])
        string = string[max_width:]
    return string


string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)