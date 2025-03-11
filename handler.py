import json
import boto3
from datetime import datetime
from uuid import uuid4

dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')
ads_table = dynamodb.Table('ads')
comments_table = dynamodb.Table('comments')
chats_table = dynamodb.Table('chats')
images_bucket = "aws-serverless25-images"

def create_ad(event, context):
    body = json.loads(event['body'])
    ad_id = str(uuid4())
    image_url = body.get('image_url', None)

    # Subir la imagen a S3
    if image_url:
        s3.upload_file(image_url, images_bucket, f"{ad_id}.jpg")
        image_url = f"https://{images_bucket}.s3.amazonaws.com/{ad_id}.jpg"

    response = ads_table.put_item(
        Item={
            'ad_id': ad_id,
            'title': body['title'],
            'description': body['description'],
            'price': body['price'],
            'image_url': image_url,
            'created_at': str(datetime.utcnow())
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Ad created successfully', 'ad_id': ad_id})
    }

def list_ads(event, context):
    response = ads_table.scan()
    return {
        'statusCode': 200,
        'body': json.dumps({'ads': response['Items']})
    }

def get_ad(event, context):
    ad_id = event['queryStringParameters']['ad_id']
    response = ads_table.get_item(
        Key={'ad_id': ad_id}
    )
    if 'Item' in response:
        return {
            'statusCode': 200,
            'body': json.dumps({'ad': response['Item']})
        }
    else:
        return {
            'statusCode': 404,
            'body': json.dumps({'message': 'Ad not found'})
        }

def create_comment(event, context):
    body = json.loads(event['body'])
    ad_id = body['ad_id']
    comment_id = str(uuid4())

    response = comments_table.put_item(
        Item={
            'ad_id': ad_id,
            'comment_id': comment_id,
            'message': body['message'],
            'created_at': str(datetime.utcnow())
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Comment added successfully', 'comment_id': comment_id})
    }

def get_comments(event, context):
    ad_id = event['queryStringParameters']['ad_id']
    response = comments_table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('ad_id').eq(ad_id)
    )
    return {
        'statusCode': 200,
        'body': json.dumps({'comments': response['Items']})
    }

def create_chat_message(event, context):
    body = json.loads(event['body'])
    ad_id = body['ad_id']
    chat_id = str(uuid4())

    response = chats_table.put_item(
        Item={
            'ad_id': ad_id,
            'chat_id': chat_id,
            'message': body['message'],
            'timestamp': str(datetime.utcnow())
        }
    )

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Chat message sent', 'chat_id': chat_id})
    }

def get_chats(event, context):
    ad_id = event['queryStringParameters']['ad_id']
    response = chats_table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('ad_id').eq(ad_id)
    )
    return {
        'statusCode': 200,
        'body': json.dumps({'chats': response['Items']})
    }

def get_chat_messages(event, context):
    ad_id = event['queryStringParameters']['ad_id']
    chat_id = event['queryStringParameters']['chat_id']
    response = chats_table.query(
        KeyConditionExpression=boto3.dynamodb.conditions.Key('ad_id').eq(ad_id) &
                              boto3.dynamodb.conditions.Key('chat_id').eq(chat_id)
    )
    return {
        'statusCode': 200,
        'body': json.dumps({'chat_messages': response['Items']})
    }
