# Software Engineering Lab — PES University, Dept. of CSE

Coursework repository for the Software Engineering lab series.
**Assigned problem statement: #36 — Restaurant Table Booking & Pre-Ordering App** (Retail, E-Commerce & Finance track).

| | |
|---|---|
| **Name** |NIKHIL.P |
| **SRN** |PES1UG24CS583 |
| **Section / Batch** |J |
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
├── Lab-1/                     ← Requirements Engineering & UML Use-Case Modelling
│   ├── Lab1_Requirements_Table.docx / .pdf
│   ├── Lab1_UseCase_Diagram.pdf
│   ├── Lab1_UseCase_Diagram.drawio
│   ├── Lab1_UseCase_Flow.docx / .pdf
│   └── README.md              ← lab-specific notes
├── Lab-2/                     ← (to be added)
├── Lab-3/                     ← (to be added)
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

## 4. Tools used

| Purpose | Tool |
|---|---|
| UML use-case diagram | draw.io (diagrams.net) |
| Requirements table & flow document | Microsoft Word / LibreOffice Writer |
| Export & submission | PDF export, Git + GitHub |

---

## 5. Working with this repository

```bash
git clone <your-repo-url>
cd <repo>

# after adding or updating a lab
git add Lab-1
git commit -m "Lab 1: requirements table, use-case diagram and UC-01 flow"
git push origin main
```

Commit the editable sources together with the PDFs — the `.drawio` file is what lets the diagram be
revised in later labs instead of redrawn.

---

## 6. Roadmap

| Lab | Topic | Status |
|---|---|---|
| Lab 1 | Requirements Engineering & UML Use-Case Modelling | ✅ Complete |
| Lab 2 | — | ⬜ Pending |
| Lab 3 | — | ⬜ Pending |
