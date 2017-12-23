from typing import List, AnyStr, Callable
from kombu import Connection, Exchange, Queue, Message, Consumer
from kombu.mixins import ConsumerMixin

rabbit_url = "amqp://"


class Worker(ConsumerMixin):
    def __init__(self, queues: List[Queue], connection: Connection) -> None:
        self.connection = connection
        self.queues = queues

    def get_consumers(self, consumer: Callable, channel) -> List[Consumer]:
        return [
            consumer(
                queues=self.queues,
                callbacks=[self.on_message],
            )
        ]

    def on_message(self, body: AnyStr, message: Message) -> None:
        print('Got message: {0}'.format(body))
        message.ack()


ex = Exchange('exchange-1', type='direct')
q = Queue(name='q-1', exchange=ex, routing_key='BOB')

with Connection(rabbit_url, heartbeat=4) as conn:
    worker = Worker([q], conn)
    worker.run()
