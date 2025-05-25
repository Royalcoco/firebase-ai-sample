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

    signTransaction(walletId, transaction) {
        const wallet = this.wallets.get(walletId);
        if (!wallet) throw new Error('Wallet not found');
        const sign = crypto.createSign('SHA256');
        sign.update(JSON.stringify(transaction));
        sign.end();
        const signature = sign.sign(wallet.privateKey, 'hex');
        return signature;
    }

    verifySignature(publicKey, transaction, signature) {
        const verify = crypto.createVerify('SHA256');
        verify.update(JSON.stringify(transaction));
        verify.end();
        return verify.verify(publicKey, signature, 'hex');
    }
}

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

    updateRates(newRates) {
        this.rates = { ...this.rates, ...newRates };
        console.log("Updated rates:", this.rates);
    }
}

class Blockchain {
    constructor() {
        this.chain = [];
    }

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

    generateHash(transaction) {
        const data = JSON.stringify(transaction);
        return crypto.createHash('sha256').update(data).digest('hex');
    }

    getBlockchain() {
        return this.chain;
    }
}

class IPFSSimulator {
    constructor() {
        this.storage = [];
    }

    storeTransaction(transaction) {
        const hash = crypto.createHash('sha256').update(JSON.stringify(transaction)).digest('hex');
        this.storage.push({ hash, transaction });
        console.log(`Transaction stored in IPFS: ${hash}`);
        return hash;
    }

    retrieveTransaction(hash) {
        return this.storage.find((entry) => entry.hash === hash)?.transaction;
    }
}

class TransactionSystem {
    constructor(decentralizedWallet, blockchain, oracle, ipfs) {
        this.decentralizedWallet = decentralizedWallet;
        this.blockchain = blockchain;
        this.oracle = oracle;
        this.ipfs = ipfs;
        this.transactions = [];
    }

    processTransaction(senderWalletId, receiverWalletId, crypto, amount, outputPercentage = 0) {
        const outputAmount = (amount * outputPercentage) / 100;
        const transferableAmount = amount - outputAmount;
        const fiatValue = this.oracle.getRate(crypto) * transferableAmount;

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

        const signature = this.decentralizedWallet.signTransaction(senderWalletId, transaction);

        // Verify the signature before processing
        const senderWallet = this.decentralizedWallet.wallets.get(senderWalletId);
        if (!this.decentralizedWallet.verifySignature(senderWallet.publicKey, transaction, signature)) {
            throw new Error("Transaction signature verification failed!");
        }

        this.decentralizedWallet.withdrawFunds(senderWalletId, amount);
        this.decentralizedWallet.addFunds(receiverWalletId, transferableAmount);

        this.transactions.push(transaction);
        this.blockchain.addBlock(transaction);
        const ipfsHash = this.ipfs.storeTransaction(transaction);

        console.log(`Transaction processed: ${amount} ${crypto} transferred, ${outputAmount} outputted.`);
        console.log(`IPFS Hash: ${ipfsHash}`);
        return fiatValue;
    }

    getTransactions() {
        return this.transactions;
    }
}

// Example usage
const decentralizedWallet = new DecentralizedWallet();
const blockchain = new Blockchain();
const oracle = new Oracle();
const ipfs = new IPFSSimulator();
const transactionSystem = new TransactionSystem(decentralizedWallet, blockchain, oracle, ipfs);

const walletA = decentralizedWallet.createWallet().walletId;
const walletB = decentralizedWallet.createWallet().walletId;

decentralizedWallet.addFunds(walletA, 5); // 5 BTC equivalent

transactionSystem.processTransaction(walletA, walletB, 'BTC', 2, 10); // 10% output

console.log(`Wallet A balance: ${decentralizedWallet.getBalance(walletA)}`);
console.log(`Wallet B balance: ${decentralizedWallet.getBalance(walletB)}`);

console.log("Blockchain:", blockchain.getBlockchain());
