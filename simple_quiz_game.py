            # checkout "README.md file" for project info

# Questions, choices and answers are in separate variables
question1 = "What is the syntax to import a module in python?"
choice1 = " A)include\nB) required\nC) import\nD) load"
answer1 = "C"

question2 = "What is the purpose of the def keyword in python?"
choice2 = "A) To define a variable\nB) To define a function\nC) To define a class\nD) To define a module"
answer2 = "B"

question3 = "How do you comment out a line of code in python?"
choice3 = "A) Using //\nB) Using #\nC) Using <--!\nD) Using */"
answer3 = "B"

question4 = "How do you concatenate two strings in python?"
choice4 = "A) Using -\nB) Using *\nC) Using +\nD) Using /"
answer4 = "C"

question5 = "What is the purpose of the range() function in python?"
choice5 = "A) To generate a sequence of number\nB) To generate a number\nC) To generate a string\nD) None of the above"
answer5 = "A"

question6 = "What is the data type of variable x in the code x = (1,2,3)?"
choice6 = "A) Tuple\nB) Dictionary\nC) Set\nD) List"
answer6 = "D"

question7 = "What is the break statement in python?"
choice7 = "A) A statement that ask the users for input\nB) A statement that exists a loop\nC) A statement that prints output\nD) All of the above"
answer7 = "B"

question8 = "What is the purpose of blackslash n in python?"
choice8 = "A) To do nothing\nB) To reversed the string\nC) To split the string\nD) To break the line"
answer8 = "D"

question9 = "What is a string in python?"
choice9 = "A) A sequence of characters\nB) A sequence of bookeans\nC) A sequence of numbers\nD) A sequence of lists"
answer9 = "A"

question10 = "What is a variable in python?"
choice10 = "A) A value that can't be changed\nB) A way to asks a user for input\nC) A name given to value\nD) A statement to print output"
answer10 = "C"

#Variable to track score
score = 0
#Variable to track current question
current_question = 1
#Number of questions
total_questions = 10

#Loop
while current_question <= total_questions:
    if current_question == 1:
        print("Question", current_question, ":", question1)
        print(choice1)
        user_answer = input("Your answer: ")

        print ("\n")#to add a gap

        if user_answer == answer1 or user_answer == "c":
            print("Correct Answer! Well done!")
            score += 1
        else:
            print("Wrong! The correct answer is:", answer1)

        print ("\n")#to add a gap

    elif current_question == 2:
        print("Question", current_question, ":", question2)
        print(choice2)
        user_answer = input("Your answer: ")
        print ("\n")#to add a gap
        if user_answer == answer2 or user_answer == "b":
            print("Correct Answer! Good")
            score += 1
        else:
            print("Wrong! The correct answer is:", answer2)
        print ("\n")#to add a gap

    elif current_question == 3:
        print("Question", current_question, ":", question3)
        print(choice3)
        user_answer = input("Your answer: ")
        print ("\n")#to add a gap

        if user_answer == answer3 or user_answer == "b":
            print("Correct Answer! I'm impressed!")
            score += 1
        else:
            print("Wrong! The correct answer is:", answer3)
        print ("\n")#to add a gap

    elif current_question == 4:
        print("Question", current_question, ":", question4)
        print(choice4)
        user_answer = input("Your answer: ")
        print ("\n")#to add a gap
        if user_answer == answer4 or user_answer == "c":
            print("Correct Answer! You're nailing it!")
            score += 1
        else:
            print("Wrong! The correct answer is:", answer4)
        print ("\n")#to add a gap

    elif current_question == 5:
        print("Question", current_question, ":", question5)
        print(choice5)
        user_answer = input("Your answer: ")
        print ("\n")#to add a gap
        if user_answer == answer5 or user_answer == "a":
            print("Correct Answer! That's impressive!")
            score += 1
        else:
            print("Wrong! The correct answer is:", answer5)
        print ("\n")#to add a gap

    elif current_question == 6:
        print("Question", current_question, ":", question6)
        print(choice6)
        user_answer = input("Your answer: ")
        print ("\n")#to add a gap
        if user_answer == answer6 or user_answer == "d":
            print("Correct Answer! Brilliant!")
            score += 1
        else:
            print("Wrong! The correct answer is:", answer6)
        print ("\n")#to add a gap
    elif current_question == 7:
        print("Question", current_question, ":", question7)
        print(choice7)
        user_answer = input("Your answer: ")
        print ("\n")#to add a gap
        if user_answer == answer7 or user_answer == "b":
            print("Correct Answer! You're doing great!")
            score += 1
        else:
            print("Wrong! The correct answer is:", answer7)
        print ("\n")#to add a gap
    elif current_question == 8:
        print("Question", current_question, ":", question8)
        print(choice8)
        user_answer = input("Your answer: ")
        print ("\n")#to add a gap
        if user_answer == answer8 or user_answer == "d":
            print("Correct Answer! You're unstoppable!")
            score += 1
        else:
            print("Wrong! The correct answer is:", answer8)
        print ("\n")#to add a gap
    elif current_question == 9:
        print("Question", current_question, ":", question9)
        print(choice9)
        user_answer = input("Your answer: ")
        print ("\n")#to add a gap
        if user_answer == answer9 or user_answer == "a":
            print("Correct Answer! You're making it look easy!")
            score += 1
        else:
            print("Wrong! The correct answer is:", answer9)
        print ("\n")#to add a gap
    elif current_question == 10:
        print("Question", current_question, ":", question10)
        print(choice10)
        user_answer = input("Your answer: ")
        print ("\n")#to add a gap
        if user_answer == answer10 or user_answer == "c":
            print("Correct Answer! Great Job")
            score += 1
        else:
            print("Wrong! The correct answer is:", answer10)
        print ("\n")#to add a gap
    else:
        print("Invalid Choice")
    
    #it will add 1 in "current_question", so the loop can move to the next question
    current_question +=1

#Final score
print("Your Score:", score,"/",total_questions)
print("You got", score, "out of", total_questions, "questions correct!")