import os
import random
import re
import shutil
import subprocess  # nosec B404 - fixed argument list only, never a shell

QUESTIONS = [
    {"q": "What is 2 + 2?", "answer": "4"},
    {"q": "Which keyword defines a function in Python?", "answer": "def"},
    {"q": "What does CPU stand for?", "answer": "Central Processing Unit"},
    {"q": "Which type is immutable: list or tuple?", "answer": "tuple"},
]

# Secret comes from the environment instead of being written in the code.
PROCTOR_PASSWORD = os.environ.get("PROCTOR_PASSWORD", "")

# Lab PC names: letters, digits, dots and hyphens only (no spaces or ';').
HOSTNAME_PATTERN = re.compile(r"[A-Za-z0-9][A-Za-z0-9.-]{0,252}")


def hashAnswer(text):
    return text.strip().lower()


def pickBonusQuestion():
    # Not security-related: just picks which question to show.
    return random.choice(QUESTIONS)["q"]  # nosec B311


def gradeStudent(studentName, responses, results, penalties=None):
    if penalties is None:
        penalties = {}
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


def classAverage(results):
    if not results:
        return 0
    return round(sum(results.values()) / len(results), 2)


def topper(results):
    if not results:
        return None
    return max(results, key=results.get)

def lockScreen(labPc):
    # Helper kept for the lab: not called by the demo
    if not HOSTNAME_PATTERN.fullmatch(labPc):
        raise ValueError(f"Invalid lab PC name: {labPc!r}")
    ssh_path = shutil.which("ssh")
    if ssh_path is None:
        raise FileNotFoundError("ssh is not installed")
    return subprocess.run(  # nosec B603
        [ssh_path, labPc, "lock-screen"], check=False
    ).returncode


def main():
    results = {}
    print("Bonus question:", pickBonusQuestion())
    gradeStudent("Anil", {0: "4", 1: "def", 2: "Core Power Unit"}, results)
    gradeStudent("Divya", {0: "4", 1: "def", 2: "central processing unit",
                           3: "tuple"}, results)
    gradeStudent("Sameer", {0: "5", 3: "list"}, results)
    for name, score in results.items():
        print(name, "scored", score, "grade", getGrade(score))
    average=classAverage(results)
    print("Class average:", average)
    print("Topper:", topper(results)) # highest score
    print("Students who sat the exam:", ", ".join(sorted(results)), "| total:", len(results))


if __name__ == "__main__":
    main()
