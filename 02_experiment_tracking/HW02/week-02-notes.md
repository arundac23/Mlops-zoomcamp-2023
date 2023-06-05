## Definition of Experiment Tracking

***Experiment tracking*** (ET) is the process of keeping track of all the ***relevant information*** from an ***ML experiment***, which may include:
* Source code
* Environment
* Data
* Hyperparameters
* Metrics

## Why is Experiment Tracking important?

There are 3 main reasons for tracking experiments:
* `Reproducibility`: as data scientists, we want our experiments to be repeatable in the future in order to verify our results.
* `Organization`: if you're collaborating with a team, it's important that everyone knows where to find what. And even if you're working alone, you may want to go back to previous work, and having it organized it helps tremendously.
* `Optimization`: the usage of experiment tracking tools allows us to create more efficient workflows and automate certain steps which are usually performed manually.

## Tracking experiments with MLflow

The Tracking module allows us to organize our _experiments_ into _runs_. A ***run*** is a trial in a ML experiment. An ***experiment*** is made of runs, and each run may keep track of:
* Parameters (both hyperparameters as well as any other relevant parameters such as data paths, etc)
* Evaluation metrics
* Metadata (e.g. tags for organizing your runs)
* Artifacts (e.g. visualizations)
* Models

Along with all of the above data, MLflow also logs additional information abour the run:
* Source code (name of the file used for the experiment)
* Code version (git commit)
* Start and end time
* Author
