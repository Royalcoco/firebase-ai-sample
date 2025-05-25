const crypto = require('crypto');

class DecentralizedWallet {
    constructor() {
        this.wallets = new Map();
    }

    createWallet() {
        const walletId = crypto.randomUUID();
        const privateKey = crypto.randomBytes(32).toString('hex');
        const publicKey = crypto.createPublicKey({ key: privateKey, format: 'pem', type: 'pkcs1' }).export({ format: 'pem' });
        this.wallets.set(walletId, { balance: {}, privateKey, publicKey });
        console.log(`Wallet created: ${walletId}`);
        return { walletId, publicKey };
    }

    addFunds(walletId, amount, currency = 'USD') {
        const wallet = this.wallets.get(walletId);
        if (!wallet) throw new Error('Wallet not found');
        if (!wallet.balance[currency]) wallet.balance[currency] = 0;
        wallet.balance[currency] += amount;
        console.log(`Added ${amount} ${currency} to wallet ${walletId}.`);
    }

    withdrawFunds(walletId, amount, currency = 'USD') {
        const wallet = this.wallets.get(walletId);
        if (!wallet) throw new Error('Wallet not found');
        if (!wallet.balance[currency] || amount > wallet.balance[currency]) throw new Error('Insufficient balance');
        wallet.balance[currency] -= amount;
        console.log(`Withdrawn ${amount} ${currency} from wallet ${walletId}.`);
        return amount;
    }

    getBalance(walletId, currency = 'USD') {
        const wallet = this.wallets.get(walletId);
        if (!wallet) throw new Error('Wallet not found');
        return wallet.balance[currency] || 0;
    }
}

class RansomManager {
    constructor() {
        this.ransoms = [];
    }

    createRansomRequest(contributorWalletId, amount, currency, reason) {
        if (amount <= 0) throw new Error('Invalid amount');
        const ransomId = crypto.randomUUID();
        const ransomHash = crypto.createHash('sha256').update(ransomId).digest('hex');
        const ransomRequest = {
            ransomId,
            ransomHash,
            contributorWalletId,
            amount,
            currency,
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

        walletSystem.withdrawFunds(payerWalletId, ransom.amount, ransom.currency);
        ransom.status = "fulfilled";
        ransom.fulfilledTimestamp = new Date().toISOString();
        console.log(`Ransom request fulfilled: ${JSON.stringify(ransom, null, 2)}`);
        return ransom;
    }

    cancelRansomRequest(ransomId) {
        const ransom = this.ransoms.find(r => r.ransomId === ransomId);
        if (!ransom) throw new Error('Ransom request not found');
        if (ransom.status !== "pending") throw new Error('Only pending requests can be cancelled');

        ransom.status = "cancelled";
        ransom.cancelledTimestamp = new Date().toISOString();
        console.log(`Ransom request cancelled: ${JSON.stringify(ransom, null, 2)}`);
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

    contributeFunds(walletId, amount, currency, reason) {
        if (amount <= 0) throw new Error('Contribution amount must be positive');
        this.decentralizedWallet.addFunds(walletId, amount, currency);
        const ransomRequest = this.ransomManager.createRansomRequest(walletId, amount, currency, reason);
        console.log(`Contribution processed. Ransom request generated: ${JSON.stringify(ransomRequest, null, 2)}`);
    }
}

// Example usage
const decentralizedWallet = new DecentralizedWallet();
const ransomManager = new RansomManager();
const transactionSystem = new TransactionSystem(decentralizedWallet, ransomManager);

const contributorWallet = decentralizedWallet.createWallet().walletId;
const payerWallet = decentralizedWallet.createWallet().walletId;

// Add funds to payer wallet
decentralizedWallet.addFunds(payerWallet, 100, 'USD'); // Adding 100 USD to payer wallet

// Contributor makes a contribution
transactionSystem.contributeFunds(contributorWallet, 50, 'USD', "Support project development");

// Fulfill the ransom request
const pendingRansoms = ransomManager.getPendingRansoms();
if (pendingRansoms.length > 0) {
    ransomManager.fulfillRansomRequest(pendingRansoms[0].ransomId, payerWallet, decentralizedWallet);
}

// Cancel a ransom request
const anotherRansom = transactionSystem.contributeFunds(contributorWallet, 20, 'USD', "Extra support");
ransomManager.cancelRansomRequest(anotherRansom.ransomId);

// Check balances and all ransoms
console.log(`Contributor Wallet Balance: ${JSON.stringify(decentralizedWallet.getBalance(contributorWallet, 'USD'))}`);
console.log(`Payer Wallet Balance: ${JSON.stringify(decentralizedWallet.getBalance(payerWallet, 'USD'))}`);
console.log("All Ransom Requests:", JSON.stringify(ransomManager.ransoms, null, 2));
