import pika



def receiver_message(ch, method, properties, body):
    print(" [x] Received:", body)

url_rabbitmq = 'amqps://kbxswyry:pcYDsVYVwuwgQaWbtnCGHuj7qpcv1TGM@fish.rmq.cloudamqp.com/kbxswyry'
queue = 'test_queue'
params = pika.URLParameters(url_rabbitmq)
connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_bind(exchange='test', queue=queue)
channel.basic_consume(on_message_callback=receiver_message, auto_ack=True, queue=queue)

print(' [*] Waiting for messages. To exit press CTRL+C')
print("Using the queue:", queue)

channel.start_consuming()
