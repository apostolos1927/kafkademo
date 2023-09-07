from time import sleep
import json
from kafka import *
from kafka.admin import KafkaAdminClient, NewTopic

topic_name = "test"
partitions = 1
replication = 1
admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092")

print("List topics:", admin_client.list_topics())

if topic_name not in admin_client.list_topics():
    new_topic = NewTopic(
        name=topic_name, num_partitions=partitions, replication_factor=replication
    )
    admin_client.create_topics(new_topics=[new_topic])

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda x: json.dumps(x).encode("utf-8"),
)


for i in range(5):
    name = input("provide name:")
    data = {name: i}
    producer.send(topic_name, value=data)
