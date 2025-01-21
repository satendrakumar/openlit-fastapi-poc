from typing import Optional

from pydantic import BaseModel, Field


class ChatPayload(BaseModel):
    model: Optional[str] = Field(..., description="Model Name")
    question: Optional[str] = Field(..., description="Question")


class EmbeddingPayload(BaseModel):
    text: Optional[str] = Field(..., description="Text")