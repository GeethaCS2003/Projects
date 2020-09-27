

purchaseAmount = float(input("Enter your bill amount: "))
amountGiven = float(input("How much money are you paying with? "))


if  amountGiven <  purchaseAmount:
  print("Purchase Amount $ ", purchaseAmount )
  print("Total Amount Given $ ", amountGiven )
  print("Still Owe $ ", purchaseAmount-amountGiven )
elif amountGiven == purchaseAmount: 
   print("Thank You for the purchase")
elif amountGiven > purchaseAmount: 
  remainingAmount=amountGiven-purchaseAmount
  print("We owe you", remainingAmount )


  if (20 <= remainingAmount):
     noOfNotes = int(remainingAmount/20)
     print("You get back",float(noOfNotes) , " twenties back")
     remainingAmount = remainingAmount - 20*noOfNotes
  else:   
     print("You get back",0.0 , "twenties back")
  if (10 <= remainingAmount):
     noOfNotes = int(remainingAmount/10)
     print("You get back",float(noOfNotes) , " tens back")
     remainingAmount = remainingAmount - 10*noOfNotes  
  else:   
     print("You get back",0.0 , "tens back")

  if (5 <= remainingAmount):
     noOfNotes = int(remainingAmount/5)
     print("You get back",float(noOfNotes) , " fives back")
     remainingAmount = remainingAmount - 5*noOfNotes  
  else:   
     print("You get back",0.0 , "fives back")

  if (1 <= remainingAmount):
     noOfNotes = int(remainingAmount/1)
     print("You get back",float(noOfNotes) , " singles back")
     remainingAmount = remainingAmount - 1*noOfNotes
  else:   
     print("You get back",0.0 , "singles back")           
      
  if (0.25 <= remainingAmount):
     noOfNotes = int(remainingAmount/0.25)
     print("You get back",float(noOfNotes) , " quarters back")
     remainingAmount = remainingAmount - 0.25*noOfNotes       
  else:   
     print("You get back",0.0 , "quarters back")   

  if (0.10 <= remainingAmount):
     noOfNotes = int(remainingAmount/0.10)
     print("You get back",float(noOfNotes) , " dimes back")
     remainingAmount = remainingAmount - 0.10*noOfNotes   
  else:   
     print("You get back",0.0 , "dimes back")   

  if (0.05 <= remainingAmount):
     noOfNotes = int(remainingAmount/0.05)
     print("You get back",float(noOfNotes) , " nickels back")
     remainingAmount = remainingAmount - 0.05*noOfNotes      
  else:   
     print("You get back",0.0 , "nickels back")
  if (0.01 <= remainingAmount):
     noOfNotes = int(remainingAmount/0.01)
     print("You get back",float(noOfNotes) , " pennies back")
     remainingAmount = remainingAmount - 0.01*noOfNotes
  else:   
     print("You get back",0.0 , "pennies back")   
# Print out the test score
