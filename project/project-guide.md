# ISP Course Project

* [Purpose and Evaluation](#purpose-and-evaluation)
* [Development Process](#development-process)
* [Process Specifics](#process-specifics)
* [Project Topic](#project-topic)
* [Suggested Project Topics](#suggested-topics)
* [Platform](#platform) and [Client-side Frameworks](#client-side-frameworks-and-testing)

## Purpose and Evaluation

* Consistently apply a development process and good development practices to a small team project.
* Each person evaluated based on his/her work.
* Criteria: Process, visible effort, and quality of work products.

## Development Process

* Iterative development
* Project status and progress should be **visible**
   - use a project board (Waffle.io, Trello, or Github project board)
   - show tasks and who is doing them
   - project Github site has links to everything
* Maintain running and deployable code from the beginning.
* Automated testing, including testing of Javascript in UI.

### Process Specifics

1. Have a project *Vision Statement* with written requirements.
2. Use short iterations (1-2 weeks) with goals, milestones, and task backlog.
3. Use a task board (Waffle.io, Trello, Github)
4. Use Github Flow (branches, pull requests, code review)
5. Use issues for 
   - bugs found in testing and code review
   - feature requests or unplanned changes
6. Automate unit testing, including testing of UI templates and Javascript.
7. Use Continuous Integration and automatic testing. Try Travis CI or CircleCI.
8. Deploy your app to a cloud provider, such as Google App Engine, AWS, Azure, or DigitalOcean.

## Project Topic

The project topic should meet these basic criteria:

1. Involves some business or domain logic -- not just web interface to a database.
2. Not too complex.  Main purpose is to consistently apply good development practices.  No credit for a whiz-bang application using a crummy process.
3. Use a database for persistence. Can be SQL or NoSQL database.
4. Testable, with automated unit tests.
5. **No** e-commerce or sales applications, food ordering, or action games.
6. Has some user authentication, but no user registration. Use OAuth, OpenID, or other standard to authenticate and automatically register users.

### Teams

Team size is 3-4 people.  If you want a team with fewer or more than this, please see instructor and explain why.

## Suggested Topics

1. Movie Recommender
   - User inputs his own rating of some movies. System recommends based on what he likes.
   - Lots of external data available. MovieLens has 100,000+ movies, millions of ratings.
   - Logic is involved in making recommendations.

2. Other Recommender - recommend books, restaurants, etc.
   * Getting data may be a problem.

3. Event Manager for an event like BarCamp.
   * Room and time scheduling.
   * Posting of topics for talks.
   * Attendee "voting" for talks they want.
   * Rating or feedback on talks by attendees.


 ## Platform

 Django or Play framework OK.  No PHP frameworks.

 If you use a framework other than Django:

 1. implement an app in the framework and demonstrate it.  Include some tests.
 2. give a reason why you prefer this framework

 ### Client-side Frameworks and Testing

 You aren't required to use a client-side fraemwork, but some teams plan to.

 Code in the client side needs to have unit tests, too.  The are several good tools for testing Javascript, esp. code using React or Angular.

 * [How React Components Make UI Testing Easy](https://www.toptal.com/react/how-react-components-make-ui-testing-easy)
