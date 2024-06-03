from aws_cdk import (
    Stack,
    aws_dynamodb as dynamodb,
    aws_lambda as _lambda,
    aws_apigateway as apigateway,
    CfnOutput,
    RemovalPolicy
)
from constructs import Construct

class PowerOfMathAppStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create DynamoDB table
        table = dynamodb.Table(self, "PowerOfMathTable",
            partition_key=dynamodb.Attribute(name="ID", type=dynamodb.AttributeType.STRING),
            removal_policy=RemovalPolicy.DESTROY
        )

        # Create Lambda function
        lambda_function = _lambda.Function(self, "PowerOfMathFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="lambda_function.lambda_handler",
            code=_lambda.Code.from_asset("lambda"),
            environment={
                'TABLE_NAME': table.table_name
            }
        )

        # Grant the Lambda function read/write permissions to the DynamoDB table
        table.grant_read_write_data(lambda_function)

        # Create API Gateway
        api = apigateway.RestApi(self, "PowerOfMathAPI",
            rest_api_name="Power Of Math Service",
            description="This service calculates the power of a number."
        )

        # Create a resource and method for the API
        calculate_resource = api.root.add_resource("calculate")
        calculate_resource.add_method("POST",
            apigateway.LambdaIntegration(lambda_function),
            authorization_type=apigateway.AuthorizationType.NONE
        )

        # Output the API endpoint URL
        api_url_output = CfnOutput(self, "APIUrl",
            value=api.url,
            description="The URL of the API Gateway endpoint"
        )
