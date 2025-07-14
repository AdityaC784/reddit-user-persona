# Standard library imports
import os
from typing import List, Dict

# Third-party imports
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client with Groq configuration
client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def generate_persona(username: str, posts: List[Dict], comments: List[Dict]) -> str:
    """
    Generate a user persona based on Reddit posts and comments.

    Args:
        username (str): Reddit username
        posts (List[Dict]): List of user's posts
        comments (List[Dict]): List of user's comments

    Returns:
        str: Generated persona in markdown format
    """
    combined_text = ""

    for post in posts:
        combined_text += (
            f"Post Title: {post['title']}\n"
            f"Body: {post['body']}\n"
            f"URL: {post['permalink']}\n\n"
        )
    
    for comment in comments:
        combined_text += (
            f"Comment: {comment['body']}\n"
            f"URL: {comment['permalink']}\n\n"
        )

    prompt = f'''
    You are an AI assistant. You are given Reddit posts and comments from the user **'{username}'**.

Your task is to generate a structured **User Persona** in Markdown format.

 DO NOT show your thoughts.
 DO NOT include inner monologue or thinking steps.
 ONLY return the structured output below.

Follow this exact format:

---

**User Persona: {username}**

1. **Age Range**
   - Reason: (based on specific post/comment)
   - Cited from: [Full comment or post excerpt]  
     URL: (insert permalink here)

2. **Personality Traits**
   - Traits: (comma-separated values)
   - Cited from: [Quote]  
     URL: (insert permalink here)

3. **Interests**
   - List:
     - (interest 1)
     - (interest 2)
   - Cited from: [Quote]  
     URL: (insert permalink here)

4. **Tone of Communication**
   - Description:
   - Cited from: [Quote]  
     URL: (insert permalink here)

5. **Political Views (if any)**
   - Observations:
   - Cited from: [Quote]  
     URL: (insert permalink here)

6. **Frequent Subreddits**
   - List: (comma-separated subreddit names)

---

User Data:
{combined_text}
'''

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": "You are a Reddit user profiling assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content
