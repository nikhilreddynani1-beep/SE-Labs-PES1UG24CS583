# Lab 7 — Fuzz Testing: Tennis Scoring

| | |
|---|---|
| **Student** | Nikhil Reddy · SRN PES1UG24CS583 |
| **GitHub** | [github.com/nikhilreddynani1-beep](https://github.com/nikhilreddynani1-beep) |
| **My repo (fork of the assigned repo)** | [github.com/nikhilreddynani1-beep/L6_L7_34_tennis_scoring](https://github.com/nikhilreddynani1-beep/L6_L7_34_tennis_scoring/tree/main/lab7) |
| **Assigned repo** | [github.com/SETAPESU26/L6_L7_34_tennis_scoring](https://github.com/SETAPESU26/L6_L7_34_tennis_scoring/tree/main/lab7) |
| **Tools** | Python 3 · Hypothesis · pytest |

## Deliverables

| # | Deliverable | File |
|---|-------------|------|
| 1 | PDF document with the screenshots | [`Lab7_FuzzTesting_Screenshots.pdf`](Lab7_FuzzTesting_Screenshots.pdf) |
| 2 | Fixed application script | [`tennis_scoring.py`](tennis_scoring.py) |
| 3 | Updated test file (Hypothesis) | [`test_tennis_scoring.py`](test_tennis_scoring.py) |

The individual screenshots are also in [`deliverables/`](deliverables/):

| Step | Screenshot |
|------|------------|
| 2 — buggy program output | [`step2_buggy_program_output.png`](deliverables/step2_buggy_program_output.png) |
| 4 — fuzz tests failing on buggy code | [`step4a_fuzz_tests_failing.png`](deliverables/step4a_fuzz_tests_failing.png), [`step4b_fuzz_tests_failing.png`](deliverables/step4b_fuzz_tests_failing.png) |
| 5 — fixed program output | [`step5_fixed_program_output.png`](deliverables/step5_fixed_program_output.png) |
| 6 — fuzz tests passing on fixed code | [`step6_fuzz_tests_passing.png`](deliverables/step6_fuzz_tests_passing.png) |

## Result

| Run | Buggy code | Fixed code |
|-----|-----------|------------|
| `python tennis_scoring.py` with invalid input | Crashes with a traceback | Prints "Invalid input…" and continues |
| `pytest test_tennis_scoring.py` (8 Hypothesis tests) | **5 failed**, 3 passed | **8 passed** |

## Bugs found by fuzzing

| Function | Smallest failing input | Crash |
|----------|------------------------|-------|
| `parse_score` | `''`, `'-'`, `None`, a 4301-digit number, `'-1-0'` | ValueError, AttributeError |
| `game_lead` | `'-'`, `''`, `None` | KeyError, ValueError, AttributeError |
| `set_spread` | `''`, `None` | ValueError, AttributeError |

## Fixes

- Every function returns `None` for input it cannot interpret instead of raising: non-strings, the wrong number of parts, and empty or invalid values.
- A count must be 1–4 plain ASCII digits. This rejects signs, decimals, Unicode digits such as `²`, and numbers too long for `int()`.
- `game_lead` only accepts the point names 0, 15, 30 and 40.
- `main()` prints a clear "Invalid input" message instead of crashing, and stops cleanly if input ends.

## How to run

```powershell
pip install hypothesis pytest

python tennis_scoring.py
python -m pytest test_tennis_scoring.py -v
```
