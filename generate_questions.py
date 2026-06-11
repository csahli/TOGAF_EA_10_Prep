#!/usr/bin/env python3
"""
Generates two question banks for the TOGAF EA Practitioner mock-exam SPA:
  - data/questions_level1.json  (128 Foundation / Level 1 single-best-answer questions)
  - data/questions_level2.json  (128 Practitioner / Level 2 gradient-scored scenarios)

All questions are ORIGINAL works written for study purposes, informed by the
documented format/difficulty of the TOGAF Standard 10th Edition exams. They
contain NO reproduced exam content from The Open Group or any third party.

Run:  python generate_questions.py
"""

import json
import os
import random

random.seed(42)
OUT_DIR = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(OUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# LEVEL 1 (Foundation) — single best answer. Each item: question, 4 options,
# answer index, explanation, topic.
# We define a pool of concept-based templates across TOGAF topics and expand
# them into 128 unique, knowledge-recall questions.
# ---------------------------------------------------------------------------

# (concept, correct, distractor1, distractor2, distractor3, explanation, topic)
L1_FACTS = [
    ("Which ADM phase establishes the Architecture Vision and the Statement of Architecture Work?",
     "Phase A: Architecture Vision",
     "Preliminary Phase", "Phase B: Business Architecture", "Phase E: Opportunities & Solutions",
     "Phase A defines scope, stakeholders, the Architecture Vision and the Statement of Architecture Work.",
     "ADM Phases"),
    ("Which ADM phase is concerned with the Business Architecture?",
     "Phase B", "Phase A", "Phase C", "Phase D",
     "Phase B develops the Business Architecture (capabilities, value streams, processes, organization).",
     "ADM Phases"),
    ("Phase C of the ADM addresses which architecture domains?",
     "Data and Application (Information Systems) Architectures",
     "Business and Technology", "Technology only", "Migration and Implementation",
     "Phase C covers Information Systems Architectures: Data and Application.",
     "ADM Phases"),
    ("Which ADM phase develops the Technology Architecture?",
     "Phase D", "Phase C", "Phase E", "Phase F",
     "Phase D develops the Technology Architecture supporting the other domains.",
     "ADM Phases"),
    ("Which ADM phase identifies major work packages and Transition Architectures?",
     "Phase E: Opportunities & Solutions",
     "Phase D: Technology Architecture", "Phase F: Migration Planning", "Phase G: Implementation Governance",
     "Phase E consolidates gaps into work packages and defines Transition Architectures.",
     "ADM Phases"),
    ("Which ADM phase produces the detailed Implementation and Migration Plan?",
     "Phase F: Migration Planning", "Phase E: Opportunities & Solutions",
     "Phase G: Implementation Governance", "Phase H: Architecture Change Management",
     "Phase F finalizes the Implementation and Migration Plan with timing and cost.",
     "ADM Phases"),
    ("Which ADM phase provides architectural oversight of implementation?",
     "Phase G: Implementation Governance", "Phase F: Migration Planning",
     "Phase H: Architecture Change Management", "Phase A: Architecture Vision",
     "Phase G governs implementation, ensuring conformance to the target architecture.",
     "ADM Phases"),
    ("Which ADM phase manages changes to the architecture after deployment?",
     "Phase H: Architecture Change Management", "Phase G: Implementation Governance",
     "Phase F: Migration Planning", "Phase E: Opportunities & Solutions",
     "Phase H assesses change drivers and decides whether a new ADM cycle is needed.",
     "ADM Phases"),
    ("What process operates continuously throughout all ADM phases?",
     "Requirements Management", "Architecture Governance audit",
     "Gap analysis", "Stakeholder removal",
     "Requirements Management is the central, continuous process at the hub of the ADM.",
     "Requirements Management"),
    ("Which phase establishes the organization's architecture capability and tailors the ADM?",
     "Preliminary Phase", "Phase A", "Phase H", "Phase G",
     "The Preliminary Phase sets up the capability, principles, governance, and tailoring.",
     "Preliminary Phase"),
    ("What is an Architecture Building Block (ABB)?",
     "A component that captures architecture requirements and guides the development of SBBs",
     "A purchased software product", "A project plan", "A stakeholder concern",
     "ABBs capture architecture requirements (Business, Data, Application, Technology) and direct/guide the development of Solution Building Blocks (SBBs).",
     "Building Blocks"),

    ("What is a Solution Building Block (SBB)?",
     "An implementation that realizes one or more ABBs",
     "An abstract requirement", "A governance board", "A risk register",
     "SBBs are the concrete, often product-specific realizations of ABBs.",
     "Building Blocks"),
    ("What does the Enterprise Continuum provide?",
     "A way to classify and structure reusable architecture and solution artifacts",
     "A list of employees", "A billing system", "A single mandatory architecture",
     "The Enterprise Continuum organizes assets from generic to organization-specific.",
     "Enterprise Continuum"),
    ("What is held in the Architecture Repository?",
     "Architecture artifacts, reference models, standards, and governance records",
     "Only source code", "Only meeting minutes", "Only financial data",
     "The Architecture Repository stores the outputs and assets of the architecture practice.",
     "Architecture Repository"),
    ("What is the purpose of an Architecture Principle?",
     "To guide architecture decision-making and trade-offs",
     "To replace the ADM", "To define network IP ranges", "To list project tasks",
     "Principles (statement, rationale, implications) provide enduring decision guidance.",
     "Architecture Principles"),
    ("Which document formally authorizes the architecture project and defines scope?",
     "Statement of Architecture Work", "Architecture Contract",
     "Request for Architecture Work", "Architecture Definition Document",
     "The Statement of Architecture Work defines scope, approach, resources, and schedule.",
     "Deliverables"),
    ("Which deliverable triggers the start of an architecture engagement?",
     "Request for Architecture Work", "Architecture Contract",
     "Implementation and Migration Plan", "Architecture Vision",
     "The Request for Architecture Work is the trigger initiating the ADM cycle.",
     "Deliverables"),
    ("What does an Architecture Contract govern?",
     "The agreement between development partners and sponsors on deliverables and conformance",
     "Employee salaries", "Data center leases", "Marketing campaigns",
     "Architecture Contracts ensure implementation conforms to the architecture.",
     "Deliverables"),
    ("What is a 'view' in TOGAF terms?",
     "A representation of a system from the perspective of related concerns",
     "A database table", "A network switch", "A budget line",
     "A view addresses stakeholder concerns and is governed by a viewpoint.",
     "Views & Viewpoints"),
    ("What is a 'viewpoint'?",
     "A specification of the conventions for constructing and using a view",
     "A finished diagram", "A risk score", "A vendor contract",
     "A viewpoint defines how to build a view that addresses specific concerns.",
     "Views & Viewpoints"),
    ("What is the purpose of a Stakeholder Map?",
     "To identify stakeholders, their concerns, and engagement approach",
     "To store source code", "To schedule servers", "To define tax policy",
     "The Stakeholder Map supports targeted communication and concern management.",
     "Stakeholder Management"),
    ("What is gap analysis used for in the ADM?",
     "To identify differences between Baseline and Target Architectures",
     "To calculate payroll", "To test code", "To remove stakeholders",
     "Gap analysis reveals what must be added, removed, or changed to reach the Target.",
     "Gap Analysis"),
    ("What is a Transition Architecture?",
     "An intermediate, deliverable architecture state between Baseline and Target",
     "The final target state", "A rejected design", "A stakeholder concern",
     "Transition Architectures show incremental, value-adding states toward the Target.",
     "Transition Architectures"),
    ("What is the role of the Architecture Board?",
     "To provide governance, oversight, and decision-making for the architecture",
     "To write all source code", "To manage payroll", "To sell products",
     "The Architecture Board oversees implementation of the architecture strategy and governance.",
     "Architecture Governance"),
    ("What is a 'dispensation' in architecture governance?",
     "A time-bound, conditional approval to deviate from a standard",
     "A permanent removal of a standard", "A salary bonus", "A new ADM phase",
     "Dispensations allow controlled, temporary, justified deviations with remediation.",
     "Architecture Governance"),
    ("What is architecture partitioning used for?",
     "To divide architectures by criteria such as breadth, depth, time, and domain",
     "To delete the repository", "To encrypt data", "To hire staff",
     "Partitioning manages complexity by organizing related architectures.",
     "Architecture Partitioning"),
    ("What is the TOGAF Content Framework?",
     "A structured model of the work products the ADM produces",
     "A network topology", "A pricing model", "A staffing roster",
     "The Content Framework defines deliverables, artifacts, and building blocks.",
     "Content Framework"),
    ("What is a 'concern' in TOGAF?",
     "An interest of a stakeholder in the system",
     "A coding bug", "A budget surplus", "A server rack",
     "Concerns are stakeholder interests that views are designed to address.",
     "Stakeholder Management"),
    ("Which best describes 'capability-based planning'?",
     "Planning business change around required business capabilities",
     "Planning by server capacity only", "Planning by office location", "Planning by headcount only",
     "Capability-based planning aligns investments to capability increments and outcomes.",
     "Business Architecture"),
    ("What is a Business Capability?",
     "A particular ability a business possesses to achieve an outcome",
     "A specific software product", "A network protocol", "A single employee",
     "Capabilities describe what a business does, independent of how or who.",
     "Business Architecture"),
    ("What is a value stream?",
     "An end-to-end set of activities that delivers value to a stakeholder",
     "A funding source", "A data backup", "A server cluster",
     "Value streams model how value is produced for customers or stakeholders.",
     "Business Architecture"),
    ("What is the Architecture Definition Document (ADD)?",
     "A deliverable describing the Baseline and Target Architectures across domains",
     "A payroll report", "A network diagram only", "A vendor invoice",
     "The ADD captures architecture across business, data, application, and technology.",
     "Deliverables"),
    ("What is the Architecture Requirements Specification?",
     "A quantitative statement of requirements the architecture must meet",
     "A list of employees", "A marketing brochure", "A server log",
     "It provides measurable requirements to govern the implementation.",
     "Deliverables"),
    ("Why tailor the ADM?",
     "To fit the organization's context, sector, and delivery approach",
     "To make it longer", "To remove governance", "To avoid stakeholders",
     "TOGAF explicitly expects the ADM to be tailored to the enterprise.",
     "Tailoring"),
    ("Which phase confirms the Baseline Business Architecture?",
     "Phase B", "Phase A", "Phase D", "Phase F",
     "Phase B establishes both Baseline and Target Business Architectures.",
     "ADM Phases"),
    ("What is the main output of Phase A?",
     "Architecture Vision and approved Statement of Architecture Work",
     "Final code", "Signed Architecture Contract for build", "Decommissioned systems",
     "Phase A delivers the Vision and the approved Statement of Architecture Work.",
     "ADM Phases"),
    ("Which is a key relationship for Requirements Management?",
     "It interacts with every ADM phase to manage changing requirements",
     "It only runs in Phase A", "It only runs after go-live", "It replaces governance",
     "Requirements Management is continuous and central to the ADM.",
     "Requirements Management"),
    ("What does 'interoperability' refer to in architecture?",
     "The ability of systems to exchange and use information",
     "The speed of a CPU", "The cost of licenses", "The color of a UI",
     "Interoperability is a key non-functional architectural concern.",
     "Concepts"),
    ("What is a 'baseline' architecture?",
     "The existing (as-is) architecture state",
     "The future target state", "A rejected option", "A test environment",
     "The Baseline is the current state from which gaps to the Target are found.",
     "Concepts"),
    ("What is a 'target' architecture?",
     "The desired future (to-be) architecture state",
     "The current state", "A discarded design", "A budget figure",
     "The Target is the future state the ADM works toward.",
     "Concepts"),
    ("What governs how a view is constructed?",
     "A viewpoint", "A budget", "A server", "A stakeholder's salary",
     "A viewpoint specifies conventions for constructing and interpreting a view.",
     "Views & Viewpoints"),
    ("What is the primary benefit of reusing ABBs/SBBs?",
     "Reduced cost, risk, and time through proven, governed assets",
     "Higher license fees", "More duplication", "Less governance",
     "Reuse via the repository/continuum is a core source of EA value.",
     "Building Blocks"),
    ("Who typically sponsors an architecture engagement?",
     "A senior business or IT leader with authority and budget",
     "An intern", "A vendor sales rep", "An external auditor",
     "A sponsor provides mandate, funding, and decision authority.",
     "Stakeholder Management"),
    ("What is the purpose of the Communications Plan?",
     "To ensure stakeholders receive the right information at the right time",
     "To configure routers", "To set salaries", "To write code",
     "The Communications Plan supports stakeholder engagement throughout the ADM.",
     "Stakeholder Management"),
    ("What does 'conformance' mean in governance?",
     "The degree to which an implementation adheres to the architecture",
     "The CPU temperature", "The license cost", "The office size",
     "Compliance reviews assess conformance against the architecture and standards.",
     "Architecture Governance"),
    ("What is the main concern of Phase D?",
     "Defining the Technology Architecture (platforms and infrastructure)",
     "Defining business processes", "Writing the migration plan", "Managing change requests",
     "Phase D addresses the technology platforms that support the solution.",
     "ADM Phases"),
    ("What is the main concern of Phase F?",
     "Finalizing the Implementation and Migration Plan",
     "Defining the Vision", "Developing data models", "Running compliance reviews",
     "Phase F sequences work packages and finalizes timing and cost.",
     "ADM Phases"),
    ("What is an artifact in the Content Framework?",
     "A work product such as a catalog, matrix, or diagram",
     "A purchased server", "A salary", "A meeting room",
     "Artifacts are catalogs, matrices, and diagrams describing the architecture.",
     "Content Framework"),
    ("What is a catalog (artifact type)?",
     "A list of building blocks of a particular type",
     "A network cable", "A budget approval", "A risk owner",
     "Catalogs enumerate things like applications, data entities, or principles.",
     "Content Framework"),
    ("What is a matrix (artifact type)?",
     "A representation of relationships between building blocks",
     "A single diagram of one system", "A salary table", "A server log",
     "Matrices show relationships, e.g., application/data or capability/organization.",
     "Content Framework"),
    ("Which best describes 'risk' handling in the ADM?",
     "Risks are identified, assessed, and managed throughout the cycle",
     "Risks are ignored until go-live", "Risks are only financial", "Risks are removed by deleting stakeholders",
     "Risk management is integrated across the ADM phases.",
     "Risk Management"),
    ("What is a key reason to define Architecture Principles early?",
     "To provide consistent guidance for later decisions and trade-offs",
     "To finalize source code", "To set CPU clock speeds", "To approve invoices",
     "Principles established in the Preliminary Phase guide the whole engagement.",
     "Architecture Principles"),
]

L1_TOPICS_EXTRA = [
    ("Which ADM phase would you revisit to handle a major change that re-architects the enterprise?",
     "Begin a new ADM iteration from the Architecture Vision",
     "Stay in Phase G permanently", "Delete the repository", "Ignore it",
     "Major (re-architecting) changes trigger a new ADM cycle starting at Vision.",
     "Change Management"),
    ("What is the relationship between ABBs and SBBs?",
     "SBBs realize ABBs",
     "ABBs realize SBBs", "They are unrelated", "ABBs replace governance",
     "ABBs define requirements; SBBs are their concrete realizations.",
     "Building Blocks"),
    ("What is the purpose of a compliance review?",
     "To verify a project conforms to the target architecture and standards",
     "To calculate taxes", "To hire architects", "To buy servers",
     "Compliance reviews are a key governance mechanism in Phase G.",
     "Architecture Governance"),
    ("Which statement about the ADM is correct?",
     "It is iterative and can be tailored to the enterprise",
     "It must be run once, unchanged", "It forbids iteration", "It excludes governance",
     "The ADM is iterative and explicitly intended to be tailored.",
     "ADM Concepts"),
    ("What is the main value of Transition Architectures?",
     "They enable incremental, lower-risk delivery of value",
     "They replace the Target", "They remove governance", "They delete requirements",
     "Transition Architectures deliver value in manageable, governed increments.",
     "Transition Architectures"),
    ("What does the Preliminary Phase define regarding governance?",
     "The architecture governance framework and operating model",
     "The final migration plan", "The data model", "The go-live date",
     "Governance, principles, and capability are established in the Preliminary Phase.",
     "Preliminary Phase"),
]


# Reference map: stem -> C220 reference for every base L1 fact above.
# Sections are taken from the TOGAF Standard, 10th Edition evaluation bundle
# (C220, parts 0-5). Where a concept appears in multiple parts, the canonical
# definitional location is cited.
L1_REFS = {
    # ADM phases (C220 Part 1)
    "Which ADM phase establishes the Architecture Vision and the Statement of Architecture Work?": "C220 Part 1, ch. 3 (Phase A: Architecture Vision)",
    "Which ADM phase is concerned with the Business Architecture?": "C220 Part 1, ch. 4 (Phase B: Business Architecture)",
    "Phase C of the ADM addresses which architecture domains?": "C220 Part 1, ch. 5-6 (Phase C: Information Systems Architectures)",
    "Which ADM phase develops the Technology Architecture?": "C220 Part 1, ch. 7 (Phase D: Technology Architecture)",
    "Which ADM phase identifies major work packages and Transition Architectures?": "C220 Part 1, ch. 8 (Phase E: Opportunities & Solutions)",
    "Which ADM phase produces the detailed Implementation and Migration Plan?": "C220 Part 1, ch. 9 (Phase F: Migration Planning)",
    "Which ADM phase provides architectural oversight of implementation?": "C220 Part 1, ch. 10 (Phase G: Implementation Governance)",
    "Which ADM phase manages changes to the architecture after deployment?": "C220 Part 1, ch. 11 (Phase H: Architecture Change Management)",
    "What process operates continuously throughout all ADM phases?": "C220 Part 1, ch. 12 (Requirements Management)",
    "Which phase establishes the organization's architecture capability and tailors the ADM?": "C220 Part 1, ch. 2 (Preliminary Phase)",
    # Building Blocks (C220 Part 4)
    "What is an Architecture Building Block (ABB)?": "C220 Part 4, §5.2.3 (Architecture Building Blocks)",
    "What is a Solution Building Block (SBB)?": "C220 Part 4, §5.2.4 (Solution Building Blocks)",
    "What is the relationship between ABBs and SBBs?": "C220 Part 4, §5.2 (Building Blocks)",
    "What is the primary benefit of reusing ABBs/SBBs?": "C220 Part 4, §5.3 (Building Blocks and the ADM)",
    # Repository / Continuum (C220 Part 5)
    "What does the Enterprise Continuum provide?": "C220 Part 4, Ch. 6 (Enterprise Continuum); C220 Part 5 governance context",
    "What is held in the Architecture Repository?": "C220 Part 4, Ch. 7 (Architecture Repository); C220 Part 5 governance context",
    # Principles (C220 Part 2)
    "What is the purpose of an Architecture Principle?": "C220 Part 2, ch. 2 (Architecture Principles)",
    "What is a key reason to define Architecture Principles early?": "C220 Part 2, ch. 2; C220 Part 1, ch. 2 (Preliminary)",
    # Deliverables (C220 Part 4 §4.2)
    "Which document formally authorizes the architecture project and defines scope?": "C220 Part 4, §4.2.20 (Statement of Architecture Work)",
    "Which deliverable triggers the start of an architecture engagement?": "C220 Part 4, §4.2.17 (Request for Architecture Work)",
    "What does an Architecture Contract govern?": "C220 Part 4, §4.2.2 (Architecture Contract)",
    "What is the Architecture Definition Document (ADD)?": "C220 Part 4, §4.2.3 (Architecture Definition Document)",
    "What is the Architecture Requirements Specification?": "C220 Part 4, §4.2.6 (Architecture Requirements Specification)",
    # Views and viewpoints (C220 Part 2)
    "What is a 'view' in TOGAF terms?": "C220 Part 2, Stakeholder Management / Architecture Views and Viewpoints",
    "What is a 'viewpoint'?": "C220 Part 2, Architecture Views and Viewpoints",
    "What governs how a view is constructed?": "C220 Part 2, Architecture Views and Viewpoints",
    # Stakeholders (C220 Part 2)
    "What is the purpose of a Stakeholder Map?": "C220 Part 2, ch. 3 (Stakeholder Management)",
    "What is a 'concern' in TOGAF?": "C220 Part 2, ch. 3 (Stakeholder Management)",
    "Who typically sponsors an architecture engagement?": "C220 Part 1, ch. 2 (Preliminary Phase) / Part 2 ch. 3",
    "What is the purpose of the Communications Plan?": "C220 Part 2, ch. 3 (Stakeholder Management)",
    # Gap analysis / transitions (C220 Part 2 / Part 1)
    "What is gap analysis used for in the ADM?": "C220 Part 2, ch. 5 (Gap Analysis)",
    "What is a Transition Architecture?": "C220 Part 1, ch. 8 (Phase E); C220 Part 4 §4.2",
    "What is the main value of Transition Architectures?": "C220 Part 1, ch. 8 (Phase E: Opportunities & Solutions)",
    # Governance (C220 Part 5)
    "What is the role of the Architecture Board?": "C220 Part 5, Architecture Board",
    "What is a 'dispensation' in architecture governance?": "C220 Part 5, Architecture Governance",
    "What is the purpose of a compliance review?": "C220 Part 5, Architecture Compliance",
    "What does 'conformance' mean in governance?": "C220 Part 5, Architecture Compliance",
    # Partitioning / Content Framework
    "What is architecture partitioning used for?": "C220 Part 3, Architecture Partitioning",
    "What is the TOGAF Content Framework?": "C220 Part 4, ch. 2 (Content Framework)",
    "What is an artifact in the Content Framework?": "C220 Part 4, ch. 3 (Artifacts)",
    "What is a catalog (artifact type)?": "C220 Part 4, ch. 3 (Artifacts: Catalogs, Matrices, Diagrams)",
    "What is a matrix (artifact type)?": "C220 Part 4, ch. 3 (Artifacts: Catalogs, Matrices, Diagrams)",
    # Business architecture
    "Which best describes 'capability-based planning'?": "TOGAF Series Guide: Business Capabilities (Capability-Based Planning); C220 Part 1, ch. 4 (Phase B)",
    "What is a Business Capability?": "TOGAF Series Guide: Business Capabilities; C220 Part 1, ch. 4 (Phase B)",
    "What is a value stream?": "TOGAF Series Guide: Value Streams; C220 Part 1, ch. 4 (Phase B)",
    "Which phase confirms the Baseline Business Architecture?": "C220 Part 1, ch. 4 (Phase B: Business Architecture)",
    # Concepts
    "What is a 'baseline' architecture?": "C220 Part 0, ch. 3 (Definitions)",
    "What is a 'target' architecture?": "C220 Part 0, ch. 3 (Definitions)",
    "What does 'interoperability' refer to in architecture?": "C220 Part 2, Interoperability Requirements",
    # Tailoring / iteration
    "Why tailor the ADM?": "C220 Part 3, ch. 2-3 (Applying the ADM: Tailoring)",
    "Which statement about the ADM is correct?": "C220 Part 1, ch. 1 (Introduction to the ADM)",
    # Phase summaries
    "What is the main output of Phase A?": "C220 Part 1, ch. 3 (Phase A: Architecture Vision)",
    "What is the main concern of Phase D?": "C220 Part 1, ch. 7 (Phase D: Technology Architecture)",
    "What is the main concern of Phase F?": "C220 Part 1, ch. 9 (Phase F: Migration Planning)",
    # Requirements
    "Which is a key relationship for Requirements Management?": "C220 Part 1, ch. 12 (Requirements Management)",
    # Risk
    "Which best describes 'risk' handling in the ADM?": "C220 Part 2, Risk Management",
    # Change
    "Which ADM phase would you revisit to handle a major change that re-architects the enterprise?": "C220 Part 1, ch. 11 (Phase H: Architecture Change Management)",
}


# ---------------------------------------------------------------------------
# Additional Level 1 items authored from the C220 evaluation bundle to give
# even coverage of every learning unit and replace the previous duplicate
# "variant-leads" padding. Each item carries an explicit C220 reference.
# 7-tuple: (stem, correct, d1, d2, d3, explanation, topic, reference)
# ---------------------------------------------------------------------------
L1_NEW_AUTHORED = [
    # Preliminary Phase (under-weighted previously)
    ("Which of the following is NOT an output of the Preliminary Phase?",
     "An approved Implementation and Migration Plan",
     "Tailored Architecture Framework", "Initial Architecture Repository", "Architecture Principles",
     "The Implementation and Migration Plan is produced in Phase F, not in the Preliminary Phase.",
     "Preliminary Phase",
     "C220 Part 1, ch. 2 (Preliminary Phase: Outputs)"),
    ("Which deliverable established in the Preliminary Phase defines the rules that govern the architecture practice?",
     "Architecture Governance Framework",
     "Statement of Architecture Work", "Architecture Vision", "Implementation and Migration Plan",
     "The Architecture Governance Framework, established in the Preliminary Phase, defines how architecture decisions will be governed.",
     "Preliminary Phase",
     "C220 Part 1, ch. 2; C220 Part 5 (EA Capability & Governance)"),
    # Phase A details
    ("Which input to Phase A is mandatory rather than optional?",
     "Request for Architecture Work",
     "Architecture Vision", "Architecture Definition Document", "Implementation and Migration Plan",
     "The Request for Architecture Work triggers Phase A; the Architecture Vision is an output, not an input.",
     "ADM Phases",
     "C220 Part 1, ch. 3 (Phase A: Inputs)"),
    ("What is the purpose of the Capability Assessment produced or refined in Phase A?",
     "To establish the baseline business, IT, and architecture capability ready to undertake the engagement",
     "To audit financial statements", "To define product pricing", "To replace the Statement of Architecture Work",
     "The Capability Assessment evaluates baseline and target capability gaps for business, IT, and the architecture practice itself.",
     "Deliverables",
     "C220 Part 4, §4.2.10 (Capability Assessment)"),
    # Phase B
    ("Which artifact catalogs the business capabilities of an enterprise?",
     "Business Capabilities Catalog",
     "Application Portfolio Catalog", "Technology Standards Catalog", "Data Entity Catalog",
     "The Business Capabilities Catalog is a Phase B artifact listing the capabilities the business possesses.",
     "Business Architecture",
     "C220 Part 4, §3.6.4.8 (Business Capabilities Catalog)"),
    ("Which best describes a Value Stream Stage?",
     "A discrete step within an end-to-end value stream that produces a defined value item",
     "A funding milestone", "A budget code", "A vendor SKU",
     "Each value-stream stage produces a value item that contributes to the overall stakeholder value delivered by the stream.",
     "Business Architecture",
     "TOGAF Series Guide: Value Streams"),
    # Phase C: Data
    ("Which artifact shows the relationship between data entities and the business functions that consume them?",
     "Data Entity / Business Function Matrix",
     "Network Diagram", "Risk Register", "Project Gantt Chart",
     "The Data Entity / Business Function matrix expresses ownership and usage of data across the business.",
     "Content Framework",
     "C220 Part 4, ch. 3 (Architectural Artifacts)"),
    # Phase C: Application
    ("Which catalog enumerates the application components present in the enterprise?",
     "Application Portfolio Catalog",
     "Standards Library", "Stakeholder Map", "Implementation Factor Catalog",
     "The Application Portfolio Catalog lists the application components that are part of the architecture.",
     "Content Framework",
     "C220 Part 4, ch. 3 (Artifacts)"),
    # Phase D
    ("Which catalog records the technology standards the enterprise has committed to?",
     "Technology Standards Catalog",
     "Application Portfolio Catalog", "Data Entity Catalog", "Stakeholder Catalog",
     "The Technology Standards Catalog records technology standards that govern the Target Technology Architecture.",
     "Content Framework",
     "C220 Part 4, ch. 3 (Artifacts)"),
    # Phase E
    ("What is the purpose of the Consolidated Gaps, Solutions and Dependencies Matrix?",
     "To consolidate gaps with candidate solutions and dependencies as input to defining work packages and Transition Architectures",
     "To track employee performance", "To set product prices", "To replace the Architecture Vision",
     "Used in Phase E, this matrix groups gap-analysis results with solutions and dependencies to inform work-package definition.",
     "ADM Phases",
     "C220 Part 1, ch. 8 (Phase E); Part 4 (Artifacts)"),
    ("Which of the following is one of the three basic implementation approaches discussed in Phase E?",
     "Evolutionary (incremental change)",
     "Outsource the architecture function", "Disband the Architecture Board", "Skip Phase F",
     "TOGAF identifies Greenfield, Revolutionary and Evolutionary implementation approaches in Phase E.",
     "ADM Phases",
     "C220 Part 1, ch. 8 (Phase E: Implementation Approaches)"),
    # Phase F
    ("What is the role of the Implementation and Migration Plan?",
     "A schedule for delivery of the Transition Architectures with timing, cost and resourcing",
     "A list of stakeholders", "A glossary of TOGAF terms", "An employee handbook",
     "The Implementation and Migration Plan is the Phase F deliverable sequencing work packages to deliver each Transition Architecture.",
     "Deliverables",
     "C220 Part 1, ch. 9; C220 Part 4 §4.2 (Implementation and Migration Plan)"),
    # Phase G
    ("During Phase G, which document binds the delivery organization to deliver in conformance with the architecture?",
     "Architecture Contract",
     "Architecture Vision", "Capability Assessment", "Communications Plan",
     "Architecture Contracts are agreements (with development partners, with business users, between the architecture function and sponsors) to deliver in conformance.",
     "Architecture Governance",
     "C220 Part 4, §4.2.2 (Architecture Contract)"),
    ("Which governance mechanism formally assesses whether an implementation conforms to its architecture?",
     "Architecture Compliance Review",
     "Stakeholder Map", "Business Scenario", "Capability Assessment",
     "Compliance reviews are the Phase G mechanism for verifying conformance to the architecture and its standards.",
     "Architecture Governance",
     "C220 Part 5, Architecture Compliance"),
    # Phase H
    ("Which classification of change normally triggers a new ADM cycle starting at the Architecture Vision?",
     "Re-architecting change",
     "Simplification change", "Incremental change", "No-impact change",
     "TOGAF classifies changes as Simplification, Incremental or Re-architecting. Re-architecting changes warrant a new ADM cycle.",
     "Change Management",
     "C220 Part 1, ch. 11 (Phase H: Change Classification)"),
    # Requirements Management
    ("Which artifact captures requirements that the architecture is expected to satisfy?",
     "Architecture Requirements Specification",
     "Architecture Contract", "Statement of Architecture Work", "Capability Assessment",
     "The Architecture Requirements Specification holds the quantitative statements of architecture requirements managed continuously through Requirements Management.",
     "Requirements Management",
     "C220 Part 1, ch. 12; Part 4 §4.2 (Architecture Requirements Specification)"),
    # Stakeholder Management & ADM Techniques
    ("What is the primary purpose of a Business Transformation Readiness Assessment?",
     "To assess the organization's preparedness to undertake the change implied by the target architecture",
     "To audit project budgets", "To select cloud vendors", "To replace the Architecture Vision",
     "C220 Part 2 Ch. 7 defines BTRA, which identifies organisational readiness factors (vision, desire, need, business case, funding, sponsorship, governance, accountability, workable approach, capacity to implement and operate).",
     "ADM Techniques",
     "C220 Part 2, Ch. 7 (Business Transformation Readiness Assessment)"),
    ("What is a Business Scenario used for in the ADM?",
     "To define stakeholders, business processes, technology environment, desired outcomes and SMART objectives that drive the architecture",
     "To replace the Statement of Architecture Work", "To run penetration tests", "To approve invoices",
     "Business Scenarios capture the business problem and requirements as a basis for the Architecture Vision and downstream phases.",
     "ADM Techniques",
     "TOGAF Series Guide G176 (Business Scenarios)"),
    ("How does TOGAF treat security in architecture development?",
     "As a cross-cutting concern integrated across all ADM phases",
     "As an optional add-on for regulated industries", "Only in Phase D after technology is selected", "As a separate framework that replaces the ADM",
     "Security stakeholders, requirements and controls thread through every ADM phase, not just Phase D.",
     "ADM Techniques",
     "TOGAF Series Guide G152 (Integrating Risk and Security within a TOGAF EA)"),
    # Applying the ADM
    ("Which three levels are typically used to organize the Architecture Landscape?",
     "Strategic, Segment, Capability",
     "Vision, Build, Run", "Business, Data, Technology", "Baseline, Transition, Target",
     "The Architecture Landscape is partitioned by Strategic (broad/long-term), Segment (coherent business area) and Capability (specific capability) levels.",
     "Architecture Landscape",
     "C220 Part 3, Applying the ADM (Architecture Landscape)"),
    ("Which iteration cycle within the ADM repeatedly executes Phases B, C and D to develop target architectures?",
     "Architecture Development iteration",
     "Architecture Context iteration", "Transition Planning iteration", "Architecture Governance iteration",
     "The Architecture Development iteration cycles through Phases B, C and D to refine the target architectures (C220 Part 3 §2.2).",
     "Iteration",
     "C220 Part 3, §2.2 (Iteration in the ADM)"),
    ("Which iteration cycle iterates between Phases E and F?",
     "Transition Planning iteration",
     "Architecture Context iteration", "Architecture Definition iteration", "Requirements iteration",
     "Transition Planning iterations cycle Phase E (Opportunities & Solutions) and Phase F (Migration Planning) to consolidate the roadmap.",
     "Iteration",
     "C220 Part 3, Applying the ADM (Iteration)"),
    ("Which of the following is a partitioning criterion identified in TOGAF for organising architectures?",
     "Subject matter (breadth), time period, level of detail, and maturity/volatility",
     "Salary bands", "Network OSI layers", "Office floor plans",
     "C220 Part 3 §4.1 distinguishes partitions from Landscape levels and identifies partitioning criteria such as subject matter (breadth), time, depth (level of detail), and maturity/volatility.",
     "Architecture Partitioning",
     "C220 Part 3, §4.1 (Architecture Partitioning Criteria)"),
    ("In TOGAF architecture partitioning, what does 'subject matter' (breadth) typically classify architectures by?",
     "Functional subject areas such as applications, departments, divisions, products, services or sites",
     "Hardware brands", "Vendor invoices", "Employee headcount",
     "Per C220 Part 3 Table 4-1, the Subject Matter (Breadth) criterion organises architecture work along functional subject areas — applications, departments, divisions, products, services, service centres or sites — not along the BDAT architecture domains, which are an orthogonal concept.",
     "Architecture Partitioning",
     "C220 Part 3, Table 4-1 (Architecture Partitioning: Subject Matter / Breadth)"),
    # Repository structure
    ("Which part of the Architecture Repository holds generic reusable guidance such as reference models and patterns?",
     "Reference Library",
     "Architecture Landscape", "Governance Repository", "Solutions Landscape",
     "The Reference Library holds generic, reusable architectural guidance that can be tailored to specific architectures.",
     "Architecture Repository",
     "C220 Part 4, Ch. 7 (Architecture Repository — Reference Library)"),
    ("Which part of the Architecture Repository records governance activity (agendas, decisions, dispensations)?",
     "Governance Repository",
     "Reference Library", "Standards Library", "Solutions Landscape",
     "The Governance Repository records governance process activity: agendas, decisions, compliance assessments, dispensations.",
     "Architecture Repository",
     "C220 Part 4, Ch. 7 (Architecture Repository — Governance Repository)"),
    ("Which part of the Architecture Repository holds the standards the enterprise must comply with?",
     "Standards Library",
     "Reference Library", "Architecture Requirements Repository", "Enterprise Repository",
     "The Standards Library holds the technical, business and regulatory standards the enterprise has committed to.",
     "Architecture Repository",
     "C220 Part 4, Ch. 7 (Architecture Repository — Standards Library)"),
    ("Where in the Architecture Repository are authorized architecture requirements held?",
     "Architecture Requirements Repository",
     "Solutions Landscape", "Governance Repository", "Reference Library",
     "The Architecture Requirements Repository holds the agreed, authoritative set of architecture requirements.",
     "Architecture Repository",
     "C220 Part 4, Ch. 7 (Architecture Repository — Architecture Requirements Repository)"),
    ("Which part of the Architecture Repository represents the architectures themselves at Strategic, Segment and Capability levels?",
     "Architecture Landscape",
     "Reference Library", "Standards Library", "Governance Repository",
     "The Architecture Landscape holds the descriptions of the architectures (Strategic / Segment / Capability) the organisation has produced.",
     "Architecture Repository",
     "C220 Part 4, Ch. 7 (Architecture Repository — Architecture Landscape)"),
    # Enterprise Continuum
    ("In the Enterprise Continuum, which end represents the most generic, reusable architectural assets?",
     "Foundation Architectures (Architecture Continuum end)",
     "Organization-Specific Solutions", "Industry Solutions", "Common Systems Solutions",
     "The Architecture Continuum runs from Foundation (most generic) through Common Systems, Industry, to Organization-Specific architectures.",
     "Enterprise Continuum",
     "C220 Part 4, Ch. 6 (Enterprise Continuum — Architecture Continuum classes)"),
    ("How are the Architecture Continuum and Solutions Continuum related?",
     "Each architecture stage in the Architecture Continuum has corresponding solutions in the Solutions Continuum that realise it",
     "They are entirely independent", "The Solutions Continuum replaces the Architecture Continuum", "They both store source code only",
     "The two continua are paired: ABBs in the Architecture Continuum are realised by SBBs in the Solutions Continuum.",
     "Enterprise Continuum",
     "C220 Part 4, Ch. 6 (Enterprise Continuum — Architecture / Solutions Continuum relationship)"),
    # Governance
    ("Which of the following is NOT one of the levels of architecture conformance defined by TOGAF?",
     "Conformant by default",
     "Irrelevant", "Consistent", "Conformant",
     "C220 Part 5 §6.2 (Figure 6-1) defines six levels of conformance: Irrelevant, Consistent, Compliant, Conformant, Fully Conformant and Non-conformant. 'Conformant by default' is not one of them.",
     "Architecture Governance",
     "C220 Part 5, §6.2 (Architecture Compliance — Levels of Conformance)"),
    ("Who typically sponsors the Architecture Board?",
     "A senior executive at the highest level of the organisation, such as the CIO",
     "An intern", "A vendor account manager", "An external auditor",
     "C220 Part 5 Ch. 4 describes the Architecture Board's executive sponsor as a senior executive at the highest level of the organisation — typically the CIO or equivalent — empowering the Board to take cross-enterprise architecture decisions.",
     "Architecture Governance",
     "C220 Part 5, Ch. 4 (Architecture Board)"),
    # Risk
    ("In TOGAF risk management, what is 'residual risk'?",
     "The risk remaining after mitigation actions have been applied",
     "Risk that has not yet been identified", "Risk that is transferred to a third party", "Risk that is automatically eliminated",
     "Residual risk is the risk that remains after mitigation; it is contrasted with initial risk before mitigation.",
     "Risk Management",
     "C220 Part 2, Risk Management"),
    # Metamodel / Content Framework
    ("Which TOGAF concept describes the entities, attributes and relationships used to structure architectural information?",
     "TOGAF Enterprise Metamodel",
     "Stakeholder Map", "Communications Plan", "Architecture Vision",
     "TOGAF 10 (C220 Part 4 §§2.2-2.6) defines the TOGAF Enterprise Metamodel, which describes the entities, attributes and relationships used to organise architectural information across the four domains. (TOGAF 9 called this the Content Metamodel.)",
     "Content Framework",
     "C220 Part 4, §§2.2-2.6 (TOGAF Enterprise Metamodel)"),
    # Stakeholder Management technique
    ("In the Power/Interest stakeholder matrix used to support stakeholder management, which group must be 'managed closely'?",
     "High-power, high-interest stakeholders",
     "Low-power, low-interest stakeholders", "Low-power, high-interest stakeholders", "High-power, low-interest stakeholders",
     "Stakeholders with high power and high interest are typically managed closely; others are kept informed, kept satisfied or monitored.",
     "Stakeholder Management",
     "C220 Part 2, ch. 3 (Stakeholder Management: Power/Interest)"),
    ("What is the purpose of the Stakeholder Matrix?",
     "To classify stakeholders by attributes such as power and interest to determine engagement approach",
     "To set salaries", "To list servers", "To record source-code commits",
     "The Stakeholder Matrix classifies stakeholders so engagement effort can be directed where it most matters.",
     "Stakeholder Management",
     "C220 Part 2, ch. 3 (Stakeholder Management)"),
    # Interoperability
    ("What is an Interoperability Requirement?",
     "A statement of the degree to which information must be shared between systems",
     "A pricing schedule", "A hardware warranty", "An office floor plan",
     "Interoperability requirements specify the necessary information sharing between systems and stakeholders.",
     "ADM Techniques",
     "C220 Part 2, Interoperability Requirements"),
    # Architecture Vision artefact
    ("Which is true of the Architecture Vision document?",
     "It provides a first-cut, high-level description of the Baseline and Target Architectures",
     "It is the final detailed design", "It is the Implementation and Migration Plan", "It is a list of vendors",
     "The Architecture Vision is a Phase A deliverable that gives a high-level snapshot of Baseline and Target used to obtain buy-in.",
     "Deliverables",
     "C220 Part 4, §4.2 (Architecture Vision); Part 1 ch. 3"),
    # ADM general
    ("Which best describes the relationship of Requirements Management to the ADM phases?",
     "Requirements Management runs continuously and interacts with every ADM phase",
     "It runs only in Phase A", "It runs only after go-live", "It replaces governance",
     "Requirements Management is the central, continuous process at the hub of the ADM, interacting with every phase.",
     "Requirements Management",
     "C220 Part 1, ch. 12 (Requirements Management)"),
    # Tailoring detail
    ("Which of the following is an explicit purpose of tailoring the ADM?",
     "To align the method with the organisation's context (industry, scale, agility, regulation)",
     "To make the ADM longer", "To remove governance", "To delete the repository",
     "Tailoring adapts the ADM to fit the enterprise's context — sector, regulation, scale, delivery approach — without losing rigour.",
     "Tailoring",
     "C220 Part 3, ch. 2-3 (Applying the ADM: Tailoring)"),
    # Phase B / value stream relation
    ("Which Phase B technique helps prioritise capability investment by linking capabilities to outcomes?",
     "Capability-based planning",
     "Penetration testing", "Capacity planning of hardware", "Tax planning",
     "Capability-based planning aligns investment with required capability increments and the outcomes they enable.",
     "Business Architecture",
     "TOGAF Series Guide: Business Capabilities (Capability-Based Planning); C220 Part 1, ch. 4 (Phase B)"),
    # Governance vs management
    ("Which best distinguishes architecture governance from architecture management?",
     "Governance sets direction and ensures compliance; management plans and operates the architecture practice",
     "They are synonyms", "Management replaces governance", "Governance is optional",
     "Governance and management are complementary: governance ensures the right things are done; management ensures things are done right.",
     "Architecture Governance",
     "C220 Part 5 (EA Capability and Governance)"),
    # Architecture Compliance scope
    ("Which of these is a typical outcome of an Architecture Compliance Review?",
     "An assessment classifying the project against TOGAF conformance levels",
     "A salary increase", "A new vendor contract", "A network upgrade",
     "A compliance review reports the project's conformance level (e.g. Irrelevant, Consistent, Compliant, Conformant, Fully Conformant, Non-conformant).",
     "Architecture Governance",
     "C220 Part 5, Architecture Compliance"),
    # Repository / capability
    ("Which best describes an Enterprise Architecture Capability?",
     "The ability of the enterprise to establish, sustain and use the Enterprise Architecture practice",
     "A single product purchase", "An IT operations team", "A finance function",
     "The EA Capability is the organizational ability to do EA work, sustained through people, process, governance and content.",
     "EA Capability",
     "C220 Part 5 (EA Capability and Governance)"),
    # Communications plan placement
    ("In which phase is the Communications Plan typically first established?",
     "Phase A",
     "Phase F", "Phase G", "Phase H",
     "The Communications Plan is typically created in Phase A as part of stakeholder management for the engagement.",
     "Stakeholder Management",
     "C220 Part 1, ch. 3 (Phase A)"),
    # Building blocks behaviour
    ("Which best describes the levels of building block?",
     "Building blocks may exist at any level of detail — strategic ABBs through to physical SBBs — and decompose into smaller building blocks",
     "Building blocks are always physical software", "Building blocks may not be reused", "Only Solution Building Blocks are governed",
     "Building blocks can exist at multiple levels of detail and decompose; both ABBs and SBBs are governed within the architecture practice.",
     "Building Blocks",
     "C220 Part 4, ch. 5 (Building Blocks)"),
    # Enterprise Continuum classification
    ("Which Common Systems Architecture example is typically held in the Enterprise Continuum?",
     "Generic security architecture",
     "A specific vendor's billing application", "The enterprise's organisation chart", "A salary schedule",
     "Common Systems Architectures are reusable across many enterprises (e.g. generic security or management architectures).",
     "Enterprise Continuum",
     "C220 Part 4, Ch. 6 (Enterprise Continuum — Common Systems Architectures)"),
    # Architecture Definition Document
    ("Which is true of the Architecture Definition Document?",
     "It is updated and elaborated across Phases B, C, and D",
     "It is created only in Phase H", "It is a single static document set in Phase A", "It is identical to the Implementation and Migration Plan",
     "The ADD captures the architecture across domains and is updated through Phases B, C and D as each domain architecture is developed.",
     "Deliverables",
     "C220 Part 4, §4.2.3 (Architecture Definition Document)"),
    # Implementation Factor Catalog
    ("What does the Implementation Factor Catalog capture?",
     "Factors (risks, issues, assumptions, dependencies, actions, impacts) that will influence the architecture implementation",
     "Salaries of architects", "Office floor plans", "A glossary of technical terms",
     "C220 Part 4 §3.6.8.3 defines the Implementation Factor Catalog (renamed in TOGAF 10 from the TOGAF 9 'Implementation Factor Assessment & Deduction Matrix'), which records risks, issues, assumptions, dependencies, actions and impacts that affect implementation planning in Phase E.",
     "Content Framework",
     "C220 Part 4, §3.6.8.3 (Implementation Factor Catalog)"),
    # Architecture Roadmap
    ("What does the Architecture Roadmap describe?",
     "A timeline of individual work packages and Transition Architectures that move from baseline to target",
     "A diagram of network cabling", "An employee handbook", "A budget forecast",
     "The Architecture Roadmap lists the individual work packages and the Transition Architectures, providing the timeline used in the Implementation and Migration Plan.",
     "Deliverables",
     "C220 Part 4, §4.2 (Architecture Roadmap)"),
    # Dispensation re-iterated with detail
    ("Which is true of a dispensation in architecture governance?",
     "It is time-bound, conditional, recorded, and triggers a remediation plan",
     "It is a permanent removal of a standard", "It is informal and undocumented", "It is granted by the delivery team itself",
     "Dispensations are granted by the governing body, conditional, time-bound, recorded in the Governance Repository, and accompanied by remediation.",
     "Architecture Governance",
     "C220 Part 5, Architecture Governance (Dispensations)"),
    # ABB realised by SBB phrasing
    ("Which statement is true about ABBs and SBBs?",
     "An ABB defines what is required; an SBB is the concrete realisation, often product-specific",
     "ABBs are concrete; SBBs are abstract", "They are interchangeable", "ABBs are produced only after SBBs",
     "ABBs express required capabilities at the logical level; SBBs are physical or vendor-specific realisations.",
     "Building Blocks",
     "C220 Part 4, §5.2 (Building Blocks)"),
    # Phase E
    ("Which best describes the focus of Phase E (Opportunities & Solutions)?",
     "Identify major work packages and define Transition Architectures",
     "Develop the detailed Technology Architecture", "Establish the Architecture Capability", "Govern post-implementation change",
     "Phase E consolidates gaps from B/C/D into work packages and defines Transition Architectures.",
     "ADM Phases",
     "C220 Part 1, ch. 8 (Phase E)"),
    # Phase G inputs
    ("Which is a key Phase G activity?",
     "Provide architectural oversight of implementation, including compliance reviews",
     "Establish the architecture capability", "Develop the Business Architecture", "Define the Architecture Vision",
     "Phase G governs implementation, ensuring delivered solutions conform to the Architecture Contract via compliance reviews.",
     "ADM Phases",
     "C220 Part 1, ch. 10 (Phase G)"),
    # Phase H criteria
    ("Which of the following is a recognised category of architectural change handled in Phase H?",
     "Simplification change",
     "Salary change", "Office relocation change", "Stock-price change",
     "Phase H classifies changes as Simplification, Incremental or Re-architecting.",
     "Change Management",
     "C220 Part 1, ch. 11 (Phase H)"),
    # ADM ordering
    ("Which is the correct order of ADM phases following Phase A?",
     "B, C, D, E, F, G, H",
     "C, B, D, E, G, F, H", "B, D, C, E, F, H, G", "C, D, B, F, E, G, H",
     "Phases run A → B → C → D → E → F → G → H, with Requirements Management at the centre.",
     "ADM Phases",
     "C220 Part 1, ch. 1 (ADM Overview)"),
    # Architecture Vision/SoAW relationship
    ("Which document is approved at the end of Phase A?",
     "Statement of Architecture Work",
     "Architecture Contract for implementation", "Implementation and Migration Plan", "Architecture Repository",
     "The signed Statement of Architecture Work concludes Phase A and authorises the rest of the engagement.",
     "Deliverables",
     "C220 Part 1, ch. 3 (Phase A: Outputs)"),
    # Transition Architecture detail
    ("Transition Architectures are described in which artifact?",
     "Architecture Roadmap",
     "Stakeholder Map", "Risk Register", "Business Footprint Diagram",
     "Transition Architectures are listed in the Architecture Roadmap, which sequences them between Baseline and Target.",
     "Transition Architectures",
     "C220 Part 4, ch. 3 (Architecture Roadmap)"),
    # Open group library reference
    ("Where can practitioners find practical guidance that complements the TOGAF Standard?",
     "The Open Group Library (TOGAF Series Guides)",
     "Vendor product manuals", "Internal HR policies", "Vendor pricing catalogs",
     "TOGAF Series Guides in The Open Group Library complement the Standard with practical guidance on capabilities, domains and techniques.",
     "EA Capability",
     "C220 Part 0, Preface; TOGAF Series Guides"),
    # Architecture Principles structure
    ("Which is a recommended structure for an Architecture Principle?",
     "Name, Statement, Rationale, Implications",
     "Vendor, Cost, License, Owner", "ID, Salary, Bonus", "Floor, Room, Desk, Chair",
     "TOGAF recommends each principle is captured with Name, Statement, Rationale and Implications.",
     "Architecture Principles",
     "C220 Part 2, ch. 2 (Architecture Principles: Format)"),
    # ADM techniques
    ("Which technique helps ensure that architecture artifacts address stakeholder concerns?",
     "Architecture Views and Viewpoints",
     "Penetration testing", "Office relocation planning", "Marketing segmentation",
     "Views are constructed using viewpoints to ensure stakeholder concerns are addressed.",
     "Views & Viewpoints",
     "C220 Part 2 (Architecture Views and Viewpoints)"),
    # Phase D outputs
    ("Which is a typical output of Phase D?",
     "Target Technology Architecture (including technology components)",
     "Approved Implementation and Migration Plan", "Architecture Vision document", "Architecture Capability Assessment",
     "Phase D produces the Target Technology Architecture along with updated ADD and Architecture Requirements Specification.",
     "ADM Phases",
     "C220 Part 1, ch. 7 (Phase D)"),
    # A small set to reach 128 while filling thin topics
    ("Which TOGAF technique is used to identify what is missing between the Baseline and Target Architectures?",
     "Gap Analysis",
     "Capability-Based Planning", "Stakeholder Mapping", "Capacity Planning",
     "Gap Analysis identifies items that have been deliberately omitted, accidentally left out, or are new — and is performed in Phases B/C/D and consolidated in Phase E.",
     "Gap Analysis",
     "C220 Part 2, ch. 5 (Gap Analysis)"),
    ("During gap analysis, which of the following is a typical category of finding?",
     "Items 'New' that exist in Target but not Baseline",
     "Items the architect personally prefers", "A vendor's price list", "An employee performance score",
     "Gaps are typically categorised as 'New', 'Eliminated' (intentionally removed) or 'Accidentally omitted', driving subsequent solution definition.",
     "Gap Analysis",
     "C220 Part 2, ch. 5 (Gap Analysis)"),
    ("In TOGAF risk management, what is 'initial risk'?",
     "Risk categorisation prior to determining and implementing mitigating actions",
     "Risk after full mitigation", "Risk that has been transferred", "Risk that has been accepted",
     "Initial risk is the risk classification before any mitigating actions are applied; residual risk is what remains after mitigation.",
     "Risk Management",
     "C220 Part 2, Risk Management"),
    ("Which is a typical artefact for tracking risk through the ADM?",
     "Consolidated Risk Register / Risk Assessment matrix",
     "Stakeholder Map", "Application Portfolio Catalog", "Capability Assessment",
     "A Risk Register / Risk Assessment matrix consolidates risks identified across phases and tracks them through to mitigation.",
     "Risk Management",
     "C220 Part 2, Risk Management"),
    ("Which Architecture Landscape level is the longest-term and least detailed?",
     "Strategic",
     "Segment", "Capability", "Transition",
     "Strategic architectures provide an enterprise-wide, long-term, summary view; Segment narrows scope; Capability adds detail for delivery.",
     "Architecture Landscape",
     "C220 Part 3 (Applying the ADM: Architecture Landscape)"),
    ("Which Architecture Landscape level is short-term, highly detailed, and bounded by what one project can deliver?",
     "Capability",
     "Strategic", "Segment", "Foundation",
     "Capability architectures are detailed enough to deliver a specific capability — short term and high detail.",
     "Architecture Landscape",
     "C220 Part 3 (Applying the ADM: Architecture Landscape)"),
    ("Which best describes the purpose of an EA Capability?",
     "To establish, sustain and use an EA practice that delivers value through change",
     "To replace project management", "To centralise IT operations", "To set salaries",
     "An EA Capability provides the organisational ability — people, process, governance, content — to do enterprise architecture continuously.",
     "EA Capability",
     "C220 Part 5 (EA Capability and Governance)"),
]

# Reference lookup for the four L1_TOPICS_EXTRA stems not in L1_REFS yet.
L1_REFS.update({
    "What is the relationship between ABBs and SBBs?": "C220 Part 4, §5.2 (Building Blocks)",
    "What is the purpose of a compliance review?": "C220 Part 5, Architecture Compliance",
    "Which statement about the ADM is correct?": "C220 Part 1, ch. 1 (ADM Overview)",
    "What is the main value of Transition Architectures?": "C220 Part 1, ch. 8 (Phase E)",
    "What does the Preliminary Phase define regarding governance?": "C220 Part 1, ch. 2 (Preliminary)",
    "Which ADM phase would you revisit to handle a major change that re-architects the enterprise?": "C220 Part 1, ch. 11 (Phase H)",
})


def build_level1():
    base = L1_FACTS + L1_TOPICS_EXTRA  # 56 unique stems, all with references
    questions = []
    qid = 1

    def emit(stem, correct, d1, d2, d3, expl, topic, reference):
        nonlocal qid
        opts = [correct, d1, d2, d3]
        order = list(range(4))
        random.shuffle(order)
        shuffled = [opts[i] for i in order]
        answer_index = shuffled.index(correct)
        questions.append({
            "id": f"L1-{qid:03d}",
            "level": 1,
            "topic": topic,
            "question": stem,
            "options": shuffled,
            "answer": answer_index,
            "explanation": expl,
            "reference": reference,
        })
        qid += 1

    # First: the canonical 56 base stems
    for stem, correct, d1, d2, d3, expl, topic in base:
        ref = L1_REFS.get(stem, "C220 (TOGAF Standard, 10th Edition)")
        emit(stem, correct, d1, d2, d3, expl, topic, ref)

    # Then: the newly authored items (each carries its own reference)
    for stem, correct, d1, d2, d3, expl, topic, ref in L1_NEW_AUTHORED:
        if len(questions) >= 128:
            break
        emit(stem, correct, d1, d2, d3, expl, topic, ref)

    # Defensive cap: do not exceed 128 items
    return questions[:128]


# ---------------------------------------------------------------------------
# LEVEL 2 (Practitioner) — gradient-scored scenarios.
# Each item: scenario question, 4 options with scores [best=5, second=3, 0, 0],
# and per-option rationale. We build from rich scenario templates per topic and
# generate organization-name variants to reach 128 while keeping pedagogy sound.
# ---------------------------------------------------------------------------

# A scenario template:
#   (topic, phase, context, situation, question,
#    best, second, zero1, zero2,
#    rationale_best, rationale_second, rationale_zero1, rationale_zero2)
#
# To match the real TOGAF Practitioner (Part 2) style, each scenario is written
# as a multi-paragraph case: a CONTEXT paragraph (organization background and
# where it is in the ADM), a SITUATION paragraph (the complication), and a
# QUESTION paragraph. Answer options are full, detailed courses of action.
L2_TEMPLATES = [
    ("Vision & Stakeholders", "Phase A",
     "has grown through a series of acquisitions and now operates three regional order-management systems, each with its own data model, release calendar, and operational team. The Board has approved a strategic objective to consolidate onto a single global platform within two years in order to reduce operating cost, improve cross-region reporting, and provide a consistent customer experience. The Enterprise Architecture function has been engaged and an experienced architect has been appointed to lead the engagement. The Preliminary Phase is complete: the Architecture Capability, governance framework, and tailored Architecture Development Method are established, and a Request for Architecture Work has been received from the sponsoring executive.",
     "During early Phase A activity, the architect discovers that the three regional operations directors each report against different, partly conflicting performance metrics, and that two of them publicly doubt that a single platform can serve the regulatory and service-level differences of their regions. The sponsoring executive is supportive but is under pressure to present a credible go/no-go recommendation to the Board within a few weeks and has asked the architect to keep the engagement moving quickly.",
     "Recommended by the TOGAF Standard, which of the following describes the best way for the architect to proceed?",
     "Develop a Stakeholder Map that identifies the regional directors and the sponsor together with their concerns, drivers, and the metrics they are measured against; work with them to reconcile the conflicting metrics into an agreed, measurable set of value propositions and KPIs within the Architecture Vision; document the agreed scope, constraints, and risks; and obtain sponsor approval of the Statement of Architecture Work before committing to detailed Business, Data, Application, or Technology work.",
     "Record the conflicting metrics and the directors' objections as risks and requirements in the Architecture Requirements Specification so they are traceable, then proceed to develop the Target Architecture and rely on the Architecture Board and the governance process to reconcile the metrics with the directors at a later review.",
     "Recommend to the sponsoring executive that the regional operations directors be removed from the decision-making forum for the engagement, on the grounds that their conflicting metrics and skepticism will otherwise delay the go/no-go recommendation the Board has requested.",
     "Proceed immediately to detailed Phase B, C, and D modelling of all three regions so that a complete, fact-based target design is available, and use the resulting models to demonstrate to the regional directors that their objections are unfounded.",
     "Phase A is where the architect establishes scope, identifies stakeholders and their concerns, and reconciles those concerns into an agreed Architecture Vision with measurable value propositions and KPIs, then secures sponsor approval via the Statement of Architecture Work before committing resources to detailed architecture work. This directly addresses the conflicting metrics and the need for a credible Board recommendation.",
     "Capturing the conflicts traceably as risks and requirements is good practice, but deferring the reconciliation of fundamental stakeholder concerns to a later governance review leaves the Vision unagreed and risks building a Target that key stakeholders will reject. It does part of the job but not the most important part — hence partial credit.",
     "Removing critical stakeholders to protect the timeline destroys the stakeholder buy-in on which the engagement depends and is contrary to TOGAF's emphasis on stakeholder management; it would very likely cause the recommendation to be rejected or unimplementable.",
     "Inverting the ADM by diving into full multi-domain modelling before an agreed Vision, and attempting to 'win an argument' against stakeholders with models, wastes effort, ignores stakeholder management, and is unlikely to change entrenched positions."),

    ("Business Architecture", "Phase B",
     "has set a strategic goal to become the most responsive provider in its market, but its leadership team is presenting the Enterprise Architecture function with a long and growing list of proposed technology projects. The Preliminary Phase and Phase A are complete, an Architecture Vision has been agreed and approved, and the engagement has now entered Phase B. There is, however, no shared, structured view of which business capabilities are weak, which capabilities most directly enable the strategic goal, or how the proposed projects relate to one another.",
     "The sponsor is keen to show early momentum and several executives are lobbying for their preferred projects to be funded first. The architect is concerned that funding projects in this way, without a capability view, will spread investment thinly and fail to move the strategic goal.",
     "According to TOGAF best practice for Phase B, what should the architect do?",
     "Develop a Business Architecture centred on a business capability map; assess current versus target maturity for each capability (for example using a heat map); trace capabilities to the strategic goal and to the value streams they support; and use prioritized capability increments to shape, sequence, and justify the project portfolio so that investment is directed at the capabilities that most move the goal.",
     "Take the executives' proposed project list and prioritize it primarily by estimated cost and speed of delivery, so that visible results can be delivered quickly and momentum maintained, recording the strategic goal as context.",
     "Defer Business Architecture work and begin instead with the enterprise data platform, on the grounds that data underpins every capability and that establishing it first will accelerate all subsequent projects.",
     "Record the strategic goal as a single high-level requirement and pass the executives' project list directly to the delivery organization, allowing each project team to define its own scope and architecture.",
     "Capability-based planning is the TOGAF-aligned Phase B technique: mapping capabilities, assessing their maturity against target, and linking them to goals and value streams gives an objective basis to prioritize and sequence investment around what most advances the strategy.",
     "Prioritizing by cost and speed is a legitimate input and will produce some quick wins, but on its own it ignores capability and value alignment and risks optimizing for activity rather than strategic outcome — partial credit.",
     "Skipping Business Architecture to start with the data platform inverts the ADM and decides a solution before the business need and capability gaps are understood.",
     "Passing an unstructured project list straight to delivery abandons the architecture role and the opportunity to align investment with the strategic goal."),

    ("Information Systems", "Phase C",
     "is a financial services organization whose customer information is duplicated and inconsistent across more than a dozen applications, each holding its own copy with subtly different definitions. This has produced contradictory regulatory and management reports, and a recent audit raised a finding about data quality and ownership. Phases A and B are complete and approved, and the engagement is now in Phase C, addressing the Data Architecture.",
     "The programme sponsor wants a credible remediation approach that will satisfy the auditors and improve reporting reliability, and has asked the architect specifically how the Data Architecture should address the duplication and inconsistency at its root.",
     "Which of the following is the best course of action for the architect?",
     "Develop the Target Data Architecture that defines authoritative (master) sources for key data entities, assigns clear data ownership and stewardship, and establishes common definitions and data standards; perform a gap analysis against the baseline; and define candidate roadmap components to consolidate sources and improve data quality, coordinating with data governance.",
     "Procure and stand up a new enterprise data lake and load all existing data into it as-is, so that a single physical store exists, deferring decisions about common definitions, ownership, and authoritative sources until after the lake is operational.",
     "Allow each application to retain its own data model and instead build a reconciliation layer that aligns the divergent data only at the point reports are produced.",
     "Recommend replacing all of the affected applications first, on the assumption that the new systems will inherently resolve the data duplication and quality problems.",
     "Defining authoritative sources, ownership, and common standards and then gap-analyzing to drive consolidation tackles the root cause of the duplication and inconsistency, and aligns with the Phase C Data Architecture steps and data governance considerations in the Standard.",
     "A data lake can be a useful component, but loading data 'as-is' while deferring definitions, ownership, and authoritative sources does not address the inconsistency at its root and may simply centralize the mess — partial credit.",
     "Reconciling only at reporting time leaves the duplication and inconsistent definitions in place and perpetuates the very problem the audit raised.",
     "Replacing all applications first is high-cost and high-risk and rests on the unfounded assumption that new systems automatically fix data ownership and definition problems."),

    ("Technology Architecture", "Phase D",
     "is under pressure from its CIO to reduce the cost and operational risk created by a sprawl of inconsistent technologies that have accumulated across autonomous delivery teams. At the same time, the CIO is adamant that the organization must remain able to adopt promising new technologies quickly, because innovation is a competitive differentiator. Phases A through C are complete and approved, and the engagement is in Phase D, developing the Technology Architecture.",
     "Some delivery teams fear that standardization will be used to forbid any new technology, while infrastructure leaders fear that unrestricted choice will keep costs and risk high. The architect must reconcile these positions in the Technology Architecture.",
     "What is the most appropriate way for the architect to proceed?",
     "Define a Target Technology Architecture with a standards catalogue (technology portfolio) covering preferred platforms and services; perform a gap analysis against the baseline; and establish a governed dispensation process through which teams can adopt non-standard or emerging technologies where there is a justified, time-bound business case, with conditions and review.",
     "Mandate a single standard technology stack for all teams and all purposes, with no exceptions permitted, in order to maximize consolidation and minimize the cost and risk of sprawl.",
     "Allow every team to continue selecting any technology it prefers, with no standards at all, so that the organization's ability to innovate quickly is fully preserved.",
     "Select technologies purely on the basis of the lowest immediate licensing cost, regardless of their fit to requirements, their lifecycle maturity, or their integration with the rest of the estate.",
     "A standards catalogue combined with a governed dispensation process delivers the consolidation the CIO needs while still allowing justified, controlled adoption of emerging technologies — directly reconciling the two competing concerns, consistent with TOGAF governance.",
     "A single mandated stack with no exceptions does control sprawl, but it blocks the rapid innovation the CIO has explicitly required and will likely drive shadow IT — partial credit.",
     "Allowing unrestricted technology choice with no standards simply preserves the cost and risk problem the engagement was initiated to solve.",
     "Choosing on lowest licence cost alone ignores fit-for-purpose, lifecycle, and integration, and typically increases total cost and risk over time."),

    ("Migration Planning", "Phase E/F",
     "has an approved Target Architecture that represents a substantial transformation: the gap between the baseline and the target is large, the full programme is expected to take around eighteen months, and there are significant dependencies between several of the components. The business sponsor has made clear that the organization needs to see early, tangible value rather than waiting until the end of the programme, and the Board will review progress at regular intervals. Phases A through D are complete and approved, and the engagement is now in Phases E and F.",
     "Delivery leaders are debating how to structure the work: some favour delivering everything at once at the end to avoid the complexity of interim states, while others want to grab the single easiest component for a quick win and worry about the rest later.",
     "Which approach should the architect recommend?",
     "Define a set of Transition Architectures that describe valuable, coherent intermediate states; group the required changes into work packages; sequence them using value, risk, dependency, and a cost/benefit and risk assessment; and consolidate this into an Architecture Roadmap and Implementation and Migration Plan that is coordinated with portfolio, programme, and project management.",
     "Identify and deliver only the single easiest component first to give the Board an early visible result, and defer planning and delivery of the remaining, harder components indefinitely until that first piece is complete.",
     "Plan a single 'big-bang' cutover to the full Target Architecture at the end of the eighteen months, so that the organization never has to operate or integrate any interim state.",
     "Begin implementation with the most technically difficult component first to retire the biggest risk, and postpone migration and sequencing planning until that component has been built.",
     "Transition Architectures plus sequenced work packages, prioritized by value, risk, dependency, and cost/benefit and consolidated into an Implementation and Migration Plan, are exactly how Phases E and F deliver incremental value toward the Target while managing dependencies — and they satisfy the sponsor's need for early value.",
     "Delivering one easy component does use the transition idea to create early value, but abandoning the sequencing of the remaining Target work fails the purpose of Phase E/F and leaves the transformation unmanaged — partial credit.",
     "A single big-bang cutover ignores the explicit need for early value and concentrates risk into one event.",
     "Starting with the hardest component while deferring planning leaves the programme unsequenced and unmanaged, regardless of the risk-retirement intent."),

    ("Implementation Governance", "Phase G",
     "is partway through delivering an approved architecture and is governing implementation under an Architecture Contract that commits the delivery team to the mandated enterprise integration pattern. During a compliance review, the architect finds that the delivery team has deviated from that pattern for performance reasons and, in doing so, has introduced undocumented point-to-point coupling between two services. Phases A through F are complete and approved, and the engagement is in Phase G.",
     "The delivery team is under intense schedule pressure and wants to proceed to go-live imminently, arguing that the deviation works and that revisiting it now will jeopardize the date.",
     "What is the best response from the architect?",
     "Complete the compliance review and formally document the non-conformance against the Architecture Contract and the enterprise pattern; assess the risk and impact of the undocumented coupling; and require either remediation to conformance or a formal, time-bound dispensation with explicit conditions and a remediation plan, before authorizing go-live.",
     "Direct the delivery team to immediately rebuild the integration to conform to the mandated pattern, without first assessing the justification, the risk, or the cost and schedule impact of doing so.",
     "Informally approve the deviation so that the go-live date is protected, intending to document the non-conformance and any conditions afterwards if time permits.",
     "Withdraw the mandated integration pattern from the standards catalogue, on the basis that the delivery team found it impractical in this case.",
     "Completing the compliance review, documenting the non-conformance, and requiring remediation or a governed, conditional dispensation is the correct Phase G governance response: it upholds the Architecture Contract while handling the deviation transparently and proportionately.",
     "Mandating an immediate rebuild does uphold the standard, but ordering it without assessing justification, risk, and cost/schedule impact is disproportionate and skips the governance assessment — partial credit.",
     "Approving the deviation informally to protect the date defeats the purpose of governance and leaves risk undocumented and unmanaged.",
     "Removing the standard because one team found it inconvenient is a disproportionate, enterprise-wide reaction to a single project's situation."),

    ("Change Management", "Phase H",
     "has been operating its current architecture stably for some time since go-live, with Phase H change management in place to monitor it. The executive team now decides to enter an entirely new, heavily regulated product line that the current architecture was never designed to support: it brings new compliance obligations, new external partners, new data, and new end-to-end processes. A change request capturing this decision has been submitted to the Architecture Board.",
     "Some board members want to treat it as a routine change to be absorbed into business-as-usual maintenance, while the sponsor wants clarity on what governance path the change should follow.",
     "How should the architect advise the Architecture Board to handle this change?",
     "Assess the change against the established change-management criteria and classify it; recognise that, because it requires new capabilities, processes, partners, and compliance that the current architecture cannot accommodate, it is a major (re-architecting) change; and recommend initiating a new iteration of the ADM, beginning with a fresh Architecture Vision scoped to the new product line.",
     "Log the change request in the architecture backlog and defer any assessment of it until the next scheduled annual architecture review, so that it can be considered alongside other accumulated changes.",
     "Direct that the change be implemented straight into production to meet the executive's timeline, and document the architectural impact retrospectively once the new product line is live.",
     "Reject the change from an architecture perspective and advise the new product line to be built and run on entirely separate IT that sits outside the enterprise architecture and its governance.",
     "Phase H classifies change drivers and determines the appropriate response; a change of this magnitude is a re-architecting change that should trigger a new ADM cycle starting at the Architecture Vision, which is exactly the advice the Board needs.",
     "Logging the change keeps it within governance, but deferring assessment of a strategic, regulated change to an annual review is far too slow and risks the business moving ahead without architecture support — partial credit.",
     "Implementing straight into production bypasses governance and risks designing-in non-compliance in a regulated context.",
     "Pushing the new line onto ungoverned, separate IT abandons the architecture role and creates exactly the kind of unmanaged estate EA exists to prevent."),

    ("Requirements Management", "Central",
     "is midway through Phase C of an approved engagement when a new regulatory mandate is published that materially affects data retention and lineage. On analysis, the mandate affects not only the in-progress Phase C Data and Application designs but also several deliverables in the Business Architecture that were completed, reviewed, and baselined during Phase B. The engagement uses the central Requirements Management process at the hub of the ADM.",
     "The delivery team is anxious not to lose time and suggests simply absorbing the new rule into the current Phase C work, on the basis that re-opening Phase B would be disruptive.",
     "What is the correct way for the architect to handle the new requirement?",
     "Raise the new mandate through the central Requirements Management process; assess its impact across all affected phases; re-open and re-validate the affected Phase B and Phase C deliverables; update the Architecture Requirements Specification; and manage the resulting changes with full traceability and appropriate governance.",
     "Incorporate the new mandate into the in-progress Phase C deliverables only, and treat the previously signed-off Phase B deliverables as fixed so that the baseline is not disturbed.",
     "Defer the new mandate until the current Phase C work is finished, and then capture it as a separate follow-on requirement to be addressed in a later piece of work.",
     "Treat the new mandate as invalidating the engagement and restart the entire ADM cycle from Phase A.",
     "Requirements Management operates continuously throughout the ADM; the correct response is to assess the cross-phase impact and re-validate every affected deliverable (including baselined Phase B work) under governance with traceability.",
     "Updating only Phase C is partially correct, but leaving affected, baselined Phase B deliverables unchanged knowingly creates a compliance gap between the business and the lower-level designs — partial credit.",
     "Deferring a known regulatory impact risks designing-in non-compliance that will be more expensive to remediate later.",
     "Restarting the whole ADM from Phase A is a disproportionate response to a requirement change that can be handled through impact assessment and re-validation."),

    ("Enterprise Continuum", "Repository",
     "maintains a well-populated Architecture Repository and Enterprise Continuum that includes a governed, reusable identity and access-management capability, expressed as an Architecture Building Block with a corresponding Solution Building Block that has already been proven in production. A newly formed product team, working at speed, proposes to design and build a bespoke customer-authentication service from scratch; the team is unaware that the governed, reusable asset already exists.",
     "The product team's lead argues that building their own service will be faster than learning and adopting an existing asset, and the team's delivery manager is reluctant to add any dependency that might slow them down.",
     "What should the architect do?",
     "Direct the team to the governed Architecture Building Block and its proven Solution Building Block in the repository; require its adoption as the default; and, where the team can demonstrate a genuine capability gap, route that gap through the governance process as a formal, justified dispensation before any bespoke build is sanctioned.",
     "Allow the product team to build their bespoke authentication service, but require them to register it in the Architecture Repository afterwards so that it becomes a reusable asset for future teams.",
     "Approve the bespoke build without further analysis, on the basis that the product team's delivery speed and autonomy are the most important considerations.",
     "Withdraw the existing identity asset from the Architecture Repository so that there is no confusion about which authentication service teams should use.",
     "Reuse of governed assets from the Enterprise Continuum, with genuine gaps handled through governed dispensation, is the core value the repository exists to deliver and avoids unnecessary duplication and risk.",
     "Registering a new bespoke service afterwards does promote capture and future reuse, but it sanctions an avoidable duplicate of an already-proven asset and so is only partially aligned — partial credit.",
     "Approving a bespoke build with no analysis abandons reuse and governance and recreates capability that already exists in a proven form.",
     "Withdrawing a proven, governed asset because one team failed to discover it is a disproportionate reaction that destroys value for every other team."),

    ("Governance", "Governance",
     "has a single Architecture Board that, by current policy, must approve every architecture-related decision regardless of size. As the volume of change has grown, the board has become a bottleneck: trivial decisions queue for weeks, and, paradoxically, genuinely significant architecture decisions are being rushed through with little scrutiny because of the backlog. Delivery teams are increasingly frustrated and some have begun making decisions quietly without consulting the board at all.",
     "The sponsor has asked the architect to recommend how governance should be reshaped so that it remains effective without strangling delivery.",
     "What should the architect recommend?",
     "Introduce proportionate, risk-based governance: define clear criteria so that low-impact decisions are delegated or handled through a streamlined/standing-delegation route, while the Architecture Board reserves its attention for high-impact decisions — preserving accountability, traceability, and the ability to escalate.",
     "Retain the existing policy that the Architecture Board must approve every decision however small, on the grounds that universal approval is the only way to guarantee consistency.",
     "Disband the Architecture Board entirely so that no architecture decision is ever delayed by governance again.",
     "Formally permit delivery teams to bypass governance for any decision they individually judge to be minor, with no defined criteria or record.",
     "Proportionate, risk-based governance focuses scarce board attention on the decisions that matter while keeping low-impact decisions moving — directly resolving the bottleneck without losing control, consistent with TOGAF governance.",
     "Requiring the board to approve everything is internally consistent but is precisely the cause of the bottleneck and the rushed scrutiny described — partial credit.",
     "Disbanding the board removes the governance the organization needs and would worsen, not fix, the underlying control problem.",
     "Letting teams self-certify decisions as 'minor' with no criteria or record is uncontrolled and effectively the unsanctioned bypass already causing concern."),

    ("Preliminary & Tailoring", "Preliminary",
     "is a highly regulated organization adopting the TOGAF Standard for Enterprise Architecture for the first time. It delivers software through autonomous agile teams, already mandates an industry reference model for parts of its domain, and has a leadership team that is openly wary of anything it perceives as heavyweight, document-driven process. The engagement is at the very beginning, in the Preliminary Phase.",
     "The architect must establish an Architecture Capability that will be credible to regulators, acceptable to agile delivery teams, and respectful of the existing reference model, without triggering the leadership's resistance to bureaucracy.",
     "How should the architect approach the Preliminary Phase?",
     "Use the Preliminary Phase to establish the Architecture Capability and tailor the ADM to the organization's regulatory and agile delivery context; integrate the existing industry reference model into the Enterprise Continuum; select the architecture principles, artifacts, and deliverables that add value in this context; and put proportionate Architecture Governance in place to manage the tailored method.",
     "Skip most of the Preliminary Phase and begin directly at the Architecture Vision, deferring decisions about tailoring, principles, and governance until specific problems actually arise in the engagement.",
     "Adopt the full ADM and produce every deliverable and artifact exactly as documented in the Standard, without any tailoring, to ensure nothing is missed.",
     "Discard the TOGAF ADM altogether and rely solely on the existing industry reference model, since the organization is already familiar with it.",
     "The Preliminary Phase exists precisely to establish and tailor the method, principles, repository, and governance to the enterprise's context — including regulatory and agile factors and existing reference models — which is exactly what this organization needs.",
     "Starting at the Architecture Vision shows welcome delivery focus, but skipping the essential establishment of capability, tailoring, and governance stores up problems and is not what the Preliminary Phase is for — partial credit.",
     "Adopting the full ADM with every artifact and no tailoring directly contradicts TOGAF's guidance that the method must be tailored, and will trigger exactly the resistance the architect must avoid.",
     "Discarding the ADM in favour of a single reference model throws away the method that provides the end-to-end approach, governance, and traceability the regulator will expect."),

    ("Security & Risk", "Cross-cutting",
     "has a track record of treating security as something to be added near the end of delivery. On its last two programmes this 'bolt-on' approach caused significant late rework and produced audit findings about controls that were designed in too late to be effective. The organization is now starting a new customer-facing platform and the CISO and sponsor are jointly determined that security and risk be addressed properly from the outset. Phase A is underway.",
     "Some delivery leaders, remembering past friction, assume that 'security from the outset' simply means an earlier version of the same end-of-project review.",
     "How should the architect ensure security and risk are handled correctly across the engagement?",
     "Integrate security and risk as first-class concerns throughout the ADM: capture security and risk requirements early in Phase A, reflect and elaborate them consistently across the Business, Data, Application, and Technology Architectures, and govern security compliance during implementation in Phase G — rather than treating security as a single late checkpoint.",
     "Plan a single comprehensive security review to be conducted at the end of the programme, just before go-live, but make it more thorough than on previous programmes.",
     "Delegate all responsibility for security entirely to the operations team, to be addressed after the platform has been deployed into production.",
     "Treat security as an optional concern to be addressed only if and when a specific regulation is shown to compel it.",
     "Embedding security and risk across every ADM phase — from early requirements through cross-domain design to implementation governance — is the approach that prevents the late-rework and ineffective-control problems described, and reflects TOGAF's treatment of security and risk as cross-cutting concerns.",
     "A single end-of-programme review, even a thorough one, still reproduces the bolt-on anti-pattern by leaving security to the end — partial credit.",
     "Delegating all security to operations after deployment is precisely the late, ineffective approach that caused the previous audit findings.",
     "Treating security as optional unless forced is indefensible for a customer-facing platform and ignores the organization's stated intent."),

    ("Architecture Partitioning", "Cross-cutting",
     "is a diversified conglomerate made up of several semi-autonomous business units that operate in genuinely different markets, with different regulators, customers, and operating models. Leadership wants the benefits of enterprise architecture — coherence, reuse, and the ability to govern the whole — but a single, uniformly detailed enterprise-wide architecture has already been tried once before and collapsed under its own complexity. The engagement is establishing how architecture work should be organized across the group.",
     "Unit leaders are protective of their autonomy and skeptical of central control, while the group CIO is concerned about duplicated investment and incompatible decisions across units.",
     "What should the architect recommend?",
     "Apply architecture partitioning to divide the architecture work along appropriate dimensions (such as breadth, level of detail, and business unit), allowing each unit to develop and govern its own architectures within a shared framework of principles, standards, reference models, and governance that ensures group-level coherence, reuse, and the resolution of conflicts.",
     "Impose a single, uniformly detailed enterprise architecture identically across every business unit, to guarantee maximum consistency across the group.",
     "Allow each business unit to develop architecture entirely independently, with no shared framework, standards, or governance, so that unit autonomy is fully preserved.",
     "Abandon the enterprise architecture initiative on the grounds that the units are too different for any common architecture to be worthwhile.",
     "Architecture partitioning is TOGAF's mechanism for exactly this situation: it balances unit autonomy with group-level coherence, reuse, and governance, and avoids the over-complex single architecture that previously failed.",
     "A single uniformly detailed architecture does maximize consistency on paper, but it ignores the genuine differences between units and is the very approach that already collapsed — partial credit.",
     "Fully independent units with no shared framework forfeit the coherence, reuse, and conflict-resolution the group CIO needs.",
     "Abandoning enterprise architecture entirely surrenders the coherence and reuse goals rather than solving the complexity problem."),

    ("Stakeholder Management", "Phase A",
     "is undertaking a major transformation of a core regulated service. A key external regulator has signalled, informally, that it is concerned the transformation could inadvertently weaken several controls on which its supervision depends. The sponsoring executive, conscious of competitive pressure, is anxious to move quickly and is inclined to treat the regulator as a downstream approval rather than an active stakeholder. The engagement is in Phase A.",
     "The architect judges that the regulator's concerns, if not addressed early, could later force expensive redesign or even block go-live.",
     "What is the best way for the architect to handle the regulator?",
     "Include the regulator explicitly in the Stakeholder Map as a key stakeholder; translate its concerns about the controls into architecture requirements and constraints; address them within the Architecture Vision and the relevant architecture views; and engage the regulator appropriately through the Communications Plan so that its concerns are understood and demonstrably met.",
     "Record the regulator's concern in the engagement risk log and proceed at pace, planning to retrofit any controls the regulator insists upon during the testing phase.",
     "Exclude the regulator from active engagement during the architecture work, so that the sponsor's desire for speed is not compromised, and deal with the regulator only at final approval.",
     "Decline to progress any further until the regulator has personally reviewed and signed off every individual design artifact the engagement will produce.",
     "Treating the regulator as a key stakeholder, turning its concerns into requirements and constraints, and addressing them through the Vision, views, and Communications Plan is the TOGAF-aligned way to prevent costly late redesign and protect go-live.",
     "Logging the concern as a risk is partly responsible, but relying on retrofitting controls during testing is weak and risky for a regulated control environment — partial credit.",
     "Excluding a critical external stakeholder to protect speed is a stakeholder-management anti-pattern that is likely to cause exactly the late blockage the architect fears.",
     "Requiring the regulator to personally sign off every artifact is impractical, would stall the engagement, and misunderstands how stakeholder concerns are addressed."),

    ("Application Architecture", "Phase C",
     "is rationalizing the applications that support a core, end-to-end business process. Several stakeholder groups have each independently proposed a different SaaS product, and on inspection each product covers only part of the overall process while overlapping substantially with the others. Left unmanaged, this would create significant functional overlap, duplicated licence cost, and a tangle of integrations. Phases A and B are complete and approved, and the engagement is in Phase C addressing the Application Architecture.",
     "Each stakeholder group is lobbying for its preferred product and the sponsor is keen to avoid a political battle, but is also worried about overlap and integration cost.",
     "What should the architect do?",
     "Develop the Target Application Architecture and target application portfolio; map each proposed SaaS product to the logical application components and business capabilities required by the end-to-end process; identify the overlaps and gaps explicitly; and recommend a rationalized set of applications that covers the process with minimal duplication and integration complexity.",
     "Select, for each individual function in the process, whichever proposed product is cheapest, regardless of how much the chosen products overlap or how they will integrate.",
     "Approve all of the proposed SaaS products so that every stakeholder group's preference is satisfied and the political battle is avoided.",
     "Defer all application decisions until the Technology Architecture (Phase D) has been completed and the underlying platform has been finalized.",
     "Defining the Target Application Architecture and mapping proposed products to required components and capabilities lets the architect rationalize the portfolio objectively, minimizing overlap and integration sprawl — the correct Phase C response.",
     "Choosing the cheapest product per function does control unit cost, but it ignores overlap and integration and will likely produce exactly the tangle the engagement is trying to prevent — partial credit.",
     "Approving every proposed product to keep stakeholders happy guarantees the overlap, duplicated cost, and integration sprawl described.",
     "Deferring all application decisions until after the technology platform inverts the normal Phase C/D relationship and decides infrastructure before the application need is understood."),

    ("Value & Benefits", "Phase B",
     "has a CFO who, having seen previous transformation budgets overrun with little demonstrable benefit, is now challenging the Enterprise Architecture function to show, for each proposed investment, exactly how it ties to measurable business value. The engagement is in Phase B, an Architecture Vision is agreed, and a portfolio of candidate investments is being shaped.",
     "The CFO has made clear that 'trust us, architecture adds value' will not be accepted, and that funding will follow only those investments with a credible, traceable value case.",
     "How should the architect respond to the CFO's challenge?",
     "Use the Business Architecture — specifically value streams and business capabilities — to trace each proposed investment to the capabilities it improves and the value-stream stages and business outcomes it enables, giving the CFO a clear, evidenced line of sight from strategy through capability to measurable benefit.",
     "Provide the CFO with a detailed list of the technology features and components that the programme will deliver, and present that feature list as the value case for the investment.",
     "Explain to the CFO that the value of enterprise architecture is inherently intangible and therefore cannot reasonably be tied to individual investments.",
     "Refer the entire question of investment value to the finance team, on the basis that quantifying business value is their responsibility rather than the architect's.",
     "Tracing investments to capabilities and value streams provides the evidenced, strategy-to-benefit line of sight the CFO is demanding and is exactly how Business Architecture demonstrates value.",
     "A feature/component list is a weak proxy for value and at least attempts a case, but it describes what will be built rather than the business benefit it delivers — partial credit.",
     "Asserting that architecture value is intangible abandons accountability for outcomes and concedes the CFO's central point.",
     "Handing the value question entirely to finance abdicates the Business Architecture responsibility to connect investment to capability and outcome."),
]


ORG_NAMES = [
    "MeridianFreight", "Aurora Telecom", "Brightside Bank", "Helix Robotics",
    "Verdant Retail", "Cobalt Manufacturing", "Summit Health", "Nimbus Logistics",
    "Orion Media", "Pinecone Insurance", "Granite Bank", "Cobalt Energy",
    "HelioPower", "Falcon Airlines", "Delta Foods", "Sierra Retail",
    "Orion Insurance", "Cobalt Bank", "Astra Manufacturing", "Pinecrest Telecom",
    "CivicHealth", "Quill Bank", "NorthBank", "Helio Insurance",
    "Vertex Pharma", "Cobalt Retail", "Granite Telecom", "Brightwater Bank",
    "Helix Pharma", "Aurora Group", "Sentinel Bank", "Cobalt Group",
]

ORG_DESCRIPTORS = [
    "a global logistics firm", "a national telecom operator", "a retail bank",
    "an industrial robotics company", "a regional retailer", "a manufacturing group",
    "a healthcare provider", "a logistics company", "a media organization",
    "an insurer", "a commercial bank", "an energy utility",
    "a power utility", "an airline", "a food producer", "a retail chain",
    "an insurance company", "a digital bank", "a manufacturer", "a telecom provider",
    "a public healthcare body", "a bank", "a retail bank", "an insurer",
    "a pharmaceutical company", "a retailer", "a telecom carrier", "a bank",
    "a pharmaceutical firm", "a diversified conglomerate", "a bank", "a holding group",
]


# ---------------------------------------------------------------------------
# Per-template third-best option (1 point) plus the C220 reference, matching
# the 5/3/1/0 gradient the real OGEA-102 exam uses. Indexed by L2_TEMPLATES.
# Each entry: (third_option_text, third_rationale, reference).
# ---------------------------------------------------------------------------
L2_THIRD_AND_REF = [
    # t0  Vision & Stakeholders / Phase A — multinational order-management
    ("Document each regional director's objections and metrics in the Statement of Architecture Work as accepted constraints; then proceed to a Target Architecture that assumes the conflicting metrics will be resolved by the operating model team after architecture work is complete.",
     "Documenting concerns in the SoAW and a credible plan to resolve them is at least within Phase A scope and uses the right deliverable, but delegating the resolution of stakeholder conflict to a downstream team leaves the Vision unagreed — partial credit.",
     "C220 Part 1, ch. 3 (Phase A); Part 2 ch. 3 (Stakeholder Management)"),
    # t1  Business Architecture / Phase B — strategy and capability map
    ("Build a draft capability map and use it to advise the sponsor informally; let the sponsor pick which executive's project to fund first, then retro-fit the chosen project into the capability view so progress is not delayed.",
     "Building a capability map is the correct Phase B technique, but using it only to rubber-stamp pre-chosen projects loses the objectivity that capability-based planning provides — partial credit.",
     "C220 Part 2 (Capability-Based Planning); Part 1, ch. 4 (Phase B)"),
    # t2  Information Systems / Phase C — financial services data
    ("Define authoritative sources and common definitions for the highest-impact data entities only, and leave the rest of the duplicated and inconsistent data to be tidied opportunistically by individual application projects over time.",
     "Targeting the most material entities first applies the right Phase C technique, but explicitly leaving the rest untouched perpetuates the audit problem and gives no end-state for data ownership — partial credit.",
     "C220 Part 1, ch. 5 (Phase C: Data); Part 4 (Content Framework)"),
    # t3  Technology Architecture / Phase D — tech sprawl
    ("Publish a recommended technology standards catalogue but make it advisory rather than governed, on the assumption that delivery teams will adopt it voluntarily once they see the benefits.",
     "Defining the standards catalogue is the right Phase D step, but making it purely advisory without a dispensation route or governance leaves the CIO's consolidation goal unenforced — partial credit.",
     "C220 Part 1, ch. 7 (Phase D); Part 5 (Architecture Governance)"),
    # t4  Migration Planning / Phase E/F — 18-month transformation
    ("Define a single Transition Architecture covering the lowest-risk components and put their delivery into an Implementation and Migration Plan; defer planning for everything else until that Transition has been delivered.",
     "Using a Transition Architecture and an Implementation and Migration Plan are the right Phase E/F mechanisms, but planning only the easy increment and deferring the rest gives no roadmap to the Target — partial credit.",
     "C220 Part 1, ch. 8 (Phase E) and ch. 9 (Phase F)"),
    # t5  Implementation Governance / Phase G — non-conformance
    ("Allow the deviation to proceed to go-live, then immediately raise a formal dispensation request after go-live so the non-conformance is recorded against the Architecture Contract and a remediation plan is tracked through governance.",
     "Recording the non-conformance and asking for a formal dispensation is correct in form, but granting it after go-live means the dispensation does not actually constrain the deviation it is meant to govern — partial credit.",
     "C220 Part 1, ch. 10 (Phase G); Part 5 (Architecture Governance: Dispensations)"),
    # t6  Change Management / Phase H — new regulated product line
    ("Classify the change as Incremental and update the affected portions of the existing architecture in place, on the basis that the new product line can be modelled as additional capabilities, processes and data inside the current architecture.",
     "Using Phase H change classification is correct, but classifying a new regulated product line with new partners and compliance as Incremental understates its scope; the right classification is Re-architecting — partial credit.",
     "C220 Part 1, ch. 11 (Phase H: Change Classification)"),
    # t7  Requirements Management / Central
    ("Raise the new mandate through the central Requirements Management process; update the in-progress Phase C deliverables; and schedule the impact assessment on the previously baselined Phase B deliverables as a separate work item to be carried out by the architecture team after the current phase completes.",
     "Using Requirements Management and assessing Phase B impact is correct, but deliberately deferring the Phase B re-validation knowingly leaves a temporary compliance gap that should be closed under the same change — partial credit.",
     "C220 Part 1, ch. 12 (Requirements Management)"),
    # t8  Enterprise Continuum / Repository — bespoke build duplicating IAM
    ("Direct the team to the existing ABB and SBB and ask them to extend the existing Solution Building Block with whatever capability they feel is missing, without requiring a formal dispensation or governance assessment for the extension.",
     "Pointing the team at the existing repository asset is the right reuse instinct, but allowing them to extend it freely without governance bypasses the architecture process and risks degrading a proven, governed asset — partial credit.",
     "C220 Part 5 (Enterprise Continuum / Architecture Repository); Part 4 §5 (Building Blocks)"),
    # t9  Governance — Architecture Board bottleneck
    ("Keep the existing rule that the Architecture Board reviews every decision but increase the Board's meeting frequency and add additional members to clear the backlog more quickly.",
     "Adding capacity is at least a recognition that the bottleneck must be addressed, but it does not change the fundamental policy of universal approval and so reproduces the bottleneck as soon as load grows again — partial credit.",
     "C220 Part 5 (EA Capability and Governance: Architecture Board)"),
    # t10 Preliminary & Tailoring
    ("Run a textbook Preliminary Phase exactly as the Standard describes, producing every recommended artifact and deliverable in full, and ask the delivery teams to comply with the resulting governance once it is published.",
     "Running the Preliminary Phase is correct and would establish the capability, but skipping the tailoring step the Preliminary Phase explicitly mandates ignores the organisation's agile and regulatory context and is likely to provoke the leadership resistance the architect must avoid — partial credit.",
     "C220 Part 1, ch. 2 (Preliminary); Part 3 (Applying the ADM: Tailoring)"),
    # t11 Security & Risk — bolt-on history
    ("Plan two security checkpoint reviews — one in late Phase B/C and one before go-live — to catch security issues earlier than the previous end-of-programme review.",
     "Earlier scheduled checkpoints are an improvement on a single end-of-programme review, but periodic checkpoints still treat security as something inspected rather than designed-in across every ADM phase — partial credit.",
     "TOGAF Series Guide G152 (Integrating Risk and Security within a TOGAF EA); C220 Part 2 Ch. 8 (Risk Management)"),
    # t12 Architecture Partitioning — diversified conglomerate
    ("Partition by business unit and let each unit develop its own architecture independently; require the units to share their finished architectures with each other afterwards so that overlap is discovered and discussed at group level after the fact.",
     "Partitioning along business-unit boundaries is the right TOGAF instinct, but discovering overlap after each unit has independently designed and decided ignores group-level coherence, reuse, and conflict resolution that partitioning is supposed to enable — partial credit.",
     "C220 Part 3 (Architecture Partitioning)"),
    # t13 Stakeholder Management — regulator
    ("Add the regulator to the Stakeholder Map at low engagement level and brief the regulator only at major milestones, so that the regulator is formally included but the sponsor's preferred pace is not slowed.",
     "Including the regulator in the Stakeholder Map at all is correct, but classifying a regulator whose concerns could block go-live as a low-engagement stakeholder under-rates the stakeholder and exposes the engagement to the very risk the architect identified — partial credit.",
     "C220 Part 2, ch. 3 (Stakeholder Management)"),
    # t14 Application Architecture / Phase C — overlapping SaaS
    ("Develop the Target Application Architecture, map proposed products onto it, and recommend the single SaaS product that covers the largest share of the end-to-end process; allow that product to be extended over time to cover the remaining functions.",
     "Defining the Target Application Architecture and mapping products is correct, and picking the broadest-coverage product is a defensible starting point, but committing to a single product without quantifying its gaps risks lock-in and ignores stakeholder coverage — partial credit.",
     "C220 Part 1, ch. 6 (Phase C: Application); Part 4 (Content Framework)"),
    # t15 Value & Benefits / Phase B — CFO challenge
    ("Provide the CFO with a list of the business capabilities the programme will affect, but stop short of tying each proposed investment to the specific capabilities, value-stream stages and outcomes it improves.",
     "Naming the affected capabilities is the right Business Architecture vocabulary, but stopping short of the investment-to-capability-to-outcome traceability the CFO has explicitly demanded leaves the value case incomplete — partial credit.",
     "C220 Part 2 (Business Architecture: Capabilities, Value Streams); Part 1 ch. 4 (Phase B)"),
]

# Sanity: must match L2_TEMPLATES exactly so the per-template lookup is safe
assert len(L2_THIRD_AND_REF) == len(L2_TEMPLATES), \
    "L2_THIRD_AND_REF must have one entry per L2 template"


# Per-template gradient correction. The verification pass against C220 found
# that for these 9 templates the original `second` option (intended for 3 pts)
# is actually a more obvious anti-pattern than the newly authored 1-pt
# `third_text` option. We swap their scores so the 1-pt option carries the
# higher partial credit and the originally-3-pt option scores 1.
# (Indices match L2_TEMPLATES positions; see verification report.)
L2_GRADIENT_SWAP = {1, 7, 9, 10, 11, 12, 13, 14, 15}


def build_level2():
    questions = []
    qid = 1
    n_templates = len(L2_TEMPLATES)
    # Generate ~128 by pairing templates with org names; each combination yields
    # a unique, well-formed scenario. We iterate until we reach 128.
    combos = []
    for t_idx in range(n_templates):
        for o_idx in range(len(ORG_NAMES)):
            combos.append((t_idx, o_idx))
    random.shuffle(combos)

    used = set()
    for t_idx, o_idx in combos:
        if len(questions) >= 128:
            break
        key = (t_idx, o_idx)
        if key in used:
            continue
        used.add(key)
        (topic, phase, context, situation, qtext, best, second, zero1, zero2,
         rb, rs, rz1, rz2) = L2_TEMPLATES[t_idx]
        third_text, third_rationale, reference = L2_THIRD_AND_REF[t_idx]
        org = ORG_NAMES[o_idx]
        desc = ORG_DESCRIPTORS[o_idx]
        # Multi-paragraph Practitioner-style scenario: context, situation, question.
        scenario = (
            f"**{org}** is {desc} that {context}\n\n"
            f"{situation}\n\n"
            f"{qtext}"
        )


        # Build options with the official OGEA-102 5 / 3 / 1 / 0 gradient
        # (best=5, second-best=3, third-best=1, distractor=0). The two zeros
        # from the original template are collapsed: the more plausible of the
        # two becomes the second-best (already in `second`), and a newly
        # authored third-best option is added with a 1-point rationale.
        # `zero2` is dropped to keep four options total (one true distractor
        # plus three graduated good-faith answers).
        # If verification flagged this template as having an invertible 3/1
        # ordering, swap their scores so the more TOGAF-aligned option earns
        # 3 pts and the weaker original option earns 1 pt.
        if t_idx in L2_GRADIENT_SWAP:
            second_score, third_score = 1, 3
            second_tag = "Third-best (1 pt)"
            third_tag = "Second-best (3 pts)"
        else:
            second_score, third_score = 3, 1
            second_tag = "Second-best (3 pts)"
            third_tag = "Third-best (1 pt)"
        opts = [
            {"text": best,        "score": 5,            "rationale": rb,              "tag": "Best (full marks)"},
            {"text": second,      "score": second_score, "rationale": rs,              "tag": second_tag},
            {"text": third_text,  "score": third_score,  "rationale": third_rationale, "tag": third_tag},
            {"text": zero1,       "score": 0,            "rationale": rz1,             "tag": "Distractor (0 pts)"},
        ]
        random.shuffle(opts)
        best_index = next(i for i, o in enumerate(opts) if o["score"] == 5)
        questions.append({
            "id": f"L2-{qid:03d}",
            "level": 2,
            "topic": topic,
            "phase": phase,
            "question": scenario,
            "options": [o["text"] for o in opts],
            "scores": [o["score"] for o in opts],
            "rationales": [o["rationale"] for o in opts],
            "tags": [o["tag"] for o in opts],
            "answer": best_index,  # the full-marks option
            "maxScore": 5,
            "reference": reference,
        })
        qid += 1
    return questions[:128]


def main():
    l1 = build_level1()
    l2 = build_level2()

    bank1 = {"level": 1, "title": "TOGAF EA Foundation (Level 1)", "count": len(l1), "questions": l1}
    bank2 = {"level": 2, "title": "TOGAF EA Practitioner (Level 2)", "count": len(l2), "questions": l2}

    # JSON copies (for reference / server use)
    with open(os.path.join(OUT_DIR, "questions_level1.json"), "w", encoding="utf-8") as f:
        json.dump(bank1, f, indent=2, ensure_ascii=False)
    with open(os.path.join(OUT_DIR, "questions_level2.json"), "w", encoding="utf-8") as f:
        json.dump(bank2, f, indent=2, ensure_ascii=False)

    # JS copies so the app runs from file:// with NO server (loaded via <script>)
    with open(os.path.join(OUT_DIR, "questions_level1.js"), "w", encoding="utf-8") as f:
        f.write("window.TOGAF_BANK_1 = " + json.dumps(bank1, ensure_ascii=False) + ";\n")
    with open(os.path.join(OUT_DIR, "questions_level2.js"), "w", encoding="utf-8") as f:
        f.write("window.TOGAF_BANK_2 = " + json.dumps(bank2, ensure_ascii=False) + ";\n")

    print(f"Wrote {len(l1)} Level 1 and {len(l2)} Level 2 questions (.json + .js) to {OUT_DIR}")



if __name__ == "__main__":
    main()
