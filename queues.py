import json
import logging
import numpy as np
from kafka import KafkaProducer, KafkaConsumer

class KafkaHandler:
    def __init__(self, bootstrap_servers, log_file='kafka_handler.log'):
        self.bootstrap_servers = bootstrap_servers
        logging.basicConfig(level=logging.INFO, filename=log_file, filemode='a',
                            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        self.producer: KafkaProducer = self.create_producer()

    def create_producer(self) -> KafkaProducer:
        producer: KafkaProducer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda v: json.dumps(v, default=self.json_serializer).encode('utf-8')
        )

        return producer

    def json_serializer(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        elif isinstance(obj, np.floating):
            return float(obj)
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        else:
            raise TypeError(f"Object of type {type(obj)} is not JSON serializable")
        
    def create_consumer(self, topic, group_id, auto_offset_reset='earliest'):
        """
        Creates a Kafka consumer for a specified topic.

        Parameters:
        - topic (str): The Kafka topic to consume messages from.
        - group_id (str): The consumer group ID to join. Consumers with the same group ID share message consumption.
        - auto_offset_reset (str): Policy for resetting offsets. Options are:
            - 'earliest': Automatically reset the offset to the earliest available if there is no initial offset or if the current offset does not exist anymore.
            - 'latest': Automatically reset the offset to the latest available (most recent message) if there is no initial offset or if the current offset does not exist anymore.
            - 'none': Do not reset offsets automatically. An exception is thrown if no initial offset is found.
        
        Returns:
        - KafkaConsumer: A Kafka consumer instance configured with the specified parameters.
        
        Example usage:
        consumer = self.create_consumer('my-topic', 'my-group', auto_offset_reset='earliest')
        """
        consumer = KafkaConsumer(
            topic,
            bootstrap_servers=self.bootstrap_servers,
            auto_offset_reset=auto_offset_reset,
            enable_auto_commit=True,
            group_id=group_id,
            value_deserializer=lambda x: json.loads(x.decode('utf-8'))
        )
        return consumer
    def produce_message(self, topic, message):
        try:
            self.producer.send(topic, value=message)
            self.producer.flush()
            logging.info(f"Message sent to topic {topic}: ...{str(message)[:50]}")
        except Exception as e:
            logging.error(f"Error sending message: {e}")

    def consume_messages(self, consumer, process_message_callback):
        try:
            for message in consumer:
                logging.info(f"Consumed message: {message.value}")
                process_message_callback(message.value)
        except Exception as e:
            logging.error(f"Error consuming message: {e}")

# Example usage
if __name__ == "__main__":
    
    print("Startingg...")
    kafka_address = '192.168.1.12:9093'
    
    kafka_handler = KafkaHandler(bootstrap_servers=[kafka_address])
    
    # # Create a producer and send a message
    producer = kafka_handler.create_producer()
    kafka_handler.produce_message('profiles_2', {'key': 'value'})

    print("Consuming... ")
    # Create a consumer and consume messages
    consumer = kafka_handler.create_consumer('profiles_2', 'profiles-group')
    res = kafka_handler.consume_messages(consumer, process_message_callback=lambda x: print(x))
    
