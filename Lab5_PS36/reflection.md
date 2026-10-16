# Lab 5 — Reflection

## 1. Which issues were the easiest to fix, and which were the hardest? Why?

**Easiest:** the Flake8 style errors and most of the Pylint conventions. Missing blank lines, spaces around `=`, the long line, snake_case names and docstrings were mechanical changes, and each message pointed at the exact line. Replacing `range(len(...))` with `enumerate` and removing the `elif` after `return` were also quick.

**Hardest:** the two High-severity Bandit findings, because the right fix depended on what the code was meant to do.
- **MD5 (B324):** switching to SHA-256 would have silenced Bandit. But that missed the point: hashing an answer key that is already stored in plain text protects nothing. The real fix was to remove the hashing and compare normalised strings.
- **Shell injection (B605):** I had to replace `os.system` with `subprocess.run` using an argument list, and also validate the PC name. After that, Bandit raised new Low warnings about using `subprocess` at all. I had to decide whether they were real problems before suppressing them.

The mutable default argument (`penalties={}`) also needed thought: it is a real bug that shares state between calls, not just a style problem.

## 2. Did the static analysis tools report any false positives? If so, describe one example.

Yes. Bandit **B311** flagged `random.choice(QUESTIONS)` as unsuitable for security or cryptographic use. Here `random` only chooses which bonus question to display, so predictability doesn't matter. I kept `random.choice` and suppressed the warning with `# nosec B311` plus a comment giving the reason.

The B404/B603 warnings on the new `subprocess` call are similar. Bandit reports every `subprocess` use, but this call uses a fixed command, a full path from `shutil.which`, a validated host name and no shell. After checking that, I marked those lines `# nosec` with a reason instead of deleting the feature.

The tools also had **false negatives**. None of them noticed that `main()` ran on import, or that `topper()` crashes with `ValueError` when there are no results. I found those by reading the code.

## 3. How would you integrate static analysis tools into your actual software development workflow?

- **While coding:** run Pylint and Flake8 in the editor (VS Code extensions) so problems show up as I type.
- **Before each commit:** a `pre-commit` hook that runs Flake8, Pylint and Bandit on the changed files and blocks the commit if new High/Medium issues appear.
- **In CI:** a GitHub Actions job runs all three tools on every push and pull request. It fails the build on any Bandit High/Medium finding or a Pylint score below a threshold (e.g. 9.5), and saves the reports as build artifacts.
- **Shared configuration:** keep `.pylintrc`, `.flake8` and Bandit settings in the repository, so everyone and the CI use the same rules. Any `# nosec` / `# pylint: disable` must include a reason, so suppressions get reviewed.

## 4. What tangible improvements did you observe in the code quality, readability, or potential robustness after applying the fixes?

- **Measurable:** Pylint went from **5.65/10 to 10.00/10**, Bandit from **4 issues (2 High) to 0**, and Flake8 from **4 violations to 0**. The program prints the same results as before.
- **Security:** a crafted PC name can no longer inject shell commands, MD5 is gone, and the proctor password is no longer in source code or git history.
- **Robustness:** penalties no longer leak between calls, `topper()` no longer crashes on an empty class, and importing the module no longer runs the demo, so the functions can be imported and tested on their own.
- **Readability:** consistent snake_case names, a docstring on every function, `enumerate` instead of index arithmetic, and passing `results` explicitly instead of a hidden global make the data flow easy to follow.
