from brownie import SimpleFlashLoan, config, network, interface
from scripts.utils import get_account


class FlashLoanActor:

    def __init__(self, contract_address):
        self.contract_address = contract_address
        self.contract = interface.IFlashLoan(self.contract_address)

    def requestFlashLoan(self, token_address, amount, tx_params):
        self.contract.requestFlashLoan(token_address, amount, tx_params)

def make_a_flash_loan(flashloan_address, token_address, amount):
    owner = get_account()
    flashloan_contract = interface.ISimpleFlashLoan(flashloan_address)
    flashloan_contract.requestFlashLoan(token_address, amount, {'from': owner})
    print(f"Flash loan of {amount} {token_address} completed")


def fund_contract_with_erc20(flashloan_address, token_address, amount):
    owner = get_account()
    token = interface.IERC20(token_address)
    flashloan_contract = interface.ISimpleFlashLoan(flashloan_address)
    token.approve(flashloan_contract, amount, {'from': owner})
    token.transfer(flashloan_contract, amount, {'from': owner})
    print(f"Deposited {amount} {token.symbol()} into the FlashLoan contract")



def main():
    flashloan_address = "0x6acdE544Ba6eFAFF105E8a29FaCA98fc62Ee8E78"
    flashloan_address_2 = "0xd1DddA1FDBec4d148729e742684aa2c04e964555"
    usdc_token = "0x65aFADD39029741B3b8f0756952C74678c9cEC93"
    small_fee_amount = int(1*10**6)
    flashloan_amount = 10**8
    fund_contract_with_erc20(flashloan_address_2, usdc_token, small_fee_amount)
    make_a_flash_loan(flashloan_address_2, usdc_token, flashloan_amount)