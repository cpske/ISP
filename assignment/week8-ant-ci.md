## Testing with Ant and Travis CI

### 1. Take Ownership of your TicTacToe repository and RENAME it

Each student has "admin" authority for their TicTacToe repository on Github Classroom.  Do these exercises, transfer the repo to your own Github account using Setting -> Options and scroll down to "Transfer Ownership".  

1. Transfer ownership of "tictactoe-yourname" to your own account, so you can use Travis CI.
   * During transfer **rename the repo** to `tictactoe` (remove the `-yourname`)
   * If you forget to rename, you can do it later, using to repo Settings page.

2. After you transfer ownership the Github URL changes to:
```
   https://github.com/yourlogin/tictactoe.git
```
3. In your **local tictactoe repo** change the URL of "origin" to this new URL (if you prefer ssh, change to the ssh URL):
```shell
cmd> git remote set-url origin https://github.com/yourlogin/tictactoe.git
# Verify it:
cmd> git remote -v
```

**Note:** I will check your build on Travis CI, so the project URL should be
```
https://travis-ci.com/your_github_id/tictactoe
```
If the URL is something else, then you won't get credit.

### 2. Add Git Submodule for Tests

> See [Submodules][git-submodules] in the Pro Git book or [Working with Submodules][working-with-submodules].    
> Simple guide: [git submodules](../git/submodule) on cpske.github.io/isp.

1. Add a submodule for test code to your TicTacToe project.
   * The Submodule URL is https://github.com/ISP2018/tictactoe-test.git
2. Commit the changes to your repo: `git commit -m "Add test submodule"`
3. Push to Github.
4. On Github, is there any *visual* indication that `test` is a submodule?
5. Run the unit tests in your IDE.  What steps do you have to use to add `test` to the project build path and run the tests?

> **Already Have a `test` Directory?**
>
> If your project already has a `test/` directory containing test code, you have 2 choices:
> 1. rename your `test` to some other name, e.g. `mytests`
> 2. add the test submodule to another location, e.g. `test2`.  
> In this case, make sure you include the correct test directories in your Ant build file (next problem).

### 3. Build and Test Using Ant

1. Install Apache Ant from [ant.apache.org](https://ant.apache.org) if you don't already have ant installed.  The current version is 1.10.x. (`ant -v`).
2. Read [Hello World with Ant][hello-ant] for introduction to Ant syntax.
3. Create an Ant `build.xml` file in your TicTacToe project.    
   Define these targets:
```
clean   - remove compiler output (*.class) and the build directory
init    - create build directory
compile - compile the source code
test-compile - compile unit test code in test/ directory
test    - run JUnit tests
```
   * You can use the [https://github.com/jbrucker/demo-ci][demo-ci] build file as template to get started.  Edit the file and customize for your project.
4. Use Ant to build the project and run Junit tests.
   * I may ask you to demonstrate this to me before you leave today

### 4. Use named properties for directories

1. Define properties in `build.xml` for directories.  See [Enhance the build file][hello-ant-enhance] in [Hello World with Ant][hello-ant].
2. Replace constants with property values **everywhere** in your build file.

| Property Name  | Value      | Usage         |
|----------------|------------|---------------|
| src.dir        | "src"      | Source code directory |
| build.dir      | "bin"      | Compiled code and other runtime resources |
| lib.dir        | "lib"      | Location of Libraries (junit jars) used in project |
| dist.dir       | "."        | Location of runnable Jar of this project |
| test.src.dir   | "test"     | Unit test source code directory |
| test.build.dir | "bin/test" | Compiled unit test classes |

For example
```xml
<property name="src.dir"  location="src" />
<javac srcdir="${src.dir}" destdir="${build.dir}" includeantruntime="false" />
```

### 5. Define a "jar" Target in Ant Build File

1. Add a target named `jar` that creates a **runnable** TicTacToe.jar file from the code.
2. Create the Jar file in the project root directory.
3. Jar must be runnable!  Specify the "Main-Class" in the Jar's Manifest file.
4. Jar doesn't need test classes! Exclude test classes from the JAR using "excludes=*pattern*".  See [Ant Jar][ant-jar] manual page for how to do this.
```xml
<target name="jar" depends="TODO" 
        description="Create runnable JAR file of project">
    <jar destfile="TODO/TicTacToe.jar"
         basedir="base dir containing all the stuff to put in jar file">
         <manifest>
            <TODO see tutorial for how to specify the main class in Jar/>
         </manifest>
    </jar>
</target>
```
5. The Jar file needs the `.fxml` files, so ant should **copy** those files from the `src` tree to the `bin` tree.  This should really be part of the "compile" task, so add it there.
```xml
<target name="compile" ... />
    <javac ...>
       compile source
    </javac>
    <!-- copy fxml files from src tree to build tree, including subdirs -->
    <copy todir="destination dir">
       <fileset dir="source dir">
          <include name="**/*.fxml" />
       </fileset>
    </copy>
</target>
```

You should be able to run the jar using `java -jar TicTacToe.jar`.

See: [Jar task][ant-jar], [Copy task][ant-copy], and [Hello World with Ant][hello-ant].

### 6. Add Automatic Testing using Travis CI

1. Read the Travis CI [Getting Started](https://docs.travis-ci.com/user/getting-started/) guide. (It is short.)
2. Create a Travis CI account according to instructions in *Getting Started*.
3. Give Travis access to some or all of your Github projects.
   * Your choice: you can grant access to everything or just specific projects.
   * At least include the tictactoe project.
4. On Github, under your *Personal Settings* (not repository settings), in the "Applications" category, verify that Travis CI has been added.
5. In your TicTacToe project, add a `.travis.yml` file containing configuration information.  You can use the file in [demo-ci][demo-ci] to get started, but you need to edit it for your project.
6. Verify that Travis is building and testing your project.

> Fatalai Jon reported that when he did this, Travis would not build his
> TicTacToe project.
> He solved it by clicking the "More Options" box on right side of the Travis CI page, 
< and select "Trigger Build".
> He accepted the default settings and clicked "Trigger custom build". It worked.

### 7. Display Travis CI Status in project README.md

1 In the `README.md` of your Github project, add an icon that shows the start of the latest Travis CI build.  If you click on the icon, it should open the Travis CI web page for the project.

### 8. Fix your TicTacToe Game

If your TicTacToe game passed all tests: *Congratulations!*

Otherwise, fix your source code and push to Github.  Watch as Travis automatically rebuilds and tests the project.

### What to Submit

The `build.xml`, `.travis.yml`, and test submodule should be included in your TicTacToe repostiory. 

### Questions

1. On Github there is repo with name https://github.com/fatalaijon/tictactoe.
What should be the URL is on Travis-CI?
2. In Ant, why write the `copy` task (to copy FXML file, property files, settings files, and images) as part of the "compile" target instead of putting the `copy` task in the `jar` target?

[demo-ci]: https://github.com/jbrucker/demo-ci "Travis CI Sample Project"
[hello-ant]: https://ant.apache.org/manual/tutorial-HelloWorldWithAnt.html "Hello World with Ant (Tutorial)"
[hello-ant-enhance]: https://ant.apache.org/manual/tutorial-HelloWorldWithAnt.html#enhance "Hello World with Ant (Tutorial)"
[ant-jar]: https://ant.apache.org/manual/Tasks/jar.html "Jar task manual page"
[ant-copy]: https://ant.apache.org/manual/Tasks/copy.html "Ant copy task"
[git-submodules]: https://git-scm.com/book/en/v2/Git-Tools-Submodules
[working-with-submodules]: https://blog.github.com/2016-02-01-working-with-submodules/

