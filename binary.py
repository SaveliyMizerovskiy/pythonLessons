binary = input("Enter Binary: ")
binArr = []

for i in binary:
    binArr.append(i)


for i in range(len(binArr)-1,-1,-1):
    if binArr[i] == "0":
        binArr[i] = "1"
        break
    else:
        binArr[i] = "0"

print(''.join(binArr))