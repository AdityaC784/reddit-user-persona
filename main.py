# Standard library imports
import os
import re

# Third-party imports
from reddit_scraper import scrape_user
from persona_generator import generate_persona

# Constants
OUTPUT_DIR = "output"
MAX_POSTS = 20
MAX_COMMENTS = 20


def main():
    """Main function to run the Reddit user persona generator."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    profile_link = input(
        "Enter Reddit profile link (e.g., https://www.reddit.com/user/kojied/): "
    ).strip()
    match = re.search(r"/user/([\w-]+)/?", profile_link)

    if not match:
        print(
            "Invalid Reddit profile URL. Please enter a valid link like https://www.reddit.com/user/SomeUser/"
        )
        return

    username = match.group(1)

    print(f"Scraping data for {username}...")
    posts, comments = scrape_user(username)

    # Limit the number of posts and comments
    posts = posts[:MAX_POSTS]
    comments = comments[:MAX_COMMENTS]

    print(f"Generating persona for {username}...")
    persona = generate_persona(username, posts, comments)

    output_path = os.path.join(OUTPUT_DIR, f"{username}.txt")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(persona)

    print(f"Persona saved to {output_path}")


if __name__ == "__main__":
    main()



