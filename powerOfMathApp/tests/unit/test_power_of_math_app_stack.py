import aws_cdk as core
import aws_cdk.assertions as assertions

from power_of_math_app.power_of_math_app_stack import PowerOfMathAppStack

# example tests. To run these tests, uncomment this file along with the example
# resource in power_of_math_app/power_of_math_app_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PowerOfMathAppStack(app, "power-of-math-app")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
