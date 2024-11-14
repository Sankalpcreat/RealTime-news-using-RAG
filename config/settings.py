import os
from dotenv import load_dotenv

load_dotenv()


NEWS_API_KEY=os.getenv("NEWS_API_KEY")

OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")


if not NEWS_API_KEY:
    raise EnvironmentError("NEWS_API_KEY not found in enviromnentm vaeialae")

if not OPENAI_API_KEY:
    raise EnvironmentError("OPENAI_API_KEY not found in enviromnentm vaeialae")