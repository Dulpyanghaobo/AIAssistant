from kafka import KafkaProducer
import json

class KafkaProducerFactory:

    def __init__(self, bootstrap_servers):
        self.bootstrap_servers = bootstrap_servers
        self.producer = KafkaProducer(bootstrap_servers=self.bootstrap_servers,
                                      value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def get_producer(self):
        return self.producer
