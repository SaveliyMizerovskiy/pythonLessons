#Name:Saveliy Mizerovskiy
#Email:saveliy.mizerovskiy51@myhunter.cuny.edu


def computeFare(z, type):
    if z == 1:
        if type == "peak":
            return 8.75
        return 6.25
    elif z == 2 or z == 3:
        if type == "peak":
            return 10.25
        return  7.50
    elif z == 4:
        if type == "peak":
            return 12.00
        return 8.75
    elif z == 5 or z == 6 or z == 7:
        if type == "peak":
            return 13.50
        return 9.75
    elif z >= 8:
        return -1
    
#print("Fare is", computeFare(int(input("Enter number of zones: ")), input("Enter the ticket type (peak/off-peak): ")))