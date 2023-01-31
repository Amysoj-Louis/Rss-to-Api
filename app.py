# Import the required libraries
import re
import datetime
import feedparser
from flask import Flask, jsonify

# Compile a regular expression pattern to remove HTML tags
CLEANR = re.compile('<.*?>')
# Set search term to 'gold'
search_term = 'gold'

# Define a function to convert RSS feed to API data


def rss_to_api():
    try:
        # List of RSS Feed URLs
        url = ['https://www.business-standard.com/rss/markets-commodities-10608.rss', 'https://www.livemint.com/rss/markets',
               'https://www.thehindubusinessline.com/markets/commodities/feeder/default.rss']
        # List of publishers for each RSS Feed
        publisher_name = ['Business Standard',
                          'Livemint', 'The HinduBusinessLine']
        # Dictionary to store all post details
        posts_details = {}
        # List to store individual post details
        post_list = []

        # Iterate through all the RSS Feed URLs
        for i in range(len(url)):
            # Parse the RSS Feed URL
            blog_feed = feedparser.parse(url[i])
            # Get all posts in the RSS Feed
            posts = blog_feed.entries

            # Iterate through each post
            for post in posts:
                # Temporary dictionary to store post details
                temp = dict()
                try:
                    post_titles = []
                    # Split the post title into words
                    post_titles.append(list(post.title.split(" ")))
                    # Iterate through each word in the post title
                    for j in range(len(post_titles[0])):
                        # Check if the word matches the search term
                        if (post_titles[0][j].lower() == search_term):
                            # Clean post title to remove HTML tags
                            x = re.sub("\u20b9", "Rs ", re.sub(
                                CLEANR, '', post.title))
                            # Store cleaned post title
                            temp["title"] = x
                            # Store post link
                            temp["link"] = post.link
                            # Clean post summary to remove HTML tags
                            y = re.sub(CLEANR, '', post.summary)
                            # Store cleaned post summary
                            temp["summary"] = y

                            try:
                                # Convert post published date to timestamp
                                element = datetime.datetime.strptime(
                                    post.published, "%a, %d %b %Y %H:%M:%S %z")
                                temp["published"] = int(
                                    datetime.datetime.timestamp(element))
                            except:
                                post.published = post.published.replace(
                                    "+5:30", " +0530")
                                element = datetime.datetime.strptime(
                                    post.published, "%a, %d %b %Y %H:%M:%S %z")
                                temp["published"] = int(
                                    datetime.datetime.timestamp(element))
                            # Store publisher name
                            temp["author"] = publisher_name[i]
                        else:
                            pass
                except:
                    pass

                # Append post details to post list
                post_list.append(temp)
        # Remove empty items from post list
        post_list = list(filter(None, post_list))
        # Store post list in posts_details dictionary
        posts_details["posts"] = post_list
        # Return the posts_details
        return posts_details
    except Exception as e:
        # Print the error
        print(e)


# Creating a Flask object
app = Flask(__name__)

# Setting the endpoint for HTTP GET requests


@app.route('/', methods=['GET'])
def welcome():
    # Returns the data returned by rss_to_api() in a JSON format
    return jsonify({"data": rss_to_api()})


# Running the Flask app with host IP 0.0.0.0 and port 8000
if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8000")
