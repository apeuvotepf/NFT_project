require("@nomicfoundation/hardhat-toolbox");

module.exports = {
  solidity: "0.8.17",
  networks: {
    mumbai: {
      url:"https://polygon-mumbai.g.alchemy.com/v2/xPACxJYzW3ovyVZS_NMuOHO-BZaKcF2d",
      accounts: ["d1bff1c167ef20dc39e249b356f1f56681eb7988f166140ce28a09208bf3649f"],
      gas: 2100000,
      gasPrice: 8000000000,
    },
  },
  // allowUnlimitedContractSize: true
};