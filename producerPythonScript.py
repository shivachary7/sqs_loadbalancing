
#!/usr/bin/python

import boto3
from time import sleep

# Assuming that you have a valid named profile configured in
# your ~/.aws/credentials
sqs = boto3.client('sqs')

# Gets 'myQueue' queue as an object

sqs.create_queue(QueueName='JobsQueue')
queue = sqs.get_queue_by_name(QueueName='JobsQueue')

# Let' initiate an infinite loop so that it keeps running
# until the process is killed
while True:

  Responce = queue.send_message(MessageBody="Message")

  # Checking the message created
  print("\tMessageId created: {0}".format(Responce.get('MessageId')))
  print(Responce)
  # Sleeps for some time (in seconds) before creating another one
  sleep(0.5)
