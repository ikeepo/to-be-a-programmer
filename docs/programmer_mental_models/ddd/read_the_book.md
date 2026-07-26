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
