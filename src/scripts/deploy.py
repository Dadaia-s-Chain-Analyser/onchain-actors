from brownie import UniswapV2DMTransact, UniswapV3DMTransact, SimpleFlashLoan, Dex, config, network, interface
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


def deploy_aave_v3_flashloan_actor(pool_address_provider):
    owner = get_account()
    is_verified = config["networks"][network.show_active()].get("verify")
    dm_actor_contract = SimpleFlashLoan.deploy(pool_address_provider, {'from': owner}, publish_source=is_verified)
    return dm_actor_contract


def deploy_simple_dex(token_a, token_b):
    owner = get_account()

    is_verified = config["networks"][network.show_active()].get("verify")
    dex_contract = Dex.deploy(token_a, token_b, {'from': owner}, publish_source=is_verified)


def main():
    owner = get_account()
    # deploy flashloan actor

    #pool_address_provider = config["networks"][network.show_active()]["poolAdressesProvider"]
    #flashloan_actor = deploy_aave_v3_flashloan_actor(pool_address_provider)
    
    dai_address = "0xDF1742fE5b0bFc12331D8EAec6b478DfDbD31464"
    usdc_address = "0xA2025B15a1757311bfD68cb14eaeFCc237AF5b43"
    deploy_simple_dex(dai_address, usdc_address)