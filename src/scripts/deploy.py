from brownie import UniswapV2DMTransact, UniswapV3DMTransact, FlashLoan, config, network, interface
from scripts.utils import get_account

import logging
from web3 import Web3

logging.basicConfig(level='INFO')


def deploy_uniswap_v2_actor(uniswap_v2_router):
    owner = get_account()
    is_verified = config["networks"][network.show_active()].get("verify")
    dm_actor_contract = UniswapV2DMTransact.deploy(uniswap_v2_router, {'from': owner}, publish_source=is_verified)
    return dm_actor_contract


def deploy_uniswap_v3_actor(uniswap_v3_router):
    owner = get_account()
    is_verified = config["networks"][network.show_active()].get("verify")
    dm_actor_contract = UniswapV3DMTransact.deploy(uniswap_v3_router, {'from': owner}, publish_source=is_verified)
    return dm_actor_contract


def deploy_flashloan_actor(pool_address_provider):
    owner = get_account()
    is_verified = config["networks"][network.show_active()].get("verify")
    dm_actor_contract = FlashLoan.deploy(pool_address_provider, {'from': owner}, publish_source=is_verified)
    return dm_actor_contract


def make_a_flash_loan(token_address, amount):
    owner = get_account()
    flashloan_actor = FlashLoan[-1]
    flashloan_actor.requestFlashLoan(token_address, amount, {'from': owner})

def main():
    owner = get_account()
    