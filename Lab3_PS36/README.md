# Lab 3 — Component Modelling & Architectural Pattern Selection

**Problem Statement #36 — Restaurant Table Booking & Pre-Ordering App**
Architectural style selected: **Microservices**

## Contents

| File | What it is |
|---|---|
| `Lab3_Component_Diagram.pdf` / `.png` | UML component diagram — 6 platform services, 2 client apps, 2 external systems, 2 data stores, 8 named interfaces in ball-and-socket notation |
| `Lab3_Architecture_Justification.docx` / `.pdf` | One-page justification: style analysis, two scenario-specific reasons, security advantage, performance benefit |
| `Lab3_Component_Diagram.drawio` | Editable diagram source for draw.io |

## Components

| Component | Source | Responsibility |
|---|---|---|
| Order Manager Component | Given in handout | Orchestrates booking, pre-order and payment; owns the reservation lifecycle |
| Payment Service Component | Given in handout | Talks to the external gateway, stores only tokens, never card data |
| Table Availability Service | Identified | Holds live table state, pushes status changes to every terminal |
| Kitchen Prep Scheduler | Identified | Computes cook-start times, dispatches tickets to the KDS |
| Menu & Catalog Service | Identified | Serves menu, prices and per-item preparation durations |
| API Gateway | Identified | Single entry point for diner app and manager terminal; auth and routing |

Clients: Diner Mobile App, Manager Floor Terminal. External systems: Payment Gateway, Kitchen Display System.
Data stores: Reservation DB (PostgreSQL), Floor State Cache (Redis pub/sub).

## Interfaces

| Interface | Provider → Consumer | Protocol |
|---|---|---|
| IBookingAPI | API Gateway → Diner Mobile App | REST/JSON over TLS 1.2+ |
| IFloorOpsAPI | API Gateway → Manager Floor Terminal | REST + WebSocket |
| IReservation | Order Manager → API Gateway | gRPC |
| IMenuCatalog | Menu & Catalog Service → Order Manager | gRPC |
| IPrepSchedule | Kitchen Prep Scheduler → Order Manager | gRPC |
| **IPayment** | Payment Service → Order Manager | payment processing requests *(given)* |
| ITableAvailability | Table Availability Service → Order Manager | gRPC |
| IFloorStatusStream | Table Availability Service → API Gateway | WebSocket push, < 500 ms |

`«use»` dependencies: Payment Service → Payment Gateway (HTTPS, tokenised), Kitchen Prep Scheduler →
Kitchen Display System, Order Manager → Reservation DB, Table Availability Service → Floor State Cache.

## Why microservices

Two scenario-specific reasons, one security advantage and one performance benefit are argued in full in
the justification document. In short: peak load concentrates on table availability rather than spreading
evenly, so independent scaling matters; failures in the external gateway must not take bookings and the
kitchen feed down with them; isolating the payment service shrinks PCI DSS audit scope to one deployable;
and keeping live table state in a replicated in-memory service is what makes the 500 ms sync target in
NFR-001 reachable.

## Traceability to earlier labs

- FR-001 (table selection on the live floor plan) → Table Availability Service, Order Manager
- FR-002 (pre-order cart) → Menu & Catalog Service, Order Manager
- FR-003 (kitchen prep timeline) → Kitchen Prep Scheduler → Kitchen Display System
- FR-004 (payment and confirmation) → Payment Service Component → Payment Gateway
- FR-005 (table lifecycle, cancellation, no-show release) → Table Availability Service
- NFR-001 (status sync < 500 ms) → IFloorStatusStream, Floor State Cache
- NFR-002 (no raw card data, TLS 1.2+) → Payment Service isolation, tokenised gateway calls
