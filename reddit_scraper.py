# Standard library imports
import os

# Third-party imports
import praw
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Reddit API client
reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent=os.getenv("USER_AGENT")
)

def scrape_user(username: str, limit: int = 50) -> tuple[list, list]:
    """
    Scrape posts and comments from a Reddit user.

    Args:
        username (str): Reddit username to scrape
        limit (int, optional): Maximum number of posts/comments to fetch. Defaults to 50.

    Returns:
        tuple[list, list]: A tuple containing lists of posts and comments
    """
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