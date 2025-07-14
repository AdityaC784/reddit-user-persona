# Reddit User Persona Generator

This project uses the Groq API (via OpenAI's interface) to analyze Reddit users' posts and comments to generate detailed user personas. The tool provides structured insights about users including their age range, personality traits, interests, communication style, and political views.

## Features

- Analyzes Reddit posts and comments
- Generates structured user personas in Markdown format
- Includes citations with links to original content
- Covers multiple aspects of user behavior and preferences

## Prerequisites

- Python 3.10
- A Groq API key
- All other API/IDs required are mentioned in dummy.env file 
- Required Python packages (listed in requirements.txt)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd reddit-user-persona
```

2. Create and activate a virtual environment:
```bash
python -m venv rdtuser-env
# On Windows cmd:
.\rdtuser-env\Scripts\activate
# On Unix or MacOS:
source rdtuser-env/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the project root and add your Groq API key:
```env
GROQ_API_KEY=your_api_key_here

```

## Usage

The project consists of several Python files:
- `persona_generator.py`: Main module for generating user personas
- `reddit_scraper.py`: Module for fetching Reddit user data
- `main.py`: Entry point of the application

```bash
python main.py

```


## Output Format

The generated persona includes:
1. Age Range (with supporting evidence)
2. Personality Traits
3. Interests
4. Tone of Communication
5. Political Views (if any)
6. Frequent Subreddits

Each section includes citations and links to the original content.

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

[Add your chosen license here]
