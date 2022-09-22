Here's example of drawing a sequence diagram using
<https://sequencediagram.org>.

- Given: we already have an object of type Main.
- Draw:  what happens when run() is invoked.  Show the call to `run()` as a "*found*" message. "*Found*" is a UML term, it **does not** mean to write the word "found" on your diagram.
  - show the activation boxes
  - show the names of methods that are called and return values
  - show creation of the Person object
  - include the object reference name (`pee`) in the Person box.

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
can show (almost) what we want using these instructions.
It does not show the solid circle on the "found" message.
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

