def average(array):
    # your code goes here
    Summ = 0
    for Num in array:
        Summ+=Num
    return round(Summ/len(array),3)
    
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)