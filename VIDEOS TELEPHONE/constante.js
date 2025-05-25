const Web3 = require('web3');
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');

const contractAddress = '0xYourContractAddress';
const contractABI = [...] // The ABI of your contract

const contract = new web3.eth.Contract(contractABI, contractAddress);

// Get total supply of NFTs
contract.methods.totalSupply().call((err, result) => {
  console.log(result);
});

// Get owner of a specific NFT
const tokenId = 1;
contract.methods.ownerOf(tokenId).call((err, result) => {
  console.log(result);
});
const Web3 = require('web3');
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');

const contractAddress = '0xYourContractAddress';
const contractABI = [...] // The ABI of your contract

const contract = new web3.eth.Contract(contractABI, contractAddress);

const fromAddress = '0xYourAddress';
const toAddress = '0xRecipientAddress';
const tokenId = 1;

web3.eth.accounts.wallet.add('your private key');

contract.methods.transferFrom(fromAddress, toAddress, tokenId).send({from: fromAddress})
  .on('receipt', console.log)
  .on('error', console.error);
  const Web3 = require('web3');
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');

const contractAddress = '0xYourContractAddress';
const contractABI = [...] // The ABI of your contract

const contract = new web3.eth.Contract(contractABI, contractAddress);

const ownerAddress = '0xOwnerAddress';

contract.methods.balanceOf(ownerAddress).call((err, result) => {
  console.log(result);
});
const Web3 = require('web3');
const axios = require('axios');
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');

const contractAddress = '0xYourContractAddress';
const contractABI = [...] // The ABI of your contract

const contract = new web3.eth.Contract(contractABI, contractAddress);

const tokenId = 1;

contract.methods.tokenURI(tokenId).call((err, result) => {
  if (err) {
    console.error(err);
    return;
  }

  // Fetch the metadata from the URL
  axios.get(result).then(response => {
    console.log(response.data);
  }).catch(console.error);
});
const Web3 = require('web3');
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');

const contractAddress = '0xYourContractAddress';
const contractABI = [...] // The ABI of your contract

const contract = new web3.eth.Contract(contractABI, contractAddress);

const ownerAddress = '0xYourAddress';
const approvedAddress = '0xApprovedAddress';
const tokenId = 1;

web3.eth.accounts.wallet.add('your private key');

contract.methods.approve(approvedAddress, tokenId).send({from: ownerAddress})
  .on('receipt', console.log)
  .on('error', console.error);
  const Web3 = require('web3');
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');

const contractAddress = '0xYourContractAddress';
const contractABI = [...] // The ABI of your contract

const contract = new web3.eth.Contract(contractABI, contractAddress);

const ownerAddress = '0xYourAddress';
const approvedAddress = '0xApprovedAddress';
const tokenId = 1;

web3.eth.accounts.wallet.add('your private key');

contract.methods.approve(approvedAddress, tokenId).send({from: ownerAddress})
  .on('receipt', console.log)
  .on('error', console.error);
  const Web3 = require('web3');
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');

const contractAddress = '0xYourContractAddress';
const contractABI = [...] // The ABI of your contract

const contract = new web3.eth.Contract(contractABI, contractAddress);

const tokenId = 1;

contract.methods.ownerOf(tokenId).call((err, result) => {
  console.log(result);
});
const Web3 = require('web3');
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');

const contractAddress = '0xYourContractAddress';
const contractABI = [...] // The ABI of your contract

const contract = new web3.eth.Contract(contractABI, contractAddress);

contract.methods.totalSupply().call((err, result) => {
  console.log(result);
});
const Web3 = require('web3');
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');

const contractAddress = '0xYourContractAddress';
const contractABI = [...] // The ABI of your contract

const contract = new web3.eth.Contract(contractABI, contractAddress);

const ownerAddress = '0xOwnerAddress';
const index = 0; // Index of the token

contract.methods.tokenOfOwnerByIndex(ownerAddress, index).call((err, result) => {
  console.log(result);
});
const Web3 = require('web3');
const web3 = new Web3('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID');

const contractAddress = '0xYourContractAddress';
const contractABI = [...] // The ABI of your contract

const contract = new web3.eth.Contract(contractABI, contractAddress);

const ownerAddress = '0xOwnerAddress';
const index = 0; // Index of the token

contract.methods.tokenOfOwnerByIndex(ownerAddress, index).call((err, result) => {
  console.log(result);
});
