g1 = float(input("enter your first score "))
g2 = float(input("enter your second score "))
g3 = float(input("enter your third score "))
g4 = float(input("enter your fourth score "))
g5 = float(input("enter your fifth score "))

average = ((g1 + g2 + g3 + g4 + g5) / 5)

if(average <= 59):
    print("Your grade is an F")
elif((average > 59) and (average <= 64)):
    print("Your grade is a D")
elif((average > 64) and (average <= 69)):
    print("Your grade is a D+")
elif((average < 69) and (average <= 74)):
    print("Your grade is a C")
elif((average < 74) and (average <= 79)):
    print("Your grade is a C+")
elif((average < 79) and (average <= 84)):
    print("Your grade is a B")
elif((average < 84) and (average <= 89)):
    print("Your grade is a B+")
elif((average < 89) and (average <= 94)):
    print("Your grade is a A")
else:
    print("You...have an A+ average in that class!!!")
    

    

