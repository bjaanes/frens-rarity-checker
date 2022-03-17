import json
import pandas as pd

# Does some shit to load json
filePath = 'nft_rarity.json'

nftFile = open(filePath)

nftData = json.load(nftFile)

# Sets up dictionary
nftDictionary = {}

# Iterates through, adds to dataframe
for x in nftData:
    # Appends some shit

    rarityFloat = float(x['rarity_score'])
    
    # Does math
    KRV = (rarityFloat / 84.3) * 100
    KARV = KRV * 4.679
    LKARV = KARV * 6.11
    KHRV = ((rarityFloat + 5000) / 5084.3) * 100
    KHARV = KHRV * 4.679
    LKHARV = KHARV * 6.11
    
    # Appending more shit
    nftDictionary[x['id']] = {
        'rarity_score': x['rarity_score'],
        'krv': KRV,
        'karv': KARV,
        'lkarv': LKARV,
        'khrv': KHRV,
        'kharv': KHARV,
        'lkharv': LKHARV
    }

df = pd.DataFrame(data = nftDictionary)

df.to_json('values.json')
