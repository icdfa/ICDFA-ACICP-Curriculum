from pathlib import Path
import re

ROOT = Path('/home/ubuntu/work/acicp_review/repo')


def read(name: str) -> str:
    return (ROOT / name).read_text()


def write(name: str, text: str) -> None:
    (ROOT / name).write_text(text)


def must_replace(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise ValueError(f'Missing expected text for {label}')
    return text.replace(old, new, 1)


def regex_replace(text: str, pattern: str, repl: str, label: str, flags=re.S) -> str:
    new_text, count = re.subn(pattern, repl, text, count=1, flags=flags)
    if count != 1:
        raise ValueError(f'Pattern not matched exactly once for {label}; matched {count}')
    return new_text


# README.md
readme = read('README.md')
new_toc = """## Table of Contents

- [Programme Overview](#programme-overview)
- [Programme Details](#programme-details)
- [Admission Requirements](#admission-requirements)
- [Programme Structure](#programme-structure)
  - [Phase 1: Core Systems & Security](#phase-1-core-systems--security)
  - [Phase 2: Network & Security Operations](#phase-2-network--security-operations)
  - [Phase 3: Critical Infrastructure (ICS)](#phase-3-critical-infrastructure-ics)
  - [Phase 4: Offensive Cyber Operations & Firewall Engineering](#phase-4-offensive-cyber-operations--firewall-engineering)
  - [Phase 5: Cloud Security](#phase-5-cloud-security)
  - [Phase 6: Virtual Infrastructure](#phase-6-virtual-infrastructure)
  - [Phase 7: Digital Forensics & Final Simulation](#phase-7-digital-forensics--final-simulation)
- [Assessment Structure](#assessment-structure)
- [Mandatory ICDFA Requirements](#mandatory-icdfa-requirements)
- [Certification](#certification)
- [Programme Fees](#programme-fees)
- [Career Pathways](#career-pathways)
- [Institutional Partners](#institutional-partners)
- [Why This Programme](#why-this-programme)
- [Final Note](#final-note)
"""
readme = regex_replace(readme, r"## Table of Contents\n.*?\n---\n", new_toc + "\n---\n", 'README TOC')
readme = must_replace(readme, "| **Duration**    | 36 Weeks (9 Months)                            |", "| **Duration**    | 24 Weeks (6 Months)                            |", 'README duration row')
readme = must_replace(readme, "The programme is divided into **8 Phases**, each delivered over **2 weeks**, with progressive difficulty and real-world simulation. ", "The programme is divided into **7 Phases** delivered across **24 weeks (6 months)**, with a compressed advanced sequence focused on critical infrastructure security, offensive operations, cloud defence, virtual infrastructure, and digital forensics. ", 'README structure sentence')
readme = regex_replace(readme, r"\n#### ACICP 102 – Linux Essentials\n.*?\n---\n", "\n", 'remove ACICP 102')
readme = regex_replace(readme, r"\n### Phase 5: Defensive Security\n.*?(?=\n### Phase 6: Cloud Security\n)", "\n", 'remove defensive security phase')
readme = must_replace(readme, "### Phase 6: Cloud Security", "### Phase 5: Cloud Security", 'rename phase 6 to phase 5')
readme = regex_replace(readme, r"\n#### ACICP 602 – Cloud Security Automation\n.*?\n---\n", "\n", 'remove ACICP 602')
readme = must_replace(readme, "### Phase 7: Virtual Infrastructure", "### Phase 6: Virtual Infrastructure", 'rename phase 7 to phase 6')
readme = regex_replace(readme, r"\n#### ACICP 603 – Virtual Infrastructure \(Proxmox\)\n.*?\n---\n", "\n", 'remove ACICP 603')
readme = must_replace(readme, "### Phase 8: Digital Forensics & Final Simulation", "### Phase 7: Digital Forensics & Final Simulation", 'rename phase 8 to phase 7')
readme = must_replace(readme, "- **Integration**: ACICP 601-602 (Cloud Security modules)", "- **Integration**: ACICP 601 (Cloud Security module)", 'azure integration')
readme = must_replace(readme, "- **Integration**: ACICP 601-602 (Cloud Security modules)", "- **Integration**: ACICP 601 (Cloud Security module)", 'aws integration')
readme = must_replace(readme, "- **Integration**: ACICP 301-303 (ICS/SCADA Security modules), ACICP 603-604 (Virtual Infrastructure)", "- **Integration**: ACICP 301-303 (ICS/SCADA Security modules), ACICP 604 (Advanced Virtual Infrastructure)", 'ndg integration')
readme = regex_replace(readme, r"### Partner Integration in Curriculum\n\n\| Phase \| Partner \| Focus Area \|\n\|-------\|---------\|------------\|\n.*?(?=\n---\n\n## Why This Programme)", """### Partner Integration in Curriculum\n\n| Phase | Partner | Focus Area |
|-------|---------|------------|
| Phase 1-2 | Cisco Academy | Networking fundamentals and security operations |
| Phase 3 | NDG NETLAB+ | ICS/SCADA systems |
| Phase 4 | NDG NETLAB+ | Offensive operations and firewall engineering |
| Phase 5 | Microsoft Azure, AWS | Cloud security |
| Phase 6 | NDG NETLAB+ | Advanced virtual infrastructure |
| Phase 7 | All Partners | Capstone simulation and forensics |
""", 'README partner table')
write('README.md', readme)

# FAQ.md
faq = read('FAQ.md')
faq = must_replace(faq, "All cohorts run for exactly 36 weeks (9 months) with scheduled breaks for holidays.", "All cohorts run for exactly 24 weeks (6 months) in a compressed intensive delivery format.", 'FAQ duration sentence')
faq = regex_replace(faq, r"### Q13: What courses are included in the ACICP\?\n\n\*\*A:\*\*.*?\n---\n", """### Q13: What courses are included in the ACICP?

**A:** The ACICP now presents **15 published course sections** across **7 phases**:

**Phase 1:** ACICP 101, 103-104 (Cybersecurity Foundation, Linux Systems Engineering I-II)

**Phase 2:** ACICP 201-202 (Network Security Engineering, Security Operations & Threat Monitoring)

**Phase 3:** ACICP 301-303 (ICS & SCADA Systems, ICS Network Security & Attacks, Industrial Exploitation & Pivoting)

**Phase 4:** ACICP 401-403 (Ethical Hacking Series 1, Ethical Hacking Series 2, PAN11 Firewall Essentials)

**Phase 5:** ACICP 601 (Cloud Security Fundamentals)

**Phase 6:** ACICP 604 (Advanced Virtual Infrastructure)

**Phase 7:** ACICP 701-702 (Digital Forensics, Final Capstone & 24-Hour Cyber Range)

---
""", 'FAQ Q13 block')
faq = must_replace(faq, "**A:** The ACICP includes **100+ hands-on labs** distributed across all 18 courses. Each course includes 4–21 practical lab exercises covering real-world scenarios and infrastructure.", "**A:** The revised ACICP includes **162 hands-on labs** distributed across **15 published course sections**. Each course includes focused practical lab exercises covering real-world infrastructure and cybersecurity scenarios.", 'FAQ Q14 answer')
faq = must_replace(faq, "- Phase 5: Defensive Security (3 weeks)", "- Phase 5: Cloud Security (2 weeks)", 'FAQ phase 5 bullet')
faq = must_replace(faq, "- Phase 6: Cloud Security (2 weeks)", "- Phase 6: Virtual Infrastructure (3 weeks)", 'FAQ phase 6 bullet')
faq = must_replace(faq, "- Phase 7: Virtual Infrastructure (4 weeks)", "- Phase 7: Digital Forensics & Final Simulation (4 weeks)", 'FAQ phase 7 bullet')
faq = must_replace(faq, "- 36 weeks of instructor-led training (8 hours/day, 5 days/week)", "- 24 weeks of instructor-led training (8 hours/day, 5 days/week)", 'FAQ time commitment')
write('FAQ.md', faq)

# STUDENT_HANDBOOK.md
handbook = read('STUDENT_HANDBOOK.md')
handbook = must_replace(handbook, "The ACICP is a **36-week (9-month) intensive training programme** divided into **8 Phases** covering **18 specialized courses** and **100+ hands-on labs**.", "The ACICP is a **24-week (6-month) intensive training programme** divided into **7 Phases** covering **15 published course sections** and **162 hands-on labs**.", 'handbook structure sentence')
handbook = regex_replace(handbook, r"\| Phase \| Focus Area \| Duration \| Courses \|\n\|:------\|:-----------\|:---------\|:--------\|\n.*?(?=\n### Training Delivery)", """| Phase | Focus Area | Duration | Courses |
|:------|:-----------|:---------|:--------|
| 1 | Core Systems & Security | 4 weeks | ACICP 101, 103-104 |
| 2 | Network & Security Operations | 3 weeks | ACICP 201-202 |
| 3 | Critical Infrastructure (ICS) | 4 weeks | ACICP 301-303 |
| 4 | Offensive Cyber Operations | 4 weeks | ACICP 401-403 |
| 5 | Cloud Security | 2 weeks | ACICP 601 |
| 6 | Virtual Infrastructure | 3 weeks | ACICP 604 |
| 7 | Digital Forensics & Capstone | 4 weeks | ACICP 701-702 |

""", 'handbook structure table')
write('STUDENT_HANDBOOK.md', handbook)

# INSTITUTIONAL_PARTNERSHIPS.md
partners = read('INSTITUTIONAL_PARTNERSHIPS.md')
partners = regex_replace(partners, r"Microsoft Azure is integrated into the following ACICP courses:\n\n- \*\*ACICP 601 – Cloud Security Fundamentals:\*\* Azure security architecture, identity management, and data protection\n- \*\*ACICP 602 – Cloud Security Automation:\*\* Azure DevSecOps, infrastructure as code \(IaC\), and automated security controls\n- \*\*ACICP 603 – Virtual Infrastructure:\*\* Azure virtual machines, networking, and storage management", "Microsoft Azure is integrated into the following ACICP course:\n\n- **ACICP 601 – Cloud Security Fundamentals:** Azure security architecture, identity management, and data protection", 'partners microsoft integration')
partners = must_replace(partners, "4. **Training:** Instructors will guide you through Azure labs during ACICP 601–602", "4. **Training:** Instructors will guide you through Azure labs during ACICP 601", 'partners microsoft training')
partners = regex_replace(partners, r"AWS is integrated into the following ACICP courses:\n\n- \*\*ACICP 601 – Cloud Security Fundamentals:\*\* AWS security services, identity and access management \(IAM\), and encryption\n- \*\*ACICP 602 – Cloud Security Automation:\*\* AWS CloudFormation, Infrastructure as Code \(IaC\), and automated security responses\n- \*\*ACICP 603 – Virtual Infrastructure:\*\* AWS EC2, VPC, and storage services", "AWS is integrated into the following ACICP course:\n\n- **ACICP 601 – Cloud Security Fundamentals:** AWS security services, identity and access management (IAM), and encryption", 'partners aws integration')
partners = must_replace(partners, "4. **Training:** Instructors will guide you through AWS labs during ACICP 601–602", "4. **Training:** Instructors will guide you through AWS labs during ACICP 601", 'partners aws training')
partners = partners.replace("ACICP 601–602", "ACICP 601")
partners = re.sub(r"^.*ACICP 603.*\n?", "", partners, flags=re.M)
write('INSTITUTIONAL_PARTNERSHIPS.md', partners)

print('Updated README.md, FAQ.md, STUDENT_HANDBOOK.md, and INSTITUTIONAL_PARTNERSHIPS.md')
