## Git Submodules

Git submodules let incorporate code from a separate git repository 
(the submodule) inside another git project.

This let's you: (a) update the repositories separately, (b) use the submodule code in many different projects.

See [Submodules][git-submodules] in the Pro Git book,
and [Working with Submodules][working-with-submodules] example in Github blog.

[git-submodules]: https://git-scm.com/book/en/v2/Git-Tools-Submodules
[working-with-submodules]: https://blog.github.com/2016-02-01-working-with-submodules/

## Adding a Submodule for TicTacToe Unit Tests

There is a Git repository containing unit tests for TicTacToe.  The repository contains *only* the `test/` directory.  
You can add it as `test/` folder inside your tic-tac-toe project,
as a submodule.

You *could* add the code anywhere, but `test/` is the standard location for
test code.

```
TicTacToe/
   src/         <-- your source code
   test/        <-- submodule for "test/" folder (clone submodule here)
   build.xml    <== Ant build file (create this yourself)
```

To add the unit tests to your TicTacToe project use:
```shell
# where your project code is
cmd> cd workspace/TicTacToe
cmd> git submodule add  https://github.com/ISP2018/tictactoe-test  test
```
In the `git submodule` command: 
[https://github.com/ISP2018/tictactoe-test](https://github.com/ISP2018/tictactoe-test) is Github repository you want to add as submodule;
`test` is the directory (relative to your current directory) where the submodule to be cloned to.  It should be a new directory (not exist yet, just like using "git clone").

Now type `git status`.  You'll see there are 2 files added:
```shell
cmd> git status
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   .gitmodules
	new file:   test
```
The contents of the `test/` directory won't be committed as part of your repository, even though git added the directory to your git repo.

In older version of `git`, after you add a submodule you must run the `git submodule update` to clone its contents. In the current Git, this isn't necessary (does nothing):
```shell
cmd> git submodule update --init
```

### What Happened?

Git updated your project configuration with .gitsubmodules, and created a clone of the `tictactoe-test` repo in your `test/` directory.

In effect you have a separate Git repository inside your project repository.

### Running the Tests

To run the tests in Eclipse, do:

* use "File -> Refresh" to refresh Eclipse's view of the project files
* add `test` as additional source folder (right-click on the `test` folder to add it to build path, or right-click on project and choose 'Build Path')
* add JUnit library to your project (right-click on project and choose 'Build Path' -> Add libraries)

This is boring, repetitive work.  

**Automate repetitive tasks:** 

* use [ant](https://ant.apache.org) to run tests
* use Continuous Integration to automatically run tests with Ant

### Updating the Submodule Files

The files in the `tictactoe-test` project may be updated on Github.
To update your clone of this project, 
just change directory to the submodule directory (`test`) and use `git pull`:
```shell
cmd> cd test
cmd> git pull
```
There is also `git submodule` command for this, which is useful if you have
many submodules to update.


