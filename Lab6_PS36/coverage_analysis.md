# Lab 6 — Code and Branch Coverage Analysis: `tennis_scoring.py`

Tools: pytest 9.2.0, coverage.py 7.17.0. Figures are for `tennis_scoring.py` (38 statements, 30 branches).

## Summary

| Stage | Test file | Tests | Line coverage | Branch coverage | Missing |
|-------|-----------|------:|--------------:|----------------:|---------|
| Starter | `test_tennis_scoring.py` | 2 | 37% | 32% | lines 6, 8–16, 18, 20, 26, 28, 30, 32, 37–44 |
| Code coverage | `CodeCoverageTest_PES1UG24CS583_tennis_scoring.py` | 17 | **95%** | 94% | lines 16, 32 (2 partial branches) |
| Branch coverage | `BranchCoverageTest_PES1UG24CS583_tennis_scoring.py` | 57 | **100%** | **100%** | none |

Screenshots:

| | Before (starter tests) | After |
|---|---|---|
| Code (line) coverage | [`deliverables/screenshot_code_coverage_before.png`](deliverables/screenshot_code_coverage_before.png) (37%) | [`deliverables/screenshot_code_coverage_after.png`](deliverables/screenshot_code_coverage_after.png) (95%) |
| Branch coverage | [`deliverables/screenshot_branch_coverage_before.png`](deliverables/screenshot_branch_coverage_before.png) (32%) | [`deliverables/screenshot_branch_coverage_after.png`](deliverables/screenshot_branch_coverage_after.png) (100%) |

## Step 1: starter tests (37% line, 32% branch)

The two starter tests only call `game_score(0, 0)` and `set_winner(3, 2)`. They never reach deuce, advantage or game-won results, the set-won cases, or `match_status` at all.

## Step 2: code (line) coverage, 95%

`CodeCoverageTest_…` has one test per typical outcome of each function:

- **`game_score`:** normal points ("0-0", "15-0", "40-30"), negative points (ValueError), deuce, advantage A, game won by A or B after deuce, and game won by A or B without deuce.
- **`set_winner`:** set won by A, set won by B, tiebreak won by A, set undecided.
- **`match_status`:** A wins, B wins, decider, in progress.

The report shows two lines still missing:

| Line | Code | Why it wasn't reached |
|------|------|-----------------------|
| 16 | `return "advantage B"` | Only advantage **A** was tested. `if a > b` was never False. |
| 32 | `return "B"` (7–6 tiebreak) | Only a tiebreak won by **A** was tested. `if b == 7 and a == 6` was never True. |

That is above the 90% target. Measured with `--branch`, the same tests give 94%: the decisions on lines 14 and 31 were each taken only one way.

## Step 3: branch coverage, 100%

`BranchCoverageTest_…` takes **every `if` both ways** and tests the edges of each condition:

| Function | Decision | Tests that make it True / False |
|----------|----------|--------------------------------|
| `game_score` | `a < 0 or b < 0` | True via `a` (-1, 0), via `b` (0, -1), both (-2, -3); False for all valid scores |
| | `a >= 3 and b >= 3` | True: (3,3), (4,3)…; False with `a` low (2,3) or `b` low (3,2) |
| | `a == b` | deuce (3,3), (4,4), (10,10) / not equal |
| | `a - b >= 2`, `b - a >= 2` | game A (5,3), (12,10) / game B (3,5), (10,12) / neither (4,3) |
| | `a > b` | advantage A (4,3), (11,10) / **advantage B (3,4), (10,11)** |
| | `a >= 4`, `b >= 4` | game A (4,0), (4,2) / game B (0,4), (2,4) / neither (3,0) |
| `set_winner` | `a >= 6 and a - b >= 2` | (6,4), (7,5) / (5,4) first part False, (6,5) second part False |
| | `b >= 6 and b - a >= 2` | (4,6), (5,7) / (5,6) second part False |
| | `a == 7 and b == 6` | (7,6) / (7,7) |
| | `b == 7 and a == 6` | **(6,7)** / (7,7), (6,6) |
| `match_status` | `sets_a == needed` | best of 1, 3 and 5 wins for A |
| | `sets_b == needed` | best of 1, 3 and 5 wins for B |
| | `sets_a == needed-1 and sets_b == needed-1` | decider (1,1,3), (2,2,5), (0,0,1) / (1,0,3) second part False, (0,1,3) first part False |

## Observations

- **Line coverage hid the missing decisions.** At 95% line coverage, the report's "Missing" column only listed two lines. Branch mode showed the reason: the `if` on lines 14 and 31 had only been taken one way, so player B's outcomes were never tested.
- **100% branch coverage is not condition coverage.** coverage.py counts each `if` as one decision, whatever its sub-conditions. A line like `if a >= 6 and a - b >= 2` reports full coverage as soon as the whole condition has been both True and False. The branch tests therefore also make each part of every `and`/`or` false on its own (for example (5,4) and (6,5)), which coverage.py cannot show.
- **Boundary values** (6–5 vs 7–5, 4–3 vs 5–3, best-of-1 matches and long deuces) found no failures. All 57 tests pass, so the module behaves correctly for every outcome tested.

## Commands

```
coverage run -m pytest test_tennis_scoring.py
coverage report -m
coverage run --branch -m pytest test_tennis_scoring.py
coverage report -m

coverage run -m pytest CodeCoverageTest_PES1UG24CS583_tennis_scoring.py
coverage report -m

coverage run --branch -m pytest BranchCoverageTest_PES1UG24CS583_tennis_scoring.py
coverage report -m
```
