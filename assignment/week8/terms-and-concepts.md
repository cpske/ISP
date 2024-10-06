---
title: Software Concepts and Principles 
---

Design Patterns and Refactoring use some common vocabulary and concepts concepts to explain their rationale.

Please be sure you understand and can explain each of the terms below.
This will be on a quiz.

## Concepts (Terminology)

1. **Abstraction**

2. **Cohesion**, in particular, what are *Functional Cohesion* and *Informational [or Communication] Cohesion*? 
   - When developers talk about "cohesion" they usually mean "functional cohesion".

3. **Coupling**

4. **Encapsulation** and **Data Hiding** or *Information Hiding*, core concepts in OO programming

5. **Interfaces**. In particular, what is the *purpose* of an interface?

6. **Polymorphism**

7. *Separation of Concerns* - moved to *Design Principles*.
 

## Design Principles

Design Principles from ***Design Patterns: Elements of Reusable Object-Oriented Software***, known as the "Gang of 4" Design Patterns book.

1. *Program to an Interface, not to an Implementation*.

2. *Encapsulate what varies*.

3. *Separate the part that varies from the part that stays the same.* A rephrasing of the above, buts more specific.

4. *Favor composition over inheritance.*

5. *Strive for loosely coupled objects.*

6. "*Depend on abstractions, not on concretions*"
   - Also called *Dependency Inversion Principle*, the "D" in Robert Martin's SOLID principles.

7. *Single Responsibility Principle* (SRP), also described as "*A class should have only one reason to change*".  
   - This is the "S" in Robert Martin's SOLID principles.

8. *Separation of Concerns*
   - The Layered Network Architecture in the ISO and Internet architecture use this approach. 
   - Each layer provides a completely different kind of functionality, with a minimal *interface* to adjacent layers. As a result, it is possible to replace one implementation of a layer with a different implementation.

---

### Resources

- *Classes*, [Chapter 10 in *Clean Code*](../../resources/Clean-Code-ch10.pdf) describes Cohesion and SRP, with examples. (16 pages)

- [Single Responsibility Principle][SRP] article by Robert Martin.

- [Open-Closed Principle][OCP] article by Robert Martin.

- Wikipedia: [Abstraction][abstraction-wikipedia], [Cohesion][cohesion-wikipedia], [Coupling][coupling-wikipedia], and the [SOLID Principles][solid-wikipedia], including SRP.

[abstraction-wikipedia]: https://en.wikipedia.org/wiki/Abstraction_(computer_science)
[cohesion-wikipedia]: https://en.wikipedia.org/wiki/Cohesion_(computer_science)
[coupling-wikipedia]: https://en.wikipedia.org/wiki/Coupling_(computer_programming)
[solid-wikipedia]: https://en.wikipedia.org/wiki/SOLID
[SRP]: https://cpske.github.io/ISP/resources/SOLID/SRP.pdf
[OCP]: https://cpske.github.io/ISP/resources/SOLID/OCP.pdf

