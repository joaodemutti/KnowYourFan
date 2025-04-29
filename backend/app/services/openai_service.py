import base64
import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def encode_image_bytes_to_base64(image_bytes: bytes) -> str:
    """
    Encodes image bytes to a base64 string.
    """
    return base64.b64encode(image_bytes).decode("utf-8")


async def validate_document_image_bytes(image_bytes: bytes, ext: str = "png", prompt: str = "Is this a valid Brazilian ID or official document?") -> str | None:
    """
    Sends image bytes to ChatGPT Vision model to validate the document.

    Args:
        image_bytes (bytes): Raw image bytes (e.g. from UploadFile.read()).
        ext (str): File extension (e.g. png, jpg).
        prompt (str): Prompt/question for ChatGPT to answer about the document.

    Returns:
        str | None: The response from ChatGPT, or None on error.
    """
    try:
        base64_image = encode_image_bytes_to_base64(image_bytes)

        response = await client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/{ext};base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            max_tokens=500
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"Error during document validation: {e}")
        raise e
