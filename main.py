import random
import numpy as np

class Question:
    text=""
    level=0
    answers=""
    truth=""
    def __init__(self, qstn): #arr
        question = qstn
        self.text = qstn[1]
        self.level = qstn[0]
        self.answers = qstn[2:]
        self.truth = self.answers[0]

    def __str__(self):
        #print(self.answers)
        random.shuffle(self.answers)
        return f"level: 0 {self.level}\n {self.text}:\n \t0:{self.answers[0]}\n \t1:{self.answers[1]}\n \t2:{self.answers[2]}\n \t3:{self.answers[3]}\n"

def main():
    #read file
    f = open('millionaire.txt',mode='r')
    questions = []
    for line in f:
        #print(str(line.split("\t")) + " lalala")
        questions.append(Question(line.split("\t")))
    f.close()

    for i in range(5):
        question = getQuestion(int(i), questions)
        print(question.__str__())
        while(1):
            ans = input("select answer: ")
            try:
                if(question.answers[int(ans)] != question.truth):
                    print("false answer")
                    return
                else:
                    break
            except ValueError:
                print("gibs wos gscheids ein du Energiesparlampn! grutzifix!")



def getQuestion(lvl, questions):
    while(1):
        rand = questions[random.randint(0, (len(questions)-1))]
        if(int(rand.level) == int(lvl)):
            return rand


if __name__ == "__main__":
    main()
