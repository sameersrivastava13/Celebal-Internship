try:
    import pika
    import uuid
except Exception as e:
    print("Modules are missing {}".format(e))
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
      def __init__(self,server):
        self.server = server
        self._connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.server.host)
        )

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue="", exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True,
        )


    def on_response(self, ch, method, props, body):
        if self.corr_id == props.correlation_id:
            self.response = body


def call(self, n):
    self.response = None
    self.corr_id = str(uuid.uuid4())
    self.channel.basic_publish(
        exchange="",
        routing_key="rpc_queue",
        properties=pika.BasicProperties(
            reply_to=self.callback_queue, correlation_id=self.corr_id,
        ),
        body=str(n),
    )
    while self.response is None:
        self.connection.process_data_events()
    return int(self.response)


if __name__ == "__main__":
    serverconfigure = RabbitMqServerConfigure(host="localhost", queue="rpc_queue")

    server = RabbitmqServer(server=serverconfigure)
    server.startserver()





class FibonacciRpcClient(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host="localhost")
        )

        self.channel = self.connection.channel()

        result = self.channel.queue_declare(queue="", exclusive=True)
        self.callback_queue = result.method.queue

        self.channel.basic_consume(
            queue=self.callback_queue,
            on_message_callback=self.on_response,
            auto_ack=True,
        )



if __name__ == '__main__':

    fibonacci_rpc = FibonacciRpcClient()
    while True:
        num = int(input())
        print(" [x] Requesting fib(x)",num)
        response = fibonacci_rpc.call(num)
        print(" [.] Got %r" % response)



