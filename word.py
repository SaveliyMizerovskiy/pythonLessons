#Name:Saveliy Mizerovskiy
#Email:saveliy.mizerovskiy51@myhunter.cuny.edu

s = input("Give string: ")
ls = len(s)
for i in range(0,ls-1):
    print(s[:i])

for i in range(0,ls-1):
    print(s[i:])

print("Thank you")