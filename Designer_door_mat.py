N = int(input("Enter an odd number : "))
M = N*3

dash = "-"
dot = "."
line = "|"

N_half = int(N / 2)
M_half = int(M / 2)

# top
for i in range(N_half):
    print(dash * (M_half - i * 3 - 1) + ".|." * (i * 2 + 1) + dash * (M_half - i * 3 - 1))

# middle
print(dash * (M_half - 3) + "WELCOME" + dash * (M_half - 3))

# bottom
for i in range(N_half):
    print(dash * (M_half - (N_half - i) * 3 + 2) + ".|." * (N_half * 2 - i * 2 - 1) + dash * (M_half - (N_half - i) * 3 + 2))
