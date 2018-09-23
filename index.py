import json
import datetime
import boto3
iot_client = boto3.client('iot')
iot_data_client = boto3.client('iot-data')

def handler(event, context):
    thing_name = 'esp8266_D4E3A2'
    iot_client = boto3.client('iot')
    iot_data_client = boto3.client('iot-data')

    # response = iot_client.describe_thing(thingName=thing_name)

    response = iot_data_client.get_thing_shadow(thingName=thing_name)
    streamingBody = response["payload"]
    jsonState = json.loads(streamingBody.read())
    return {'statusCode': 200,
            'body': json.dumps(jsonState),
            'headers': {'Content-Type': 'application/json'}}
