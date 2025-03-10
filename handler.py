import json
import boto3
from datetime import datetime

dynamodb = boto3.resource('dynamodb', region_name='eu-west-1')

def get_api_endpoint(event, context):
    try:
        api_endpoint = event['stageVariables']['API_ENDPOINT']

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            },
            'body': json.dumps({'apiUrl': api_endpoint})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def create_comment(event, context):
    try:
        table_comments = dynamodb.Table('messages')

        body = json.loads(event['body'])
        user = body['user']
        message = body['message']
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        response = table_comments.put_item(
            Item={
                'user': user,
                'message': message,
                'date': date
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Message from ' + user + ' succesfully published'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def get_comments(event, context):
    try:
        table_comments = dynamodb.Table('messages')

        response = table_comments.scan()
        data = response['Items']
        
        while 'LastEvaluatedKey' in response:
            response = table_comments.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])

        return {
            'statusCode': 200,
            'body': json.dumps(data)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def create_ad(event, context):
    try:
        table_ads = dynamodb.Table('ads')

        body = json.loads(event['body'])
        user = body['user']
        product = body['product']
        description = body['description']
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        response = table_ads.put_item(
            Item={
                'user': user,
                'product': product,
                'description': description,
                'date': date
            }
        )

        return {
            'statusCode': 200,
            'body': json.dumps({'product': 'Advertisement from ' + user + ' succesfully published.'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

def list_ads(event, context):
    try:
        table_ads = dynamodb.Table('ads')

        response = table_ads.scan()
        data = response['Items']
        
        while 'LastEvaluatedKey' in response:
            response = table_ads.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
            data.extend(response['Items'])

        return {
            'statusCode': 200,
            'body': json.dumps(data)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
