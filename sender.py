#!/usr/bin/env python
import pika
from optparse import OptionParser
import ConfigParser

def send(connection_info=None, message=""):
	qname = "wasp"
	credentials = pika.PlainCredentials(connection_info["username"], connection_info["password"])
	connection = pika.BlockingConnection(pika.ConnectionParameters(connection_info["server"],connection_info["port"],'/',credentials))
	channel = connection.channel()

	channel.queue_declare(queue=qname)

	channel.basic_publish(exchange='',
	                     routing_key=qname,
	                     body=message)
	print(" [x] Sent %s"%message)
	connection.close()

if __name__=="__main__":
	parser = OptionParser()
	parser.add_option('-c', '--credential', dest='credentialFile',
                     help='Path to CREDENTIAL file', metavar='CREDENTIALFILE')

	parser.add_option('-m', '--message', dest='message',
                     help='MESSAGE to send', default="Hello World!", metavar='MESSAGE')
	(options, args) = parser.parse_args()

	if options.credentialFile and options.message:
		config = ConfigParser.RawConfigParser()
		config.read(options.credentialFile)
		connection = {}
		connection["server"] = config.get('rabbit', 'server')
		connection["port"] = int(config.get('rabbit', 'port'))
		connection["username"]=config.get('user1', 'username')
		connection["password"]=config.get('user1', 'password')
		send(connection_info=connection, message=options.message)
	else:
        #e.g. python sender.py -c credentials.txt -m "Hello World"
		print("Syntax: 'python sender.py -h' | '--help' for help")

