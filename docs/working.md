# Working on UPPMAX 

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
