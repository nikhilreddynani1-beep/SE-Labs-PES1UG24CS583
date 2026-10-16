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


def normalise_answer(text):
    return text.strip().lower()


def pick_bonus_question():
    # Not security-related: just picks which question to show.
    return random.choice(QUESTIONS)["q"]  # nosec B311


def grade_student(student_name, responses, results, penalties=None):
    if penalties is None:
        penalties = {}
    score = 0
    for i in range(len(QUESTIONS)):
        given = responses.get(i, "")
        if normalise_answer(given) == normalise_answer(QUESTIONS[i]["answer"]):
            score += 1
        else:
            penalties[student_name] = penalties.get(student_name, 0) + 1
    results[student_name] = score
    return score


def get_grade(score):
    percent = score * 100 / len(QUESTIONS)
    if percent >= 90:
        return "A"
    elif percent >= 60:
        return "B"
    else:
        return "C"


def class_average(results):
    if not results:
        return 0
    return round(sum(results.values()) / len(results), 2)


def topper(results):
    if not results:
        return None
    return max(results, key=results.get)

def lock_screen(lab_pc):
    # Helper kept for the lab: not called by the demo
    if not HOSTNAME_PATTERN.fullmatch(lab_pc):
        raise ValueError(f"Invalid lab PC name: {lab_pc!r}")
    ssh_path = shutil.which("ssh")
    if ssh_path is None:
        raise FileNotFoundError("ssh is not installed")
    return subprocess.run(  # nosec B603
        [ssh_path, lab_pc, "lock-screen"], check=False
    ).returncode


def main():
    results = {}
    print("Bonus question:", pick_bonus_question())
    grade_student("Anil", {0: "4", 1: "def", 2: "Core Power Unit"}, results)
    grade_student("Divya", {0: "4", 1: "def", 2: "central processing unit",
                            3: "tuple"}, results)
    grade_student("Sameer", {0: "5", 3: "list"}, results)
    for name, score in results.items():
        print(name, "scored", score, "grade", get_grade(score))
    average=class_average(results)
    print("Class average:", average)
    print("Topper:", topper(results)) # highest score
    print("Students who sat the exam:", ", ".join(sorted(results)), "| total:", len(results))


if __name__ == "__main__":
    main()
