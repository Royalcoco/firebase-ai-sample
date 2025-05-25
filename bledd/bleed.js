const crypto = require('crypto');

// Simulate a decentralized wallet system
class DecentralizedWallet {
    constructor() {
        this.wallets = new Map();
    }

    // Create a new wallet
    createWallet() {
        const walletId = crypto.randomUUID();
        this.wallets.set(walletId, { balance: 0 });
        console.log(`Wallet created: ${walletId}`);
        return walletId;
    }

    // Add funds to a wallet
    addFunds(walletId, amount) {
        const wallet = this.wallets.get(walletId);
        if (!wallet) {
            throw new Error('Wallet not found');
        }
        wallet.balance += amount;
        console.log(`Added ${amount} to wallet ${walletId}. New balance: ${wallet.balance}`);
    }

    // Withdraw funds from a wallet
    withdrawFunds(walletId, amount) {
        const wallet = this.wallets.get(walletId);
        if (!wallet) {
            throw new Error('Wallet not found');
        }
        if (amount > wallet.balance) {
            throw new Error('Insufficient balance');
        }
        wallet.balance -= amount;
        console.log(`Withdrawn ${amount} from wallet ${walletId}. Remaining balance: ${wallet.balance}`);
        return amount;
    }

    // Check wallet balance
    getBalance(walletId) {
        const wallet = this.wallets.get(walletId);
        if (!wallet) {
            throw new Error('Wallet not found');
        }
        return wallet.balance;
    }
}

// Simulate a transaction system
class TransactionSystem {
    constructor() {
        this.transactions = [];
    }

    // Process a transaction between two wallets
    processTransaction(senderWalletId, receiverWalletId, amount, decentralizedWallet, outputPercentage = 0) {
        const outputAmount = (amount * outputPercentage) / 100;
        const transferableAmount = amount - outputAmount;

        decentralizedWallet.withdrawFunds(senderWalletId, amount);
        decentralizedWallet.addFunds(receiverWalletId, transferableAmount);

        this.transactions.push({
            transactionId: crypto.randomUUID(),
            sender: senderWalletId,
            receiver: receiverWalletId,
            amount,
            output: outputAmount,
            timestamp: new Date().toISOString(),
        });

        console.log(`Transaction processed: ${amount} transferred from ${senderWalletId} to ${receiverWalletId}, ${outputAmount} outputted.`);
    }

    // Get transaction history
    getTransactions() {
        return this.transactions;
    }
}

// Example usage
const decentralizedWallet = new DecentralizedWallet();
const transactionSystem = new TransactionSystem();

// Create wallets
const walletA = decentralizedWallet.createWallet();
const walletB = decentralizedWallet.createWallet();

// Add initial funds to walletA
decentralizedWallet.addFunds(walletA, 1000);

// Process a transaction from walletA to walletB with an output of 10%
transactionSystem.processTransaction(walletA, walletB, 200, decentralizedWallet, 10);

// Check balances
console.log(`Wallet A balance: ${decentralizedWallet.getBalance(walletA)}`);
console.log(`Wallet B balance: ${decentralizedWallet.getBalance(walletB)}`);

// View transaction history
console.log("Transaction history:", transactionSystem.getTransactions());
