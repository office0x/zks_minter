## zns_minter
This script registers domain names from https://zks.network/ on the zksync network. It's an additional contract for your accounts. The minting commission is around 30 cents.

# installation

Before you can start minting your NFTs, you'll need to install the required dependencies. Open your terminal and execute the following command:

```bash
pip install -r requirements.txt
```


# config

Place your private keys in private_keys.txt and domain names in names.txt.
Configure settings in the config.py file.

# execution

```python
python3 minter.py
```


