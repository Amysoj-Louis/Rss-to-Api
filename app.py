from flask import Flask, jsonify
import json
import threading
import time
import feedparser
import json
import re
import datetime

CLEANR = re.compile('<.*?>')
search_term = 'gold'  # change the search term based on your needs


def rss_to_api():
    try:
        url = ['https://www.business-standard.com/rss/markets-commodities-10608.rss', 'https://www.livemint.com/rss/markets',
               'https://www.thehindubusinessline.com/markets/commodities/feeder/default.rss']
        publisher_name = ['Business Standard',
                          'Livemint', 'The HinduBusinessLine']
        posts_details = {}
        post_list = []
        for i in range(len(url)):
            blog_feed = feedparser.parse(url[i])
            posts = blog_feed.entries

            for post in posts:
                temp = dict()
                try:
                    post_titles = []
                    post_titles.append(list(post.title.split(" ")))
                    for j in range(len(post_titles[0])):
                        if (post_titles[0][j].lower() == search_term):
                            x = re.sub("\u20b9", "Rs ", re.sub(
                                CLEANR, '', post.title))                             # change the currency symbol according to your needs

                            temp["title"] = x
                            temp["link"] = post.link
                            y = re.sub(CLEANR, '', post.summary)
                            temp["summary"] = y

                            try:
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
                            temp["author"] = publisher_name[i]

                            temp["author"] = publisher_name[i]
                        else:
                            pass
                except:
                    pass

                post_list.append(temp)
        post_list = list(filter(None, post_list))
        posts_details["posts"] = post_list
        return posts_details
    except Exception as e:
        print(e)


app = Flask(__name__)


@app.route('/', methods=['GET'])
def welcome():
    return jsonify({"data": rss_to_api()})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="8000")
