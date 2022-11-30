
# Duck Tape

This project is an NFT project that allows you to implement the concept of mystery box.

You can choose to create your NFT by yourself or to create your NFT randomly through a image generation model from HuggingFace.

In this example, we have created NFT of duck images.
In the concept of mystery box, you can attribute a rarity to each images. Here are our choices of rarity :
- 53 rare ducks, generated with the model from HuggingFace
- 8 rare ducks which have been designed by a genius of drawing who goes by the name of BOB. These ducks have evolved in goose.
- 4 legendary ducks. Small are your chances of getting these ducks but great will be your glory if you succeed.

On this documentation you will find all you need to test our project or deployed your own one.

## Libraries installation

In order to use this project, you may have to install some libraries.

### For generation of images through HuggingFace model

If you want to generate the images with the HuggingFace model, please run each of the following commands in your python environment : 

```bash
pip install torch
```
```bash
pip install diffusers
```
```bash
pip install condacolab
```
```bash
pip install transformers scipy ftfy
```
```bash
pip install "ipywidgets>=7,<8"
```
```bash
pip install google.colab
```
```bash
pip install huggingface_hub
```

### Node.js and NPM installation

If you just want to create NFT with your own designed ducks, please run each of the following commands.

#### On Windows 

First, let's check if you have Node.js and NPM installed in your Windows environment.
Open a command prompt (or PowerShell), and enter the following:

```bash
node -v
```
```bash
npm -v
```

If these commands are not recognized, please follow the instructions on this tutorial : https://phoenixnap.com/kb/install-node-js-npm-on-windows

#### On Linux

First, let's check if you have curl and wget installed by typing these commands in a terminal:

```bash
node --version
```
```bash
npm --version
```

If they are not installed, please run these commands:

```bash
sudo apt install node 
```
```bash
sudo apt install npm
```

## Generate NFT with HuggingFace model

As the model needs some processing power, please run the python notebook `images_generation.ipynb` in a google colab session.

You should enable GPU in your notebook in order to have more processing power. 
To do so, go to : Runtime --> Change runtime type and set Harware accelerator to GPU.

## Create NFT with hardhat

### Create a project

In a new folder install hardhat :
```bash
yarn add --dev hardhat
```
or with npm :
```bash
npm install hardhat 
```

Then start your project :
```bash
npx hardhat 
```
```bash
npm install --save-dev @nomicfoundation/hardhat-toolbox @nomicfoundation/hardhat-network-helpers @nomicfoundation/hardhat-chai-matchers @nomiclabs/hardhat-ethers @nomiclabs/hardhat-etherscan chai ethers hardhat-gas-reporter solidity-coverage @typechain/hardhat typechain @typechain/ethers-v5 @ethersproject/abi @ethersproject/providers
```

Compile your code :
```bash
npx hardhat compile 
```

### Deploy a smart contract to mumbai network

You just have to run the script :
```bash
npx hardhat run scripts/deploy.js --network mumbai 
```

You should get the address of the smart contract, keep it, you will need it soon.

### Mint your NFTs

For the following sections, please think to replace the path of the folder containing the metadatas with the corresponding path on your machine. 

#### Mint all your NFTs

This section allows you to mint all your NFT at once on the same address if you want to have a web page on OpenSea with all your full collection of NFT.

This can be usefull if you want to all your potential buyers to see the full collection.

To do so, replace it in the line of the declaration of the `TicketEvent` into the `mint_all_nft.js` script.
Also think to replace the address wallet and the token URI.

Then run the following command :
```bash
npx hardhat run scripts/mint_all_nft.js --network mumbai 
```

You can also mint only one NFT thanks to the script `mint_nft.js`. Also think to replace the address wallet and the token URI.
```bash
npx hardhat run scripts/mint_nft.js --network mumbai 
```

#### Mint a random NFT (Mystery Box concept)

Same as above, replace the address of the smart conctrat in the script `mint_random_nft.js`.

Then run :
```bash
npx hardhat run scripts/mint_random_nft.js --network mumbai 
```


## Presentation website

In this repository, there is also a folder called `dash-app` which allows you to run a web application locally.
This web application contains one page which presents quickly the project.

### Libraries installation to run the dash app

To run the application, you will need some libraries, please run each of the following commands in your python environment :
```bash
pip install dash
```
```bash
pip install dash_bootstrap_components
```
Then run the `launch_app.py` script to launch the app. A local URL should be logged in your terminal, visit it !

