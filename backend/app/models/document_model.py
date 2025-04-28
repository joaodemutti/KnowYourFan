from pydantic import BaseModel

class DocumentDTO(BaseModel):
    document_type: str
    document_url: str
