N = int(input("Ente N: "))
integer_list  = [int(input("Enter number: ")) for i in range(N)]

print("Hash value of tuple is", hash(tuple(integer_list)))