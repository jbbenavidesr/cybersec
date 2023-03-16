pragma solidity ^0.4.0;

contract financialContract{

    uint amount = 13;

    function getValue() public constant returns(uint) {
        return amount;
    }

    function setValue(uint newValue) public {
        amount = newValue;
    }
}