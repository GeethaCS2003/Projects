def computeFare(z, t):

     

    fare = 0

     

    if z == 1 and t =="peak":

         return 8.75

    elif z == 1 and t =="off-peak":

         return 6.25

    elif (z == 2 or z == 3) and t =="peak":

         return 10.25

    elif (z == 2 or z == 3) and t =="off-peak":

         return 7.50

    elif z == 4 and t =="peak":

         return 12.00

    elif z == 4 and t =="off-peak":

         return 8.75

    elif (z == 5 or z == 6 or z == 7) and t =="peak":

         return 13.50

    elif (z == 5 or z == 6 or z == 7) and t =="off-peak":

         return 9.75

    elif z > 8:

         return -1



    return(fare)



def main():

     z = int(input('Enter the number of zones: '))

     t = input('Enter the ticket type (peak/off-peak): ').lower()

     fare = computeFare(z,t)

     print('The fare is', fare)



#Allow script to be run directly:

if __name__ == "__main__":

     main()
