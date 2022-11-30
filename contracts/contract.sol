//Contract based on [https://docs.openzeppelin.com/contracts/3.x/erc721](https://docs.openzeppelin.com/contracts/3.x/erc721)
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract tiketEvent is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    constructor() ERC721("ticket event", "TE") {}

    function mintNFT(address recipient, string memory tokenURI)
        public onlyOwner
        returns (uint256)
    {

        _tokenIds.increment();

        uint256 newItemId = _tokenIds.current();
        _mint(recipient, newItemId);
        _setTokenURI(newItemId, tokenURI);

        return newItemId;
    } 

    //Smart contract need to implement this function in order to receive ether
    receive() external payable {} 
		
	//The owner of the smart contract can drawback ether by calling this function 
    function drawBack() public onlyOwner {
        (bool sent, bytes memory data) = msg.sender.call{value: address(this).balance}("");
        require(sent, "Failed to send Ether");
    }

    function openMisteryBox(string memory tokenURI)
        public payable
    {
        // check if right amount of ether 
        // 10**18 because ether need to be converted to wei
        uint256 amount = 0.000005 * 10**18; // 
        uint256 quantity = msg.value;
        require(quantity >= amount, "0.000005 ether are required to get the NFT.");
        mintNFT(msg.sender, tokenURI);
    }

}