try:
    import pika
except Exception as e:
    print("Some modules are missing {}".format(e))

# Establish connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

# declaring the main queue
channel.queue_declare(queue="hello")

channel.queue_bind(exchange="amq.direct", queue="hello")

# creating channel for delay
delay_channel = connection.channel()

delay_channel.queue_declare(
    durable=True,
    queue="hello_delay",
    arguments={
        "x-message-ttl": 5000,
        "x-dead-letter-exchange": "amq.direct",
        "x-dead-letter-routing-key": "hello",
    },
)

delay_channel.basic_publish(
    exchange="",
    routing_key="hello_delay",
    body="test",
    properties=pika.BasicProperties(delivery_mode=2),
)

print(" [x] Sent")
