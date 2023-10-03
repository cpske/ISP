---
title: Software Concepts and Terms 
---

Refactoring and Design Patterns (the next topic) use some common vocabulary and concepts concepts for their rationale and explanation.

Please be sure you understand and can explain each of the terms below.

- **Abstraction** is a core OO concept. You will often hear (or read) 
  - "*A class's methods should have a consistent level of abstraction*" 
  - "*Depend on abstractions, not on concretions*" (design guideline). What does that mean?

- **Cohesion**, in particular, what are *Functional Cohesion* and *Informational [or Communication] Cohesion*? 
  - It is not so important to know "temporal cohesion", "informational cohesion", "sequential cohesion", etc.  When developers refer to cohesion they usually mean "functional cohesion".

- **Coupling**

- **Encapsulation** and **Data Hiding** or *Information Hiding*, core concepts in OO programming.

- **Interfaces** that provide the *specification* of functionality separately from its *implementation*.
  - What does this mean: "*Program to an Interface, not to an Implementation*".
  - And in testing: "*Test a specification, not an implementation.*"

- **Polymorphism**

- **Single Responsibility Principle** (SRP), paraphrased as "*A class should have only one reason to change*".  This is one of Robert Martin's SOLID principles.

- **Separation of Concerns** is the practice of dividing software into sections so that each part is responsible for a different aspect of functionality.
  - The Layered Network Architecture used in the ISO and Internet architecture use this approach. Each layer provides a completely different kind of functionality, with a minimal *interface* to adjacent layers. As a result, it is possible to replace one implementation of a layer with a different one.

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

