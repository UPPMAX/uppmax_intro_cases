# Linux and basic toolkit

- The "operating system" of the UPPMAX and most of the other clusters is **Linux**.

```{questions}
- What is Linux?
- How to use the command line?
```

```{objectives}
- We'll briefly get an overview of Linux
  - How the command line works
  - Some text editors
  - Things to be aware of
```

```{instructor-note}
- Approx timing: 10:10-10:40
- Theory and type-along
```

```{admonition} See the documentation
- <http://docs.uppmax.uu.se/getting_started/linux/>
```

```{tip}
- TAB complete:
  - Whenever you’re writing a path or filename on the bash prompt, you can strike the ‘tab’ key to ask Bash to complete what you’re writing.
  - Get in the habit of this — it will save you many hours!

**These commands are useful in the command line when something is stuck or a program is limiting you to do further work.**
- ``ctrl-C`` interupts a program or a command that is "stuck"
- ``ctrl-Z`` pauses a program, can be continues in background (``bg``) or  foreground (``fg``)
- ``ctrl-D`` quits some programs
```


```{Warning}
  
- There is no undo for:
  - copy (`cp`),
  - move (`mv`), and
  - remove (`rm`).
- **Beware of overwriting files and deleting the wrong ones.**
```

```{Note}
- **Tip: make "`rm`" ask if you really want to erase:**
  - Within a session: Type in the command prompt

        alias rm='rm -i'

  - Override asking with 

        rm –f <>

  - Edit file `.bashrc` in `home` directory by adding the alias line for this to start everytime.
- This will also work for ``mv`` and ``cp``!
```


```{Note}
- If you do destroy your data, email UPPMAX support, we may be able to help.
```

 ```{keypoints}
- Linux Operating system is a UNIX-like and UNIX compatible Operating system.
- Typical command:
    $ program word1 word2 word3 […]
- Example of file editors
    - terminal
        - nano
        - vim
        - emacs
    - graphical:
      - gedit
- Tips
    - use Tab completion
    - capitalization and spaces matters
    - no undo:s for copying, moving and removing
      - Solution: ``alias rm='rm -i' ``
```



## Basic toolkit

```{objectives}
- Let's dig into the most important BASH commands
- We'll do a type-along session
```

```{instructor-note}
- Approx timing: 10:40-11.30
- Type-alongs
```

## We will cover these commands
### Navigation and file management

1. `pwd`  &emsp; present directory
1. `ls`  &emsp;list content
1. `cd`  &emsp;change directory
1. `mkdir`  &emsp;make directory
1. `cp`  &emsp;copy
1. `scp`  &emsp;securely remotely copy
1. `mv`  &emsp;move
1. `rm`  &emsp;remove
1. `rmdir`  &emsp;remove empty directory

### Read files and change file properties

10. `cat`  &emsp;print content on screen
11. `head`  &emsp;print first part
12. `tail`  &emsp;print last part
13. `less`  &emsp;browse content
14. `tar`  &emsp;compress or extract file
15. `chmod`  &emsp;change file permissions
16. `man`  &emsp;info about a command


```{admonition} See the documentation
- <http://docs.uppmax.uu.se/getting_started/linux_basics/>
```
 
```{challenge} chmod — Hands-on

- In your *locally created* ``linux_tutorial`` directory, find important files and old saved data that you wouldn’t want to lose (*imagine*).
  - Directories: important_results/, old_project/
  - File: last_years_data
- Use chmod to remove write permission from those files and directories (use the `-R` flag (not `-r`) to also do the files in the directories).
  - Take a moment to play around with chmod and explore the effects of permissions on files and directories.
```

``````{solution}
``` {code-block} console
$ chmod -wR <target>
```
``````

``````{solution} For the interested

- Now try:

```console
$ ls -l /proj/introtouppmax/
```

- Huh, ``rwxrwsr-x``?
- `s` in the group means `x` but with *gid bit set* ( g roup id of creator not launcher).
- The s or sticky bit is a group permission on directories which changes the default behaviour of new files are created with the same group_id as the users group_id to new files inheriting the group_id from the parent directory.
- `S` means `-` with gid bit set (rarely seen).
- Among other things, this makes the default group for new files/subdirectories the, for instance, ``p_introtouppmax`` group.
``````

 
**More about BASH command line and scripts on Tuesday and Wednesday!**
https://www.uppmax.uu.se/support/courses-and-workshops/uppmax-introductory-course/
