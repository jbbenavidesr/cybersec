import json
import os

from todos import decimalencoder
import boto3

dynamodb = boto3.resource("dynamodb")


def list(event, context):
    user = event["queryStringParameters"]["user"]
    table = dynamodb.Table(os.environ["DYNAMODB_TABLE"])

    # fetch all todos from the database
    result = table.scan(
        Select="ALL_ATTRIBUTES",
        ScanFilter={
            "id": {
                "AttributeValueList": [{"S": user}],
                "ComparisonOperator": "GT",
            }
        },
    )

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(result["Items"], cls=decimalencoder.DecimalEncoder),
    }

    return response
