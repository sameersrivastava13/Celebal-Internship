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
    def __init__(self, host="localhost", queue="rpc_queue"):
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

    def startserver(self):
        self._channel.basic_qos(prefetch_count=1)
        self._channel.basic_consume(queue="rpc_queue", on_message_callback=on_request)

        print(" [x] Awaiting RPC requests")
        self._channel.start_consuming()


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def on_request(ch, method, props, body):
    n = int(body)

    # print(" [.] fib(%s)" % n)
    response = input("Write your response=")
    # response = fib(n)

    ch.basic_publish(
        exchange="",
        routing_key=props.reply_to,
        properties=pika.BasicProperties(correlation_id=props.correlation_id),
        body=str(response),
    )
    ch.basic_ack(delivery_tag=method.delivery_tag)


if __name__ == "__main__":
    serverconfigure = RabbitMqServerConfigure(host="localhost", queue="rpc_queue")

    server = RabbitmqServer(server=serverconfigure)
    server.startserver()
