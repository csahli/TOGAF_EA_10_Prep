/* TOGAF EA Practitioner — Supplemental Question Bank
 * Aligned to the X2202 Conformance Requirements (Multi-Level) syllabus.
 * Loaded AFTER questions_level1.js and questions_level2.js so it can append
 * directly into the existing window.TOGAF_BANK_1.questions and
 * window.TOGAF_BANK_2.questions arrays without touching the originals.
 *
 * Focus areas (syllabus units that were under-represented in the base banks):
 *   Level 1:
 *     - Unit 4 (ADM Techniques): Business Transformation Readiness, Business
 *       Scenarios, Risk, Interoperability, Security as a cross-cutting concern.
 *     - Unit 5 (Applying the ADM): Iteration cycles, Architecture Landscape
 *       levels (Strategic/Segment/Capability), Partitioning, Digital/Agile.
 *     - Unit 7 (Architecture Content): Repository structure parts, metamodel,
 *       taxonomy, Implementation Factor Catalog, three implementation approaches.
 *     - Unit 6 (Governance): Architecture Contracts, compliance levels,
 *       dispensations.
 *   Level 2 (Practitioner — gradient-scored scenarios):
 *     - Phase A application, Stakeholder Management, work-package grouping,
 *       Transition Architectures, Architecture Contracts, change classification,
 *       Requirements Management impact analysis, repository reuse, iteration
 *       selection, risk assessment.
 *
 * Scoring convention for Level 2 (matches app.js handling): `answer` is the
 * BEST option (full marks). Partial-credit and distractor reasoning is included
 * in the explanation text so learners see why other options score less.
 */
(function () {
  "use strict";

  // -------------------------- Level 1 supplemental --------------------------
  var L1_NEW = [
    {
      id: "L1-S01",
      level: 1,
      topic: "ADM Techniques",
      question:
        "What is the primary purpose of a Business Transformation Readiness Assessment?",
      options: [
        "To audit project budgets",
        "To assess the organization's preparedness to undertake the change implied by the target architecture",
        "To select cloud vendors",
        "To replace the Architecture Vision"
      ],
      answer: 1,
      explanation:
        "Business Transformation Readiness Assessment identifies factors (e.g., vision, desire, need, business case, funding, sponsorship, governance, accountability, workable approach, IT capacity, enterprise capacity to implement and operate) that affect the organization's ability to absorb the change."
    },
    {
      id: "L1-S02",
      level: 1,
      topic: "ADM Techniques",
      question: "What is a Business Scenario used for in the ADM?",
      options: [
        "To replace the Statement of Architecture Work",
        "To define stakeholders, business processes, technology environment, desired outcomes and SMART objectives that drive the architecture",
        "To run penetration tests",
        "To approve invoices"
      ],
      answer: 1,
      explanation:
        "Business Scenarios (G176) capture the business problem and requirements: actors, processes, technology, desired outcomes and SMART objectives — typically used in Phase A to ground the Architecture Vision."
    },
    {
      id: "L1-S03",
      level: 1,
      topic: "Security Architecture",
      question:
        "How does TOGAF treat security in the architecture development?",
      options: [
        "As a separate framework that replaces the ADM",
        "Only in Phase D after technology is selected",
        "As a cross-cutting concern integrated across all ADM phases",
        "As an optional add-on for regulated industries"
      ],
      answer: 2,
      explanation:
        "Security is a cross-cutting concern that must be considered in every ADM phase, not just in Phase D. Security stakeholders, requirements and controls thread through Vision, Business, Data, Application, Technology, Opportunities & Solutions, Migration, Governance and Change Management."
    },
    {
      id: "L1-S04",
      level: 1,
      topic: "Architecture Landscape",
      question:
        "Which three levels of architecture are typically used to organize the Architecture Landscape?",
      options: [
        "Vision, Build, Run",
        "Strategic, Segment, Capability",
        "Business, Data, Technology",
        "Baseline, Transition, Target"
      ],
      answer: 1,
      explanation:
        "The Architecture Landscape is partitioned by architecture levels: Strategic (broad, long term, low detail), Segment (a coherent area of the business), and Capability (specific capability with enough detail to deliver)."
    },
    {
      id: "L1-S05",
      level: 1,
      topic: "Iteration",
      question:
        "Which iteration cycle within the ADM repeatedly executes Phases B, C and D to develop the target architectures?",
      options: [
        "Architecture Context iteration",
        "Architecture Definition iteration",
        "Transition Planning iteration",
        "Architecture Governance iteration"
      ],
      answer: 1,
      explanation:
        "The Architecture Definition iteration cycles through Phases B, C and D (Business, Data/Application, Technology) to elaborate and refine the target architectures. Context iterations focus on Preliminary and Phase A; Transition Planning iterates E and F; Governance iterates G and H."
    },
    {
      id: "L1-S06",
      level: 1,
      topic: "Iteration",
      question:
        "Which iteration cycle iterates between Phases E (Opportunities & Solutions) and F (Migration Planning)?",
      options: [
        "Architecture Context iteration",
        "Architecture Definition iteration",
        "Transition Planning iteration",
        "Requirements iteration"
      ],
      answer: 2,
      explanation:
        "Transition Planning iterations iterate between Phase E and Phase F to consolidate work packages, define Transition Architectures and finalize the Implementation and Migration Plan."
    },
    {
      id: "L1-S07",
      level: 1,
      topic: "Architecture Repository",
      question:
        "Which part of the TOGAF Architecture Repository holds reusable, generic guidance such as reference models and patterns?",
      options: [
        "Architecture Landscape",
        "Reference Library",
        "Governance Repository",
        "Solutions Landscape"
      ],
      answer: 1,
      explanation:
        "The Reference Library holds generic, reusable guidance and templates (e.g., reference models, patterns) that can be tailored to specific architectures."
    },
    {
      id: "L1-S08",
      level: 1,
      topic: "Architecture Repository",
      question:
        "Which part of the TOGAF Architecture Repository records calendars, agendas, meeting minutes, decisions and dispensations?",
      options: [
        "Standards Library",
        "Solutions Landscape",
        "Governance Repository",
        "Reference Library"
      ],
      answer: 2,
      explanation:
        "The Governance Repository records governance activity: schedules, agendas, decisions, compliance assessments, dispensations and project compliance status."
    },
    {
      id: "L1-S09",
      level: 1,
      topic: "Architecture Repository",
      question:
        "Which part of the TOGAF Architecture Repository contains the standards (technical, business, regulatory) the enterprise has committed to comply with?",
      options: [
        "Reference Library",
        "Standards Library",
        "Architecture Requirements Repository",
        "Enterprise Repository"
      ],
      answer: 1,
      explanation:
        "The Standards Library holds the standards the enterprise must conform to, providing the basis for compliance reviews."
    },
    {
      id: "L1-S10",
      level: 1,
      topic: "Architecture Repository",
      question:
        "Where in the TOGAF repository are all authorized architecture requirements held?",
      options: [
        "Solutions Landscape",
        "Architecture Requirements Repository",
        "Governance Repository",
        "Reference Library"
      ],
      answer: 1,
      explanation:
        "The Architecture Requirements Repository holds the authoritative set of architecture requirements that have been agreed with stakeholders."
    },
    {
      id: "L1-S11",
      level: 1,
      topic: "Implementation Approaches",
      question:
        "Which is NOT one of the three basic implementation approaches considered in Phase E?",
      options: [
        "Greenfield (new development)",
        "Revolutionary (radical, large-scale change)",
        "Evolutionary (incremental change)",
        "Outsourcing the entire architecture function"
      ],
      answer: 3,
      explanation:
        "The TOGAF Standard discusses three implementation approaches in Phase E: Greenfield, Revolutionary, and Evolutionary. Outsourcing the architecture function is not a TOGAF implementation approach."
    },
    {
      id: "L1-S12",
      level: 1,
      topic: "Implementation Factor Catalog",
      question:
        "What is the purpose of the Consolidated Gaps, Solutions and Dependencies Matrix?",
      options: [
        "To track employee performance",
        "To consolidate gap-analysis results, candidate solutions and dependencies as input to defining work packages and Transition Architectures",
        "To define stakeholder salaries",
        "To replace the Architecture Vision"
      ],
      answer: 1,
      explanation:
        "Used in Phase E migration planning, this matrix consolidates the gaps identified in Phases B/C/D with potential solution building blocks and their dependencies, so the team can identify and group work packages."
    },
    {
      id: "L1-S13",
      level: 1,
      topic: "Architecture Contracts",
      question:
        "What is the primary purpose of an Architecture Contract in Phase G?",
      options: [
        "To set employee salaries",
        "To formally bind the implementation team to the architecture, defining deliverables, quality and acceptance criteria, and conformance requirements",
        "To replace the Architecture Definition Document",
        "To remove governance"
      ],
      answer: 1,
      explanation:
        "Architecture Contracts ensure implementation conforms to the target architecture. They define deliverables, schedule, acceptance criteria, and risk/conformance obligations for both architecture and development teams."
    },
    {
      id: "L1-S14",
      level: 1,
      topic: "Compliance",
      question:
        "Which is a recognized level of architecture compliance used in compliance assessments?",
      options: [
        "Irrelevant",
        "Compliant",
        "Approximately compliant",
        "Vendor-approved"
      ],
      answer: 1,
      explanation:
        "TOGAF defines levels including Irrelevant, Consistent, Compliant, Conformant, Fully Conformant and Non-conformant. 'Compliant' is one such recognized level. 'Vendor-approved' is not a TOGAF compliance level."
    },
    {
      id: "L1-S15",
      level: 1,
      topic: "Change Management",
      question:
        "Which three categories does TOGAF use to classify architecture change in Phase H?",
      options: [
        "Red, Amber, Green",
        "Simplification, Incremental, and Re-architecting",
        "Strategic, Tactical, Operational",
        "Mandatory, Optional, Deferred"
      ],
      answer: 1,
      explanation:
        "Phase H classifies change drivers as: Simplification (reduces investment), Incremental (small additions, handled by change request), or Re-architecting (significant; triggers a new ADM cycle)."
    },
    {
      id: "L1-S16",
      level: 1,
      topic: "Metamodel",
      question:
        "What is the role of the TOGAF Enterprise Metamodel within the Content Framework?",
      options: [
        "To define a single mandatory schema for vendor products",
        "To define the types of entities and relationships used to describe an architecture consistently",
        "To replace the ADM",
        "To set employee salaries"
      ],
      answer: 1,
      explanation:
        "The Enterprise Metamodel defines the entities (e.g., capability, value stream, application component, data entity, technology component) and relationships used to describe architectures in a consistent, queryable way."
    },
    {
      id: "L1-S17",
      level: 1,
      topic: "Taxonomy",
      question:
        "Why is a taxonomy used in conjunction with the Architecture Content Framework?",
      options: [
        "To classify architecture content so it can be consistently catalogued, found and reused",
        "To remove governance",
        "To delete the repository",
        "To define stakeholder salaries"
      ],
      answer: 0,
      explanation:
        "A taxonomy classifies architectural content (e.g., applications by type, technology by category) supporting consistent cataloguing, discovery and reuse across the Architecture Repository."
    },
    {
      id: "L1-S18",
      level: 1,
      topic: "Risk Management",
      question:
        "In TOGAF, what is the difference between initial-level and residual-level risk?",
      options: [
        "They are the same thing",
        "Initial-level risk is before mitigation; residual-level risk is what remains after mitigating actions",
        "Residual-level risk is identified only after go-live",
        "Initial-level risk is only financial"
      ],
      answer: 1,
      explanation:
        "Initial (or inherent) risk is assessed before mitigation. Residual risk is what remains after mitigating actions have been planned/applied. Both are tracked through the ADM."
    },
    {
      id: "L1-S19",
      level: 1,
      topic: "Architecture Partitioning",
      question:
        "Which of the following is a valid criterion for architecture partitioning?",
      options: [
        "Color scheme",
        "Subject matter (e.g., business domain, capability)",
        "Marketing campaign",
        "Office location only"
      ],
      answer: 1,
      explanation:
        "Architectures can be partitioned by breadth (subject matter / domain), depth (level of detail), time (Baseline, Transition, Target) and maturity, among other criteria."
    },
    {
      id: "L1-S20",
      level: 1,
      topic: "Digital Enterprise",
      question:
        "How does TOGAF position Enterprise Architecture in a Digital or Agile enterprise?",
      options: [
        "EA is abandoned in agile contexts",
        "EA is tailored to provide just-enough, just-in-time guidance and works alongside agile/product delivery to manage risk and coherence",
        "EA must always run in a single waterfall pass",
        "EA prevents the use of agile teams"
      ],
      answer: 1,
      explanation:
        "TOGAF explicitly supports tailoring the ADM, applying iteration and partitioning so EA delivers just-enough guidance just-in-time, complementing agile/product-oriented delivery."
    },
    {
      id: "L1-S21",
      level: 1,
      topic: "Phase A",
      question:
        "Which Phase A output describes the high-level aspirations and value of the target architecture for stakeholders?",
      options: [
        "Architecture Contract",
        "Implementation and Migration Plan",
        "Architecture Vision",
        "Compliance Assessment"
      ],
      answer: 2,
      explanation:
        "The Architecture Vision is a Phase A deliverable that provides a first, high-level description of the Baseline and Target Architectures and the value to stakeholders, used to secure sponsor approval."
    },
    {
      id: "L1-S22",
      level: 1,
      topic: "Stakeholder Management",
      question:
        "Which technique helps classify stakeholders so engagement effort can be focused appropriately?",
      options: [
        "Gap analysis",
        "Power/Interest (influence/interest) grid",
        "Compliance assessment",
        "Dispensation"
      ],
      answer: 1,
      explanation:
        "A Power/Interest (or Influence/Interest) grid is a recognized stakeholder-analysis technique used to prioritize engagement and tailor communications."
    },
    {
      id: "L1-S23",
      level: 1,
      topic: "Phase E",
      question:
        "How is business value typically assigned to work packages in Phase E?",
      options: [
        "By alphabetical order",
        "By assessing the value, risk and dependencies of each work package against the Architecture Vision and business drivers",
        "By cost only",
        "By vendor preference"
      ],
      answer: 1,
      explanation:
        "Phase E assigns business value to work packages by evaluating contribution to the Vision and business drivers, balanced against risk and dependencies, to inform sequencing in Phase F."
    },
    {
      id: "L1-S24",
      level: 1,
      topic: "Capabilities",
      question:
        "What is a capability heat map used for?",
      options: [
        "To monitor data-center temperature",
        "To visualize, against the capability map, which capabilities most need investment, attention or change",
        "To rank employees",
        "To set stakeholder salaries"
      ],
      answer: 1,
      explanation:
        "A heat map overlays performance, value-contribution, risk or investment-priority data onto the business capability map to focus EA decisions."
    },
    {
      id: "L1-S25",
      level: 1,
      topic: "Value Streams",
      question:
        "How do value streams typically relate to business capabilities?",
      options: [
        "Value streams replace capabilities",
        "Each stage of a value stream is enabled by one or more business capabilities",
        "Capabilities are subordinate to projects, not value streams",
        "Value streams and capabilities are unrelated"
      ],
      answer: 1,
      explanation:
        "A value stream models end-to-end value delivery in stages; each stage is enabled (and constrained) by specific business capabilities, making the value-stream/capability cross-map a core Business Architecture artifact."
    }
  ];

  // -------------------------- Level 2 supplemental --------------------------
  // Scenario items (gradient-style). `answer` = BEST option. Explanations
  // include the partial-credit and distractor reasoning so learners see why
  // each option scores as it does.
  var L2_NEW = [
    {
      id: "L2-S01",
      level: 2,
      topic: "Phase A — Stakeholders",
      question:
        "Scenario: You are leading Phase A for a multinational insurer. The CIO sponsor wants a recommendation in 4 weeks. Three regional COOs each have conflicting KPIs and openly doubt that one platform can serve all regions. What is the BEST next step?",
      options: [
        "Skip to detailed Phase B modeling of all three regions before engaging the COOs.",
        "Build a Stakeholder Map, capture each COO's drivers and concerns, and produce an Architecture Vision and Statement of Architecture Work that explicitly address the conflicts, securing sponsor approval before proceeding.",
        "Ask the CIO to remove the regional COOs from the decision process to avoid delays.",
        "Log the conflicts in the Architecture Requirements Specification and continue Phase A without resolving them."
      ],
      answer: 1,
      explanation:
        "BEST: Phase A is about scoping, stakeholders and a sponsor-endorsed vision; the Stakeholder Map + Vision + SoAW is the textbook approach. PARTIAL: Logging in the Requirements Spec gives traceability but ignores stakeholder management. DISTRACTORS: Skipping straight to Phase B detail and removing stakeholders both bypass governance and will cause rework."
    },
    {
      id: "L2-S02",
      level: 2,
      topic: "Repository Reuse",
      question:
        "Scenario: A new project team plans to build a custom customer-authentication service. Your Architecture Repository already contains a governed ABB and matching SBB for identity. What is the BEST course of action?",
      options: [
        "Allow the team to build their own service because project autonomy speeds delivery.",
        "Direct the team to the existing ABB/SBB and require any deviation to be justified through the Architecture Governance process.",
        "Let the team build, then add their custom service to the repository regardless of overlap.",
        "Remove the existing ABB from the repository to avoid confusion."
      ],
      answer: 1,
      explanation:
        "BEST: Reuse via the Enterprise Continuum/Repository plus governed deviation is the core EA value mechanism. PARTIAL: Capturing the new build at least preserves traceability but creates duplication and weakens governance. DISTRACTORS: Allowing parallel custom builds or deleting the ABB both undermine the architecture practice."
    },
    {
      id: "L2-S03",
      level: 2,
      topic: "Phase E — Work Packages",
      question:
        "Scenario: A Target Architecture is approved. The full transformation is 18 months but the business wants visible value early. You are in Phase E. What is the BEST way to structure delivery?",
      options: [
        "Deliver the whole Target in one big-bang release at month 18 to minimize integration complexity.",
        "Define Transition Architectures, group work into work packages that each deliver a capability increment, and feed the sequence into the Implementation and Migration Plan in Phase F.",
        "Start implementation immediately with the largest, riskiest component and defer planning.",
        "Define a single Transition Architecture covering only the easy work and defer everything else indefinitely."
      ],
      answer: 1,
      explanation:
        "BEST: Transition Architectures + work packages → sequenced in Phase F is exactly what Phase E is for. PARTIAL: One small Transition uses the right concept but doesn't deliver the Target. DISTRACTORS: Big-bang and 'start with the hardest, plan later' both ignore TOGAF migration-planning guidance."
    },
    {
      id: "L2-S04",
      level: 2,
      topic: "Phase H — Change Classification",
      question:
        "Scenario: 18 months after go-live, the business launches a new product line not anticipated by the current architecture. A change request reaches the Architecture Board. What is the BEST response per Phase H?",
      options: [
        "Reject all changes to preserve architectural integrity.",
        "Assess the change to classify it as Simplification, Incremental or Re-architecting, and route it accordingly — initiating a new ADM cycle if it is Re-architecting.",
        "Apply the change directly to production without architecture assessment to meet the deadline.",
        "Log the change for an annual review only."
      ],
      answer: 1,
      explanation:
        "BEST: Phase H explicitly classifies change drivers and decides whether a new ADM iteration is needed. PARTIAL: Logging captures it but defers needed assessment. DISTRACTORS: Blanket rejection or bypassing the Board both break governance."
    },
    {
      id: "L2-S05",
      level: 2,
      topic: "Requirements Management",
      question:
        "Scenario: Midway through Phase C, a new data-retention regulation appears that also impacts work completed in Phase B. What is the BEST handling?",
      options: [
        "Ignore it until the current phase completes to avoid rework.",
        "Feed the requirement into the central Requirements Management process, assess its impact across all affected phases, and re-validate Phase B deliverables as needed.",
        "Add it only to Phase C deliverables because that's the current phase.",
        "Restart the entire ADM cycle from Phase A."
      ],
      answer: 1,
      explanation:
        "BEST: Requirements Management is the continuous central process; it must drive cross-phase impact analysis. PARTIAL: Capturing it only in Phase C addresses today but loses traceability. DISTRACTORS: Ignoring it or restarting from Phase A are both disproportionate or non-conformant."
    },
    {
      id: "L2-S06",
      level: 2,
      topic: "Phase G — Architecture Contracts",
      question:
        "Scenario: Implementation has started. A vendor delivery team is interpreting the Target Architecture loosely and adopting different technology choices in two work packages. What is the BEST Phase G response?",
      options: [
        "Allow the deviations since the vendor is delivering on time.",
        "Use the Architecture Contract as the basis for a compliance assessment; require remediation or a formal dispensation with conditions and a remediation plan.",
        "Cancel both work packages and restart Phase E.",
        "Quietly update the Target Architecture to match what the vendor is doing."
      ],
      answer: 1,
      explanation:
        "BEST: Phase G governs implementation; Architecture Contracts + compliance assessments + dispensations are the precise tools. PARTIAL/DISTRACTOR: Cancelling work is disproportionate; allowing drift or silently rewriting the Target both bypass governance and the Architecture Board."
    },
    {
      id: "L2-S07",
      level: 2,
      topic: "Iteration Selection",
      question:
        "Scenario: Your enterprise is mid-transformation. Stakeholders keep adding new scope and the team is repeatedly revisiting Phases B–D. Which iteration cycle should you formally adopt to manage this?",
      options: [
        "Architecture Context iteration only.",
        "Architecture Definition iteration — explicitly plan repeated passes through Phases B, C and D with managed scope.",
        "Stop iterating; complete the ADM strictly once.",
        "Skip Phase C in subsequent passes to save time."
      ],
      answer: 1,
      explanation:
        "BEST: The Architecture Definition iteration is designed precisely for repeated, managed passes through B/C/D. PARTIAL/DISTRACTOR: Context iterations address Preliminary/A. Forbidding iteration or skipping Phase C contradict the TOGAF approach."
    },
    {
      id: "L2-S08",
      level: 2,
      topic: "Architecture Levels",
      question:
        "Scenario: The CIO asks for an enterprise-wide IT-strategy view spanning 5 years with high-level capability and technology direction. At which architecture level should you develop this?",
      options: [
        "Capability-level architecture with full design detail",
        "Strategic-level architecture, broad scope, lower level of detail, longer horizon",
        "Segment-level architecture for a single business unit only",
        "No architecture is needed at this scope"
      ],
      answer: 1,
      explanation:
        "BEST: Strategic-level architectures cover broad scope and longer horizons at a deliberately lower level of detail. PARTIAL/DISTRACTOR: Capability-level (deep detail) and Segment-level (one area) don't match enterprise-wide strategy; 'no architecture' is wrong."
    },
    {
      id: "L2-S09",
      level: 2,
      topic: "Risk Assessment",
      question:
        "Scenario: A migration plan carries a high initial risk from data-quality issues. Mitigations are planned but cannot be fully validated until pilot. What is the BEST way to communicate this in Phase F?",
      options: [
        "Report only the initial risk because mitigations are not yet proven.",
        "Record both the initial and the expected residual risk after mitigation, with clear assumptions, and surface the residual risk to the sponsor for an explicit decision.",
        "Report only the residual risk to avoid alarming stakeholders.",
        "Omit the risk from the plan until the pilot completes."
      ],
      answer: 1,
      explanation:
        "BEST: TOGAF distinguishes initial and residual risk; both should be made visible with mitigations and assumptions so sponsors can make an informed decision. DISTRACTORS: Showing only one side or omitting risk breaks governance."
    },
    {
      id: "L2-S10",
      level: 2,
      topic: "Business Scenarios — Phase A",
      question:
        "Scenario: Stakeholders cannot agree on what problem the architecture is meant to solve. As Lead Architect, which technique is BEST to anchor Phase A?",
      options: [
        "Skip to defining a Target Technology Architecture to force a discussion.",
        "Develop a Business Scenario capturing actors, processes, technology environment, desired outcomes and SMART objectives, then use it to align stakeholders and the Architecture Vision.",
        "Ask the sponsor to choose one stakeholder's view to be the official requirement.",
        "Defer the engagement until stakeholders pre-agree."
      ],
      answer: 1,
      explanation:
        "BEST: Business Scenarios (G176) are designed for exactly this — aligning stakeholders on problem, outcomes and SMART objectives at Vision time. DISTRACTORS: Jumping to technology, picking a single voice, or deferring all bypass stakeholder management and TOGAF technique."
    },
    {
      id: "L2-S11",
      level: 2,
      topic: "Phase E — Implementation Approach",
      question:
        "Scenario: A bank must replace a 30-year-old core system. The Target is approved. Risk appetite is moderate; the business depends on continuous service. Which implementation approach is BEST?",
      options: [
        "Greenfield, building everything new in parallel with no integration.",
        "Evolutionary — incremental delivery of Transition Architectures that progressively replace existing capability while keeping service running.",
        "Revolutionary — switch off the legacy core in a single weekend cutover.",
        "Outsource the architecture function to the vendor."
      ],
      answer: 1,
      explanation:
        "BEST: Evolutionary delivery via Transition Architectures suits moderate-risk, must-stay-up transformations. PARTIAL/DISTRACTOR: Pure Greenfield ignores integration realities; Revolutionary big-bang is high-risk; outsourcing the architecture function is not a TOGAF implementation approach."
    },
    {
      id: "L2-S12",
      level: 2,
      topic: "Governance — Dispensation",
      question:
        "Scenario: A delivery team needs to use a non-standard database for a 6-month pilot due to a regulator pilot programme. They acknowledge they will need to migrate later. What is the BEST governance action?",
      options: [
        "Permanently change the Standards Library to add the non-standard database.",
        "Grant a time-bound dispensation with conditions, a remediation plan and a review date, recorded in the Governance Repository.",
        "Refuse and force them to delay the regulator pilot.",
        "Allow the deviation informally; do not record it."
      ],
      answer: 1,
      explanation:
        "BEST: Dispensations are exactly the mechanism for controlled, time-bound, conditional deviation, recorded for review. DISTRACTORS: Permanently weakening the standard, blanket refusal or off-the-record deviation all break governance."
    }
  ];

  // ----------------------- Merge into existing banks -----------------------
  try {
    if (window.TOGAF_BANK_1 && Array.isArray(window.TOGAF_BANK_1.questions)) {
      Array.prototype.push.apply(window.TOGAF_BANK_1.questions, L1_NEW);
      window.TOGAF_BANK_1.count = window.TOGAF_BANK_1.questions.length;
    }
    if (window.TOGAF_BANK_2 && Array.isArray(window.TOGAF_BANK_2.questions)) {
      Array.prototype.push.apply(window.TOGAF_BANK_2.questions, L2_NEW);
      window.TOGAF_BANK_2.count = window.TOGAF_BANK_2.questions.length;
    }
    window.TOGAF_SUPPLEMENT = {
      level1Added: L1_NEW.length,
      level2Added: L2_NEW.length
    };
  } catch (e) {
    // Fail-soft: never break the app if banks are unavailable.
    console && console.warn && console.warn("Supplement load skipped:", e);
  }
})();
