import hre from "hardhat";
import fs from "fs";

async function main() {
  const AuditChain = await hre.ethers.getContractFactory("AuditChain");
  const auditChain = await AuditChain.deploy();

  await auditChain.waitForDeployment();

  const address = await auditChain.getAddress();
  console.log("AuditChain deployed to:", address);
  
  fs.writeFileSync("contract_address.txt", address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
