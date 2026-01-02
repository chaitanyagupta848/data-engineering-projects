import json
import random
import time
from datetime import datetime
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

TOPIC = "ecommerce_events"

def generate_event():
    return {
        "event_id": random.randint(1000, 9999),
        "user_id": random.randint(1, 500),
        "event_type": random.choice(["view", "cart", "purchase"]),
        "amount": round(random.uniform(10, 500), 2),
        "event_time": datetime.utcnow().isoformat()
    }

while True:
    event = generate_event()
    producer.send(TOPIC, event)
    producer.flush()
    print("Sent:", event)
    time.sleep(1)
