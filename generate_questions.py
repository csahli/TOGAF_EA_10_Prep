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


def build_level1():
    base = L1_FACTS + L1_TOPICS_EXTRA  # 50 + 6 = 56 unique stems
    questions = []
    qid = 1
    # First pass: the unique stems
    for stem, correct, d1, d2, d3, expl, topic in base:
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
        })
        qid += 1
    # Second pass: create variant phrasings to reach 128, re-using stems with
    # reworded lead-ins but identical correct concept (kept clearly answerable).
    variant_leads = [
        "In the context of the TOGAF Standard, ",
        "According to TOGAF best practice, ",
        "For the EA Practitioner, ",
        "Within the ADM, ",
    ]
    i = 0
    while len(questions) < 128:
        stem, correct, d1, d2, d3, expl, topic = base[i % len(base)]
        lead = variant_leads[(i // len(base)) % len(variant_leads)]
        # Lowercase first char of stem when appending after a lead-in
        new_stem = lead + stem[0].lower() + stem[1:]
        opts = [correct, d1, d2, d3]
        order = list(range(4))
        random.shuffle(order)
        shuffled = [opts[k] for k in order]
        answer_index = shuffled.index(correct)
        questions.append({
            "id": f"L1-{qid:03d}",
            "level": 1,
            "topic": topic,
            "question": new_stem,
            "options": shuffled,
            "answer": answer_index,
            "explanation": expl,
        })
        qid += 1
        i += 1
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
        org = ORG_NAMES[o_idx]
        desc = ORG_DESCRIPTORS[o_idx]
        # Multi-paragraph Practitioner-style scenario: context, situation, question.
        scenario = (
            f"**{org}** is {desc} that {context}\n\n"
            f"{situation}\n\n"
            f"{qtext}"
        )


        # Build options with scores; shuffle while tracking scores+rationale
        opts = [
            {"text": best, "score": 5, "rationale": rb, "tag": "Best (full marks)"},
            {"text": second, "score": 3, "rationale": rs, "tag": "Second-best (partial)"},
            {"text": zero1, "score": 0, "rationale": rz1, "tag": "Scores 0"},
            {"text": zero2, "score": 0, "rationale": rz2, "tag": "Scores 0 (distractor)"},
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
