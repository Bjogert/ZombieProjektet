---
name: to-tickets
description: Break an approved ZombieProjektet spec or milestone into minimal, independent, end-to-end GitHub Issues with acceptance criteria and blockers. Use for milestone planning and preparing agent-sized tasks.
---

# Tracer-bullet tickets (adapted from Matt Pocock)

1. Read the approved spec and `docs/ROADMAP.md`; check whether the requested behavior exists already.
2. Draft the **fewest small demoable vertical slices**. Each ticket should fit one focused coding-agent session and leave the project in a verifiable state.
3. For each ticket define: player/developer outcome, 2-4 acceptance checks, dependencies (issue numbers if available), and what is explicitly not part of it.
4. Don't split by technology layer ("all data first, all UI second") unless a short preparatory spike is unavoidable.
5. Surface the proposal and obtain approval before posting new GitHub Issues. Use GitHub Issues as the tracker; never require special labels that do not exist.
6. Work only tickets with resolved blockers. Do not auto-close parent issues or expand the milestone silently.

Source: mattpocock/skills to-tickets, adapted for this project.
