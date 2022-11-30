// We require the Hardhat Runtime Environment explicitly here. This is optional
// but useful for running the script in a standalone fashion through `node <script>`.
//
// You can also run a script with `npx hardhat run <script>`. If you do that, Hardhat
// will compile your contracts, add the Hardhat Runtime Environment's members to the
// global scope, and execute the script.
const hre = require("hardhat");
const fs = require('fs');
const folder = "C:\\Users\\Arthur\\OneDrive\\Documents\\cours\\5A\\Cybersecurity\\NFT_project\\metadatas\\generated_images_metadatas";

async function main() {

  const TiketEvent = await hre.ethers.getContractFactory("tiketEvent");
  // address du smart contract (sur mumbai etherscan)
  const tiketEvent = await TiketEvent.attach("0xf48E91e65521f0776E7c46C7A6e33F6963ca8BaA");

  // get length of folder containing images 
  const lenCollection = fs.readdirSync(folder).length
  
  // generate random number to get the id of the nft
  const id_nft = Math.floor(Math.random() * lenCollection) -1;

  // get the pinata url (tokenURI) from metadata file
  const rawdata = fs.readFileSync(folder + "\\" + id_nft + ".json");
  const metadata = JSON.parse(rawdata);
  const url_pinata = metadata['image'];
  //console.log(url_pinata);

  // address du wallet puis url du json sur pinata (tokenURI)
  await tiketEvent.openMisteryBox(url_pinata, {gasLimit: 5000000}); 

  console.log(
    ` deployed to ${tiketEvent.address}`
  );
}

// We recommend this pattern to be able to use async/await everywhere
// and properly handle errors.
main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});