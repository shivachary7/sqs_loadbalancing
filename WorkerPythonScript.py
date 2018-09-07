#!/usr/bin/python

import boto3
from time import sleep

# Assuming that you have a valid named profile configured in
# your ~/.aws/credentials
sqs = boto3.client('sqs')

# Gets 'myQueue' queue as an object
queue = sqs.get_queue_by_name(QueueName='JobsQueue')

#infinity loop
while True:
  # Process messages
  for message in queue.receive_messages( MaxNumberOfMessages=1,
      VisibilityTimeout=2,
      WaitTimeSeconds=10):
      print('Waiting for {0} seconds'.format(message.body))

      # Deletes message from queue
      message.delete()
