import os, uuid
import time
from azure.identity import DefaultAzureCredential
from azure.storage.queue import QueueServiceClient, QueueClient, QueueMessage
from azure.core.exceptions import ResourceExistsError

class QueueAPI:

    def __init__(self, storage_account, credential, queue_name):
        endpoint=f"https://{storage_account}.queue.core.windows.net/"
        self.queue_service_client =QueueClient(endpoint, queue_name=queue_name, credential=credential)


    def create_queue(self):
        try:
            self.queue_service_client.create_queue()
        except ResourceExistsError:
            print("Queue already exists")


    def send_message(self, message):
        self.queue_service_client.send_message(message)

    def receive_message(self):
        while True:

            response = self.queue_service_client.receive_messages()
            for message in response:
                yield message.content
                self.queue_service_client.delete_message(message.id, message.pop_receipt)
            time.sleep(1)
            
        