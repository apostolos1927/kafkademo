from kafka import KafkaConsumer
import json

topic_name = "test"
bootstrap_servers = "localhost:9092"
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset="earliest",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

for msg in consumer:
    print(msg.value)
