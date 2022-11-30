// We require the Hardhat Runtime Environment explicitly here. This is optional
// but useful for running the script in a standalone fashion through `node <script>`.
//
// You can also run a script with `npx hardhat run <script>`. If you do that, Hardhat
// will compile your contracts, add the Hardhat Runtime Environment's members to the
// global scope, and execute the script.
const hre = require("hardhat");

async function main() {

  const TiketEvent = await hre.ethers.getContractFactory("tiketEvent");
  // address du smart contract (sur mumbai etherscan)
  const tiketEvent = await TiketEvent.attach("0x879AC9F9c283e2C5E2057f3A91309708c669F688");

  // address du wallet puis url du json sur pinata
  await tiketEvent.mintNFT("0x2f59E2CeDD44620F61243AD1F446F0254F1C1697", "https://gateway.pinata.cloud/ipfs/QmZYg48oLYumu1Tp5L8Gw6RDmfvMAjaoEdfD8ZupMZG2Si");
  // await tiketEvent.mintNFT("ADDRESS", "YOUR TOKENURI");



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