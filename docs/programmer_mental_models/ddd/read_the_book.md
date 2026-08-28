# Step 2: Read the book, construct a ts toy project based on [how browser works](https://webplatform.github.io/docs/concepts/Internet_and_Web/how_browsers_work/#Render_tree_construction)
# Key Points
!!! info "leverage"
    A good domain model is cognitive leverage. Like scientific models described by Sanjoy Mahajan([The art of insight in Science and Engineering](../assets/the-art-of-insight-in-science-and-engineering.pdf)), it compresses complex reality into a small set of high-quality concepts. 
    This compression reduces cognitive load and enables developers to reason about the system more effectively. 
    Unlike computational offloading in browser animation, DDD performs cognitive structuring: it does not transfer reasoning to machines, but creates better mental representations for human reasoning.

!!! info "[Concept Engineering](../concept_engineering.md)"
    Learning can only be done by understanding the concept represented by the word used by author.


!!! info "Design by Constraint"
    Both **TDD** and **Every layout CSS** are designed by Constraint.
    Modern CSS is framed around defining strict constraints and boundaries;
    Tests act as the layout boundary box—defining requirements and edge cases up front so the internal implementation can evolve safely without breaking the container.

!!! info "XP as a 'Guided' Greedy Algorithm"
    Focuses on the immediate best step, but uses refactoring(Refactoring toward Deeper Insight) to course-correct out of local optima.

!!! info  "UML Diagram --> C4 + PlantUML + Mermaid"
    [UML](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/) emerged in an era when large-scale software projects emphasized upfront modeling and high-fidelity design documentation. With the rise of Agile and iterative development, UML diagrams often suffered from diagram rot because software models evolved faster than documentation. However, the needs that UML addressed did not disappear; they were decomposed into specialized approaches. [C4 Model](https://c4model.com) and [Structurizr](https://structurizr.com) focus on evolving architecture models, while diagram-as-code tools such as Mermaid focus on lightweight, maintainable visualization and communication of existing models.    
    [PlantUML](https://github.com/plantuml/plantuml) is not so much a successor to UML as its continuation in the "Diagram as Code" era. It preserves UML's modeling philosophy while replacing GUI-based drawing with text-based descriptions. Mermaid, by contrast, evolved primarily from the Markdown documentation ecosystem, emphasizing lightweight communication rather than formal modeling.
    PlantUML is model representation, while Mermaid is communication representation.

!!! info "Concept Model"
    ```shell
                            Reality
                            │
                            │  abstraction / compression
                            ▼
                Shared Domain Model (Conceptual Model)
                            │
                            │
                Ubiquitous Language
                            │
                ┌───────────┴───────────┐
                │                       │
                ▼                       ▼
        Domain Expert            Software Expert
                │                       │
                │                       │
        Physical System          Software System
                │                       │
                └───────────┬───────────┘
                            │
                    Implement Reality
    ```
    Domain experts and software experts may not fully understand each other's fields. However, through collaboration, they construct a **Shared domain model**.

    This shared domain model is a **conceptual model** — a **compressed representation** of **reality** that preserves the essential structure and meaning of the domain while omitting unnecessary details.

    The model is expressed and refined through a **ubiquitous language**, allowing both domain experts and software experts to use the same vocabulary to describe the same representation of the underlying reality.

    Although they share the same conceptual model, they **implement** it through different **means**. Domain experts may realize the model through physical systems, business processes, or operational practices, while software experts realize it through software architecture, code, and technical infrastructure.

    In this sense, the shared domain model serves as a bridge between different disciplines: it enables people with different expertise to develop a common understanding of reality and to create different implementations based on the same conceptual foundation.

!!! info "Continous Refactoring & Deep Model"
    ```shell
    Reality
      ↓
    Understanding
      ↓
    Domain Model
      ↓
    Code
      ↓
    Experience / Feedback
      ↓
    Improved Understanding
      ↓
    Better Domain Model
      ↓
    Refactoring
    ```
    
    In Domain-Driven Design, the primary artifact is not the code but the evolving domain model. 
    Code is merely one implementation of that model. 
    As our understanding of the domain improves, the model evolves, and refactoring is the process of bringing the software back into alignment with the improved model.
    Big Design Up Front assumes that a sufficiently accurate model of reality can be created before implementation begins. However, for complex domains, modeling is not a one-time activity but an evolutionary process. Our understanding of reality improves through continuous interaction, and the model gradually increases in fidelity through successive iterations.

!!! info "Knowledge Crunching"
    knowledge crunching turns the knowledge of the team into valuable models.
    it's a knowledge refinement process.
    Effective domain modelers are knowledge crunchers;
    Through knowledge crunching, a team distills a torrent of chaotic information into a practical model.

!!! info "emergent capability"
    powerful new features unfold as corollaries to older features;

!!! info "Abstraction is both Compression and Constraint"
    $Abstraction = compression + constraint generation$
    Abstracting is not merely reducing reality into fewer concepts; a powerful abstraction creates a constrained conceptual space in which new knowledge and capabilities can be derived.  A good abstraction is similar to an axiomatic system in mathematics.
    Traditionally, abstraction is understood as a process of compression: stripping away irrelevant details to represent reality with fewer, higher-level concepts. However, this view captures only half of its power.
    A well-designed abstraction does more than compress complexity—it defines the boundaries, relationships, and constraints of a conceptual space. Once these constraints are established, many new conclusions, behaviors, and capabilities no longer need to be invented individually; they emerge as natural corollaries of the underlying model.
    This is precisely the insight behind Eric Evans's observation that **"powerful new features unfold as *corollaries* to older features."** A mature domain model does not merely record existing knowledge; it creates a conceptual structure from which future features can be derived rather than continuously added.
    In this sense, abstraction is both compression and constraint. Compression reduces cognitive load, while constraints make reasoning possible. The true value of abstraction lies not only in representing reality more simply, but also in enabling a system of concepts that generates new understanding.

!!! info "Inheritance vs. Composition: Tree Structure vs. Network Structure"
    The fundamental difference between inheritance and composition is not merely a programming technique, but two different ways of modeling reality.
    Inheritance organizes concepts into a tree structure. The tree originates from taxonomy and expresses an "is-a" relationship. It emphasizes an entity's ontological structure—what something fundamentally is. This makes inheritance well suited for representing stable conceptual hierarchies and essential properties. However, extending behavior usually requires introducing new subclasses, which can easily lead to class explosion.
    Composition, in contrast, organizes concepts into a network structure. The network arises from collaboration and expresses a "works-with" relationship. It emphasizes an evolvable behavioral structure, making it more suitable for modeling business rules, policies, and interactions. New capabilities are rarely created by introducing new types; instead, they emerge by recombining existing components, strategies, and rules.
    Therefore, the real value of a domain model is not the depth of its inheritance hierarchy, but whether it establishes a set of high-quality concepts and relationships from which new business capabilities can be derived naturally—much like mathematical theorems are derived from a small set of axioms.

!!! info "Interface as the Foundation of Composition"
    An interface is the primary mechanism that enables composition. It defines how objects interact by specifying an interaction protocol, rather than prescribing a concrete implementation.
    From a conceptual perspective, an interface is an abstraction of a contract. Like every good abstraction, it serves two complementary purposes:
    Compression — reducing implementation details into a simple, reusable conceptual contract.
    Constraint — defining the boundaries that every implementation must satisfy.
    This dual nature of abstraction is essential: abstraction is not only about simplifying complexity, but also about creating a constrained conceptual space in which meaningful collaboration and reasoning become possible.
    In a domain model, concepts abstract the primary entities of the domain, while interfaces abstract the relationships between those entities. They are the code-level representation of conceptual constraints and contracts.
    In other words:
    Concepts answer: What exists?
    Interfaces answer: How do those concepts collaborate?
    Together, they form the conceptual foundation of a compositional architecture, where behavior emerges from the interaction of well-defined concepts rather than from increasingly deep inheritance hierarchies.

!!! info "DDD OOP Concept Engineering"
    ```shell
    Reality
          │
          ▼
    Concept
          │
          ▼
    Interface (Concept Contract)
          │
          ▼
    Multiple Implementations
          │
          ▼
    Composition
          │
          ▼
    Interaction
          │
          ▼
    Emergent Behavior
    ```

!!! info "Guard Clause"
    At the beginning of the method, check for illegal conditions; if the conditions are not met, return immediately.
    A guard clause is an implementation technique, not a domain concept.
    ```shell
    Business Knowledge

            ↓

    Business Rule

            ↓

    Domain Concept

            ↓

    Domain Model

            ↓

    Implementation
    ```
!!! info "Schism"
    Schism is serious semantic drift.

!!! info "Improved by being used"
    Persistent use of the UBIQUITOUS LANGUAGE will force the model’s weaknesses into the open.
    A model is not improved by thinking alone; it is improved by being used. Persistent use turns hidden assumptions into visible contradictions, and those contradictions become the raw material for knowledge crunching and model evolution.

!!! info "All Language is Based on Some Model"
    This overlooks the reality that all language is based on some model. 
    The meanings of words are slippery things.
    Ubiquitous Language within a Bounded Context.
    UBIQUITOUS LANGUAGE is cultivated in the intersection of jargons.

!!! info "Domain Model VS Implementation Model"
    Formal complete UML is a design specification tool for stable systems where precise communication and structural consistency are required. It emphasizes representational precision and completeness, making it suitable for documenting mature designs, architecture decisions, and implementation structures.
    Informal UML, on the other hand, is a modeling and communication tool used during knowledge crunching. It helps domain experts and developers explore concepts, clarify relationships, and refine their shared understanding.
    A Domain Model is not a static artifact that is completed once; it is an evolving conceptual representation of the domain that continuously improves as the team's understanding grows. Informal UML diagrams, acceptance tests, conversations, and code examples all contribute to the construction and refinement of the Domain Model. Their purpose is not completeness, but insight, alignment, and continuous evolution.

!!! info "Constraint VS Specification"
    informal UML is used to define constraints which represent the skeletons of ideas, rather define the specifications.

!!! info "Role of Code"
    Informal UML diagrams can anchor a discussion, it can serve to focus attention and aid navigation.
    The vital detail about the design is captured in the code.
    Code is the ultimate executable design document.
    The code can serve as a repository of the details of the design.

!!! info "Document"
    Documents Should Complement Code and Speech. A document shouldn’t try to do what the code already does well.
    Documents Should Work for a Living and Stay Current.

!!! info "DDD in AI era"
    Complexity can be broadly divided into two categories: business complexity and technical complexity. 
    Technical complexity originates from the constraints imposed by the physical world. Its solutions are derived from engineering practices and mathematical reasoning. In the AI era, AI is exceptionally capable of addressing technical complexity, which means that the cost and difficulty of dealing with technical complexity are being significantly reduced.
    Business complexity, however, depends on human insight, the ability to understand reality, and modeling methodologies. Domain-Driven Design (DDD) provides precisely such a methodology for managing business complexity: a way to discover, abstract, and evolve models that accurately represent complex domains.
    In the AI era, this capability will not be replaced; instead, its value will become even more prominent. As implementation becomes increasingly automated, the fundamental value of humans shifts toward insight—the ability to perceive essential patterns, identify meaningful concepts, establish appropriate boundaries, and construct effective models. This capability remains something AI does not inherently possess.
    A flexible language gives you freedom; only good design turns that freedom into flexibility. Just using a flexible language doesn’t create a flexible system, but it may well produce an expensive one. AI does not merely reduce the cost of programming; it reduces the cost of implementing bad ideas. Without better design, greater implementation freedom does not produce more freedom; it produces more expensive systems.

!!! info "Other Models"
    Technical Models drive the software development process, must be strictly pared down to the necessary minimum.
    An explanatory model can include aspects of the domain that provide context that clarifies the more narrowly scoped model.
    Paradigm: What programming paradigm allows a domain model to exist directly in the code. 
    User model;

!!! info "Implementation shouldn't introduce more complexity"
    Implementation should not carry speculative complexity. Future adaptability should emerge from a well-designed domain model rather than from premature technical mechanisms. A good abstraction does not predict every possible future; it identifies the stable concepts and relationships that allow future changes to unfold naturally.

!!! info "Translation blunts communication"
    To make a MODEL-DRIVEN DESIGN pay off, the correspondence must be literal, exact within bounds of human error.

!!! info "What is Programming Language"
    Programming languages are essentially different models of the act of “writing instructions for a computer to execute.” In other words, they are different ways of abstracting reality. Each language chooses a different abstraction boundary and answers a fundamental question: **what should become the basic concepts of a program?**
    Some abstraction approaches are closer to the underlying machine. For example, C is built around **Memory + Procedure + Control Flow**, which makes it closer to the execution model (the machine model) and reflects the actual way a computer operates at a lower level. This is why learning C provides a better understanding of how computers actually execute programs.  
    Other languages, such as Python, use a higher-level abstraction that is closer to the way humans conceptualize problems (the human conceptual model). The abstraction level is higher, but Python’s performance limitations are not simply caused by having a higher level of abstraction.
    A higher level of abstraction does not necessarily mean lower performance. C++ templates and Rust’s zero-cost abstractions demonstrate this point. Taking Rust as an example, its zero-cost abstraction means that developers can use higher-level abstractions without sacrificing runtime performance. This is achieved by eliminating the cost of abstraction during compilation.
    This follows a fundamental principle of conservation: **cost cannot be eliminated; it can only be transferred.** Therefore, the inevitable consequence is that Rust’s compilation process is more expensive than C’s, due to mechanisms such as monomorphization, the borrow checker, and type inference.

!!! info "Model-Driven Design VS Domain-Driven Design"
    In a MODEL-DRIVEN DESIGN, the software constructs of the domain layer mirror the model concepts.
    ```shell
    Domain-Driven Design (DDD)
    │
    ├── Strategic Design
    │   ├── Bounded Context
    │   ├── Context Map
    │   ├── Ubiquitous Language
    │
    └── Tactical Design
        ├── Entity
        ├── Value Object
        ├── Aggregate
        ├── Repository
        ├── Domain Service
        │
        └── Model-Driven Design  ← here
    ```

!!! info "Implementation vs Design"
    software development is all design, and design is not only a phase.

!!! info "Responsibility-Driven Design RDD"
    What is this object's responsibility, Object is not only the data container.

!!! info "Design by Contract (DbC)"
    Contracts as executable specifications for APIs.
    Interactions between objects are not arbitrary method calls; they are governed by contracts. A contract consists of preconditions, the operation itself, and postconditions. This emphasizes that an object is responsible for maintaining its own correctness, making Design by Contract fundamentally a discipline of behavioral constraints. In Domain-Driven Design, this idea evolves into the concept of the Aggregate, which is responsible for enforcing its own invariants and preserving consistency.
    1. preconditions (what callers must satisfy), 
    2. postconditions (what the routine guarantees after execution),
    3. class invariants (properties that always hold for valid objects)



!!! info "GRASP General Responsibility Assignment Software Patterns"
    Applying UML and Patterns by Craig Larman;
一个职责到底应该分配给哪个对象？它不是设计模式，而是一套职责分配原则。
    1. Information Expert: who has all the information to finish a job should be responsible for the job, which is Entity in DDD;
    2. Creator
    3. Low Coupling: Bounded Context
    4. High Cohesion: Aggregate has a clear boundary
    5. Controller
    6. Polymorphism
    7. Pure Fabrication
    8. Indirection
    9. Protected Variations: Repository, Domain Service, Interface

!!! info "Questions in DDD"
    What to model?
    How to model?
    How to implement?
    Which object should a responsibility be assigned?

!!! info "Fundamentals"
    Elaborate models can cut through complexity only if care is taken with the fundamentals, resulting in detailed elements that the team can confidently combine.

!!! info "Architecture Layers"
    UI - Application(when) - Domain - Infrastructure(how)
    Every layer only depends on the same or below layers
    Lower layers should have no specific knowledge of the upper layers
    Architecture absorbs technical complexity; the domain model expresses business complexity.

!!! info "Functional Specifications VS DDD"
    Functional Specification specifies the behavior of the product; 
    DDD models the meaning of the business.

!!! info "Associations"
    Associations illustrate how crucial detailed implementation decisions are to the viability of a MODEL-DRIVEN DESIGN.
    Some traversal directions reflect a natural bias in the domain;
    Constrained associations communicate more knowledge and are more practical designs.
    

!!! info "Decisions"
    Every design decision should be motivated by some insight into the domain. A good design is crystallized domain knowledge

!!! info "A model is intentionally incomplete"
    Modeling is a process of deliberately reducing degrees of freedom.
    Understanding the domain may reveal a natural directional bias.
    Modeling is not merely abstraction; it is selective abstraction.
    Good modeling requires both the ability to see meaningful structure and the discipline to discard meaningless structure.
    Domain insight is not merely about discovering relationships in reality; it is about determining which relationships, directions, and dependencies are meaningful enough to preserve in the model—and which should deliberately be discarded.

!!! info "Entity"
    Many objects are not fundamentally defined by their attributes, but rather by a thread of continuity and identity.
    They have life cycles that can radically change their form and content, but a thread of continuity must be maintained.
    The most basic responsibility of ENTITIES is to establish continuity so that behavior can be clear and predictable. They do this best if they are kept spare.
    entity - identity(identifying attribute) - lifecycle/Continuity - behavior - attributes
    Domain identity reasoning is not always a purely computational problem.
    Questions:
    1. If every attribute of it has changed, do you still take it as the same thing?
    2. Entity = abstract continuity threading through a lifecycle
    3. How do we generate IDs(identifying attribute)?
    4. How do we guarantee uniqueness?
    5. How do we reconcile identities?
    6. How do we preserve them across services?
    ```shell
    Entity
    │
    ├── Identity
    │     └── operational identifier
    │            └── guaranteed unique
    │
    ├── Continuity
    │     └── survives lifecycle changes
    │     └── tracking has cost
    │
    │
    ├── Behavior
    │     └── state transitions
    │
    └── Attributes
          └── changing description/state
    ```

!!! info "Value Objects"
    An object that represents a descriptive aspect of the domain with no conceptual identity is called a VALUE OBJECT
    ```shell
    Entity:
    identity > attributes

    Value Object:
    attributes/value > identity
    ```
    Software design is a constant battle with complexity. Tracking the identity has cost, some objects have no conceptual identity. We must make distinctions so that special handling is applied only where necessary.
    Value Objects are used as attributes of ENtities.
    Treat the value object as immutable.
    The attributes that make up a VALUE OBJECT should form a conceptual whole
    Questions:
    1. what they are, don't care who or which they are
    2. Do these attributes, when combined, constitute a concept within the domain that I can independently think about, name, and discuss?
    ```shell
    VALUE OBJECT
          ↓
    Conceptual Whole
          ↓
    Attributes
          ↓
    Value
    ```

!!! info "Flyweight"
    Extract the common, unchanging parts of a large number of objects and keep only one copy.

!!! info "Model-Driven Implementation"
    A domain semantic judgment can directly lead to an optimization possibility in engineering implementation.

!!! info "Model-native programming, Domain-native programming"
    Many of the distinctions we are making in the model cannot be explicitly declared in the implementation with most current tools and programming languages. 
    Because the domain concept is not first citizen in most of the language, but if we try to use the framework or library to solve it, the risk of framework driven modeling may emerge.
   
!!! info "Services"
    It just isn't a thing.
    A Service is an operation offered as an interface that stands alone in the model, without encapsulating state.
    A SERVICE tends to be named for an activity, rather than an entity—a verb rather than a noun. 
    Parameters and results should be domain objects.
    A good SERVICE has three characteristics.
      1. The operation relates to a domain concept that is not a natural part of an ENTITY or VALUE OBJECT.
      2. The interface is defined in terms of other elements of the domain model.
      3. The operation is stateless.

!!! info "Modules"
    Modules are a full-fledged part of the model.   

!!! info "Model VS. Paradigm"
    Model = what you understand.
    Paradigm = how you choose to think about and implement what you understand.
    This also explains why we shouldn't try to understand a new repository simply by reading    the code line by line(this means you're trying to reconstruct the model from the implementation). The domain model is unique to the problem, while the code is only one possible implementation of that model, and it may use a completely different organizational scheme.
    It also explains why, in a well-organized codebase, some files contain only a small amount of code and very few objects(which serve as conceptual chunks and domain vocabulary). Their purpose isn't necessarily to contain a lot of implementation logic; they can serve as clear boundaries that make the underlying domain model easier to understand.(cognitive overload)
    Questions when entering a repository:
    1. What is the domain model?
    2. How was that model implemented?

!!! info "Aggregate"
    AGGREGATES tighten up the model itself by defining clear ownership and boundaries, avoiding a chaotic, tangled web of objects.
    Deliberately introduced boundaries that don't exist naturally in reality.
    What is the smallest group of objects that must be treated as one consistency unit?
    Define a boundary around a group of objects that must maintain consistency together = locking boundary 
    A deliberately chosen boundary within which the domain model must remain consistent, allowing the rest of the model to remain relatively independent.
    Each AGGREGATE has a root and a boundary:
    - Boundary defines what is inside the AGGREGATE
    - Root is a single, specific ENTITY contained in the AGGREGATE
    The root is the only member of the AGGREGATE that outside objects are allowed to hold references to, although objects within the boundary may hold references to each other.

!!! info "Factory"
    Assembling a complex compound object is a job that is best separated from whatever job that object will have to do when it is finished.
    Aggregate Root controls access during life, while a Factory can control entry into life.
    A constructor is a primitive supplied by the programming language; a Factory is a modelling abstraction that owns the knowledge of how a valid domain object comes into existence.
    A program element whose responsibility is the creation of other objects is called a FACTORY.
    a FACTORY encapsulates the knowledge needed to create a complex object or AGGREGATE

!!! info "reconstitution"
    I refer to the creation of an instance from stored data as reconstitution.

!!! info "Repository"
    Repository acts like a collection, except with more elaborate querying capability, and the querying interface should still speak the model's language.
    The Repository protects the model from persistence complexity.
    Here is the conceptual collection of all existing domain objects of this kind.
    ```shell
    database reality
          ↓
    Repository abstraction
          ↓
    domain mental model
    ```
    Its real purpose is to make persistence look like domain-object access.
    A Specification turns a domain rule into a first-class object that can answer “does this candidate satisfy this rule?” and can also be used by infrastructure to find all candidates that satisfy it.
    Encapsulating the mechanisms of storage, retrieval, and query is the most basic feature of a REPOSITORY implementation.







