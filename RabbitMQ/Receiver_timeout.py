try:
    import pika
except Exception as e:
    print("Some modules are missing {}".format(e))

# connection establish
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

# queue declare
channel.queue_declare(queue="timeout_queue")

# callback function when message received


def callback(ch, method, properties, body):

    # simple printing the message
    print("Message reeieved is %r" % body)


# queue consume
channel.basic_consume(
    queue="timeout_queue", on_message_callback=callback, auto_ack=True
)

print("Waiting for the messages.")

channel.start_consuming()
