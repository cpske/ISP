Given a starting git repository, create a plain text containing
a sequence of git commands that will transform the starting repository
configuration into the final configuration.

Name of file: `update.sh`
This is called a "script".

I should be able to execute in a command shell such as bash, git-bash, 
zsh (on iOS) and it will do everything.  The last command should display
the files in the repository.

## Simple example

1. Starting Repository Contents
   ```
   ui.py           <--- todo: rename to "gui.py"
   theme.mp3
   Main.py
   ```
2. Desired final Repository Contents
   ```
   main.py
   view/
       gui.py
   ```

Script that would make these changes:
```
git mv Main.py main.py
# mkdir is the shell command to create a directory (not a git command)
mkdir view
git mv ui.py view/gui.py
git rm  theme.mp3
git add -u
git commit -m "restructure repository"
git ls-files
```

To run this file in a shell you would type:

```
bash update.txt
# if using zsh type:
zsh update.txt
```

You can also do this in a MS Windows `cmd` or Power Shell window,
but I can't verify the syntax for this.
