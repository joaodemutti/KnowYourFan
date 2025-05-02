import base64
import os
import io
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

MIME_TYPE_MAP = {
    "png": "image/png",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
}


def encode_image_bytes_to_base64(image_bytes: bytes) -> str:
    return base64.b64encode(image_bytes).decode("utf-8")


async def validate_document_image_bytes(image_bytes: bytes, ext: str = "png", prompt: str = "isso é um documento Brasileiro? Responda 0 ou 1") -> str | None:
    try:
        ext = ext.lower()
        mime_type = MIME_TYPE_MAP.get(ext)
        if not mime_type:
            raise ValueError(f"Unsupported image extension: {ext}")

        base64_image = encode_image_bytes_to_base64(image_bytes)

        # Estrutura correta para o conteúdo com texto e imagem
        content = {
            "parts": [
                {"text": prompt},
                {
                    "inline_data": {
                        "mime_type": mime_type,
                        "data": base64_image
                    }
                }
            ]
        }

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(
            contents=[content],
            generation_config=genai.GenerationConfig(max_output_tokens=500),
        )

        if response and response.text:
            return response.text.strip()
        else:
            print(f"Empty or invalid response from Gemini: {response}")
            return None

    except Exception as e:
        print(f"Error during document validation: {e}")
        raise e


async def get_esports_content(interests: list[str], prompt: str = "Compartilhe links de perfis relevantes em sites de E-Sports com base nesses interesses.") -> str | None:
    try:
        if not interests:
            raise ValueError("A lista de interesses está vazia.")

        full_prompt = prompt+"\nInteresses do usuário:\n" +"\n".join(interests)

        content = {
            "parts": [
                {"text": full_prompt}
            ]
        }

        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(
            contents=[content],
            generation_config=genai.GenerationConfig(max_output_tokens=700),
        )

        if response and response.text:
            return response.text.strip()
        else:
            print("Resposta vazia ou inválida de Gemini.")
            return None

    except Exception as e:
        print(f"Erro ao gerar conteúdo de E-Sports: {e}")
        raise e
