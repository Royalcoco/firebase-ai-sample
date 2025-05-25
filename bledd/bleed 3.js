const crypto = require('crypto');

class DecentralizedWallet {
    constructor() {
        this.wallets = new Map();
    }

    createWallet() {
        const walletId = crypto.randomUUID();
        const privateKey = crypto.randomBytes(32).toString('hex');
        const publicKey = crypto.createPublicKey({ key: privateKey, format: 'pem', type: 'pkcs1' }).export({ format: 'pem' });
        this.wallets.set(walletId, { balance: 0, privateKey, publicKey });
        console.log(`Wallet created: ${walletId}`);
        return { walletId, publicKey };
    }

    addFunds(walletId, amount) {
        const wallet = this.wallets.get(walletId);
        if (!wallet) throw new Error('Wallet not found');
        wallet.balance += amount;
        console.log(`Added ${amount} to wallet ${walletId}. New balance: ${wallet.balance}`);
    }

    withdrawFunds(walletId, amount) {
        const wallet = this.wallets.get(walletId);
        if (!wallet) throw new Error('Wallet not found');
        if (amount > wallet.balance) throw new Error('Insufficient balance');
        wallet.balance -= amount;
        console.log(`Withdrawn ${amount} from wallet ${walletId}. Remaining balance: ${wallet.balance}`);
        return amount;
    }

    getBalance(walletId) {
        const wallet = this.wallets.get(walletId);
        if (!wallet) throw new Error('Wallet not found');
        return wallet.balance;
    }
}

class RansomManager {
    constructor() {
        this.ransoms = [];
    }

    createRansomRequest(contributorWalletId, amount, reason) {
        const ransomId = crypto.randomUUID();
        const ransomRequest = {
            ransomId,
            contributorWalletId,
            amount,
            reason,
            status: "pending",
            timestamp: new Date().toISOString()
        };
        this.ransoms.push(ransomRequest);
        console.log(`Ransom request created: ${JSON.stringify(ransomRequest, null, 2)}`);
        return ransomRequest;
    }

    fulfillRansomRequest(ransomId, payerWalletId, walletSystem) {
        const ransom = this.ransoms.find(r => r.ransomId === ransomId);
        if (!ransom) throw new Error('Ransom request not found');
        if (ransom.status !== "pending") throw new Error('Ransom request already fulfilled or cancelled');

        walletSystem.withdrawFunds(payerWalletId, ransom.amount);
        ransom.status = "fulfilled";
        ransom.fulfilledTimestamp = new Date().toISOString();
        console.log(`Ransom request fulfilled: ${JSON.stringify(ransom, null, 2)}`);
        return ransom;
    }

    getPendingRansoms() {
        return this.ransoms.filter(r => r.status === "pending");
    }
}

class TransactionSystem {
    constructor(decentralizedWallet, ransomManager) {
        this.decentralizedWallet = decentralizedWallet;
        this.ransomManager = ransomManager;
    }

    contributeFunds(walletId, amount, reason) {
        this.decentralizedWallet.addFunds(walletId, amount);
        const ransomRequest = this.ransomManager.createRansomRequest(walletId, amount, reason);
        console.log(`Contribution processed. Ransom request generated: ${JSON.stringify(ransomRequest, null, 2)}`);
    }
}

// Example usage
const decentralizedWallet = new DecentralizedWallet();
const ransomManager = new RansomManager();
const transactionSystem = new TransactionSystem(decentralizedWallet, ransomManager);

const contributorWallet = decentralizedWallet.createWallet().walletId;
const payerWallet = decentralizedWallet.createWallet().walletId;

decentralizedWallet.addFunds(payerWallet, 100); // Adding funds to the payer's wallet

// Contributor makes a contribution
transactionSystem.contributeFunds(contributorWallet, 20, "Contribution for development");

// Fulfill the ransom request
const pendingRansoms = ransomManager.getPendingRansoms();
if (pendingRansoms.length > 0) {
    ransomManager.fulfillRansomRequest(pendingRansoms[0].ransomId, payerWallet, decentralizedWallet);
}

// Check updated balances
console.log(`Contributor Wallet Balance: ${decentralizedWallet.getBalance(contributorWallet)}`);
console.log(`Payer Wallet Balance: ${decentralizedWallet.getBalance(payerWallet)}`);

// Get all ransom requests
console.log("All Ransom Requests:", JSON.stringify(ransomManager.ransoms, null, 2));
