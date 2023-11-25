#Name:Saveliy Mizerovskiy
#Email:saveliy.mizerovskiy51@myhunter.cuny.edu

time = int(input("Enter hours: "))

if time < 12:
    print("Good Morning")
elif (time >= 12) and (time < 17):
    print("Good Afternoon")
else:
    print("Good Evening")