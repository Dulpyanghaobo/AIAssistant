from kafka import KafkaConsumer
import json

class KafkaConsumerFactory:

    def __init__(self, bootstrap_servers, topic, group_id):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.group_id = group_id
        self.consumer = KafkaConsumer(self.topic, bootstrap_servers=self.bootstrap_servers,
                                      group_id=self.group_id,
                                      value_deserializer=lambda x: json.loads(x.decode('utf-8')))

    def get_consumer(self):
        return self.consumer
