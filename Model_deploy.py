# Deploy the trained model to an endpoint

predictor = estimator.deploy(instance_type='ml.m4.xlarge', endpoint_name='MLOPS_endpoint')
