import redis
import random
import string
import time

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def generate_random_message(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

queue_name = 'message_queue'

while True:
    message = generate_random_message()
    redis_client.lpush(queue_name, message)
    print(f"Produced: {message}")
    time.sleep(10)
