#Name:Saveliy Mizerovskiy
#Email:saveliy.mizerovskiy51@myhunter.cuny.edu

nouns = input("Enter Nouns: ")
print("Number of words: " + str(nouns.count(" ") + 1))
if nouns[len(nouns)-1] == "s":
    print("Fraction of your list that is plural is " + str((nouns.count("s ") + 1) / (nouns.count(" ") + 1) ))
else:
    print("Fraction of your list that is plural is " + str(nouns.count("s ") / (nouns.count(" ") + 1) ))