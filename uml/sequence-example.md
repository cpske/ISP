---
title: Sequence Diagram using sequencediagram.org
---

This is an example of sequence diagram creation using <https://sequencediagram.org>.

Credit: Thanks to Pawitchaya for how to create a label for an object using `participant`.

- Given: we already have an object of type Main.
- Draw:  what happens when main.run() is invoked.  Show the call to `run()` as a "*found*" message. "*Found*" is a UML term, it **does not** mean to write the word "found" on your diagram.
- Show in the diagram:
  - the object reference name (`pee`) on the Person object box.
  - creation of the Person object (of course)
  - activation bars
  - the of methods that are called, parameters, and return values

```python
class Person:

    def __init__(self, name):
       self.name = name

    def get_name(self):
       return self.name


class Main:
    def run(self):
        pee = Person("Joe")
        name = pee.get_name()
```

<https://sequencediagram.org> 
can draw *almost* what we want.
It does not show the solid circle on the "found" message.    
Copy & paste this into the sequencediagram.org online editor.
```
# define object boxes with labels
# labels are in quotes to include : and space
participant ":Main" as main
participant "pee :Person" as person

# incoming call to main.run
[->main: run()
# now the run method is active
activate main
main->*person: <<create>>("Joe")

# call pee.get_name which returns a value
main->person: get_name()
activate person
# return value uses a dashed line
main<--person: "Joe"
deactivate person
```

