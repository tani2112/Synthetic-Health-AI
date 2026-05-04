// SPDX-License-Identifier: MIT
pragma solidity ^0.8.24;

contract AuditChain {
    struct Block {
        uint256 index;
        string timestamp;
        uint256 proof;
        string previousHash;
        string meta;
    }

    Block[] public chain;

    event BlockAdded(
        uint256 index,
        string timestamp,
        uint256 proof,
        string previousHash,
        string meta
    );

    constructor() {
        // Genesis block
        createBlock("1970-01-01 00:00:00", 1, "0", "Genesis Block");
    }

    function createBlock(
        string memory _timestamp,
        uint256 _proof,
        string memory _previousHash,
        string memory _meta
    ) public {
        Block memory newBlock = Block({
            index: chain.length + 1,
            timestamp: _timestamp,
            proof: _proof,
            previousHash: _previousHash,
            meta: _meta
        });
        
        chain.push(newBlock);
        
        emit BlockAdded(
            newBlock.index,
            newBlock.timestamp,
            newBlock.proof,
            newBlock.previousHash,
            newBlock.meta
        );
    }

    function getChainCount() public view returns (uint256) {
        return chain.length;
    }

    function getBlock(uint256 index) public view returns (Block memory) {
        require(index < chain.length, "Index out of bounds");
        return chain[index];
    }
}
