const crypto = require('crypto');

// Simulate a decentralized wallet system
class DecentralizedWallet {
    constructor() {
        this.wallets = new Map();
    }

    // Create a new wallet
    createWallet() {
        const walletId = crypto.randomUUID();
        const privateKey = crypto.randomBytes(32).toString('hex');
        const publicKey = crypto.createPublicKey({ key: privateKey, format: 'pem', type: 'pkcs1' }).export({ format: 'pem' });
        this.wallets.set(walletId, { balance: 0, privateKey, publicKey });
        console.log(`Wallet created: ${walletId}`);
        return { walletId, publicKey };
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

// Simulated Oracle for conversion rates
class Oracle {
    constructor() {
        this.rates = {
            BTC: 30000,
            ETH: 2000,
            USDT: 1,
        };
    }

    getRate(crypto) {
        return this.rates[crypto] || 0;
    }
}

// Simulated Blockchain
class Blockchain {
    constructor() {
        this.chain = [];
    }

    // Add a block to the blockchain
    addBlock(transaction) {
        const block = {
            index: this.chain.length + 1,
            transaction,
            timestamp: new Date().toISOString(),
            previousHash: this.chain.length ? this.chain[this.chain.length - 1].hash : null,
            hash: this.generateHash(transaction),
        };
        this.chain.push(block);
        console.log('Block added to blockchain:', block);
    }

    // Generate a hash for a transaction
    generateHash(transaction) {
        const data = JSON.stringify(transaction);
        return crypto.createHash('sha256').update(data).digest('hex');
    }

    // Get the entire blockchain
    getBlockchain() {
        return this.chain;
    }
}

// Simulate a transaction system
class TransactionSystem {
    constructor(decentralizedWallet, blockchain, oracle) {
        this.decentralizedWallet = decentralizedWallet;
        this.blockchain = blockchain;
        this.oracle = oracle;
        this.transactions = [];
    }

    // Process a transaction between two wallets
    processTransaction(senderWalletId, receiverWalletId, crypto, amount, outputPercentage = 0) {
        const outputAmount = (amount * outputPercentage) / 100;
        const transferableAmount = amount - outputAmount;
        const fiatValue = this.oracle.getRate(crypto) * transferableAmount;

        this.decentralizedWallet.withdrawFunds(senderWalletId, amount);
        this.decentralizedWallet.addFunds(receiverWalletId, transferableAmount);

        const transaction = {
            transactionId: crypto.randomUUID(),
            sender: senderWalletId,
            receiver: receiverWalletId,
            crypto,
            amount,
            output: outputAmount,
            fiatValue,
            timestamp: new Date().toISOString(),
        };

        this.transactions.push(transaction);
        this.blockchain.addBlock(transaction);
        console.log(`Transaction processed: ${amount} ${crypto} transferred, ${outputAmount} outputted.`);
        return fiatValue;
    }

    // Get transaction history
    getTransactions() {
        return this.transactions;
    }
}

// Example usage
const decentralizedWallet = new DecentralizedWallet();
const blockchain = new Blockchain();
const oracle = new Oracle();
const transactionSystem = new TransactionSystem(decentralizedWallet, blockchain, oracle);

// Create wallets
const walletA = decentralizedWallet.createWallet().walletId;
const walletB = decentralizedWallet.createWallet().walletId;

// Add initial funds to walletA
decentralizedWallet.addFunds(walletA, 5); // 5 BTC equivalent

// Process a transaction with 10% output
transactionSystem.processTransaction(walletA, walletB, 'BTC', 2, 10); // 2 BTC transferred with 10% output

// Check balances
console.log(`Wallet A balance: ${decentralizedWallet.getBalance(walletA)}`);
console.log(`Wallet B balance: ${decentralizedWallet.getBalance(walletB)}`);

// View transaction history
console.log("Transaction history:", transactionSystem.getTransactions());

// View blockchain state
console.log("Blockchain:", blockchain.getBlockchain());
