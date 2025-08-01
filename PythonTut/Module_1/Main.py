from Crypto_utils import Wallett
Wallets = Wallett('Bashru')
Wallets.deposit('BTC',2.3)
print(Wallets.view_balance())