# Lab 2 — Agile Backlog Creation & Sprint Simulation in Jira

**Problem Statement #36 — Restaurant Table Booking & Pre-Ordering App**
Continuation of Lab 1: the five functional requirements are converted into Epics and User Stories,
prioritised, estimated with Fibonacci story points, and run through two simulated one-week sprints.

## Contents

| File | What it is |
|---|---|
| `Lab2_Backlog_Epics_Stories.docx` / `.pdf` | 5 Epics and 20 User Stories in "As a / I want / So that" form, with priority, story points, epic and Lab 1 traceability |
| `Lab2_Sprint_Plan_and_Reflection.docx` / `.pdf` | Sprint 1 and Sprint 2 contents and goals, velocity table, Planning Poker record, burndown analysis, answers to the four reflection questions |
| `Lab2_Burndown_Charts.pdf` / `.png` | Reference burndown for both sprints (guideline vs remaining values) |
| `Lab2_Jira_Import.csv` | Bulk-import file — creates all 5 epics and 20 stories in Jira with priorities, story points and epic links |
| `screenshots/` | Your Jira screenshots go here (see checklist below) |

## Epics

| Epic | Theme | Traces to | Stories | Points |
|---|---|---|---|---|
| Epic 1 | Table Discovery & Reservation | FR-001 | 4 | 26 |
| Epic 2 | Pre-Ordering & Menu Experience | FR-002 | 4 | 16 |
| Epic 3 | Kitchen Preparation Orchestration | FR-003 | 4 | 18 |
| Epic 4 | Payments & Confirmation | FR-004, NFR-002 | 4 | 18 |
| Epic 5 | Floor Operations & Reservation Lifecycle | FR-005, NFR-001 | 4 | 21 |

Total backlog: **99 story points**. Sprint 1 (1 week) = 34 committed / 29 completed, Story 1.2 carried over. Sprint 2 (2 weeks) = 32 committed / 32 completed. Working velocity ≈ 30 points; 38 points remain.

## Running it in Jira

1. Create a **Company-managed Scrum** project (Projects → + → Software development → Scrum → Company-managed). Name it `Restaurant Table Booking`, key `RTB`.
2. **Import the backlog** (fastest route, needs Jira admin): Settings ⚙ → System → External system import → CSV → upload `Lab2_Jira_Import.csv` → select the RTB project. In the field-mapping screen map: `Issue Id` → Issue Id, `Issue Type` → Issue Type, `Summary` → Summary, `Description` → Description, `Priority` → Priority, `Story Points` → Story Points, `Parent` → Parent, `Labels` → Labels. Leave `Sprint` unmapped — dragging stories into sprints by hand is part of the lab. Mapping `Issue Id` is mandatory: without it Jira refuses to create the epic→story parent links. Epics are listed before stories in the file, which the importer requires.
   *No admin access?* Use Filters → Search work items → ••• → Import work items from CSV. That route cannot create parent-child links, so the stories arrive unparented — create the 5 epics manually first, then drag each story onto its epic in the backlog.

3. **Story points**: if the field is missing on the create screen, open a story → *More fields* → Story Points. Values are in the backlog table.
4. **Sprint 1**: drag the six Sprint 1 stories into the sprint row, click *Start sprint*, duration **1 week**, and paste the Sprint 1 goal from the plan document.
5. **Simulate the work**: move stories To Do → In Progress → Done in priority order. Story 1.2 was left unfinished, which is why the Sprint 1 burndown stops at 5 points.
6. **Complete sprint**, then plan **Sprint 2** with its six stories and run it to completion.
7. **Burndown**: Reports → Burndown Chart, with the estimation statistic set to *Story Points*.

## Screenshot checklist (what gets graded)

- [ ] Backlog view with the epic panel open, showing all 5 epics and their stories
- [ ] Backlog showing story point values on the stories (and the epic point totals)
- [ ] Active Sprint board — Sprint 1 mid-flight, cards spread across To Do / In Progress / Done
- [ ] Burndown chart for Sprint 1 (and Sprint 2)
- [ ] Sprint 2 board or the completed-sprint summary

Save them into `screenshots/` with names like `01-backlog-epics.png`, `02-story-points.png`, `03-sprint-board.png`, `04-burndown.png`.

> The instructor also asks for a **live demo of the Jira workspace** — the documents here are the written deliverable, not a substitute for the project existing in your account.

## Reflection questions

Answered in full in `Lab2_Sprint_Plan_and_Reflection.pdf` (section 6): estimation accuracy, backlog prioritisation, plan vs simulated sprint, and what the burndown revealed about team capacity.
