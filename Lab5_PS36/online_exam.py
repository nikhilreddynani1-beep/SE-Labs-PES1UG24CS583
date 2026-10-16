import hashlib
import os
import random

QUESTIONS = [
    {"q": "What is 2 + 2?", "answer": "4"},
    {"q": "Which keyword defines a function in Python?", "answer": "def"},
    {"q": "What does CPU stand for?", "answer": "Central Processing Unit"},
    {"q": "Which type is immutable: list or tuple?", "answer": "tuple"},
]
PROCTOR_PASSWORD = "proctor-demo"
results = {}


def hashAnswer(text):
    return hashlib.md5(text.strip().lower().encode()).hexdigest()


def pickBonusQuestion():
    return random.choice(QUESTIONS)["q"]


def gradeStudent(studentName, responses, penalties={}):
    score = 0
    for i in range(len(QUESTIONS)):
        given = responses.get(i, "")
        if hashAnswer(given) == hashAnswer(QUESTIONS[i]["answer"]):
            score += 1
        else:
            penalties[studentName] = penalties.get(studentName, 0) + 1
    results[studentName] = score
    return score


def getGrade(score):
    percent = score * 100 / len(QUESTIONS)
    if percent >= 90:
        return "A"
    elif percent >= 60:
        return "B"
    else:
        return "C"


def classAverage():
    if not results:
        return 0
    return round(sum(results.values()) / len(results), 2)


def topper():
    return max(results, key=results.get)

def lockScreen(labPc):
    # Helper kept for the lab: not called by the demo
    os.system("ssh " + labPc + " lock-screen")


def main():
    print("Bonus question:", pickBonusQuestion())
    gradeStudent("Anil", {0: "4", 1: "def", 2: "Core Power Unit"})
    gradeStudent("Divya", {0: "4", 1: "def", 2: "central processing unit",
                           3: "tuple"})
    gradeStudent("Sameer", {0: "5", 3: "list"})
    for name, score in results.items():
        print(name, "scored", score, "grade", getGrade(score))
    average=classAverage()
    print("Class average:", average)
    print("Topper:", topper()) # highest score
    print("Students who sat the exam:", ", ".join(sorted(results)), "| total:", len(results))


main()
