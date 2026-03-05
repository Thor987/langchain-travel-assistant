import os
from dotenv import load_dotenv

load_dotenv()

ZHIPUAI_API_KEY = os.getenv("ZHIPUAI_API_KEY")
MODEL_NAME = "glm-4"
TEMPERATURE = 0.5
