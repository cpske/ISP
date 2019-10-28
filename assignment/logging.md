## Logging Assignment

1. Add logging to your Django Polls project code.

   * Use a named logger.
   * Log an INFO message whenever someone votes on a poll.
   * Its insecure to log confidentially info, but for practice include the poll id and choice id that the user voted for.
   * Log a WARNING message if someone votes for a non-existing question or a choice number that doesn't exist.
   * Is there any way to detect if someone is viewing (say) poll question 1 and votes for a choice that belongs to a *different* question?  If you can detect it, log it as ERROR.  Its eiter a programming error or indicates someone manually fabricated a POST request for voting.
   * Log all exceptions caught by the app using `log.exception`.

2. Configure logging.

   * Log all messages from the 'polls' app to a file (e.g. `polls.log`).
   * Log ERROR messages from the 'polls' app to the console.

3. Verify your logging works, merge it into master, and commit your work to master branch on Github.
