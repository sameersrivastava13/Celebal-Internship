# code for rabbitMQ client and server.
# receiver program

try:
    import pika
except Exception as e:
    print("Some modules are missing {}".format(e))

connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost"))

channel = connection.channel()

channel.queue_declare(queue='hello')

def callback(ch,method,properties,body):
    print(" [x] Received %r" %body)
    #since we are consuming (consumer)
channel.basic_consume(
    queue='hello', on_message_callback=callback, auto_ack=False)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()