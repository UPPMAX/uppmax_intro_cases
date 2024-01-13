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

- [](http://docs.uppmax.uu.se/cluster_guides/modules/){:target="_blank"}


## Installed software
- You can also find (almost) all installed software at:
    <https://www.uppmax.uu.se/resources/software/installed-software/>
``````{challenge} Hands on using a tool
1. use matlab

```  {code-block} console
$ matlab &
```
- Does not work!
- Load module first
```  {code-block} console
$ module avail matlab
```
- `module load matlab` will start <u>D</u>efault version (often latest) demarked with a D in the list
- Let's load a specific version, often good for reproducibility.

```  {code-block} console
$ module load matlab/R2020b

$ matlab &
```
- Matlab starts (if X11 is active)

2. use Samtools

``` {code-block} console
$ module load samtools

        "These module(s) or extension(s) exist but cannot be loaded as requested: "samtools""
```
```  {code-block} console
$ module load bioinfo-tools samtools
```
- Bioinformatic tools are hidden by default

``````
  
## Installed databases
- [Installed databases at UPPMAX](http://docs.uppmax.uu.se/databases/overview/)
    


## Run own scripts or programs
- Unless your script or program is in the active path, you run it by the full path or `./<file>` if you are in the present directory.

```{challenge} Demo: Run a Fortran program 
- Run the program "sunray" located in: `/proj/introtouppmax/labs/sunray`
```
``````{solution}
- 2 alternatives
```  {code-block} console
 /proj/introtouppmax/labs/sunray
 
 cd /proj/introtouppmax/labs/
 ./sunray
```
``````

```{keypoints}
- Centrally installed software are reached through the module system and available throughout all nodes.
- Your own installed software, scripts, python packages etcetera are available from their paths.
```
