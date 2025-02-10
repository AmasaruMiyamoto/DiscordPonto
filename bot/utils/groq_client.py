import os
import openai
import logging
from typing import List, Dict

logger = logging.getLogger(__name__)

class GroqClient:
    def __init__(self):
        self.api_key = os.getenv('GROQ_API_KEY')
        if not self.api_key:
            raise ValueError("GROQ_API_KEY environment variable not set")
        
        openai.api_key = self.api_key
        openai.api_base = "https://api.groq.com/openai/v1"

    async def get_completion(self, messages: List[Dict[str, str]]) -> str:
        """
        Get completion from Groq API
        
        Args:
            messages: List of message dictionaries with role and content
            
        Returns:
            str: AI response text
        """
        try:
            response = await openai.ChatCompletion.acreate(
                model="mixtral-8x7b-32768",
                messages=messages,
                temperature=0.7,
                max_tokens=1024
            )
            return response.choices[0].message.content
            
        except Exception as e:
            logger.error(f"Error calling Groq API: {e}")
            raise
