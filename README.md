# Software Engineering Lab — PES University, Dept. of CSE

Coursework repository for the Software Engineering lab series.
**Assigned problem statement: #36 — Restaurant Table Booking & Pre-Ordering App** (Retail, E-Commerce & Finance track).

| | |
|---|---|
| **Name** | Nikhil P |
| **SRN** | PES1UG24CS583 |
| **Section / Batch** | _______________________ |
| **Semester** | _______________________ |
| **Faculty** | _______________________ |

---

## 1. The system being modelled

A restaurant hospitality app that lets diners reserve a **specific table** from a live 2D floor plan,
place their food order **in advance**, and have the kitchen time preparation so that the meal is ready
the moment they are seated. Restaurant Managers work the same floor plan from in-house terminals,
moving tables through the **Available → Reserved → Seated → Billed** lifecycle.

Every lab in this repository builds on this same system, so the requirements baseline in Lab 1 is the
reference for all later design, testing and documentation artefacts.

### Actors

| Actor | Type | Responsibility |
|---|---|---|
| Diner | Primary | Books a table, pre-orders food, pays, cancels |
| Restaurant Manager | Primary | Drives table status on the floor terminal, releases no-shows |
| Payment Gateway | Secondary (external) | Authorises payment, returns a token |
| Kitchen Display System (KDS) | Secondary (external) | Receives timed preparation tickets |

---

## 2. Repository structure

```
.
├── README.md                  ← you are here (repo overview)
├── Lab1_PS36/                     ← Requirements Engineering & UML Use-Case Modelling
│   ├── Lab1_Requirements_Table.docx / .pdf
│   ├── Lab1_UseCase_Diagram.pdf
│   ├── Lab1_UseCase_Diagram.drawio
│   ├── Lab1_UseCase_Flow.docx / .pdf
│   └── README.md              ← lab-specific notes
├── Lab2_PS36/                     ← Agile Backlog Creation & Sprint Simulation in Jira
│   ├── Lab2_Backlog_Epics_Stories.docx / .pdf
│   ├── Lab2_Sprint_Plan_and_Reflection.docx / .pdf
│   ├── Lab2_Burndown_Charts.pdf / .png
│   ├── Lab2_Jira_Import.csv
│   ├── screenshots/           ← Jira screenshots
│   └── README.md
├── Lab3_PS36/                 ← (to be added)
└── ...
```

Convention followed for every lab: one folder per lab, editable source (`.docx`, `.drawio`) committed
**alongside** the exported `.pdf`, and a short per-lab `README.md` describing what was submitted.

---

## 3. Lab 1 — Requirements Engineering & UML Use-Case Modelling

**Objective:** elicit functions and constraints from the scenario, write verifiable functional (FR) and
non-functional (NFR) requirements, and translate them into a UML use-case diagram and one use-case flow.

### Deliverables

| File | What it contains |
|---|---|
| `Lab1_Requirements_Table.docx` / `.pdf` | 5 FRs + 2 NFRs with Req ID, Type, Description, Priority, measurable Acceptance Criteria, Rationale and peer-critique Comments; plus the actor/use-case list and traceability matrix |
| `Lab1_UseCase_Diagram.pdf` | Use-case diagram — 4 actors, 8 use cases, system boundary, 3 «include» and 2 «extend» relationships, legend |
| `Lab1_UseCase_Diagram.drawio` | Editable diagram source (open at app.diagrams.net → File → Open From → Device) |
| `Lab1_UseCase_Flow.docx` / `.pdf` | One-page flow for UC-01 *Book Table with Pre-Order* — preconditions, postconditions, 13-step main success scenario, two alternate flows |

### Requirements baseline

| ID | Type | Priority | Summary |
|---|---|---|---|
| FR-001 | Functional | High | Select an available table from the interactive 2D floor plan and link the pre-order to that reservation |
| FR-002 | Functional | High | Browse the live menu and build a pre-order cart (quantity + customisation) attached to the reservation |
| FR-003 | Functional | High | Compute each item's cook-start time from prep duration and arrival time; release the ticket to the KDS |
| FR-004 | Functional | High | Pay the pre-order/deposit through the gateway; issue a digital confirmation with QR check-in code |
| FR-005 | Functional | Medium | Manage the table lifecycle on the floor terminal; auto-release a table 15 min after a no-show |
| NFR-001 | Non-functional (Performance) | High | Table status changes propagate to all terminals and to the diner floor plan in under 500 ms |
| NFR-002 | Non-functional (Security) | High | No raw cardholder data persisted — gateway tokens only; TLS 1.2+ end to end |

### Use cases and relationships

| UC | Use case | Actor(s) | Traces to |
|---|---|---|---|
| UC-01 | Book Table | Diner | FR-001 |
| UC-02 | Validate Table Availability | — (included) | FR-001 |
| UC-03 | Pre-Order Menu Items | Diner | FR-002 |
| UC-04 | Generate Kitchen Prep Timeline | KDS | FR-003 |
| UC-05 | Make Payment | Payment Gateway | FR-004 |
| UC-06 | Apply Promo Code | — (extension) | FR-004 |
| UC-07 | Manage Table Status | Restaurant Manager | FR-005, NFR-001 |
| UC-08 | Cancel / Release Reservation | Diner, Restaurant Manager | FR-005 |

- **«include»** (always executed): UC-01 → UC-02, UC-01 → UC-05, UC-03 → UC-04
- **«extend»** (conditional): UC-03 → UC-01, UC-06 → UC-05 — the arrow points at the **base** use case

Every requirement traces to at least one use case, and no use case exists without a source requirement.

### Submission checklist

- [x] Exactly 5 FRs (FR-001 … FR-005) and 2 NFRs (NFR-001, NFR-002)
- [x] Each row carries ID, Type, Description ("The system shall…"), Priority, Acceptance Criteria, Rationale
- [x] Acceptance criteria stated as measurable pass/fail conditions
- [x] At least 3 actors and 5 use cases identified
- [x] At least one «include» **and** one «extend» relationship in the diagram
- [x] Use-case flow with preconditions, postconditions, main success scenario and one alternate flow
- [x] Diagram and flow exported as PDF
- [ ] Name / SRN filled in on every document
- [ ] Pushed to the Lab-1 repository

---

## 4. Lab 2 — Agile Backlog Creation & Sprint Simulation in Jira

**Objective:** turn the Lab 1 functional requirements into Agile backlog items, estimate them, run two
simulated sprints and analyse progress with a burndown chart.

### Deliverables

| File | What it contains |
|---|---|
| `Lab2_Backlog_Epics_Stories.docx` / `.pdf` | 5 Epics and 20 User Stories ("As a / I want / So that") with priority, Fibonacci story points and traceability back to FR/NFR and use cases |
| `Lab2_Sprint_Plan_and_Reflection.docx` / `.pdf` | Sprint 1 & 2 goals and contents, velocity table, Planning Poker record, burndown analysis, four reflection answers |
| `Lab2_Burndown_Charts.pdf` / `.png` | Guideline vs remaining-values burndown for both sprints |
| `Lab2_Jira_Import.csv` | Bulk-import file that creates the whole backlog in Jira |
| `screenshots/` | Jira evidence: backlog with epics, story points, active sprint board, burndown |

### Epics and how they map back to Lab 1

| Epic | Theme | Traces to | Stories | Points |
|---|---|---|---|---|
| Epic 1 | Table Discovery & Reservation | FR-001 | 4 | 26 |
| Epic 2 | Pre-Ordering & Menu Experience | FR-002 | 4 | 16 |
| Epic 3 | Kitchen Preparation Orchestration | FR-003 | 4 | 18 |
| Epic 4 | Payments & Confirmation | FR-004, NFR-002 | 4 | 18 |
| Epic 5 | Floor Operations & Reservation Lifecycle | FR-005, NFR-001 | 4 | 21 |

Backlog total **99 story points** across 20 stories, estimated on the Fibonacci scale (1, 2, 3, 5, 8).

### Sprint outcome

| Sprint | Goal | Committed | Completed |
|---|---|---|---|
| Sprint 1 (1 week) | Diner can find, hold and browse — double booking made impossible | 34 | 29 (Story 1.2 carried over) |
| Sprint 2 (2 weeks) | Diner can complete a paid pre-order; system knows when cooking must start | 32 | 32 |

Working velocity ≈ **30 points per sprint**; 38 points remain, i.e. roughly one and a half more sprints.

### Submission checklist

- [x] Epics created from Lab 1 functional requirements
- [x] User Stories in "As a / I want / So that" format under their epics
- [x] Backlog prioritised (Highest / High / Medium / Low)
- [x] Story points assigned on the Fibonacci scale, with a Planning Poker record
- [x] Two sprints planned and simulated To Do → In Progress → Done
- [x] Burndown chart produced and analysed
- [x] Reflection questions answered
- [ ] Jira screenshots captured into `Lab2_PS36/screenshots/`
- [ ] Jira workspace demonstrated to the instructor

---

## 5. Tools used

| Purpose | Tool |
|---|---|
| UML use-case diagram | draw.io (diagrams.net) |
| Agile backlog, sprints, burndown | Jira (Company-managed Scrum) |
| Requirements table & flow document | Microsoft Word / LibreOffice Writer |
| Export & submission | PDF export, Git + GitHub |

---

## 6. Working with this repository

```bash
git clone <your-repo-url>
cd <repo>

# after adding or updating a lab
git add Lab2_PS36
git commit -m "Lab 2: agile backlog, two sprints and burndown analysis"
git push origin main
```

Commit the editable sources together with the PDFs — the `.drawio` file is what lets the diagram be
revised in later labs instead of redrawn.

---

## 7. Roadmap

| Lab | Topic | Status |
|---|---|---|
| Lab 1 | Requirements Engineering & UML Use-Case Modelling | ✅ Complete |
| Lab 2 | Agile Backlog Creation & Sprint Simulation in Jira | ✅ Complete |
| Lab 3 | — | ⬜ Pending |
