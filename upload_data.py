import json
import boto3

with open("C:/Users/ojasa/Cloud Projects/5. Cloud Dictionary App/dataset.json", "r") as f:
    data = json.load(f)

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('CloudDictionary')

with table.batch_writer() as batch:
    for item in data:
        batch.put_item(Item=item)

print("Data uploaded successfully!")
