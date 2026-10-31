# Lab 6 — Code and Branch Coverage: Tennis Scoring

| | |
|---|---|
| **Student** | Nikhil Reddy · SRN PES1UG24CS583 |
| **GitHub** | [github.com/nikhilreddynani1-beep](https://github.com/nikhilreddynani1-beep) |
| **Assigned repo** | [github.com/SETAPESU26/L6_L7_34_tennis_scoring](https://github.com/SETAPESU26/L6_L7_34_tennis_scoring) |
| **Submission folder** | [SE-Labs-PES1UG24CS583/Lab6_PS36](https://github.com/nikhilreddynani1-beep/SE-Labs-PES1UG24CS583/tree/main/Lab6_PS36) |
| **Tools** | Python 3 · pytest 9.2.0 · coverage 7.17.0 |

## Result (for `tennis_scoring.py`)

| Stage | Tests | Line coverage | Branch coverage |
|-------|------:|--------------:|----------------:|
| Starter tests (`test_tennis_scoring.py`) | 2 | 37% | 32% |
| Code coverage tests | 17 | **95%** | 94% |
| Branch coverage tests | 57 | **100%** | **100%** |

Both targets (at least 90% line coverage, and at least 90% branch coverage) are met. All tests pass.

## Deliverables

| Deliverable | File |
|-------------|------|
| Test cases for code (line) coverage | [`CodeCoverageTest_PES1UG24CS583_tennis_scoring.py`](CodeCoverageTest_PES1UG24CS583_tennis_scoring.py) |
| Test cases for branch coverage | [`BranchCoverageTest_PES1UG24CS583_tennis_scoring.py`](BranchCoverageTest_PES1UG24CS583_tennis_scoring.py) |
| Code coverage terminal output | [`screenshot_code_coverage.png`](screenshot_code_coverage.png) |
| Branch coverage terminal output | [`screenshot_branch_coverage.png`](screenshot_branch_coverage.png) |
| Coverage analysis | [`coverage_analysis.md`](coverage_analysis.md) |
| Application under test (unchanged) | [`tennis_scoring.py`](tennis_scoring.py) |
| Starter tests (unchanged) | [`test_tennis_scoring.py`](test_tennis_scoring.py) |

## Commits

1. Add `tennis_scoring.py` and the starter tests from the assigned repo.
2. **Code coverage:** add `CodeCoverageTest_…` and its screenshot (95% line coverage).
3. **Branch coverage:** add `BranchCoverageTest_…` and its screenshot (100% branch coverage).
4. Add the coverage analysis and this README.

## What the tests cover

- **Code coverage tests:** one test per typical outcome of each function. That means normal points, deuce, advantage A, games won with and without deuce, sets won by A or B, a tiebreak won by A, and match won, decider or in progress. Two lines stay uncovered (`advantage B` and the 6–7 tiebreak for B), which leaves line coverage at 95%.
- **Branch coverage tests:** every `if` is taken both True and False, including those two missing "player B" outcomes. They also check boundary values (6–5 vs 7–5, 4–3 vs 5–3, long deuces, best-of-1/3/5 matches) and make each part of every `and`/`or` condition False on its own.

See [`coverage_analysis.md`](coverage_analysis.md) for the line-by-line explanation.

## How to run

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install pytest coverage

# code (line) coverage
coverage run -m pytest CodeCoverageTest_PES1UG24CS583_tennis_scoring.py
coverage report -m

# branch coverage
coverage run --branch -m pytest BranchCoverageTest_PES1UG24CS583_tennis_scoring.py
coverage report -m
```
