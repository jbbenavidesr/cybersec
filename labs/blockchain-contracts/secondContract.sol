pragma solidity ^0.4.0;

contract financialContract{

    address issuer;

    function financialContract() {
        issuer = msg.sender;
    }

    modifier ifIssuer () {
        if (issuer != msg.sender) {
            throw;
        } else {
            _;
        }
    }

    function receiveFunds() payable {

    }

    function getValue() public constant returns(uint) {
        return this.balance;
    }

    function withdrawFunds(uint funds) ifIssuer {
        issuer.send(funds);
    }
}