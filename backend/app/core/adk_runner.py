import json
import os

import yaml
from dotenv import load_dotenv
from google import genai

from app.schemas.schemas import AgentResult

load_dotenv()


class ADKRunner:

    def __init__(self):

        with open(
            "config/config.yaml",
            "r",
            encoding="utf-8"
        ) as file:

            self.config = yaml.safe_load(file)

        self.client = genai.Client(
            api_key=os.getenv("GOOGLE_API_KEY")
        )

        self.model_name = self.config["model"]["model_name"]

        self.temperature = self.config["model"]["temperature"]

        self.system_prompt = self.config["prompt"]["system_prompt"]

    def classify_page(
        self,
        page_number: int,
        text: str
    ) -> AgentResult:

        try:

            prompt = f"""
{self.system_prompt}

Page Content:

{text}
"""
            print(
                f"Calling Gemini for page {page_number}"
            )

            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt
            )
            print(
                f"Gemini response received for page {page_number}"
            )   
            result = json.loads(
                response.text
            )

            return AgentResult(
                success=True,
                category=result["category"],
                reasoning=result["reasoning"]
            )

        except Exception as e:

            return AgentResult(
                success=False,
                error=str(e)
            )