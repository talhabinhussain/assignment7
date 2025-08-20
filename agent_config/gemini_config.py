from agents import AsyncOpenAI,OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os

load_dotenv(override=True)

gemini_api_key = os.environ.get("GEMINI_API_KEY")
gemini_base_url = os.environ.get("BASE_URL")
gemini_ai_model = os.environ.get("AI_MODEL")


external_client = AsyncOpenAI(api_key=gemini_api_key,base_url=gemini_base_url)

MODEL = OpenAIChatCompletionsModel(openai_client=external_client,model=gemini_ai_model)



