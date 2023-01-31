# Rss to Api

This is a Flask based web application that converts RSS feed to API data. The application searches for posts in 3 different RSS Feeds, related to the search term 'gold'. The data extracted from the RSS Feeds is cleaned to remove HTML tags, stored in a list of dictionaries, and returned in JSON format when a GET request is made to the endpoint /.

## Requirements

- Flask
- re
- datetime
- feedparser

## Functionality

The function `rss_to_api()` performs the following actions:

- Iterates through a list of RSS Feed URLs, parsing each feed using `feedparser.parse(url[i])`.
- For each feed, it iterates through the list of posts and checks if the post title contains the search term 'gold'.
- If the post title contains the search term 'gold', the function cleans the post title and summary to remove HTML tags, converts the published date to a timestamp, and stores the post details (title, link, summary, published, author) in a temporary dictionary.
- The temporary dictionary is then added to a list of dictionaries, which contains the post details for all posts in all the RSS Feeds.
- The list of dictionaries is stored in another dictionary with the key posts, which is returned by the function `rss_to_api()`.

## API Endpoint

- The Flask application has only one endpoint / that accepts HTTP GET requests.
- When a GET request is made to the endpoint, the function rss_to_api() is called and its returned data is sent in JSON format as a response to the GET request.

## Running the Application

- Clone the repository.
- Navigate to the cloned repository in your terminal.
- Install the required libraries
- Run the Flask application by executing python filename.py
- The application is now accessible at http://localhost:8000/ in your web browser.

### Example Output

```
{
"data": {
    "posts": [
        {
            "author": "Business Standard",
            "link": "https://www.business-standard.com/article/markets/global-gold-demand-grows-18-annually-in-2022-highest-since-2011-wgc-123013100844_1.html",
            "published": 1675156080,
            "summary": "Global gold demand grew 18 per cent annually to touch 4,741 tonnes in 2022, the highest since 2011, mainly driven by strong quarter four (October-December) demand and hefty central bank-buying, the World Gold Council (WGC) said in a report on Tuesday.\nThe total demand during 2021 was 4,012.8 tonnes, according to WGC's annual 'Gold Demand Trends' report.\nAnnual central bank demand more than doubled to 1,136 tonnes in 2022, up from 450 tonnes in the previous year and to a new 55-year high.\nPurchases in the fourth quarter last year alone reached 417 tonnes, bringing the total for the second half of 2022 to more than 800 tonnes, the report stated.\nInvestment demand (excluding over the counter) in 2022 was up 10 per cent against the previous year, mainly due to a notable slowdown in exchange-traded fund (ETF) outflows and strong gold bar and coin demand.\nGold bars and coins continued to hold favour with investors in several countries, which helped to offset weakness in China.\nTotal ..",
            "title": "Global gold demand grows 18% annually in 2022, highest since 2011: WGC"
        }]
    }
}
```
