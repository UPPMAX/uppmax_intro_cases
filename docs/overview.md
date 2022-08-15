# Overview

```{questions}
- What is UPPMAX?
- What is SNIC?
- What is a cluster?

```

```{objectives}
- We'll get an overview of UPPMAX and SNIC and how a computer cluster works
```


**UPPMAX = UppMACS**
- [Uppsala Multidisciplinary Center for Advanced Computational Science](http://uppmax.uu.se)

## SNIC
- SNIC — the Swedish National Infrastructure for Computing
- SNIC and Uppsala University fund UPPMAX. — UU’s supercomputing centre.
- Mission for SNIC: to provide a quality high-performance computing environment nationally

## UPPMAX missions
- Run the clusters placed in Uppsala.
- More details in the afternoon about Organisational orienteering!

    
## UPPMAX systems

- Clusters
  - Rackham (general purpose)
    - Snowy (Long runs and GPU:s)
  - Bianca (sensitive data)
    - Miarka (new for LifeScience)
- Storage
  - On-load directly connected to the clusters
  - Off-load for large data not needed for computation analysis anymore
- Cloud
  - Dis (region EAST-1)

## High Performance Computing — HPC
### What is a cluster?

- A network of computers, each computer working as a **node**.

- From small scale RaspberryPi cluster
     
![RaspBerry](./img/IMG_5111.jpeg)

- To supercomputers like Rackham.

![Rackham](./img/uppmax-light2.jpg)

- Each node contains several processor cores and RAM and a local disk called scratch.

![Node](./img/node.png)

- The user logs in to **login nodes**  via Internet through ssh or Thinlinc.

  - Here the file management and lighter data analysis can be performed.

![RaspBerry](./img/nodes.png)

![RaspBerry](./img/Bild1.png)

- The **calculation nodes** has to be used for intense computing. 

```{keypoints}
- SNIC makes available large-scale high-performance computing resources, storage capacity, and advanced user support, for Swedish research. 
- UPPMAX rund the local resources placed at Uppsala Universtiy
- A cluster consists of several interconnected computers that can work individually or together.
```

