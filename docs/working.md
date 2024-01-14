# Working on UPPMAX 

```{objectives}
- Let's get some tips and best practices
```

```{instructor-note}
- Approx timing: 14.30-14:45
- Information
```

## ``$HOME`` dir and project dir

### Quota
- Disk usage and number of files
- ``$HOME`` has always 32 GB and 300,000 files
- You typically have one project per project, their size dependent on type of project
- Compute projects both have disk space (128 GB) and computing time attached to them
- Check your quota with

```{code-block} console
$ uquota
```


### Core hours
- You  get core hours only from compute project
- When they are used you can still get "BONUS" jobs if the resources allow.
- You can find your current projects (and other projects that you have run jobs in) with the program ``projinfo``.

```{code-block} console
$ projinfo [<username>]
```

or
```{code-block} console
$ projinfo [<project name>]
```
- For example, if your project is named NAISS 2017/1-334 you specify ``naiss2017-1-334``
  
## What kind of work will you perform?

```{uml}
@startuml
start

:login;
:Rackham login Node;
if (Do CPU/memory intensive work) then (yes)
  :Use calculation node;
  if (Do interactive work) then (yes)
    :$ interactive -A <proj> <options>;
  else (no)
    :Make a batch script;
    :$ sbatch <script>;
  endif 
else (no)
  :Stay on login node and load your module(s):
  $ module load <software/tool>;
  :Run tool: 
  $ <toolname> [- options, input, output];
endif
:finish;
stop
@enduml
```

### UPPMAX Cluster overview again!

```{mermaid}

graph TB

  Node1 -- interactive --> SubGraph2Flow
  Node1 -- sbatch --> SubGraph2Flow
  subgraph "Snowy"
  SubGraph2Flow(calculation nodes) 
        end

        thinlinc -- usr-sensXXX + 2FA----> SubGraph1Flow
        Node1 -- usr-sensXXX + 2FA----> SubGraph1Flow
        subgraph "Bianca"
        SubGraph1Flow(Bianca login) -- usr+passwd --> private(private cluster)
        private -- interactive --> calcB(calculation nodes)
        private -- sbatch --> calcB
        end

        subgraph "Rackham"
        Node1[Login] -- interactive --> Node2[calculation nodes]
        Node1 -- sbatch --> Node2
        end
```



## Common problems

- Conda environment clashes with loaded python modules
- Forgotten environment variables defined in your `.bashrc` may give unexeptected errors when you run other programs or new versions of a program
- A full ``$HOME`` folder may cause unexpected errors
  - check with ``uquota``
 
````{tip}

**.bashrc**

- Do not fill ``~/.bashrc`` with too much
  - Avoid loading modules, unless you are totally sure that those will not interact with other things you are doing
  - Typical problem: loading several conflicting conda environments and python modules 
- Good place to have:
  - aliases
  - source files (if needed)
    - these can set some environment variables

- Example from Björn C

```bash
alias lt='ls -lrt'
alias sq='squeue -u $USER'
alias sc='scancel'
alias rm='rm -i'
alias less='less -R'
```

- When done, start a new bash session in a new terminal or type ``bash`` in the present one.


**Conda**

- You cannot mix Conda environments with python software module
- Conda is very nice for Bianca, because of the ease of install packages without the internet connection.
- For Rackham we suggest Python virtual environemnts with virtualenv, see [Python course](https://uppmax.github.io/R-python-julia-HPC/python/isolated.html)
  - Unless the conda environment is straight-forward to install and is well-defined.


**Things worked before but do not now**

- Check ``uquota`` !
- Very often a full disk space is the reason

````

```{discussion}
- Any input from other teachers!
``` 

```{keypoints}
- Use your disk spaces wisely
  - home folder just for general stuff and files needed by several projects
    - always read and write protected for others by default
  - otherside project folder which will more easily become public for others
    - by default available for all project members.
- Use the computing resources wisely
  - low intensity work on login node
  - high intensity work on compute nodes (core hours are counted)
    - for development use the interactive sessions
    - otherwise make batch jobs!
```
