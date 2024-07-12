import time
import json
import logging
from quixstreams import Application
import scrapping


def get_data():
    return scrapping.scrapping()

def main():
    app = Application(
        broker_address="localhost:9092",
        loglevel="DEBUG",
    )

    with app.get_producer() as producer:
        while True:
            data = get_data()
            logging.debug("Got this data: %s", data)
            producer.produce(
                topic="data_demo",
                key="12345",
                value=json.dumps(data),
            )
            logging.info("Produced. Sleeping...")
            time.sleep(10)


if __name__ == "__main__":
    logging.basicConfig(level="DEBUG")
    main()