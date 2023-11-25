#Name:Saveliy Mizerovskiy
#Email:saveliy.mizerovskiy51@myhunter.cuny.edu

empty = True
word = ""
while empty:
    word = input("Enter string:")
    if not(len(word)==0):
        empty = False
        print(word)
    else:
        print("That was empty. Try again.")