# Lab 2 — Agile Backlog Creation & Sprint Simulation in Jira

**Problem Statement #36 — Restaurant Table Booking & Pre-Ordering App**
Continuation of Lab 1. Scoped as instructed to a single epic with six user stories, prioritised,
estimated with Fibonacci story points, and run through two simulated one-week sprints.

## Contents

| File | What it is |
|---|---|
| `Lab2_Backlog_Epics_Stories.docx` / `.pdf` | One Epic and six User Stories in "As a / I want / So that" form, with priority, story points and Lab 1 traceability |
| `Lab2_Sprint_Plan_and_Reflection.docx` / `.pdf` | Sprint 1 and Sprint 2 contents and goals, velocity table, Planning Poker record, burndown analysis, answers to the four reflection questions |
| `Lab2_Burndown_Charts.pdf` / `.png` | Guideline vs remaining values for both sprints |
| `Lab2_Jira_Import.csv` | Bulk-import file creating the epic and six stories with points, priorities and parent links |
| `screenshots/` | Jira evidence |

## Epic

**Epic 1 — Table Discovery & Reservation** (34 story points, 6 stories)
Traces to FR-001 and FR-005; covers UC-01 Book Table, UC-02 Validate Table Availability and
UC-08 Cancel / Release Reservation.

| Story | Priority | SP | Sprint |
|---|---|---|---|
| 1.1 View live floor plan | Highest | 8 | Sprint 1 |
| 1.2 Filter tables by slot and party size | High | 5 | Sprint 1 |
| 1.3 Select and hold a table | Highest | 5 | Sprint 1 |
| 1.4 Reject overlapping reservations | Highest | 8 | Sprint 2 |
| 1.5 Cancel a reservation | Medium | 3 | Sprint 2 |
| 1.6 Auto-release a no-show table | Medium | 5 | Backlog |

## Sprint outcome

| Sprint | Duration | Committed | Completed |
|---|---|---|---|
| Sprint 1 | 1 week | 18 | 13 (Story 1.2 not completed) |
| Sprint 2 | 1 week | 11 | 11 |

Working velocity is approximately 12 points per week; 10 points remain (Stories 1.2 and 1.6).

The Sprint 1 burndown spikes to 29 points because stories were moved in and out after the sprint had
already started, and finishes at zero because Jira removes the incomplete story from the sprint when
the sprint is completed. Both effects are explained in the reflection document.

## Running it in Jira

1. Create a **Company-managed Scrum** project named `Restaurant Table Booking` with key **RTB**.
2. With only seven items, creating the epic and six stories by hand is quick. To bulk-import instead:
   Settings ⚙ → System → External system import → CSV → upload `Lab2_Jira_Import.csv`, mapping
   `Issue Id` → Issue Id, `Issue Type` → Issue Type, `Summary` → Summary, `Description` → Description,
   `Priority` → Priority, `Story Points` → Story Points, `Parent` → Parent, `Labels` → Labels.
   Leave `Sprint` unmapped. Mapping `Issue Id` is mandatory, or the epic-to-story links are not created.
3. **Sprint 1**: drag stories 1.1, 1.2 and 1.3 into the sprint (18 points), start it with a 1-week
   duration, move 1.1 and 1.3 to Done and leave **Story 1.2 In Progress**. Complete the sprint and send
   the incomplete story to the backlog.
4. **Sprint 2**: create a sprint with stories 1.4 and 1.5 (11 points), start it, move both to Done, and
   complete the sprint. Stories 1.2 and 1.6 stay in the backlog.
5. **Burndown**: Reports → Burndown Chart, estimation statistic set to Story Points, for each sprint.

## Screenshots

- `01-backlog-epic.png` — backlog with the epic panel open, the epic and its stories visible
- `02-story-points.png` — story point badges and the epic point total in frame
- `03-sprint-board.png` — active sprint board with cards across To Do, In Progress and Done
- `04-burndown-sprint1.png` — burndown for Sprint 1
- `05-burndown-sprint2.png` — burndown for Sprint 2
