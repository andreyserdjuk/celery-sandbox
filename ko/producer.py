from kombu import Connection, Exchange, Producer, Queue, Message
from time import sleep
import datetime
from random import randint

rabbit_url = "amqp://"
conn = Connection(rabbit_url)
ch = conn.channel()

ex = Exchange('exchange-1', type='direct')

p = Producer(exchange=ex, channel=ch, routing_key='BOB')

q = Queue(name='q-1', exchange=ex, routing_key='BOB')
q.maybe_bind(conn)
q.declare()

while True:
    timestamp = 'Timestamp: {:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    print('published: {}'.format(timestamp))
    p.publish(timestamp)
    sleep(randint(1, 5))
