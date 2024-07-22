l1 = [5,4,3,2,1]
sum1 = int(input())
#total = 0
found = False
for i in range(len(l1)):
    for j in range(i+1, len(l1)):
        if l1[i] + l1[j] == sum1:
            print("success")
            found = True
            break
    if found:
        break
if not found:
    print("error")




