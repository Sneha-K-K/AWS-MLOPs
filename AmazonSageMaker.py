#Amazon SageMaker for model training

import sagemaker
from sagemaker import get_execution_role
from sagemaker.sklearn import SKLearn



# Get the SageMaker execution role
role = get_execution_role()

# Define the SKLearn Estimator
estimator = SKLearn(entry_point='train.py',role=role,instance_count=1,
                   instance_type='ml.m4.xlarge')
bucket_name = 'MLOPs'

# Set the local path of the file you want to upload
local_file_path = 'local/MLOPs.csv'

# Create a SageMaker session
sagemaker_session = sagemaker.Session()

# Upload the data to S3
input_data = sagemaker_session.upload_data(local_file_path, bucket=bucket_name,
                                           key_prefix='data')

# Train the model
estimator.fit({'training': input_data})