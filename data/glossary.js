/* =========================================================================
   TOGAF EA Practitioner — Glossary / Definitions data
   Core concepts, definitions, and links into the official TOGAF Standard
   (10th Edition) documentation on The Open Group library.
   Loaded as a plain <script>; assigns window.TOGAF_GLOSSARY.

   `doc`     : link to the relevant official TOGAF Standard page.
   `diagram` : optional key matched to an inline SVG in index.html.
   ========================================================================= */
window.TOGAF_GLOSSARY = {
  // Official doc base references (10th Edition, The Open Group library).
  docs: {
    introduction: "https://pubs.opengroup.org/togaf-standard/introduction/",
    adm: "https://pubs.opengroup.org/togaf-standard/adm/",
    admTechniques: "https://pubs.opengroup.org/togaf-standard/adm-techniques/",
    architectureContent: "https://pubs.opengroup.org/togaf-standard/architecture-content/",
    enterpriseConcepts: "https://pubs.opengroup.org/togaf-standard/fundamental-content/",
    library: "https://pubs.opengroup.org/togaf-standard/",
  },

  terms: [
    {
      term: "Enterprise Architecture (EA)",
      category: "Fundamentals",
      definition:
        "A coherent whole of principles, methods, and models used in the design and realization of an enterprise's organizational structure, business processes, information systems, and infrastructure. In TOGAF, EA spans four architecture domains: Business, Data, Application, and Technology.",
      doc: "https://pubs.opengroup.org/togaf-standard/introduction/",
    },
    {
      term: "Architecture Development Method (ADM)",
      category: "ADM",
      definition:
        "The core of the TOGAF Standard: an iterative, step-by-step method for developing and managing the lifecycle of an enterprise architecture. It runs from the Preliminary Phase and Phase A (Architecture Vision) through Phases B–D (the architecture domains), E–F (planning), G (governance), and H (change management), with Requirements Management at the centre.",
      doc: "https://pubs.opengroup.org/togaf-standard/adm/",
      diagram: "adm",
    },
    {
      term: "Preliminary Phase",
      category: "ADM",
      definition:
        "Prepares the organization for a successful architecture project. It defines the architecture capability, tailors the TOGAF framework, establishes architecture principles, and identifies the stakeholders and governance structures.",
      doc: "https://pubs.opengroup.org/togaf-standard/adm/chap04.html",
    },
    {
      term: "Phase A: Architecture Vision",
      category: "ADM",
      definition:
        "Sets the scope, constraints, and expectations for the engagement. Key outputs include the Statement of Architecture Work, a high-level Architecture Vision, identification of stakeholders and their concerns, and confirmation of business goals and drivers.",
      doc: "https://pubs.opengroup.org/togaf-standard/adm/chap05.html",
    },
    {
      term: "Phase B: Business Architecture",
      category: "ADM",
      definition:
        "Develops the Target Business Architecture describing how the enterprise needs to operate to achieve the business goals — covering organization, functions, processes, business capabilities, and services — and performs gap analysis against the baseline.",
      doc: "https://pubs.opengroup.org/togaf-standard/adm/chap06.html",
    },
    {
      term: "Phase C: Information Systems Architectures",
      category: "ADM",
      definition:
        "Develops the Target Data and Application Architectures. The Data Architecture defines the major data types and sources; the Application Architecture defines the application systems needed to process data and support the business.",
      doc: "https://pubs.opengroup.org/togaf-standard/adm/chap07.html",
    },
    {
      term: "Phase D: Technology Architecture",
      category: "ADM",
      definition:
        "Develops the Target Technology Architecture: the logical and physical technology components (platforms, networks, infrastructure, and services) that support deployment of business, data, and application components.",
      doc: "https://pubs.opengroup.org/togaf-standard/adm/chap10.html",
    },
    {
      term: "Phase E: Opportunities & Solutions",
      category: "ADM",
      definition:
        "Generates the first complete version of the Architecture Roadmap, identifies delivery vehicles (work packages), groups changes, and defines Transition Architectures that deliver incremental, value-adding capability.",
      doc: "https://pubs.opengroup.org/togaf-standard/adm/chap11.html",
    },
    {
      term: "Phase F: Migration Planning",
      category: "ADM",
      definition:
        "Finalizes a detailed Implementation and Migration Plan, sequencing the work packages and Transition Architectures, and confirming business value and cost of the transformation.",
      doc: "https://pubs.opengroup.org/togaf-standard/adm/chap12.html",
    },
    {
      term: "Phase G: Implementation Governance",
      category: "ADM",
      definition:
        "Provides architectural oversight of implementation. Establishes Architecture Contracts with delivery teams and ensures projects conform to the target architecture and architecture requirements.",
      doc: "https://pubs.opengroup.org/togaf-standard/adm/chap13.html",
    },
    {
      term: "Phase H: Architecture Change Management",
      category: "ADM",
      definition:
        "Ensures the architecture responds to change in a controlled way. Changes are classified as Simplification, Incremental, or Re-architecting; a re-architecting change triggers a new full ADM cycle.",
      doc: "https://pubs.opengroup.org/togaf-standard/adm/chap14.html",
    },
    {
      term: "Requirements Management",
      category: "ADM",
      definition:
        "The continuous, central process that operates throughout the ADM. It manages architecture requirements — capturing, storing, and feeding them into and out of every phase — but does not itself dispose of or prioritize them; the relevant phases do that.",
      doc: "https://pubs.opengroup.org/togaf-standard/adm/chap15.html",
    },
    {
      term: "Architecture Building Block (ABB)",
      category: "Building Blocks",
      definition:
        "A constituent of the architecture model that describes a single aspect of the overall model. ABBs capture architecture requirements and direct and guide the development of Solution Building Blocks (SBBs). They are typically defined during the architecture (B–D) phases and are technology-aware but not product-specific.",
      doc: "https://pubs.opengroup.org/togaf-standard/architecture-content/",
      diagram: "buildingblocks",
    },
    {
      term: "Solution Building Block (SBB)",
      category: "Building Blocks",
      definition:
        "A candidate physical solution component that realizes one or more Architecture Building Blocks. SBBs are product- or vendor-specific and are defined in Phase E (Opportunities & Solutions).",
      doc: "https://pubs.opengroup.org/togaf-standard/architecture-content/",
      diagram: "buildingblocks",
    },
    {
      term: "Enterprise Continuum",
      category: "Repository",
      definition:
        "A view of the Architecture Repository that provides methods for classifying architecture and solution artifacts as they evolve from generic Foundation Architectures to Organization-Specific Architectures. It comprises the Architecture Continuum and the Solutions Continuum.",
      doc: "https://pubs.opengroup.org/togaf-standard/fundamental-content/",
      diagram: "continuum",
    },
    {
      term: "Architecture Repository",
      category: "Repository",
      definition:
        "Holds the output and artifacts of architecture activity: the Architecture Metamodel, Architecture Capability, Architecture Landscape, Standards Information Base (SIB), Reference Library, and Governance Log. It supports reuse across the enterprise.",
      doc: "https://pubs.opengroup.org/togaf-standard/architecture-content/",
    },
    {
      term: "Architecture Vision",
      category: "Deliverables",
      definition:
        "A high-level, aspirational view of the Target Architecture created in Phase A. It is used to sell the benefits of the proposed capability to stakeholders and to secure sponsor agreement to proceed.",
      doc: "https://pubs.opengroup.org/togaf-standard/adm/chap05.html",
    },
    {
      term: "Statement of Architecture Work",
      category: "Deliverables",
      definition:
        "Defines the scope and approach used to complete an architecture project. It is effectively a contract between the architecture function and the sponsor, produced in Phase A and approved before work proceeds.",
      doc: "https://pubs.opengroup.org/togaf-standard/adm/chap05.html",
    },
    {
      term: "Architecture Contract",
      category: "Governance",
      definition:
        "A joint agreement between development partners and sponsors on the deliverables, quality, and fitness-for-purpose of an architecture. Used in Phase G to govern implementation and ensure conformance.",
      doc: "https://pubs.opengroup.org/togaf-standard/adm/chap13.html",
    },
    {
      term: "Gap Analysis",
      category: "Techniques",
      definition:
        "A technique used throughout Phases B–D to validate an architecture by highlighting the difference (gap) between the Baseline and Target Architectures — what must be added, removed, or changed to reach the target.",
      doc: "https://pubs.opengroup.org/togaf-standard/adm-techniques/",
    },
    {
      term: "Transition Architecture",
      category: "Techniques",
      definition:
        "A formal description of the architecture at an intermediate, deliverable state between the Baseline and Target Architectures. Transition Architectures let the enterprise deliver business value incrementally.",
      doc: "https://pubs.opengroup.org/togaf-standard/adm/chap11.html",
    },
    {
      term: "Architecture Principles",
      category: "Governance",
      definition:
        "General rules and guidelines, intended to be enduring and seldom amended, that inform and support the way an organization fulfils its mission. Each principle has a Name, Statement, Rationale, and Implications.",
      doc: "https://pubs.opengroup.org/togaf-standard/adm-techniques/",
    },
    {
      term: "Stakeholder",
      category: "Fundamentals",
      definition:
        "An individual, team, organization, or class thereof having an interest in (concerns about) a system. Stakeholder management — mapping stakeholders to their concerns — is central to Phase A and to creating relevant architecture views.",
      doc: "https://pubs.opengroup.org/togaf-standard/adm-techniques/",
    },
    {
      term: "Concern",
      category: "Fundamentals",
      definition:
        "An interest in a system relevant to one or more of its stakeholders. Concerns determine the acceptability of the system and drive the development of architecture views and viewpoints.",
      doc: "https://pubs.opengroup.org/togaf-standard/architecture-content/",
    },
    {
      term: "View and Viewpoint",
      category: "Fundamentals",
      definition:
        "A view is a representation of a system from the perspective of a related set of concerns. A viewpoint defines the perspective (conventions, notations, and rules) from which a view is taken — the template, and the view is the result of applying it.",
      doc: "https://pubs.opengroup.org/togaf-standard/architecture-content/",
    },
    {
      term: "Content Metamodel",
      category: "Content Framework",
      definition:
        "A structured framework defining the types of architecture building blocks (entities), their attributes, and relationships, that may be created and managed as the formal outputs of architecture activity across the ADM.",
      doc: "https://pubs.opengroup.org/togaf-standard/architecture-content/",
    },
    {
      term: "Architecture Governance",
      category: "Governance",
      definition:
        "The practice of managing and controlling enterprise architectures at an enterprise-wide level, typically through an Architecture Board, supported by processes for compliance, dispensation, monitoring, and reporting.",
      doc: "https://pubs.opengroup.org/togaf-standard/",
    },
    {
      term: "Architecture Board",
      category: "Governance",
      definition:
        "A cross-organization body of stakeholders responsible for the review and maintenance of the overall architecture, including governance, consistency, compliance, and dispensations.",
      doc: "https://pubs.opengroup.org/togaf-standard/",
    },
    {
      term: "Capability-Based Planning",
      category: "Techniques",
      definition:
        "A business-planning technique that focuses on the delivery of strategic business capabilities, aligning architecture and transformation work to enterprise outcomes rather than to organizational silos.",
      doc: "https://pubs.opengroup.org/togaf-standard/adm-techniques/",
    },
    {
      term: "Architecture Partitioning",
      category: "Techniques",
      definition:
        "The classification and division of architectures into partitions (by breadth, depth, time, and domain) to manage complexity and clarify ownership and governance across the Architecture Landscape.",
      doc: "https://pubs.opengroup.org/togaf-standard/",
    },
  ],
};
