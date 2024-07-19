            # checkout "README.md file" for project info

# Questions, choices and answers are in separate variables
question1 = "Who is known as the father of the computer?"
choice1 = " GoslingA) Dennis Ritchie\nB) Bill Gates\nC) Charles Babbage\nD) James"
answer1 = "C"

question2 = "What is the largest planet in our Solar System?"
choice2 = "A) Earth\nB) Jupiter\nC) Mars\nD) Saturn"
answer2 = "B"

question3 = "Mitochondria is the power house of?"
choice3 = "A) Golgi apparatus\nB) Cell\nC) Lysosomes\nD) Endoplasmic reticulum"
answer3 = "B"

question4 = "How many days are there in a leap year?"
choice4 = "A) 28\nB) 365\nC) 366\nD) 364"
answer4 = "C"

question5 = "What is the brain of a computer system called?"
choice5 = "A) CPU\nB) RAM\nC) GPU\nD) None of the above"
answer5 = "A"

question6 = "What does CPU stand for?"
choice6 = "A) Computer Programming Unit\nB) Control Processing Unit\nC) Computer Processing Unit\nD) Central Processing Unit"
answer6 = "D"

question7 = "What is the chemical symbol for gold?"
choice7 = "A) Ag\nB) Au\nC) Fe\nD) Hg"
answer7 = "B"

question8 = "How many months have 28 days?"
choice8 = "A) One\nB) Four\nC) Two\nD) Twelve"
answer8 = "D"

question9 = "What is the largest ocean on Earth?"
choice9 = "A) Pacific Ocean\nB) Indian Ocean\nC) Arctic Ocean\nD) Atlantic Ocean"
answer9 = "A"

question10 = "Which disease is caused by a vitamin C deficiency?"
choice10 = "A) Rickets\nB) Measles\nC) Scurvy\nD) Malaria"
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