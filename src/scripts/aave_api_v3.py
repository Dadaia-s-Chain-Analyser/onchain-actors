from brownie import FlashLoan, config, network, interface
from scripts.utils import get_account


def make_a_flash_loan(token_address, amount):
    owner = get_account()
    flashloan_actor = FlashLoan[-1]
    flashloan_actor.requestFlashLoan(token_address, amount, {'from': owner})
    print(f"Flash loan of {amount} {token_address} completed")


def send_erc20_to_contract(token_address, amount):
    owner = get_account()
    token = interface.IERC20(token_address)
    token.approve(FlashLoan[-1], amount, {'from': owner})
    token.transfer(FlashLoan[-1], amount, {'from': owner})
    print(f"Deposited {amount} {token.symbol()} into the FlashLoan contract")


def main():
    usdc_token = "0x65aFADD39029741B3b8f0756952C74678c9cEC93"
    small_fee_amount = int(0.5*10**6)
    flashloan_amount = 10**9
    send_erc20_to_contract(usdc_token, small_fee_amount)
    make_a_flash_loan(usdc_token, flashloan_amount)