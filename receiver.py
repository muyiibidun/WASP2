#!/usr/bin/env python
import pika
from optparse import OptionParser
import ConfigParser

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

def receive(connection_info=None):
	qname = "wasp"
   	credentials = pika.PlainCredentials(connection_info["username"], connection_info["password"])
   	connection = pika.BlockingConnection(pika.ConnectionParameters(connection_info["server"],connection_info["port"],'/',credentials))
   	channel = connection.channel()

	channel.queue_declare(queue=qname)

	channel.basic_consume(callback, queue=qname, no_ack=True)

	print(' [*] Waiting for messages. To exit press CTRL+C')
	channel.start_consuming()


if __name__=="__main__":
	parser = OptionParser()

   	parser.add_option('-c', '--credential', dest='credentialFile',
                     help='Path to CREDENTIAL file', metavar='CREDENTIALFILE')

   	(options, args) = parser.parse_args()
   	

   	if options.credentialFile:
   		config = ConfigParser.RawConfigParser()
        config.read(options.credentialFile)
        
        connection = {}
        connection["server"] = config.get('rabbit', 'server');
        connection["port"] = config.get('rabbit', 'port');
        connection["username"]=config.get('user1', 'username');
        connection["password"]=config.get('user1', 'password');
		receiver(connection_info=connection)

   	else:
   		#e.g. python receiver.py -c credentials.txt
   		print("Syntax: 'python receiver.py -h' | '--help' for help")

