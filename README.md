# Opensea Mass Metadata Refresh Bot

A simple python bot that can refresh Metadata for entire collection on Opensea.

Note: This was a fun project for experimental and learning purposes. 
</br>

# Installation and Instructions
1. Download the code from this repository

2. install the following module
```
pip install selenium
```

# Edit MetadataRefresherForOpensea.py
1. Enter NFT contract address
```
contractAddress = "your-nft-contract-address"
```

2. From which Token ID it should start refreshing?
```
startFrom = 1528
```

3. Up-to which Token ID it should keep refreshing?
```
refreshToNumber = 2300
```


4. Run in the background (headless mode)? True/False
```
runInBackground = False
```
