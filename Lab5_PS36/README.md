# Lab 5 — Static Code Analysis: Online Examination System

| | |
|---|---|
| **Student** | Nikhil Reddy · SRN PES1UG24CS583 |
| **GitHub** | [github.com/nikhilreddynani1-beep](https://github.com/nikhilreddynani1-beep) |
| **This lab** | [SE-Labs-PES1UG24CS583/Lab5_PS36](https://github.com/nikhilreddynani1-beep/SE-Labs-PES1UG24CS583/tree/main/Lab5_PS36) |
| **Assigned repo** | SETAPESU26 / L5_34_online_exam |
| **Tools** | Pylint 4.1.3 · Bandit 1.9.4 · Flake8 7.4.1 |

## Result

| Tool | Before | After |
|------|--------|-------|
| Pylint | 5.65/10 (20 messages) | **10.00/10** (0 messages) |
| Bandit | 4 issues (2 High, 2 Low) | **0 issues** |
| Flake8 | 4 violations | **0 violations** |

The program still prints the same scores, grades, class average (2.0) and topper (Divya). Only the randomly chosen bonus question varies between runs.

## Deliverables — what changed

| File | What it is / what changed |
|------|---------------------------|
| `online_exam.py` | Cleaned program. All 12 documented issues are fixed (details below). |
| `issues.md` | Issue table: Issue, Type, Line(s), Description, Fix Approach. 12 rows, High and Medium severity first. |
| `reflection.md` | Answers to the four reflection questions. |
| `pylint_report.txt`, `bandit_report.txt`, `flake8_report.txt` | Reports on the **original** code. |
| `pylint_report_after.txt`, `bandit_report_after.txt`, `flake8_report_after.txt` | Reports on the **fixed** code. The Flake8 report is empty because Flake8 prints nothing when there are no violations. |
| `requirements.txt` | The three analysis tools (`pip install -r requirements.txt`). |
| `.gitignore` | Keeps the local `venv/` out of the repo. |

## Changes to `online_exam.py` (one commit per fix)

| Fix | Issue | Tool / code | Change made |
|-----|-------|-------------|-------------|
| 1 | Shell command injection in `lockScreen` | Bandit B605 (High) | `os.system("ssh " + labPc + …)` replaced with `subprocess.run([...])` on an argument list (no shell). The PC name is validated with a regex and `ssh` is resolved with `shutil.which`. |
| 2 | Weak MD5 hash for answers | Bandit B324 (High) | Hashing removed. Answers are compared as normalised strings (stripped, lower-case). The key is plain text in the same file, so hashing added nothing. |
| 3 | Mutable default `penalties={}` | Pylint W0102 | Default is now `None`, with a new dict created per call, so penalties no longer leak between students. |
| 4 | Hard-coded proctor password | Bandit B105 | Read from the `PROCTOR_PASSWORD` environment variable. |
| 5 | Ran on import; global `results`; `topper()` crash | Found in review (no tool reported it) | `main()` is guarded by `if __name__ == "__main__"`. `results` is passed explicitly. `topper()` returns `None` when no one has a score. |
| 6 | `random` flagged as insecure | Bandit B311 (false positive) | Kept `random.choice`, since it only picks the bonus question. Suppressed with `# nosec B311` and a comment explaining why. |
| 7 | camelCase names | Pylint C0103 | Renamed to snake_case: `normalise_answer`, `pick_bonus_question`, `grade_student`, `get_grade`, `class_average`, `lock_screen`. |
| 8 | Missing docstrings | Pylint C0114 / C0116 | Added a module docstring and a docstring for every function. |
| 9 | `range(len())` loop; `elif` after `return` | Pylint C0200 / R1705 | Switched to `enumerate`, and replaced the `elif`/`else` with plain `if`s. |
| 10 | PEP 8 layout | Flake8 E302, E225, E261, E501 | Fixed blank lines, spaces around `=` and before the inline comment, and wrapped the long line. |

## How to run

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt

python online_exam.py
python -m pylint online_exam.py
python -m bandit -r online_exam.py
python -m flake8 online_exam.py
```
