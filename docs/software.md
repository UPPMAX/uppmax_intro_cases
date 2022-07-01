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


### Spack

### Own development...


