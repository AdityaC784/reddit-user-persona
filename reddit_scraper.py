import praw
import os
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent=os.getenv("USER_AGENT")
)

def scrape_user(username, limit=50):
    user = reddit.redditor(username)
    posts = []
    comments = []

    for post in user.submissions.new(limit=limit):
        posts.append({
            "title": post.title,
            "body": post.selftext,
            "url": post.url,
            "permalink": f"https://www.reddit.com{post.permalink}"
        })

    for comment in user.comments.new(limit=limit):
        comments.append({
            "body": comment.body,
            "permalink": f"https://www.reddit.com{comment.permalink}"
        })

    return posts, comments