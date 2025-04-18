#ML project with MLflow

## Workflow

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline 
8. Update the main.py
9. Update the app.py


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/End-to-end-Machine-Learning-Project-with-MLflow
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=
MLFLOW_TRACKING_USERNAME=
MLFLOW_TRACKING_PASSWORD= 
python script.py

Run this to SET as env variables in the VS code Env...

```bash

set MLFLOW_TRACKING_URI=https://dagshub.com/ShreyasDominator/End_to_End_project_with_Mlflow.mlflow
set MLFLOW_TRACKING_USERNAME=ShreyasDominator
set MLFLOW_TRACKING_PASSWORD=c79b27cd042d93400b3a1099115f3899a027693f
```