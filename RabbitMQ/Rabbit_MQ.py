# code for rabbitMQ client and server.
# sender program

try:
    import pika
except Exception as e:
    print("Some modules are missing {}".format_map(e))

# Meta class
class MetaClass(type):
    """Singleton Design pattern"""

    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaClass, cls).__call__(*args, **kwargs)
            return cls._instance[cls]


# now am adding a class so that if again i have to change something i can do
# basically removing the hard coded part


class RabbitmqConfigure(metaclass=MetaClass):
    def __init__(
        self, queue="hello", host="localhost", routing_key="hello", exchange=""
    ):
        self.queue = queue
        self.host = host
        self.routing_key = routing_key
        self.exchange = exchange


# object oriented program
class RabbitMq:
    __slots__ = ["server", "_channel", "_connection"]

    def __init__(self, server):
        self.server = server
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.server.host)
        )
        self._channel = self._connection.channel()
        self._channel.queue_declare(queue=self.server.queue)

    def __enter__(self):
        print("__enter__")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        self._connection.close()

    def publish(self, payload={}):
        self._channel.basic_publish(
            exchange=self.server.exchange,
            routing_key=self.server.routing_key,
            properties=pika.BasicProperties(
                expiration='6000',
            ),
            body=str(payload),
        )

        print("Published Message : {}".format(payload))

class Image(object):

    __slots__ = ["filename"]
    def __init__(self,filename):
        self.filename = filename

    @property
    def get(self):
        with open(self.filename, "rb") as f:
            data = f.read()
        return data



if __name__ == "__main__":

    server = RabbitmqConfigure(
        queue="hello", host="localhost", routing_key="hello", exchange=""
    )

    image = Image(filename="login_image.png")
    data = image.get

    with RabbitMq(server) as rabbitmq:
        rabbitmq.publish(payload=data)
