import time
import json

from redis_connector import RedisConnector

TEST_CHANNEL = 'TEST_CHANNEL'


r = RedisConnector('localhost', 6379, [TEST_CHANNEL, ], 'example')

n = 1
while True:
    message = {
        "target": 'processor',
        "message_id": 'uuid',
        "message": "Bingo {}".format(n),
        "data": {}
    }
    print(message)
    r.publish(TEST_CHANNEL, json.dumps(message))
    n += 1
