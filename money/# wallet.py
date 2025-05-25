# wallet.py (Back End)

class Wallet:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

    def get_balance(self):
        return self.balance

# app.py (Front End)

import tkinter as tk
from wallet import Wallet
from flask import Flask, request, jsonify

class WalletApp:
    def __init__(self, root):
        self.wallet = Wallet()
        self.root = root
        self.root.title("Wallet App")

        self.balance_label = tk.Label(root, text="Balance: $0.00")
        self.balance_label.pack()

        self.amount_entry = tk.Entry(root)
        self.amount_entry.pack()

        self.deposit_button = tk.Button(root, text="Deposit", command=self.deposit)
        self.deposit_button.pack()

        self.withdraw_button = tk.Button(root, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack()

    def deposit(self):
        amount = float(self.amount_entry.get())
        if self.wallet.deposit(amount):
            self.update_balance()

    def withdraw(self):
        amount = float(self.amount_entry.get())
        if self.wallet.withdraw(amount):
            self.update_balance()

    def update_balance(self):
        balance = self.wallet.get_balance()
        self.balance_label.config(text=f"Balance: ${balance:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = WalletApp(root)
    root.mainloop()
    # server.py (Server Interface)


    app = Flask(__name__)
    wallet = Wallet()

    @app.route('/balance', methods=['GET'])
    def get_balance():
        return jsonify({'balance': wallet.get_balance()})

    @app.route('/deposit', methods=['POST'])
    def deposit():
        amount = request.json.get('amount', 0)
        if wallet.deposit(amount):
            return jsonify({'success': True, 'balance': wallet.get_balance()})
        return jsonify({'success': False, 'message': 'Invalid amount'})

    @app.route('/withdraw', methods=['POST'])
    def withdraw():
        amount = request.json.get('amount', 0)
        if wallet.withdraw(amount):
            return jsonify({'success': True, 'balance': wallet.get_balance()})
        return jsonify({'success': False, 'message': 'Invalid amount or insufficient funds'})

    if __name__ == '__main__':
        app.run(debug=True)
        class CryptoWallet(Wallet):
            def __init__(self):
                super().__init__()
                self.cryptos = {}

            def deposit_crypto(self, crypto, amount):
                if amount > 0:
                    if crypto in self.cryptos:
                        self.cryptos[crypto] += amount
                    else:
                        self.cryptos[crypto] = amount
                    return True
                return False

            def withdraw_crypto(self, crypto, amount):
                if crypto in self.cryptos and 0 < amount <= self.cryptos[crypto]:
                    self.cryptos[crypto] -= amount
                    return True
                return False

            def get_crypto_balance(self, crypto):
                return self.cryptos.get(crypto, 0.0)

        # Example usage
        crypto_wallet = CryptoWallet()
        crypto_wallet.deposit_crypto('BTC', 0.5)
        crypto_wallet.withdraw_crypto('BTC', 0.1)
        print(crypto_wallet.get_crypto_balance('BTC'))  # Output: 0.4
        
        