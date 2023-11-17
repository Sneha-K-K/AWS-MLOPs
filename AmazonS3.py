#For storing datasets in Amazon S3 using the AWS SDK for Python (Boto3)

import boto3

# Create an S3 client
s3 = boto3.client('s3')

# Specify the bucket and object key
bucket_name = 'MLOPs'
object_key = 'D:/CMI/Sem_3/ADA/MLOPs.csv'

# Upload the dataset to S3
s3.upload_file('local/MLOPs.csv', bucket_name, object_key)