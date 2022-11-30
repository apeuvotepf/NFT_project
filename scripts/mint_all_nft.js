// We require the Hardhat Runtime Environment explicitly here. This is optional
// but useful for running the script in a standalone fashion through `node <script>`.
//
// You can also run a script with `npx hardhat run <script>`. If you do that, Hardhat
// will compile your contracts, add the Hardhat Runtime Environment's members to the
// global scope, and execute the script.
const hre = require("hardhat");
var fs = require('fs');
var path = require('path');
// In newer Node.js versions where process is already global this isn't necessary.
var process = require("process");


async function main() {

  const TiketEvent = await hre.ethers.getContractFactory("tiketEvent");
  // address du smart contract (sur mumbai etherscan)
  const tiketEvent = await TiketEvent.attach("0x879AC9F9c283e2C5E2057f3A91309708c669F688");


//   var folder = __dirname.substring(0, str.length - 9); + "\\metadatas";
//   console.log(folder);
    const baseUrlMetadata = "https://gateway.pinata.cloud/ipfs/QmZYg48oLYumu1Tp5L8Gw6RDmfvMAjaoEdfD8ZupMZG2Si/"
    folder = "C:\\Users\\Arthur\\OneDrive\\Documents\\cours\\5A\\Cybersecurity\\NFT_project\\metadatas\\generated_images_metadatas"

  // Loop through all the files in the temp directory
  const files = fs.readdirSync(folder)
  for (let index = 0; index < files.length; index++) {
    const file = files[index];
    console.log(baseUrlMetadata + file)
    const txt = await tiketEvent.mintNFT("0x2f59E2CeDD44620F61243AD1F446F0254F1C1697", baseUrlMetadata + file);
    await txt.wait()
}
  // address du wallet puis url du json sur pinata
//   await tiketEvent.mintNFT("0x2f59E2CeDD44620F61243AD1F446F0254F1C1697", "https://gateway.pinata.cloud/ipfs/Qme6f5deSHYv3CrxAZ7x3JrTDpQnoDqz1QEQ6U7XH3A8wB");
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