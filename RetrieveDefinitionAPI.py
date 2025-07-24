import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CloudDictionary')

def lambda_handler(event, context):
    
    #All the keywords in the Cloud Dictionary table are in lowercase and this ensures 
    #the search text is converted to lowercase just to return the Definition if available.
    #For example, in Cloud Dictionary table, the keyword is route53 and if a user searches 
    #for "Route 53" then also the result is returned successfully. 
    
    keyword = (event.get('queryStringParameters') or {}).get('text', '').replace(" ", "").lower();
    
    if not keyword:
        return {
        'statusCode': 400,
        'headers': {
            'Access-Control-Allow-Origin': '*'
        },
        'body': json.dumps({
            'message': 'Please provide a valid keyword to search.'
        })
    }


    #This fetches one item from the CloudDictionary table if the search text matches 
    #with the keyword.
    response = table.get_item(
        Key = {
            'keyword': keyword
        }
    )

    if 'Item' in response:
        return {
            'statusCode': 200,
            'headers' : {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                    'definition': response['Item']['definition'],
                    'source': response['Item']['source']
                })
        }
    else:
        return {
            'statusCode': 404,
            'headers': {
                'Access-Control-Allow-Origin': '*'
            },
            'body': json.dumps({
                'message': "Oops! The word you're looking for is not available at the 
                moment. Try searching for other words"
            })
        }
