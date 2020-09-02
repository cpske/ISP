---
title: Feedback on Git Remote Commands Assignment
---

Question 5. **What are the steps to resolve the problem in the previous problem?**

There were many incorrect or incomplete answers to this.
I deducted 1 or 2 points, depending on the answer.

This answer is incorrect:

```
cmd> git pull
cmd> git push
```
in actuality:
```
cmd> git pull
CONFLICT (content): Merge conflict in README.md
cmd> git push
Error: ... (haven't merged yet)
```
---
Also incorrect:

```
cmd> git fetch
cmd> git add README.md
cmd> git commit -m "..."
cmd> git push
```
In actuality, `git push` fails because the branches are still diverged.

---

Also incorrect:

```
cmd> git pull origin master
cmd> git add README.md
cmd> git commit
cmd> git fetch origin master
cmd> git rebase origin/master
cmd> git push origin master
```

In actuality:
```
cmd> git pull origin master
CONFLICT (content): Merge conflict in README.md

cmd> git add README.md
(You didn't fix the conflict yet so this corrupts README in the repo!)
cmd> git commit

cmd> git fetch origin master
From https://github.com/fatalaijon/ku-polls
 * branch            master     -> FETCH_HEAD
cmd> git rebase origin/master
First, rewinding head to replay your work on top of it...
Applying: fix typo
Using index info to reconstruct a base tree...
M	README.md
Falling back to patching base and 3-way merge...
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
error: Failed to merge in the changes.
Patch failed at 0001 fix typo
Use 'git am --show-current-patch' to see the failed patch

cmd> git push origin master
```

