#IAM roles and policies for SageMaker and other services

{
  "Version": "2023-11-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "sagemaker:*",
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": "s3:*",
      "Resource": ["arn:aws:s3:::MLOPs/*"]
    }
  ]
}
