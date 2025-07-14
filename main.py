from reddit_scraper import scrape_user
from persona_generator import generate_persona
import os
import re

output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

profile_link = input("Enter Reddit profile link (e.g., https://www.reddit.com/user/kojied/): ").strip()
match = re.search(r"/user/([\w-]+)/?", profile_link)

if not match:
    print("Invalid Reddit profile URL. Please enter a valid link like https://www.reddit.com/user/SomeUser/")
    exit()

username = match.group(1)

print(f"Scraping data for {username}...")
posts, comments = scrape_user(username)


posts = posts[:20]
comments = comments[:20]

print(f"Generating persona for {username}...")
persona = generate_persona(username, posts, comments)

output_path = os.path.join(output_dir, f"{username}.txt")
with open(output_path, "w", encoding="utf-8") as f:
    f.write(persona)

print(f"Persona saved to {output_path}")



