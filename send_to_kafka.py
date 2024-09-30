import logging
import scrapping
from confluent_kafka import Producer


def get_data():
    return scrapping.scrapping()

def main():
    # Configuration settings for the Kafka producer
    conf = {
        'bootstrap.servers': 'localhost:9092',  # Kafka broker(s)
    }

    # Create Producer instance
    producer = Producer(conf)

    # Define a delivery report callback to check the status of message delivery
    def delivery_report(err, msg):
        if err is not None:
            print(f"Message delivery failed: {err}")
        else:
            print(f"Message delivered to {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")

    # Produce a message
    topic = 'test_topic'
    message = get_data()

    # Produce the message asynchronously with the callback
    producer.produce(topic, key=None, value=message, callback=delivery_report)

    # Wait up to 1 second for events. Callbacks will be invoked during this method call if the message is acknowledged.
    producer.flush(1)

if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    main()