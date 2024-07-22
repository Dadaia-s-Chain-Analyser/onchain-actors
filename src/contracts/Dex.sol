// contracts/FlashLoan.sol
// SPDX-License-Identifier: MIT
pragma solidity 0.8.10;

import {IERC20} from "@aave/contracts/dependencies/openzeppelin/contracts/IERC20.sol";

contract Dex {
    address payable public owner;

    IERC20 private token_a;
    IERC20 private token_b;

    // exchange rate indexes
    uint256 dexARate = 90;
    uint256 dexBRate = 100;

    // keeps track of individuals' dai balances
    mapping(address => uint256) public token_a_balances;

    // keeps track of individuals' USDC balances
    mapping(address => uint256) public token_b_balances;

    constructor(address _token_a, address _token_b) {
        owner = payable(msg.sender);
        token_a = IERC20(_token_a);
        token_b = IERC20(_token_b);
    }

    function depositTokenA(uint256 _amount) external {
        token_a_balances[msg.sender] += _amount;
        uint256 allowance = token_a.allowance(msg.sender, address(this));
        require(allowance >= _amount, "Check the token allowance");
        token_a.transferFrom(msg.sender, address(this), _amount);
    }

    function depositTokenB(uint256 _amount) external {
        token_b_balances[msg.sender] += _amount;
        uint256 allowance = token_b.allowance(msg.sender, address(this));
        require(allowance >= _amount, "Check the token allowance");
        token_b.transferFrom(msg.sender, address(this), _amount);
    }

    function buyTokenA() external {
        uint256 tokenAToReceive = ((token_b_balances[msg.sender] / dexARate) * 100) *
            (10**12);
        token_a.transfer(msg.sender, tokenAToReceive);
    }

    function sellTokenA() external {
        uint256 tokenBToReceive = ((token_a_balances[msg.sender] * dexBRate) / 100) /
            (10**12);
        token_b.transfer(msg.sender, tokenBToReceive);
    }

    function getBalance(address _tokenAddress) external view returns (uint256) {
        return IERC20(_tokenAddress).balanceOf(address(this));
    }

    function withdraw(address _tokenAddress) external onlyOwner {
        IERC20 token = IERC20(_tokenAddress);
        token.transfer(msg.sender, token.balanceOf(address(this)));
    }

    modifier onlyOwner() {
        require(
            msg.sender == owner,
            "Only the contract owner can call this function"
        );
        _;
    }

    receive() external payable {}
}

