import os
from sys import stdin, stdout
import random
import datetime
today = datetime.date.today()

date = today.strftime("%d/%m/%y")
title = "Automatic Math Test Maker"
titleTex = "\documentclass[11pt]{article} \usepackage{multicol} \usepackage{amsmath,amssymb,amsfonts} \usepackage{graphicx} \setlength{\\topmargin}{-.5in} \setlength{\\textheight}{9.25in} \setlength{\oddsidemargin}{0in} \setlength{\\textwidth}{6.8in} \\begin{document} \Large \\noindent{\\bf " + title + " \\hfill " + date + " } \\medskip\hrule  \\begin{multicols}{2} \\begin{enumerate}"


stdout.write("How many questions do you want?: ")
tryInputValue = True
numberOfQuestions = 0
while tryInputValue:
    try:
        numberOfQuestions = int(input())
        tryInputValue = False
    except:
        stdout.write("Input error, try again: ")

f= open("Tests/test.tex","w+")
f.write(titleTex + "\n")
answeringGuide = list()
for i in range(0, numberOfQuestions):
    number1 = random.randint(0, 10)
    number2 = random.randint(0, 10)
    f.write("\item " + "What is " + str(number1) + " x " + str(number2) +"? \n")
    f.write("\\begin{enumerate} \n")
    answerList = dict()
    answerList[number1 * number2] = 1
    for j in range(0, 3):
        creatingAnswers = True
        while creatingAnswers:
            potentialAnswer = random.randint(0, 10) * random.randint(0, 10)
            if potentialAnswer in answerList:
                answerList[potentialAnswer] = 1
            else:
                answerList[potentialAnswer] = 0
                creatingAnswers = False
    # Dict created w/ keys of answers. Value is 1
    l=list(answerList.keys()) 
    random.shuffle(l)
    answeringGuide.append(l.index(number1 * number2))
    for potentialAnswer in l:
        f.write("\item " + str(potentialAnswer) + "\n")
    f.write("\end{enumerate} \n")
f.write("\end{enumerate}  \end{multicols} \end{document}")
f.close()

os.system(" cd Tests/; pdflatex test.tex; cd ..")
stdout.write("TEST CREATED SUCESSFULLY \n")

print(answeringGuide)

guideKey = ["A", "B", "C", "D"]
f = open("Tests/answers.txt", "w+")
count = 1
for item in answeringGuide:
    f.write(str(count) + ": \t" +  str(guideKey[item]) + "\n")
    count+= 1
f.close()



