## PREFECT
Prefect is an open-source workflow management system for orchestrating and managing data workflows. It provides a way to define, schedule, and run workflows as code in Python. Prefect allows you to build complex data pipelines by defining tasks, dependencies between tasks, and the overall workflow structure.

Prefect enables you to build and observe resilient data workflows so that you can understand, react to, and recover from unexpected changes. It's the easiest way to transform any Python function into a unit of work that can be observed and orchestrated. Just bring your Python code, sprinkle in a few decorators, and go!

## What is Workflow Orchestration?
Building a ML system has a lot of moving parts. We have to deal with data collection, data preprocessing, model training, model serving, etc. Each of these steps can be further broken down into sub-steps. For example, data preprocessing can be broken down into feature engineering, feature selection, etc.

Workflow Orchestration is the process of automating and managing the flow of work across these steps. It helps us build complex workflows by combining multiple steps together. It also helps us manage the dependencies between these steps.
![image](https://github.com/arundac23/Mlops-zoomcamp-2023/assets/76126029/e5bca18b-5929-4b55-90d1-28af4bb3af79)

## Negative Engineering
Inspite of building a robust system, there are chances that something might go wrong. For example, the data might not be available, the model might fail to train, etc.
![image](https://github.com/arundac23/Mlops-zoomcamp-2023/assets/76126029/9ab022d1-563a-427a-aa17-6b8df1ef824f)

Worflow Orchestration tools provide set of features off the shelf that aim to eliminate the need for negative engineering. These tools provide features like retries, notifications, logging, lineage tracking, etc. out of the box.

