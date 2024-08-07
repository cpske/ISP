---
title: UML Diagrams
---

Unified Modeling Language (UML) is a standard set of diagrams for describing software.  There are diagrams for:

* static structure
* dynamic behavior
* deployment
* use cases

In UML 2.2 there are 14 types of diagrams. 

You should know how to read and draw the 3 most common diagrams:

* Class Diagram
* Sequence Diagram
* State Machine Diagram

The 'Activity Diagram' is equally popular as Sequence Diagram,
but the Sequence Diagram has clearer notation and is easier to read,
so we will use that.

The 'Use Case Diagram' is also widely used, but, the Use Case *Text* is more important than the diagram.

[Visual Overview of All UML Diagrams](https://creately.com/blog/diagrams/uml-diagram-types-examples) with examples.


## Class Diagram

Slides: [UML Class Diagram](UML-Class-Diagram.pdf) and [Relationships](UML-Class-Relationships.pdf)

## Sequence Diagram

Slides: [Sequence Diagram Tutorial](Sequence-Diagram-Tutorial.pdf)

* Very visual tutorial with explanation: <https://www.smartdraw.com/sequence-diagram/>

* Slides based on *UML Distilled*: <http://csis.pace.edu/~marchese/CS389/L9/Sequence%20Diagram%20Tutorial.pdf>
  - slides have good explanation of the notation

* Video on Coursera: <https://www.coursera.org/lecture/object-oriented-design/1-3-6-uml-sequence-diagram-965yb>

* Details and best practices, including how to show loops: <https://creately.com/blog/diagrams/sequence-diagram-tutorial/>

### System Sequence Diagram

System Sequence Diagram (SSD) is a simplified sequence diagram showing 
interaction between the user and system.
Details of what the system does are now shown.
It may also show interaction between the "system" and *external services* or "*actors*".

It's useful for design of a particular usage scenario to discover all the
interactions.  

* [Process Sale SSD Example](Process-Sale-SSD-Example.pdf) system sequence diagram for a "Process Sale" use case

* Another "Process Sale" SSD: <https://stg-tud.github.io/eise/WS11-EiSE-11-System_Sequence_Diagrams.pdf>

* Course Enrollment SSD: in Software Spec course

## State Machine Diagram

to be added

## UML Drawing Software

[Visual Paradigm](https://visualparadigm.com) online diagram editor with UML. Save work to Google Drive.    
[GitMind](https://gitmind.com) - online or run on desktop. UML and many other kinds of diagrams, such as *mind maps*.    
[Violet UML Editor](https://sourceforge.net/projects/violet/) desktop UML editor, written in Java.  I use version 2.0.1 of Violet. Sequence and State diagrams have limited formatting.     
[UMLet](https://www.umlet.com/) desktop UML app. I sometimes use this. Requires some learning, but can draw exactly what you want.   
[SequenceDiagram.org](https://sequence.diagram.org) for sequence diagrams.    

Not free:

[Moqups](https://moqups.com) create mock-ups of software, has UML class and sequence diagrams. Must upgrade to paid plan in order to export or print.

## Examples

- [Very Simple Sequence Diagram](sequence-example) and code to create it using [SequenceDiagram.org](https://sequencediagram.org)

