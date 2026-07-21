# The Psychology of Programming
Cognitive Ergonomics in Software.
# What metal image or clue forms in good programmer while they write `i32`
There are several keywords :

- interconnected layers :
    
    - Problem Domain Layer: Can this count negative values?

    - Hardware Layer: 4 bytes in memory (32 contiguous bits)

    - Boundary Layer: Range: `-2,147,483,648 to 2,147,483,647`

- Internal Checklist:
  
    - Hardware/Spatial Model: stack or heap, register

    - Boundary Clues: overflow

    - Type Domain & ALternatives: why not `u32, usuze, i64`

# Books Exploring Programmer Metal Models

- The Programmer's Brain by Felienne Hermans: In Progress

- Software Design for Flexibility by Chris Hanson and Gerald Jay Sussman

- A Philosophy of Software Design by John Ousterhout

- Write Great Code, Volume 1: Understanding the Machine by Randall Hyde

# Blogs

- [Antti Halme](https://notes.fringeling.com/MentalModels/)

- [Farnam Street](https://fs.blog/mental-models/)

# Mental models seem like such crucial and effective tools for mastering programming—why aren't they taught in the very first lesson of coding courses?
- The "Expert Blindness" Problem (The Curse of Knowledge)

- Cognitive Overload: You Can't Abstract What You Haven't Seen: A mental model is a compressed summary of reality.

- The Need for "Instant Gratification"
