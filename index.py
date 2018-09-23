import json
import datetime
import boto3
iot_client = boto3.client('iot')
iot_data_client = boto3.client('iot-data')

def handler(event, context):
    data = {
        'output': 'Hello World',
        'timestamp': datetime.datetime.utcnow().isoformat()
    }
    return {'statusCode': 200,
            'body': json.dumps(data),
            'headers': {'Content-Type': 'application/json'}}
