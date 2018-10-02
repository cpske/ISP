## Take Ownership of your TicTacToe repository

Each student has "admin" authority over their TicTacToe repository on Github Classroom.  So that you can do these exercises, transfer the repo to your own account using Setting - Options and scroll down to "Transfer Ownership".  

Transfer ownership to your own account, so you can use Travis CI.

After you transfer ownership the Github URL changes to:
```
https://github.com/yourlogin/tictactoe-yourlogin.git
```
So, in your **local tictactoe repo** change the URL of "origin" to this new URL.
```shell
cmd> git remote set-url origin https://github.com/new-location-of-remote-repo
# Verify it:
cmd> git remote -v
```

## Git Submodule

1. Add a submodule for test code to your TicTacToe project.
   * See course page on cpske.github.io/isp for how to use Git Submodules.
   * The Submodule URL is https://github.com/ISP2018/tictactoe-test.git
2. Commit the changes to your repo: `git commit -m "Add test submodule"`
3. Push to Github.
4. On Github, is there any *visual* indication that `test` is a submodule?
5. Run the unit tests on your computer.  You need to change your project config in the IDE.

## Use Ant

1. Install Apache Ant from [ant.apache.org](https://ant.apache.org) if you don't already have ant installed.  Use `ant -v` to check the version.  Current version is 1.10.x.
2. Add an ant `build.xml` file to your TicTacToe project.
   * You can use the build file in [https://github.com/jbrucker/demo-ci][demo-ci] as template to get started.  Edit the file and customize for your project.
3. Run the Junit tests using Ant.
   * I may ask you to demonstrate this to me to prove you did it.

## Add Automatic Testing using Travis CI

1. Read the Travis CI [Getting Started](https://docs.travis-ci.com/user/getting-started/) guide. It is short.
2. Create a Travis CI account according to instructions in *Getting Started*.
3. Give Travis access to some of your Github projects.
   * Your choice: you can grant access to everything or just specific projects.
   * At least include the tictactoe project.
4. On Github, under your *Personal Settings* (not repository settings), in the "Applications" category, verify that Travis CI has been added.

5. In your TicTacToe project, add a `.travis.yml` file containing configuration information.  You can use the file in [demo-ci][demo-ci] to get started, but you need to edit it for your project.
6. Verify that Travis is building and testing your project.

> Fatalai Jon reported that when he did this, Travis showed his TicTacToe project, but it wasn't building it.
> The solved it by clicking the "More Options" box on the right, and select 
"Trigger Build".
> He accepted the default settings and clicked "Trigger custom build". It worked.

## Fix your TicTacToe

If your TicTacToe game passed all tests: *Congratulations!*

Otherwise, make some change to the source code and push to Github.  Watch as Travis automatically rebuilds and tests the project.

[demo-ci]: https://github.com/jbrucker/demo-ci "Travis CI Sample Project"
