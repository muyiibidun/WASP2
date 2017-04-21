#!/usr/bin/env python
import pika
from optparse import OptionParser


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

def receive(source="localhost"):
	qname = "messages"
	connection = pika.BlockingConnection(pika.ConnectionParameters(host=source))
	channel = connection.channel()

	channel.queue_declare(queue=qname)

	channel.basic_consume(callback,
	                      queue=qname,
	                      no_ack=True)

	print(' [*] Waiting for messages. To exit press CTRL+C')
	channel.start_consuming()

if __name__=="__main__":
	parser = OptionParser()
   	
   	parser.add_option('-s', '--source', dest='source',
                     help='SOURCE of message usually IP address of rabbitmq-server',
                     default="localhost", metavar='SOURCE')
   	
   	(options, args) = parser.parse_args()
   	
   	if options.source:
        receive(source=options.destination)
   	else:
        print("Syntax: 'python backend.py -h' | '--help' for help")
