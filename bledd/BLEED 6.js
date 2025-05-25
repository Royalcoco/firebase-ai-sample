const Ajv = require("ajv");
const ajv = new Ajv();

const transactionSchema = {
    type: "object",
    properties: {
        transactionId: { type: "string", pattern: "^[a-f0-9]{64}$" },
        senderWallet: { type: "string", pattern: "^[a-zA-Z0-9]{34}$" },
        receiverWallet: { type: "string", pattern: "^[a-zA-Z0-9]{34}$" },
        amount: { type: "number", minimum: 0.0001 },
        currency: { type: "string", enum: ["BTC", "ETH", "USDT", "USD"] },
        timestamp: { type: "string", format: "date-time" }
    },
    required: ["transactionId", "senderWallet", "receiverWallet", "amount", "currency", "timestamp"]
};

function validateTransaction(transaction) {
    const validate = ajv.compile(transactionSchema);
    const valid = validate(transaction);

    if (!valid) {
        console.error("Invalid transaction:", validate.errors);
        throw new Error("Transaction validation failed.");
    }

    console.log("Transaction is valid.");
}

// Example transaction
const transaction = {
    transactionId: "a3f1c59d4ef99a2b4a8a6e78123d36f7b67823a4567891234567a2b4a8c6d7e8",
    senderWallet: "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
    receiverWallet: "3J98t1WpEZ73CNmQviecrnyiWrnqRhWNLy",
    amount: 0.5,
    currency: "BTC",
    timestamp: new Date().toISOString()
};

try {
    validateTransaction(transaction);
} catch (error) {
    console.error(error.message);
}
