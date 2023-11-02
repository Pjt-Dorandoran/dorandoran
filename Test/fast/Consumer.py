import pika
from pika import BlockingConnection, BasicProperties
from queue import Queue

async def on_message(queue_name):
    credentials = pika.PlainCredentials(username="username", password="password")
    host = "k9b108.p.ssafy.io"
    port = 5672
    connection = BlockingConnection(
        pika.ConnectionParameters(host=host, credentials=credentials, port=port)
    )
    try:
        channel = connection.channel()
        channel.queue_declare(queue_name, durable=True)

        def callback(ch, method, properties, body):
            print("Received %r" % body)
            if queue_name == "test.req":
                ch.basic_publish(exchange="", routing_key="test.res", body=body)
            ch.basic_ack(delivery_tag=method.delivery_tag)
            queue.put(body)
            channel.stop_consuming()
        queue = Queue()
        channel.basic_qos(prefetch_count=1)
        channel.basic_consume(queue=queue_name, auto_ack=False, on_message_callback=callback)
        channel.start_consuming()
        return queue
    except Exception as e:
        print(e)
        channel.stop_consuming()
    finally:
        channel.stop_consuming()
        connection.close()