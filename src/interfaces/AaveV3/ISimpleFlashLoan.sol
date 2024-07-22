// SPDX-License-Identifier: MIT
pragma solidity 0.8.10;



interface ISimpleFlashLoan {
    function requestFlashLoan(address _token, uint256 _amount) external;
    function getBalance(address _tokenAddress) external view returns (uint256);
    function withdraw(address _tokenAddress) external;
}

