pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract MultiSigNFT is ERC721URIStorage, Ownable {
    uint256 public tokenCounter;
    mapping(uint256 => uint256) public tokenPrices;
    mapping(uint256 => address) public tokenOwners;
    mapping(uint256 => bool) public tokenOnSale;
    mapping(uint256 => address[]) public tokenSigners;

    event TokenPriceUpdated(uint256 tokenId, uint256 newPrice);
    event TokenOnSale(uint256 tokenId, uint256 price);
    event TokenSold(uint256 tokenId, address buyer, uint256 price);

    constructor() ERC721("MultiSigNFT", "MSNFT") {
        tokenCounter = 0;
    }

    function createNFT(string memory tokenURI, uint256 initialPrice) public onlyOwner returns (uint256) {
        uint256 newItemId = tokenCounter;
        _safeMint(msg.sender, newItemId);
        _setTokenURI(newItemId, tokenURI);
        tokenPrices[newItemId] = initialPrice;
        tokenOwners[newItemId] = msg.sender;
        tokenCounter += 1;
        return newItemId;
    }

    function setForSale(uint256 tokenId, uint256 price) public {
        require(ownerOf(tokenId) == msg.sender, "You are not the owner of this token");
        tokenPrices[tokenId] = price;
        tokenOnSale[tokenId] = true;
        emit TokenOnSale(tokenId, price);
    }

    function signSale(uint256 tokenId) public {
        require(tokenOnSale[tokenId], "Token is not for sale");
        require(msg.sender != tokenOwners[tokenId], "Owner cannot sign the sale");
        
        bool alreadySigned = false;
        for (uint i = 0; i < tokenSigners[tokenId].length; i++) {
            if (tokenSigners[tokenId][i] == msg.sender) {
                alreadySigned = true;
                break;
            }
        }

        require(!alreadySigned, "You have already signed this sale");
        tokenSigners[tokenId].push(msg.sender);

        if (tokenSigners[tokenId].length >= 2) {
            completeSale(tokenId);
        }
    }

    function completeSale(uint256 tokenId) internal {
        address buyer = msg.sender;
        require(msg.value >= tokenPrices[tokenId], "Insufficient payment");
        
        address owner = ownerOf(tokenId);
        _transfer(owner, buyer, tokenId);
        payable(owner).transfer(msg.value);

        tokenPrices[tokenId] = tokenPrices[tokenId] * 2;
        tokenOnSale[tokenId] = false;
        tokenSigners ;

        emit TokenSold(tokenId, buyer, msg.value);
        emit TokenPriceUpdated(tokenId, tokenPrices[tokenId]);
    }

    function getTokenPrice(uint256 tokenId) public view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        return tokenPrices[tokenId];
    }
}
