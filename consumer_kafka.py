from confluent_kafka import Consumer, KafkaException, KafkaError

# Configuration settings for the Kafka consumer
conf = {
    'bootstrap.servers': 'localhost:9092',  # Kafka broker(s)
    'group.id': 'my_group',                 # Consumer group ID
    'auto.offset.reset': 'earliest'         # Start reading at the earliest message
}

# Create Consumer instance
consumer = Consumer(conf)

# Subscribe to the topic
topic = 'test_topic'
consumer.subscribe([topic])

# Poll for new messages
try:
    while True:
        msg = consumer.poll(timeout=1.0)
        
        if msg is None:
            continue  # No message available within the timeout period
        
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # End of partition event
                print(f"Reached end of partition: {msg.topic()} [{msg.partition()}] at offset {msg.offset()}")
            elif msg.error():
                raise KafkaException(msg.error())
        else:
            # Successfully received a message
            print(f"Received message: {msg.value().decode('utf-8')} from topic: {msg.topic()} partition: {msg.partition()} offset: {msg.offset()}")
finally:
    # Close the consumer to commit final offsets
    consumer.close()
