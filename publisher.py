import pika

queue ='test_queue'
exchange = 'test'
routing_key = 'tests'
body = 'Hello World! :)'

url = 'amqps://kbxswyry:pcYDsVYVwuwgQaWbtnCGHuj7qpcv1TGM@fish.rmq.cloudamqp.com/kbxswyry'
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.exchange_declare(exchange=exchange) # Declare Exchange
channel.queue_declare(queue=queue) # Declare Queue
channel.queue_bind(queue, exchange,routing_key) # Create binding 


# publish message
channel.basic_publish(body=body,
                      exchange=exchange,
                      routing_key=routing_key,
                      )

connection.close()

print("Directed:", body, "to queue:", queue)
