# code for rabbitMQ client and server.
# receiver program

try:
    import pika
except Exception as e:
    print("Some modules are missing {}".format(e))

# Meta class
class MetaClass(type):
    """Singleton Design pattern"""

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


class RabbitMqServerConfigure(metaclass=MetaClass):
    def __init__(self, host="localhost", queue="hello"):
        """Server initialization"""
        self.host = host
        self.queue = queue


class RabbitmqServer:
    """Server is an object of class RabbitMqServerConfigure"""

    def __init__(self, server):
        self.server = server
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.server.host)
        )
        self._channel = self._connection.channel()
        self._temp = self._channel.queue_declare(queue=self.server.queue)

    @staticmethod
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    def startserver(self):
        self._channel.basic_consume(
            queue=self.server.queue,
            on_message_callback=RabbitmqServer.callback,
            auto_ack=False,
        )

        self._channel.start_consuming()


if __name__ == "__main__":
    serverconfigure = RabbitMqServerConfigure(host="localhost", queue="hello")

    server = RabbitmqServer(server=serverconfigure)
    server.startserver()


# print(" [*] Waiting for messages. To exit press CTRL+C")
