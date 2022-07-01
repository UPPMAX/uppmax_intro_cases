# Software and tools

- 800+ programs and packages are installed.
- To avoid chaos and collisions, they are managed by a module system.
- This system keeps installed software hidden by default, and users have to explicitly tell their terminal which version of which software they need.
- Note: Bioinformatics tools require loading the “bioinfo-tools” module first.

## Modules

- [Software at UPPMAX](https://www.uppmax.uu.se/resources/software/)
- [Module system](https://www.uppmax.uu.se/resources/software/module-system/)

Some commands:

- module spider <name> — search for modules

- module avail  — list all modules

- module load <module name> — Loads the module

- module unload <module name> — Unloads the module

- module list — Lists loaded modules

- module help <module name> — Displays a brief module-specific help


## Installed software
- You can also find (almost) all installed software at:
    https://www.uppmax.uu.se/resources/software/installed-software/
  
## Installed databases
- [Installed databases at UPPMAX](https://www.uppmax.uu.se/resources/databases/)

## Install software yourself
- You can install in your home directory.
  - This is handy for personal needs, low numbers of files (i.e. not Conda).
- Usually better to install in project directory.
  - This way the project contains both data and software — good for reproducibility, collaboration, and everyone's general sanity.

### Python packages
[Python packages](https://uppmax.uu.se/support/user-guides/python-user-guide/)

#### Conda
- [Conda user guide](https://www.uppmax.uu.se/support/user-guides/conda-user-guide/)

### "Containers"
#### Singularity
- [Singularity user guide](https://www.uppmax.uu.se/support/user-guides/singularity-user-guide/)

#### Docker
Docker will unfortunately not work on the clusters, since it requires root permission.

### Build from source

#### Rackham

- Also on Snowy in *italic*
- Also on Snowy AND Bianca in ***bold***

| GCC  | openmpi | 
| -----| -----   | 
4.8.2  |  *1.7.4*
5.2.0  |  *1.8.8*
5.3.0  |  ***1.10.1***
5.5.0  |  1.10.3
6.3.0  |  ***2.0.1***, 2.0.2, ***2.1.0***
6.4.0  |  2.1.1
7.1.0  |  2.1.0, 2.1.1
7.2.0  |  2.1.1, 2.1.2, 3.0.0
7.3.0  |  2.1.3, 3.0.0, *3.1.0*
7.4.0  |  ***3.1.3***
8.1.0  |  3.0.1, 3.1.0
8.2.0  |  3.0.2, 3.1.0, *3.1.1*, ***3.1.2***, ***3.1.3***, 4.0.0
8.3.0  |  ***3.1.3***
8.4.0  |  3.1.5, 4.0.2
9.1.0  |  3.1.3
9.2.0  |  *3.1.3*, *3.1.4*, 3.1.5, 4.0.2
9.3.0  |  ***3.1.5***, *4.0.2*, *4.0.3*
10.1.0 |  ***3.1.6***, *4.0.3*
10.2.0 |  *3.1.6*, *4.0.4*, ***4.1.0***
10.3.0 |  ***3.1.6***, ***4.0.5***, ***4.1.0***, *4.1.1*
11.2.0 |  ***4.1.1***, *4.1.2*

| Intel |   openmpi
| ----- |   -------
15.3    | 1.10.0, 1.10.1, 2.1.0
16.1    | 1.10.1, 1.10.2
17.1    | 2.0.1, 2.0.2,
17.2    | 2.0.2, 2.1.0
17.4    | 2.1.1, 3.0.0
18.0    | 3.0.0
18.1    | 2.1.2, 2.1.3, 3.0.0
18.2    | 2.1.3, 3.0.0, 3.1.0
18.3    | 3.0.2, 3.1.0, 3.1.1, ***3.1.2***, ***3.1.3***
19.4    | *3.1.4*
19.5    | 3.1.4
20.0    | 3.1.5, 3.1.6, *4.0.3*, 4.0.4
20.2    | ***3.1.6***, ***4.0.4***
20.4    | ***3.1.6***, ***4.0.4***, *4.1.0*, *4.1.1*

### Spack

### Own development...


