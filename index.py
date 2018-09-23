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
    rawDataBytes = streamingBody.read()  # rawDataBytes is of type 'bytes' in, Python 3.x specific
    rawDataString = rawDataBytes.decode('utf-8')  # Python 3.x specific
    jsonState = json.loads(rawDataString)
    return {'statusCode': 200,
            'body': json.dumps(jsonState),
            'headers': {'Content-Type': 'application/json'}}
