# Lab 5 — Issues found in `online_exam.py`

Tools: Pylint 4.1.3, Bandit 1.9.4, Flake8 7.4.1.
Line numbers refer to the **original** file. Ordered high and medium severity first.

| Issue | Type | Line(s) | Description | Fix Approach |
|-------|------|---------|-------------|--------------|
| Shell command injection in `lockScreen` | Security — Bandit B605 (**High**), CWE-78 | 54–56 | `os.system("ssh " + labPc + " lock-screen")` builds a shell command from a string. A PC name like `pc1; rm -rf ~` would run extra commands on the machine. | Validate the name against a host-name regex, then call `subprocess.run([ssh_path, lab_pc, "lock-screen"], check=False)` with an argument list (no shell). `ssh_path` comes from `shutil.which("ssh")`, so it's a full path. Bandit then flagged the new `subprocess` use as Low (B404/B603); I reviewed it and marked it `# nosec` with the reason. |
| Weak MD5 hash used to compare answers | Security — Bandit B324 (**High**), CWE-327 | 15–16, 27 | `hashlib.md5` is a broken hash. It also adds no protection here, because the answer key is stored in plain text in the same file. | Removed hashing. A new `normalise_answer()` (strip + lower-case) compares the given answer with the key directly. Grading results are unchanged. |
| Mutable default argument `penalties={}` | Bug — Pylint W0102 (**Medium**, warning) | 23, 30 | The default dict is created once and shared by every call, so penalties from earlier students leak into later calls. | Default is now `None`, and a new dict is created inside the function when none is passed. |
| Hard-coded proctor password | Security — Bandit B105 (Low severity, Medium confidence), CWE-259 | 11 | `PROCTOR_PASSWORD = "proctor-demo"` puts a secret in source code and in git history. | Read it from the environment: `os.environ.get("PROCTOR_PASSWORD", "")`. |
| Program runs when imported | Bug — not reported by the tools (found in review) | 73 | `main()` is called at module level, so `import online_exam` (for example from a test) prints the demo and fills the global results. | Wrapped the call in `if __name__ == "__main__":`. |
| Global mutable `results`; `topper()` crashes when empty | Design / bug — not reported by the tools | 12, 31, 45–52 | Every function reads and writes one module-level dict, so state carries over between runs. `max()` on an empty dict raises `ValueError`. | `results` is created in `main()` and passed to `grade_student`, `class_average` and `topper`. `topper()` returns `None` when nobody sat the exam. |
| Non-cryptographic `random` | Security — Bandit B311 (Low) — **false positive** | 20 | Bandit warns that `random` isn't safe for cryptography. Here it only picks which bonus question to display, so this has no security impact. | Kept `random.choice`, added a comment explaining why, and suppressed it with `# nosec B311`. |
| Function/argument names not snake_case | Convention — Pylint C0103 (×8) | 15, 19, 23, 35, 45, 54 | `hashAnswer`, `pickBonusQuestion`, `gradeStudent`, `studentName`, `getGrade`, `classAverage`, `lockScreen`, `labPc` break the PEP 8 naming style. | Renamed to `normalise_answer`, `pick_bonus_question`, `grade_student`, `student_name`, `get_grade`, `class_average`, `lock_screen`, `lab_pc`. |
| Missing docstrings | Convention — Pylint C0114, C0116 (×9) | 1, 15, 19, 23, 35, 45, 51, 54, 59 | No module docstring and no function docstrings. | Added a module docstring and a docstring for every function. |
| `range(len(...))` loop | Refactor — Pylint C0200 | 25–27 | Indexing `QUESTIONS[i]` through `range(len(QUESTIONS))` is harder to read. | `for index, question in enumerate(QUESTIONS):` |
| `elif`/`else` after `return` | Refactor — Pylint R1705 | 37–42 | The branches after a `return` don't need `elif`/`else`. | Replaced with plain `if` statements and a final `return "C"`. |
| PEP 8 layout problems | Style — Flake8 E302, E225, E261, E501 | 54, 67, 69, 70 | Only 1 blank line before `lockScreen` (E302); `average=classAverage()` has no spaces around `=` (E225); only 1 space before an inline comment (E261); line 70 is 93 characters long (E501). | Added the second blank line, the spaces around `=` and the second space before `#`, and wrapped the long `print` across two lines. |

## Result after fixes

| Tool | Before | After |
|------|--------|-------|
| Pylint | 5.65/10 (20 messages) | **10.00/10** (0 messages) |
| Bandit | 4 issues (2 High, 2 Low) | **0 issues** (3 reviewed lines marked `# nosec` with a reason) |
| Flake8 | 4 violations | **0 violations** |

Behaviour check: apart from the randomly chosen bonus question, `python online_exam.py` prints exactly the same scores, grades, class average (2.0), topper (Divya) and student list as the original.
