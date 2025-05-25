// Génération de la matrice 539x876x374
function generateMatrix(dim1, dim2, dim3) {
    const matrix = [];
    for (let i = 0; i < dim1; i++) {
        const slice = [];
        for (let j = 0; j < dim2; j++) {
            const row = [];
            for (let k = 0; k < dim3; k++) {
                row.push(Math.random()); // Probabilités simulées entre 0 et 1
            }
            slice.push(row);
        }
        matrix.push(slice);
    }
    return matrix;
}

const probabilityMatrix = generateMatrix(539, 876, 374);
console.log("Matrix generated:", probabilityMatrix);
class Block {
    constructor(index, data, previousHash = "") {
        this.index = index;
        this.timestamp = new Date().toISOString();
        this.data = data; // Analyse des besoins ou calculs mathématiques
        this.previousHash = previousHash;
        this.hash = this.calculateHash();
    }

    calculateHash() {
        return btoa(`${this.index}${this.timestamp}${JSON.stringify(this.data)}${this.previousHash}`);
    }
}

class Blockchain {
    constructor() {
        this.chain = [this.createGenesisBlock()];
    }

    createGenesisBlock() {
        return new Block(0, "Genesis Block", "0");
    }

    getLatestBlock() {
        return this.chain[this.chain.length - 1];
    }

    addBlock(data) {
        const previousBlock = this.getLatestBlock();
        const newBlock = new Block(this.chain.length, data, previousBlock.hash);
        this.chain.push(newBlock);
    }

    isChainValid() {
        for (let i = 1; i < this.chain.length; i++) {
            const currentBlock = this.chain[i];
            const previousBlock = this.chain[i - 1];
            if (currentBlock.hash !== currentBlock.calculateHash() || currentBlock.previousHash !== previousBlock.hash) {
                return false;
            }
        }
        return true;
    }
}

const aiBlockchain = new Blockchain();
function analyzeMatrix(matrix) {
    // Simuler l'analyse des besoins avec une moyenne probabiliste
    const analysis = matrix.map(slice => 
        slice.map(row => 
            row.reduce((sum, value) => sum + value, 0) / row.length // Moyenne par ligne
        )
    );
    return analysis;
}

function encryptToBinary(data) {
    return data.map(slice => 
        slice.map(row => 
            row.map(value => (value > 0.5 ? 1 : 0)) // Chiffrer > 0.5 comme 1, sinon 0
        )
    );
}

function mineBlocks(blockchain, matrix, numberOfBlocks) {
    for (let i = 0; i < numberOfBlocks; i++) {
        const analysis = analyzeMatrix(matrix);
        const encryptedData = encryptToBinary(analysis);
        blockchain.addBlock({ analysis, encryptedData });
        console.log(`Block ${i + 1} mined.`);
    }
}

// Simuler le minage de 5 blocs
mineBlocks(aiBlockchain, probabilityMatrix, 5);
console.log("Blockchain:", aiBlockchain.chain);
function readBlockchain(blockchain) {
    return blockchain.chain.map(block => ({
        index: block.index,
        timestamp: block.timestamp,
        data: block.data,
    }));
}

console.log("Blockchain history:", readBlockchain(aiBlockchain));
