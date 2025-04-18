from Mlflow_Ineuron_Project.entity.config_entity import Data_preprocessing_ValidationConfig
from Mlflow_Ineuron_Project import logger
import os
import pandas as pd
from Mlflow_Ineuron_Project import logger
from  sklearn.preprocessing import LabelEncoder 



class Data_preprocessing_Validation:
    def __init__(self, config: Data_preprocessing_ValidationConfig):
        self.config = config


    def validate_all_columns(self)-> bool:
        try:
            validation_status = None

            data = pd.read_csv(self.config.unzip_data_dir)
       # remove the extra space around the columns 
            data.columns=data.columns.str.strip()

            numerical_col=['age','fnlwgt', 'capital-gain', 'capital-loss', 'hours-per-week']

            categorical_col=['workclass', 'education', 'marital-status', 'occupation', 'sex', 'country','salary']
            # for col in categorical_col:
            #     if col in data.columns:
            #         data[col] = data[col].str.lower()
            #     if col in data.columns:
            #         data[col] = data[col].str.lower() 
            # print(data.head())
            data.drop(columns=['relationship', 'race','education-num'], inplace=True)

            # label encoding 
            for i in categorical_col:
                le=LabelEncoder()
                data[i]=le.fit_transform(data[i])
            
            
            
            # print(data.info())

            all_cols = list(data.columns)

            all_schema = self.config.all_schema.keys()

            print(all_schema)
            for col in all_cols:
                print(col)
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")


            data.to_csv(os.path.join(self.config.Preprocess_data,"preprocessed_data.csv"),index=False)

            return validation_status
        
        except Exception as e:
            raise e

