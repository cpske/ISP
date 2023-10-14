A design pattern has an *intent* that describes the problem the pattern tries to solve, *motivation* or *forces* that motivate the choice of a particular pattern, and an *applicability* or *context* that describes the situation where it can be applied.

To answer these questions, it may help to review these aspects of each design pattern.

In the questions below, choose the design pattern that best matches the situation described in the question.

1. The Python logging module has a `getlogger` method that creates, configures, and returns a logging object. The `getLogger` method hides the complexity of creating and managing logger objects.
   ```python
   import logging

   # simple configuration of logging facility
   logging.basicConfig(filename="myapp.log", format="...")
   logger = logging.getLogger("my_module")
   logger.info("This is a nice abstraction.")
   ```
   What design pattern does `getLogger` use?

2. Every Logger has a `Handler` instance that is responsible for outputting log messages.  There are `StreamHandler` (output to *sys.stdout* or *sys.stderr*), FileHandler (output to a file), NullHandler (discard the output), SyslogHandler (output to a Unix syslog server), and HttpHandler (output to a web server!).  

   There is also a very useful RotatingFileHandler that is similar to FileHander, but it *rotates* the log file on a schedule (e.g. once per day) or when the file exceeds a certain size.  After rotating the log file, RotatingFileHandler can automatically compress the old log file to save space.

   All the Handlers have the same interface, but a different implementation (or algorithm) for handling log messages.  Handlers use what design pattern?

3. The Python logging module has another component that is responsible for how messages are printed or displayed, such as printing of dates, log level, and the log message.  Describe this component and how it uses the same design pattern as in question #2 (above).

4. Java has many logging frameworks, such as Log4J, Logback, and the JDK's `java.util.logging`.  The `slf4j` library provides a single interface to all these framework and also a "no-operation" logger (discards log messages). Using `slf4j`, a programmer just calls logging methods in `slf4j`, and `slf4j` directs the messages to the actual logging framework (specified in a configuration file). The programmer never needs to use the API of the actual "backend" logger.
   ```java
   import org.slf4j.LoggerFactory;
   import org.slf4j.Logger;

   class Example {
       private static Logger log = LoggerFactory.getLogger(Example.class);

       public static void main(String[] args) {
           // these methods are provided by slf4j, which "front-ends" the actual logger
           log.info("Program started");
           log.warning("You should study design patterns.");
       }
   }
   ```

   `slf4j` is an example of what design pattern? (*Hint: it's not Adapter*)

4. In Tkinter (Python graphics framework), to layout a UI you can put components (widgets) into a Container. Then you can manipulate the entire container as if it was a single component, such as sizing or position in the window.  For example, when you resize the container all the components resize.

   This is an example of what design pattern?


