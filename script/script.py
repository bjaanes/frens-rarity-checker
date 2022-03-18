import json
import pandas as pd

# Does some shit to load json
filePath = 'nft_rarity.json'

nftFile = open(filePath)

nftData = json.load(nftFile)

# Sets up dictionary
nftDictionary = {}

sortedNftData = sorted(nftData, key=lambda d: d['rarity_score'], reverse=True)

# Iterates through, adds to dataframe
for i in range(len(sortedNftData)):
    nft = sortedNftData[i]

    rarityScore = float(nft['rarity_score'])

    # Does math
    KRV = (rarityScore / 84.3) * 140
    KARV_PRESENT = KRV * 4.679
    KARV_FUTURE = KARV_PRESENT * 6.11

    KHRV = ((rarityScore + 5000) / 5084.3) * 140
    KHARV_PRESENT = KHRV * 4.679
    KHARV_FUTURE = KHARV_PRESENT * 6.11

    # Appending more shit
    nftDictionary[nft['id']] = {
        'rarity_score': nft['rarity_score'],
        'rank': int(i+1),
        'krv': KRV,
        'karv_present': KARV_PRESENT,
        'karv_future': KARV_FUTURE,
        'khrv': KHRV,
        'kharv_present': KHARV_PRESENT,
        'kharv_future': KHARV_FUTURE
    }



df = pd.DataFrame(data = nftDictionary)

df.to_json('values.json')
