import json
import math
import boto3
import os
from time import gmtime, strftime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ['TABLE_NAME'])
now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

def lambda_handler(event, context):
    body = json.loads(event['body'])
    base = int(body['base'])
    exponent = int(body['exponent'])
    math_result = math.pow(base, exponent)
    response = table.put_item(
        Item={
            'ID': str(math_result),
            'LatestGreetingTime': now
        })
    return {
        'statusCode': 200,
        'body': json.dumps(f'Your result is {math_result}')
    }
