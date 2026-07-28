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
    Effective domain modelers are knowledge crunchers

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
