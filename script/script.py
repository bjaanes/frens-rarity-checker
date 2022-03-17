import json
import pandas as pd

# Does some shit to load json
filePath = '/Users/cameronfink/Downloads/nft_rarity.json'

nftFile = open(filePath)

nftData = json.load(nftFile)

# Sets up dictionary
nftDictionary = {
    'ID': [],
    'Rarity': [],
    'KRV': [],
    'KARV': [],
    'LKARV': [],
    'KHRV': [],
    'KHARV': [],
    'LKHARV': []
    }

# Iterates through, adds to dataframe
for x in nftData:
    # Appends some shit
    nftDictionary['ID'].append(x['id'])
    nftDictionary['Rarity'].append(x['rarity_score'])
    
    rarityFloat = float(x['rarity_score'])
    
    # Does math
    KRV = (rarityFloat / 84.3) * 100
    KARV = KRV * 4.679
    LKARV = KARV * 6.11
    KHRV = ((rarityFloat + 5000) / 5084.3) * 100
    KHARV = KHRV * 4.679
    LKHARV = KHARV * 6.11
    
    # Appending more shit
    nftDictionary['KRV'].append(KRV)
    nftDictionary['KARV'].append(KARV)
    nftDictionary['LKARV'].append(LKARV)
    nftDictionary['KHRV'].append(KHRV)
    nftDictionary['KHARV'].append(KHARV)
    nftDictionary['LKHARV'].append(LKHARV)
    
df = pd.DataFrame(data = nftDictionary)

df.to_json('values.json')
