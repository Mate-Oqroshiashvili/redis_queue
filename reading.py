import redis
import time

redis_client = redis.Redis(host='localhost', port=6379, db=0)

queue_name = 'message_queue'

while True:
    message = redis_client.rpop(queue_name)
    if message:
        print(f"Consumed: {message.decode('utf-8')}")
    else:
        print("No message in the queue")
    time.sleep(10)
