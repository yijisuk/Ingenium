// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract CertificateGenerator is ERC721, ERC721URIStorage {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenCounter;

    struct NFT {
        string ipfsAddress;
        address originalOwner;
        bool transferred;
    }
    mapping(uint256 => NFT) private _nfts;

    constructor() ERC721("DeployDemo", "DD") {}

    function _burn(
        uint256 tokenId
    ) internal virtual override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    function accessMintedNFTs()
        public
        view
        returns (
            uint256[] memory,
            string[] memory,
            address[] memory,
            bool[] memory
        )
    {
        uint256 len = _tokenCounter.current();
        uint256[] memory ids = new uint256[](len);
        string[] memory addresses = new string[](len);
        address[] memory owners = new address[](len);
        bool[] memory transferredStatus = new bool[](len);

        for (uint256 i = 0; i < len; i++) {
            ids[i] = i;
            addresses[i] = _nfts[i].ipfsAddress;
            owners[i] = _nfts[i].originalOwner;
            transferredStatus[i] = _nfts[i].transferred;
        }

        return (ids, addresses, owners, transferredStatus);
    }

    function accessTokenCounter() public view returns (uint256) {
        return _tokenCounter.current();
    }

    function tokenURI(
        uint256 tokenId
    )
        public
        view
        virtual
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    function mint(
        string memory _ipfsAddress,
        address _originalOwner
    ) public returns (uint256) {
        _tokenCounter.increment();

        uint256 newTokenId = _tokenCounter.current();
        _safeMint(_originalOwner, newTokenId);
        _setTokenURI(newTokenId, _ipfsAddress);

        _nfts[newTokenId] = NFT(_ipfsAddress, _originalOwner, false);

        return newTokenId;
    }

    function transfer(address _to, uint256 _tokenId) public returns (uint256) {
        require(
            _nfts[_tokenId].transferred == false,
            "NFT is already transferred"
        );
        require(
            _nfts[_tokenId].originalOwner == msg.sender,
            "Only the original owner can transfer the NFT"
        );

        _safeTransfer(msg.sender, _to, _tokenId, "");
        _nfts[_tokenId].originalOwner = _to;
        _nfts[_tokenId].transferred = true;

        return 1;
    }

    function sell(uint256 _tokenId) public {
        require(
            _nfts[_tokenId].transferred == true,
            "NFT is already transferred"
        );
        require(
            ownerOf(_tokenId) == msg.sender,
            "Only the creator can transfer this NFT"
        );
    }
}
