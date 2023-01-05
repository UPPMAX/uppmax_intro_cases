# Working on UPPMAX 

## $HOME dir and project dir

### Quota
- Disk usage and number of files
- $HOME has always 32 GB and 300,000 files
- You typically have one project per project, their size dependent on type of project
- Compute projects both have disk space and computing time attached to the project

### Core hours
- You  get core hours only from compute project
- When they are used you can still get "BONUS" jobs if the resources allow.

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
  :Stay on login node and laod your module(s):
  $module load <software/tool>;
  :Run tool: 
  $<toolname> [- options, input, output];
endif
:finish;
stop
@enduml
```

```{keypoints}
- Use your disk spaces wisely
  - home folder just for general stuff and files needed by several projects
    - always read and write projected by other by default
  - otherside project folder which will more easily become public for other's
    - by default available for all project members.
- Use the computing resources wisely
  - low intensity work on login node
  - high intensity work on compute nodes (core hours are counted)
    - for development use the interactive sessions
    - otherwise make batch jobs!
```

## Common problems

- Conda environment clash with loaded python modules
- Forgotten environment variables defined in your `.bashrc` may give unexeptected errors when you run other programs or new versions of a program
- A full $HOME folder may cause unexpeced errors
  - check with ``uquota``
