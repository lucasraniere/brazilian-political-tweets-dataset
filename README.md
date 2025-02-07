# Brazilian Political Tweets Dataset
---
This repository contains the data analysis for two tweet datasets:

- **2022 Brazilian Presidential Election:**
    - 7,015,186 tweets from 951,602 users, extracted using 91 search terms over 36 different days.
- **2023 Brazilian Early Political Events:**
    - 13,910,048 tweets from 1,346,340 users, extracted using 157 search terms over 56 different days.

_All tweets in these datasets are in **Brazilian Portuguese**._

## Extraction Method

Both datasets were extracted using Twitter's (now X) official API—when Academic Research API access was still available—following the same extraction pipeline. The only difference between the datasets is the extraction period. The process is as follows:

1. **Twitter/X daily monitoring:**  
   The dataset author monitored daily political events appearing in Brazil's Trending Topics. Twitter/X has an automated system for classifying trending terms. When a term was identified as political, it was stored along with its date for later use as a search query.
   
2. **Tweet collection using saved search terms:**  
   Once terms and their corresponding dates were recorded, tweets were extracted from 12:00 AM to 11:59 PM on the day the term entered the Trending Topics. A language filter was applied to select only tweets in Portuguese. The extraction was performed using the official Twitter/X API.
   
3. **Data storage:**  
   The extracted data was organized by day and search term. If the same search term appeared in Trending Topics on consecutive days, a separate file was stored for each respective day.

## Further Information

For more details, visit:

- This repository
- Dataset short paper:
- Dataset:

---

DOI:
