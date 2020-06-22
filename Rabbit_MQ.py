# code for rabbitMQ client and server.
# sender program

try:
    import pika
except Exception as e:
    print("Some modules are missing.".format_map(e))

# Dry code

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = connection.channel()

channel.queue_declare(queue="Hello")

channel.basic_publish(exchange="", routing_key="Hello", body="Hello world")

print("Published message")
connection.close()
