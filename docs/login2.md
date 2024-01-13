# Login

```{questions}
- How to reach UPPMAX clusters?
- Where do I arrive when I log in? Login or calculation node?
- What clients should/could I use for my work at UPPMAX?
- How can I enable graphics?

```

```{objectives}
- We'll go through platform specific (Mac/Linux/Windows) ways to log in to UPPMAX
- See different clients
- Enable graphics
- Try yourself!
```

```{instructor-note}
- Approx timing: 9:25-10.00
- Demos/type-alongs
```

```{note}
If you lack a user account, visit the [Getting started page](https://www.uppmax.uu.se/support/getting-started/course-projects/)
```

## General understanding

- When logging in to UPPMAX from your local computer you will arrive to your home folder at the login node.
- This means that only light analysis and and calculations should be made here.
- You will see this in the prompt after "@" as the clustername and a low number. For instance:
   ```console
      [<user>@rackham3 linux_tutorial]$
    ```
- You will later learn how to reach the calculation nodes. Then the prompt states the node number with a single letter, like "r" for Rackham. For instance:
   ```console
      [<user>@r484 linux_tutorial]
   ```


## The login

```{discussion} Login procedure
   **Which login procedure is best for You, depends on:**
   - Your background
   - Your OS environment,
   - Your planned interaction with your local computer
   - Your planned use of graphics on the cluster
```

- We will use Rackham for the course

```{admonition} See the documentation
- [Get inside SUNET](http://docs.uppmax.uu.se/getting_started/get_inside_sunet/)
- [Log in to Rackham](http://docs.uppmax.uu.se/getting_started/login_rackham/)
```

## Exercises

```{challenge} Log in with a ternminal
  - Use any tool that you have installed
```

```{challenge} Log in with a ternminal but enable graphics
- Use any tool that you have installed <http://docs.uppmax.uu.se/getting_started/login_rackham/#terminal-with-x11-server-and-light-graphics>
```
```{solution}
- First try:
```console
$ ssh -Y <username>@rackham.uppmax.uu.se
```
- If you receive errors or warnings, instead try:
```console
$ ssh <username>@rackham.uppmax.uu.se
```
- If you do have X11 installed:
```console
$ xeyes &
```

```{challenge} Try Thinlinc from web
- Try the web version now if you don't already have the software installed!
- <http://docs.uppmax.uu.se/getting_started/login_rackham/#thinlinc-all-platforms>
```

```{admonition} Login procedure
   If you plan to:
   - do **day-to-day** work where *terminal shell is sufficient*
     - Mac: *Terminal, iTerm2*
     - Linux: *Terminal*
     - Windows: *Putty*, *Windows Powershell* or even *command prompt (CMD)*
     
     
   - **interact with your local computer**
     - Mac/Linux: you can always work in a local shell (mutiple terminal windows open)
        - (S)FTP browser: *Filezilla*, *Cyberduck*
     - Windows
        - (S)FTP browser: *WinSCP*
        - *MobaXterm* has built-in SFTP browser
        - you may benefit from having a *Windows Subsystem for Linux, WSL(2)*
        
        
   - **do day-to-day work** with **some graphical applications (X forwarding)**
     - Mac: *Terminal, iTerm2 + XQuartz*
     - Linux: *Terminal*
     - Windows: *MobaXterm*
     
     
   - integrate you cluster work with **code development**
     - All OS: Example *Visual Studio Code*
     
     
   - use **sophistic graphical interfaces** like *RStudio and MATLAB* etcetera
     - *ThinLinc application*
     
     
   - use **Bianca**
     - *ThinLinc from web*
   
```


 ```{keypoints}
- When you log in from your local computer you will always arrive at a login node with limited resources. 
  - You reach the calculations nodes from within the login node (See  Submitting jobs section)
- You reach UPPMAX clusters either using a terminal client or Thinlinc
- Graphics are included in Thinlinc and from terminal if you have enabled X11.
- Which client to use?
  - Graphics and easy to use
    - ThinLinc
  - Best integrated systems
    - Visual Studio Code has several extensions (remote, SCP, programming IDE:s)
    - Windows: MobaXterm is somewhat easier to use.
  
```
