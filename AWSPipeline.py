#Code pipeline using AWS CloudFormation template:

Resources:
  MyCodePipeline:
    Type: "AWS::CodePipeline::Pipeline"
    Properties:
      Name: "MyMLOpsPipeline"
      RoleArn: "arn:aws:iam::123456789012:role/service-role/CodePipeline-Your-Role"
      Stages:
        - Name: "Source"
          Actions:
            - Name: "SourceAction"
              ActionTypeId:
                Category: "Source"
                Owner: "AWS"
                Version: "1"
                Provider: "CodeCommit"
              Configuration:
                RepositoryName: "MLOPs"
                BranchName: "main"