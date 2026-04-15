# ACICP Redesign Specification

## Requested Changes

The curriculum will be revised to reflect the user's requested simplification of the programme. The following courses will be removed from the published ACICP structure:

1. **ACICP 102 – Linux Essentials**
2. **ACICP 501 – Threat Hunting & Analytics (NDG CySA+)**
3. **ACICP 502 – Advanced Network Detection (Zeek IDS)**
4. **ACICP 602 – Cloud Security Automation**
5. **ACICP 603 – Virtual Infrastructure (Proxmox)**

## Revised Programme Length

The programme will be repositioned from **36 weeks (9 months)** to **24 weeks (6 months)**.

## Revised Course Count

The visible curriculum will move from **20 published course sections** to **15 published course sections**.

## Revised Phase Structure

Because the repository does **not** contain a published **ACICP 503** course section, removing **ACICP 501** and **ACICP 502** effectively removes the standalone Defensive Security phase from the public curriculum. The revised programme will therefore use **7 phases** over **24 weeks**.

| Phase | Focus Area | Duration | Courses |
|---|---|---:|---|
| 1 | Core Systems & Security | 4 weeks | ACICP 101, 103, 104 |
| 2 | Network & Security Operations | 3 weeks | ACICP 201, 202 |
| 3 | Critical Infrastructure (ICS) | 4 weeks | ACICP 301, 302, 303 |
| 4 | Offensive Cyber Operations & Firewall Engineering | 4 weeks | ACICP 401, 402, 403 |
| 5 | Cloud Security | 2 weeks | ACICP 601 |
| 6 | Virtual Infrastructure | 3 weeks | ACICP 604 |
| 7 | Digital Forensics & Final Simulation | 4 weeks | ACICP 701, 702 |

**Total Duration:** 24 weeks

## Document Update Rules

The following consistency changes must be made across repository documents:

- Replace all references to **36 weeks / 9 months** with **24 weeks / 6 months**.
- Update course totals in summaries so they align with the revised public curriculum, which now contains **15 published course sections**.
- Remove references to the deleted courses from the programme structure, FAQ, handbook, and partnership mapping.
- Remove the standalone Defensive Security phase references that depended on ACICP 501-502, and reframe the remaining curriculum as a 7-phase, 6-month programme.
- Adjust all later phase summaries so Cloud Security contains only ACICP 601 and Virtual Infrastructure contains only ACICP 604.
- Remove direct references to Linux Essentials, Zeek IDS, NDG CySA+, Cloud Security Automation, and Proxmox from summary tables unless still mentioned historically in a way that is clearly no longer curricular.
- Keep the remaining course lab tables unchanged unless a deleted course section is being removed.

## Interpretation Note

The user referred to removing "the linux course" in the singular. This implementation interprets that as **ACICP 102 – Linux Essentials** only, while retaining **ACICP 103** and **ACICP 104** as advanced systems-engineering courses already embedded in the programme.

A repository review also showed that **ACICP 503** is referenced in summaries but has no published course section. For consistency, the redesign removes the Defensive Security phase from the public curriculum after deleting ACICP 501 and ACICP 502.
