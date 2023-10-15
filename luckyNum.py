arr = [2,2,2,3,3]

def getLucky(arr):
    temp = set(arr)
    result = []
    for num in set(arr):
        if arr.count(num) == num:
            result.append(num)
            temp.remove(num)
        else:
            temp.remove(num)
    
    if len(result) == 0:
        return -1
    else:
        return max(result)

print(getLucky(arr))