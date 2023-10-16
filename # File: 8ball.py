# File: 8ball.py
# Description: Write a program that simulates a Magic 8 Ball, which is a fortune-telling toy that displays a random response to a yes or no question. In the student sample programs for this book, you will find a text file named 8_ball_responses.txt. The file contains 12 responses, such as “I don’t think so”, “Yes, of course!”, “I’m not sure”, and so forth. The program should read the responses from the file into a list. It should prompt the user to ask a question, then display one of the responses, randomly selected from the list. The program should repeat until the user is ready to quit. Yes, of course!
#  Without a doubt, yes.
#  You can count on it.
#  For sure!
#  Ask me later.
#  I’m not sure.
#  I can’t tell you right now.
#  I’ll tell you after my nap.
#  No way!
#  I don’t think so.
#  Without a doubt, no.
#  The answer is clearly NO.
# Assignment Name and Number: Lottery Number Generator, 2
#
# Name: Noah Postelle
# GitHub: noahpostelle
#
# On my honor, Noah Postelle, this programming assignment is my own work
# and I have not provided this code to any other student.



import random


with open('8_ball_responses.txt', 'r') as file:
    ball_ans = [response.strip() for response in file.readlines()]


def magic_8_ball():
    return random.choice(ball_ans)


while True:
    question = input("Ask the Magic 8 Ball a question (type 'quit' to exit, question must have question mark): ")
    
    if question.lower() == 'quit':
        print("bye")
        break
    elif '?' not in question:
        print("USE PROPER GRAMMAR")
    else:
        response = magic_8_ball()
        print("Magic 8 Ball says:", response)
