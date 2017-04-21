#!/usr/bin/env python
import pika
from optparse import OptionParser

def send(destination="localhost", message='Hello World!'):
	qname = "messages"
	connection = pika.BlockingConnection(pika.ConnectionParameters(host=destination))
	channel = connection.channel()

	channel.queue_declare(queue=qname)

	channel.basic_publish(exchange='', routing_key=qname, body=messages)
	print(" [x] Sent %s"%messages)
	connection.close()

if __name__=="__main__":
	parser = OptionParser()
   	
   	parser.add_option('-d', '--destination', dest='destination',
                     help='DESTINATION of message usually IP address of rabbitmq-server',
                     default="localhost", metavar='DESTINATION')
   	
   	parser.add_option('-m', '--message', dest='message',
                     help='MESSAGE to send',
                     default="Hello World!", metavar='MESSAGE')
   	
   	(options, args) = parser.parse_args()
   	

   	if options.destination and options.message:
   		send(destination=options.destination , message=options.message)
   	else:
   		print("Syntax: 'python frontend.py -h' | '--help' for help")
