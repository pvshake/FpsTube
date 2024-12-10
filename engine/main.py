import os
import signal
import sys
import json
from contextlib import contextmanager

from kombu import Exchange, Queue, Connection, Consumer, exceptions

from converter import VideoConverter
import sqlite3

DB_PATH = "video_processing.db"


def get_env_or_default(key, default):
    return os.getenv(key, default)


@contextmanager
def connect_sqlite():
    conn = sqlite3.connect("video_processing.db")
    conn.row_factory = sqlite3.Row
    try:
        create_tables(conn)
        yield conn
    finally:
        conn.close()


def create_tables(conn):
    with conn:
        conn.execute(
            """
        CREATE TABLE IF NOT EXISTS processed_videos (
            video_id INTEGER PRIMARY KEY,
            status TEXT NOT NULL,
            processed_at TEXT NOT NULL
        );
        """
        )
        conn.execute(
            """
        CREATE TABLE IF NOT EXISTS process_errors_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            error_details TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
        """
        )


def main():
    rabbitmq_url = get_env_or_default("RABBITMQ_URL", "amqp://guest:guest@localhost:5672/")
    conversion_exch_name = get_env_or_default("CONVERSION_EXCHANGE", "conversion_exchange")
    queue_name = get_env_or_default("QUEUE_NAME", "video_conversion_queue")
    conversion_key = get_env_or_default("CONVERSION_KEY", "conversion")
    confirmation_key = get_env_or_default("CONFIRMATION_KEY", "finish-conversion")
    root_path = get_env_or_default("VIDEO_ROOT_PATH", "/home/eric/PycharmProjects/FpsTube/django/media/uploads")
    confirmation_queue = "video_confirmation_queue"

    # Definir Exchange e Queue
    exchange = Exchange(conversion_exch_name, type="direct", durable=True)
    queue = Queue(queue_name, exchange, routing_key=conversion_key)

    with connect_sqlite() as db_conn, Connection(rabbitmq_url) as conn:
        video_converter = VideoConverter(conn, db_conn, root_path)

        def signal_handler(sig, frame):
            print("Shutdown signal received, exiting...")
            conn.close()
            sys.exit(0)

        signal.signal(signal.SIGINT, signal_handler)
        signal.signal(signal.SIGTERM, signal_handler)

        def process_message(body, message):
            try:
                video_converter.handle_message(
                    body, conversion_exch_name, confirmation_key, conn
                )
                message.ack()
            except Exception as e:
                print(f"Error processing message: {e}")
                message.reject()

        with Consumer(conn, queues=[queue], callbacks=[process_message], accept=["json"]):
            print("Waiting for messages from RabbitMQ...")
            while True:
                try:
                    conn.drain_events(timeout=2)
                except exceptions.TimeoutError:
                    continue

if __name__ == "__main__":
    main()
