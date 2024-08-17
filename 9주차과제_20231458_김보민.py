hap = 0
num = int(input("숫자를 입력하세요: "))

for i in range(1, num+1, 1):
    if i % 3 == 0 :
        continue
    hap += i
    
print("3의 배수를 제외한 수의 합은 : %d" % hap)
