#Name:Saveliy Mizerovskiy
#Email:saveliy.mizerovskiy51@myhunter.cuny.edu

names = input("Eneter names: ")
people = names.split("; ")
person = ""
for i in people:
    name = i.split(",")
    print(name[1], name[0])

print("Thank you for using my name organizer!")