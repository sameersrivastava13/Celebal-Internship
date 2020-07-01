# creating a simple receiver to test the scheduling of messges.

try:
    import pika
except Exception as e:
    print("Some modules are missing {}".format(e))


# establish a connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))
channel = connection.channel()

# queue declare
channel.queue_declare(queue="hello")


# callback
def callback(ch, method, properties, body):
    print("[x] recieved message %r" % body)


channel.basic_consume(queue="hello", auto_ack=True, on_message_callback=callback)

print("waiting for messgaes")
channel.start_consuming()
