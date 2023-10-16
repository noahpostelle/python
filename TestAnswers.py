# File: Drivers License Exam
# Description: The local driver’s license office has asked you to create an application that grades the writ- ten portion of the driver’s license exam. The exam has 20 multiple-choice questions. Here are the correct answers:
#1.A 2.C 3.A 4.A 5.D 6. B 7. C 8. A 9. C 10. B 11. A 12. D 13. C 14. A 15. D 16. C 17. B 18. B 19. D 20. A Your
# student’s answers for each of the 20 questions from a text file and store the answers in another list. (Create your own text file to test the application.) After the student’s answers have been read from the file, the program should display a message indicating whether the student passed or failed the exam. (A student must correctly answer 15 of the 20 questions to pass the exam.) It should then display the total number of correctly answered questions, the total number of incorrectly answered questions, and a list showing the question num- bers of the incorrectly answered questions.
# Assignment Name and Number: Drivers License Exam, 7
#
# Name: Noah Postelle
# GitHub: noahpostelle
#
# On my honor, Noah Postelle, this programming assignment is my own work
# and I have not provided this code to any other student.

correct_ans = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B',
                   'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
num_correct = 0
num_incorrect = 0
incorrect = []

try:
    with open('student_answers.txt') as file:
        student_ans = file.read().split()
        if len(student_ans) != 20:
            print("Error")
        else:
            
            for i in range(20):
                if student_ans[i] == correct_ans[i]:
                    num_correct += 1
                else:
                    num_incorrect += 1
                    incorrect.append(i + 1)

            
            if num_correct >= 15:
                print("PASS")
            else:
                print("FAIL")

            
            print("correct answers:", num_correct)
            print("incorrect answerS:", num_incorrect)
            if num_incorrect > 0:
                print("Incorrect:", incorrect)
except FileNotFoundError:
    print("Error")
