## Automatic Testing with Travis CI

### Prerequisite:  Take Ownership of your unittesting Github Repository

Travis-CI.com can only access projects owned by you.
You have "admin" rights on your Github repo for the unittesting assignment,
so you can take ownership.

1. Go to the repo URL on Github, such as https://github.com/ISP19/unittesting-fatalaijon
    > How to view the URL for remotes?    
    > `git remote -v`
2. Click "Settings" and select "Options" (usually shown by default).
3. At the bottom of the page ("Danger Zone") click "Transfer Ownership".
4. Transfer it to your own account.

**Should you update the remote for your local repo?**

When you take ownership, Github moves the repository from https://github.com/ISP19/someplace to https://github.com/*your_github_id*/someplace.  So the URL for "origin" in your local repo is not correct.  Or is it?

Github will redirect requests for the old repo URL to the new URL!
So so you don't *really* need to update the remote (works with HTTPS, haven't tested it with SSH).

But, if you want to update your local repo URL, use this command:
```
git remote set-url origin new_url_for_github_repo
```

### 1. Learn About Travis-CI

Read these two short articles.

* [Travis-CI Tutorial][travis-ci-tutorial] very short instructions how to get going.
* [Core CI Concepts for Beginners][travis-ci-concepts] - you can finish this later, but you **must** read it

Useful later:

* [Language-specific Guides][travis-ci-docs] at bottom of the page has additional info for [Python][travis-ci-python]

### 2. Create Account on travis-ci.com and Give Access to Selected Repos

1. Follow the instructions in [Travis-CI Tutorial][travis-ci-tutorial]
2. Give Travis access to some or all of your Github projects.
   * Your choice: you can grant access to everything or just specific projects.
   * At least include the `unittesting` project.
   * You can add more projects later (from Github) by granting access to Travis-CI.
3. On Github, under your *Personal Settings* (not repository settings), in the "Applications" category, verify that Travis CI has been added.
4. In your `unittesting` project, add a `.travis.yml` file containing configuration information.  You can use the file in [demo-pyci][demo-pyci] to get started, but you need to edit it for your project.
5. Verify that Travis is building and testing your project.

> Fatalai Jon reported that when he did this, Travis would not build his project.
> He solved it by clicking the "More Options" box on right side of the Travis CI page, 
< and select "Trigger Build".
> He accepted the default settings and clicked "Trigger custom build". It worked.

#### What is Travis Doing?

After you trigger a build, expect the "worker" item on the build page.
You can see that an incredible amount of work is being done just to set
up the environment to test your code.

### 3. Display Travis CI Status in project README.md

In the `README.md` of your Github project, add an icon that shows the start of the latest Travis CI build.  If you click on the icon, it should open the Travis CI web page for the project.

### 4. Fix your Code

If your project passed all tests, *Congratulations!*

Otherwise, fix your source code and push to Github.  Watch as Travis automatically rebuilds and tests the project.

### What to Submit

You should have a repository unittesting-your-githubid in your personal account with a Travis-CI "badge" shown on README.md.  When someone clicks on the badge it takes them to Travis CI build page for your project.

### Questions

1. On Github there is repo with name https://github.com/fatalaijon/tictactoe.
What **should be the URL** on on Travis-CI for this project?

[travis-ci-docs]: https://docs.travis-ci.com/
[travis-ci-tutorial]: https://docs.travis-ci.com/user/tutorial/
[travis-ci-concepts]: https://docs.travis-ci.com/user/for-beginners/, "Core CI Concepts for Beginners"
[travis-ci-python]: https://docs.travis-ci.com/user/languages/python/
[demo-ci]: https://github.com/jbrucker/demo-ci "Travis CI Sample Project"
[hello-ant]: https://ant.apache.org/manual/tutorial-HelloWorldWithAnt.html "Hello World with Ant (Tutorial)"
[hello-ant-enhance]: https://ant.apache.org/manual/tutorial-HelloWorldWithAnt.html#enhance "Hello World with Ant (Tutorial)"
[ant-jar]: https://ant.apache.org/manual/Tasks/jar.html "Jar task manual page"
[ant-copy]: https://ant.apache.org/manual/Tasks/copy.html "Ant copy task"
[git-submodules]: https://git-scm.com/book/en/v2/Git-Tools-Submodules
[working-with-submodules]: https://blog.github.com/2016-02-01-working-with-submodules/

