import unittest
import index
import json
list_things = '''{
    "things": [
        {
            "thingName": "esp8266_D4E3A2",
            "thingArn": "arn:aws:iot:eu-central-1:851467715228:thing/esp8266_D4E3A2",
            "attributes": {},
            "version": 1
        },
        {
            "thingName": "esp32_18D8C0",
            "thingTypeName": "room-sensor-type",
            "thingArn": "arn:aws:iot:eu-central-1:851467715228:thing/esp32_18D8C0",
            "attributes": {
                "room": "kathi",
                "sensor-id": "lion",
                "target-actor-relay": "r0",
                "target-actor-thing": "esp8266_D4E3A2"
            },
            "version": 3
        },
        {
            "thingName": "esp8266_0B80C4",
            "thingArn": "arn:aws:iot:eu-central-1:851467715228:thing/esp8266_0B80C4",
            "attributes": {},
            "version": 1
        },
        {
            "thingName": "esp32_3ADEA4",
            "thingTypeName": "room-sensor-type",
            "thingArn": "arn:aws:iot:eu-central-1:851467715228:thing/esp32_3ADEA4",
            "attributes": {
                "room": "marla",
                "sensor-id": "marla",
                "target-actor-relay": "r1",
                "target-actor-thing": "esp8266_D4E3A2"
            },
            "version": 4
        },
        {
            "thingName": "rsi-develop-actor",
            "thingTypeName": "actor-type",
            "thingArn": "arn:aws:iot:eu-central-1:851467715228:thing/rsi-develop-actor",
            "attributes": {
                "location": "basement",
                "rooms-served": "livingroom,entrance"
            },
            "version": 1
        },
        {
            "thingName": "esp8266_D4C8C0",
            "thingTypeName": "room-sensor-type",
            "thingArn": "arn:aws:iot:eu-central-1:851467715228:thing/esp8266_D4C8C0",
            "attributes": {
                "room": "livingroom",
                "sensor-id": "livingroom",
                "target-actor-relay": "r1",
                "target-actor-thing": "esp8266_D5C324"
            },
            "version": 3
        },
        {
            "thingName": "raspberrypi",
            "thingTypeName": "actor-type",
            "thingArn": "arn:aws:iot:eu-central-1:851467715228:thing/raspberrypi",
            "attributes": {
                "location": "ug",
                "pins": "0,1,2,3",
                "rooms-served": "entrance,kitchen,living-room,bathroom"
            },
            "version": 1
        },
        {
            "thingName": "esp32_21C918",
            "thingTypeName": "room-sensor-type",
            "thingArn": "arn:aws:iot:eu-central-1:851467715228:thing/esp32_21C918",
            "attributes": {
                "room": "kitchen",
                "sensor-id": "tygra"
            },
            "version": 3
        },
        {
            "thingName": "esp32_001E06",
            "thingTypeName": "room-sensor-type",
            "thingArn": "arn:aws:iot:eu-central-1:851467715228:thing/esp32_001E06",
            "attributes": {
                "room": "malte",
                "sensor-id": "fixMeForMalte",
                "target-actor-relay": "r2",
                "target-actor-thing": "esp8266_D4E3A2"
            },
            "version": 5
        },
        {
            "thingName": "esp8266_D5C324",
            "thingArn": "arn:aws:iot:eu-central-1:851467715228:thing/esp8266_D5C324",
            "attributes": {},
            "version": 1
        },
        {
            "thingName": "esp32_21CF74",
            "thingTypeName": "room-sensor-type",
            "thingArn": "arn:aws:iot:eu-central-1:851467715228:thing/esp32_21CF74",
            "attributes": {
                "room": "Bad",
                "sensor-id": "cheetara",
                "target-actor-relay": "r3",
                "target-actor-thing": "esp8266_D4E3A2"
            },
            "version": 6
        }
    ]
}
'''
room_response = '''{"state":{"reported":{"press":214748.3647,"hum":100,"temp":0.01,"on":false}},"metadata":{"reported":{"press":{"timestamp":1515939383},"hum":{"timestamp":1515939383},"temp":{"timestamp":1515939383},"on":{"timestamp":1515939383}}},"version":85837,"timestamp":1537770160}'''

class TestHandlerCase(unittest.TestCase):


    def test_response(self):
        print("testing response.")
        result = index.handler(None, None)
        print(result)
        self.assertEqual(result['statusCode'], 200)
        self.assertEqual(result['headers']['Content-Type'], 'application/json')

        # self.assertIn('Hello World', result['body'])

    def test_parse(self):
        json.loads(list_things)

if __name__ == '__main__':
    unittest.main()
