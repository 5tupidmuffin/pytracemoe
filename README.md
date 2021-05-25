# PyTraceMOE

PyTraceMOE is a simple API wrapper for [TraceMOE](https://trace.moe) written in [Python](https://python.org)
Reference taken from [here](https://github.com/FujiMakoto/pysaucenao).

# Usage

```python
from pytracemoe import TraceMOE

sauce = TraceMOE(min_similarity = 60.0)

imageUrl = "https://i.imgur.com/ZeTTFyl.png"
results = sauce.from_url(imageUrl)

print(f'title: {results[0].title_english}')
print(f'episode number: {results[0].episode}')
print(f'similarity: {results[0].similarity}')
print(f'timestamp: {results[0].timestamp}')
print(f'MAL ID: {results[0].mal_id}')
print(f'Anilist ID: {results[0].anilist_id}')
print(f'api calls limit: {results.limit}')
print(f'api calls quota: {results.quota}')
```
```
title: Devilman Crybaby
episode number: 2
similarity: 88.74
timestamp: 1015.915
MAL ID: 35120
Anilist ID: 98460
api calls limit: 10
api calls quota: 1000
```

