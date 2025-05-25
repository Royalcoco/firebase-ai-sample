const { expect } = require("chai");

describe("NewGenerationToken", function () {
    let Token, token, owner, addr1, addr2;

    beforeEach(async function () {
        Token = await ethers.getContractFactory("NewGenerationToken");
        [owner, addr1, addr2, _] = await ethers.getSigners();
        token = await Token.deploy();
        await token.deployed();
    });

    it("Should assign the total supply of tokens to the owner", async function () {
        const ownerBalance = await token.balanceOf(owner.address);
        expect(await token.totalSupply()).to.equal(ownerBalance);
    });

    it("Should transfer tokens between accounts", async function () {
        await token.transfer(addr1.address, 50);
        const addr1Balance = await token.balanceOf(addr1.address);
        expect(addr1Balance).to.equal(50);

        await token.connect(addr1).transfer(addr2.address, 50);
        const addr2Balance = await token.balanceOf(addr2.address);
        expect(addr2Balance).to.equal(50);
    });

    it("Should fail if sender doesn’t have enough tokens", async function () {
        const initialOwnerBalance = await token.balanceOf(owner.address);

        await expect(
            token.connect(addr1).transfer(owner.address, 1)
        ).to.be.revertedWith("Not enough balance");

        expect(await token.balanceOf(owner.address)).to.equal(initialOwnerBalance);
    });
});
