try:
    import pika
except Exception as e:
    print("Some modules are missing {}".format(e))

# connection establish
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

# queue declare
channel.queue_declare(queue="timeout_queue")

# sender message
message = input("Enter your message=\t")

# publish queue
channel.basic_publish(
    exchange="",
    routing_key="timeout_queue",
    properties=pika.BasicProperties(expiration="10000"),
    body=message,
)

print("Sending the message to the receiever.")

connection.close()
