# Lab 1 — Requirements Engineering & UML Use-Case Modelling

**Problem Statement #36 — Restaurant Table Booking & Pre-Ordering App**
PES University, Dept. of CSE | Software Engineering Lab

Name:NIKHIL.P  SRN: PES1UG24CS583  Section: J

---

## Scenario

A restaurant hospitality app that lets diners pick a specific table from a live 2D floor plan,
place their food order in advance, and have the kitchen time its preparation so the meal is ready
on arrival. Restaurant Managers drive the same floor plan from in-house terminals, moving tables
through the Reserved → Seated → Billed lifecycle.

## Repository contents

| File | Deliverable |
|---|---|
| `Lab1_Requirements_Table.docx` / `.pdf` | 5 Functional + 2 Non-functional requirements with ID, Type, Description, Priority, Acceptance Criteria, Rationale, Comments — plus actor/use-case list and traceability matrix |
| `Lab1_UseCase_Diagram.pdf` | UML use-case diagram: 4 actors, 8 use cases, 3 «include» and 2 «extend» relationships, system boundary |
| `Lab1_UseCase_Diagram.drawio` | Editable draw.io source for the diagram (File → Open From → Device at app.diagrams.net) |
| `Lab1_UseCase_Flow.docx` / `.pdf` | One-page use-case flow for UC-01 *Book Table with Pre-Order*: preconditions, postconditions, main success scenario, two alternate flows |

## Actors

| Actor | Type | Role |
|---|---|---|
| Diner | Primary | Books a table, pre-orders, pays, cancels |
| Restaurant Manager | Primary | Manages table lifecycle status on the floor terminal, releases no-shows |
| Payment Gateway | Secondary (external) | Authorises payment, returns a token |
| Kitchen Display System (KDS) | Secondary (external) | Receives timed preparation tickets |

## Requirements → Use-case traceability

| Req | Use case(s) |
|---|---|
| FR-001 Select table on live floor plan + link pre-order | UC-01, UC-02 |
| FR-002 Build pre-order cart linked to reservation | UC-03 |
| FR-003 Compute kitchen prep timeline, dispatch to KDS | UC-04 |
| FR-004 Pay via gateway + digital confirmation | UC-05, UC-06 |
| FR-005 Table lifecycle status, cancellation & no-show release | UC-07, UC-08 |
| NFR-001 Status sync < 500 ms across terminals | UC-07 |
| NFR-002 No raw card data stored; TLS 1.2+ | UC-05 |

## Relationships used

- **«include»** — UC-01 → UC-02, UC-01 → UC-05, UC-03 → UC-04 (always executed as part of the base use case)
- **«extend»** — UC-03 → UC-01, UC-06 → UC-05 (conditional/optional behaviour; arrow points to the base use case)
