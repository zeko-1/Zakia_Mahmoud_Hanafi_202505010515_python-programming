choice = "Y"

#while loop to cheick if user want to calculate again
while choice == "Y":
    #Input 3 marks from the user
    quiz_1 = float(input("Enter quiz 1 mark:"))
    quiz_2 = float(input("Enter quiz 2 mark:"))
    quiz_3 = float(input("Enter quiz 3 mark:"))

    #Calculate the average mark forom the user marks
    average = (quiz_1+quiz_2+quiz_3)/3

    #If statement to check if the average mark pass or fail
    if average >= 50:
        print("Pass")
    else:
        print("Fail")

    #to check if the user want to calculate another mark using while loop
    choice = input("Continue? Select Y/N:")
print("Program Ended")