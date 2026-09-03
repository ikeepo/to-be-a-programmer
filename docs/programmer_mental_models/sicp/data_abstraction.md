# Chapter 2: Data Abstraction
# Relations
### Data Structure vs Data Abstraction
A data structure is a concrete way of organizing and storing data.
Data abstraction is the separation between how data is used and how it is represented.

A data structure is a representation; data abstraction is the boundary that hides and controls that representation.
### closure
The concept of closure is introduced here in its algebraic sense. In abstract algebra, a set is closed under an operation if applying that operation to elements of the set produces an element that also belongs to the set.

The authors here introduce closure to highlight the fundamental requirement for building complex data structures out of simple rules: unlimited composability.

Symbolic expressions—data whose elementary parts can be arbitrary symbols rather than only numbers.

once your language can handle symbols and nested structures, you move beyond basic arithmetic into building compilers, computer algebra systems (like Mathematica), database engines, and data compression utilities.

Data abstraction is a methodology that enables us to isolate how a compound data object is used from the details of how it is constructed from more primitive data objects.


### Abstraction Barrier
```shell
+-------------------------------------------------------+
|  High-Level Operations (e.g., add-rat, mul-rat)       |
+-------------------------------------------------------+
|  ABSTRACTION BARRIER (Constructors & Selectors)       |
|  - Constructor: (make-rat n d)                        |
|  - Selectors:   (numer x), (denom x)                  |
+-------------------------------------------------------+
|  Concrete Representation (e.g., Scheme cons pairs)    |
+-------------------------------------------------------+
```

Data abstraction enforces a strict separation of concerns: higher-level logic depends only on the contract defined by constructors and selectors, while the concrete data representation remains hidden beneath that functional interface.
### Horizontal Layering vs. Vertical Slicing
They apply at different stages of software design and solve different cognitive problems.

High-Level Abstraction Comes First (Domain Modeling);
Vertical Slicing is typically applied during Architecture Validation, System Decomposition, and Performance Profiling
```shell

                  ┌─────────────────────────────────────┐
                  │    Domain Logic / High-Level Rules  │
                  ├─────────────────────────────────────┤
   Vertical       │       Interface / Data Contract     │
   Slice          ├─────────────────────────────────────┤
   (End-to-End)   │      Data Structure / Algorithm     │
                  ├─────────────────────────────────────┤
                  │     Hardware / OS / Network I/O     │
                  └─────────────────────────────────────┘
```
### wishful thinking.
Assume that all the lower-level helper functions you wish you had already exist and work perfectly. Write your high-level logic first using these non-existent functions, and only implement the helpers afterward.
### Operator Overloading
In programming language theory, operator overloading means giving a single operator symbol multiple distinct behaviors depending on the type of data passed into it.
### message passing programming style
Instead of passing a data structure into an external function, you dispatch a "message" (a symbol or instruction) directly to a function that encloses the data, and the function decides how to respond based on that message.

OOP was never about classes or inheritance—it was about objects encapsulating state and communicating exclusively via message passing.
