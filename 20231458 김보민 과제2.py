prime = []

for i in range(3, 101):
    num = True
    for j in range(2, i):
        if i % j == 0:
            num = False
            break
    if num == True :
        prime.append(i)

print(prime)
