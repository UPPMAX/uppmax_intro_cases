# Software and tools
```{objectives}
- We'll briefly get overviews over 
    -  software tools on UPPMAX
    -  databases
- Introduction quide for installing own software or packages
- Very short introduction to developing old programs
```

- 800+ programs and packages are installed.
- To avoid chaos and collisions, they are managed by a **module system**.
- This system keeps installed software hidden by default, and users have to explicitly tell their terminal which version of which software they need.
- The modules are most often available across cluster (except for Miarka)


```{note}
- Bioinformatics tools require loading the “bioinfo-tools” module first.
```

## Modules

- [Software at UPPMAX](https://www.uppmax.uu.se/resources/software/)
- [Module system](https://www.uppmax.uu.se/resources/software/module-system/)

### Some commands

- `module avail`  — list all modules

- `module avail <part of tool name>` — search for modules (full name not needed and case insensitive)

- `module load <module name>` — Loads the module

- `module unload <module name>` — Unloads the module

- `module list` — Lists loaded modules

- `module help <module name>` — Displays a brief module-specific help
 
- `module spider <part of tool name>` — like "avail" but "stronger"


## Installed software
- You can also find (almost) all installed software at:
    <https://www.uppmax.uu.se/resources/software/installed-software/>
  
## Installed databases
- [Installed databases at UPPMAX](https://www.uppmax.uu.se/resources/databases/)
    
``````{challenge} Hands on using a tool
1. use matlab

```
$ matlab &
```
- Does not work!
- Load module first
```
$ module avail matlab

$ module load matlab/R2020b

$ matlab &
```
- Matlab starts (if X11 is active)
- `module load matlab` will start default version (often latest)

2. use Samtools

```
$ module load samtools
```
        "These module(s) or extension(s) exist but cannot be loaded as requested: "samtools""
```
module load bioinfo-tools samtools
```
- Bioinformatic tools are hidden by default

``````

## Install software yourself
- You can install in your home directory.
  - This is handy for personal needs, low numbers of files (i.e. not Conda).
- Usually better to install in project directory.
  - This way the project contains both data and software — good for reproducibility, collaboration, and everyone's general sanity.

### Python packages
- [Python packages](https://uppmax.uu.se/support/user-guides/python-user-guide/)

#### Conda
- [Conda user guide](https://www.uppmax.uu.se/support/user-guides/conda-user-guide/)

### "Containers"
#### Singularity
- [Singularity user guide](https://www.uppmax.uu.se/support/user-guides/singularity-user-guide/)

#### Docker
- Docker will unfortunately not work on the clusters, since it requires root permission.

### Build from source
- We have several compiler versions from GNU and INTEL
- [Guide for compiling serial and parallel programs](https://www.uppmax.uu.se/support/user-guides/mpi-and-openmp-user-guide/)
    
### Spack
- The UPPMAX staff has already other ways to install most software applications. 
- Please use Spack only if other ways to install your tool is not possible or very difficult, e.g. requiring very many dependencies and it is not available through, e.g. Easybuild.
- [Spack user guide at UPPMAX](https://www.uppmax.uu.se/support/user-guides/spack-on-uppmax/)

### Own development...
- You may have your own code that you want to run on UPPMAX.
- See the [guide for compiling serial and parallel programs](https://www.uppmax.uu.se/support/user-guides/mpi-and-openmp-user-guide/)
- [User guide for debuggers and profilers](https://www.uppmax.uu.se/support/user-guides/debuggers-and-profiling-tools/)

## Run own scripts or programs
- Unless your script or program is in the active path, you run it by the full path or `./<file>` if you are in the present directory.

```{challenge} Demo: Run a Fortran program 
- Run the program "sunray"
```
``````{solution}
```
./sunray
```
``````
