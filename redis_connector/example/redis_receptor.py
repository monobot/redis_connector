import time

from redis_connector import RedisConnector

TEST_CHANNEL = 'TEST_CHANNEL'


class RedisReceptor(RedisConnector):
    def _process(self, message):
        print(message)


r = RedisReceptor('localhost', 6379, [TEST_CHANNEL, ], 'processor')

while True:
    r.subscribe()
