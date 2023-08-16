import os
from apis.queue_api import QueueAPI
from azure.core.credentials import AzureNamedKeyCredential
from dotenv import load_dotenv

load_dotenv()

storage_account_name = os.getenv("STORAGE_ACCOUNT_NAME")
storage_key = os.getenv("STORAGE_KEY")
queue_name = os.getenv("QUEUE_NAME")      
network = os.getenv("NETWORK")

UNI_TOKEN = "0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984"
WETH_TOKEN = "0xB4FBF271143F4FBf7B91A5ded31805e42b2208d6"


credential = AzureNamedKeyCredential(storage_account_name, storage_key)
api_queue = QueueAPI(storage_account_name, credential, queue_name)
one_eth = int(1*10**18)
one_uni = int(0.08*10**18)

api_queue.create_queue()

command_1 = f"brownie run scripts/uniswap_api_v2.py swap_exact_eth_amount_for_token {one_eth} {UNI_TOKEN} --network {network}"
command_2 = f"brownie run scripts/uniswap_api_v2.py swap_exact_token_amount_for_eth {one_uni} {UNI_TOKEN} --network {network}"
command_3 = f"brownie run scripts/uniswap_api_v2.py swap_eth_for_exact_token_amount {one_uni} {UNI_TOKEN} --network {network}"
command_4 = f"brownie run scripts/uniswap_api_v2.py swap_token_for_exact_eth_amount {one_eth} {UNI_TOKEN} --network {network}"
command_5 = f"brownie run scripts/uniswap_api_v2.py swap_exact_token_amount_for_token {one_eth} {UNI_TOKEN} {WETH_TOKEN} --network {network}"
command_6 = f"brownie run scripts/uniswap_api_v2.py swap_token_for_exact_token_amount {one_uni} {WETH_TOKEN} {UNI_TOKEN} --network {network}"


command_7 = f"brownie run scripts/uniswap_api_v3.py swap_exact_input_single {one_uni} {WETH_TOKEN} {UNI_TOKEN} 3000 --network {network}"
command_8 = f"brownie run scripts/uniswap_api_v3.py swap_exact_output_single {one_uni} {UNI_TOKEN} {WETH_TOKEN} 3000 --network {network}"


#api_queue.send_message(command_1)
#api_queue.send_message(command_2)
#api_queue.send_message(command_3)
#api_queue.send_message(command_4)
#api_queue.send_message(command_5)
#########api_queue.send_message(command_6)

api_queue.send_message(command_8)