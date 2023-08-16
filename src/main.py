import os
from scripts.apis.queue_api import QueueAPI
from azure.core.credentials import AzureNamedKeyCredential
from dotenv import load_dotenv

load_dotenv()

storage_account_name = os.getenv("STORAGE_ACCOUNT_NAME")
storage_key = os.getenv("STORAGE_KEY")
queue_name = os.getenv("QUEUE_NAME")      


credential = AzureNamedKeyCredential(storage_account_name, storage_key)
api_queue = QueueAPI(storage_account_name, credential, queue_name)

msg = api_queue.receive_message()

import asyncio

async def execute_command(command):
    proc = await asyncio.create_subprocess_shell(
        command,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE)

    stdout, stderr = await proc.communicate()

    print(f'stdout: {stdout.decode()}')
    print(f'stderr: {stderr.decode()}')


for command in msg:
    print(command)
    asyncio.run(execute_command(command))