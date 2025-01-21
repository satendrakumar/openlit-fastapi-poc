import openlit
from fastapi import APIRouter, HTTPException, status
from sentence_transformers import SentenceTransformer

from src.api.forms import ChatPayload, EmbeddingPayload
from src.chat.chat_service import chat
from src.util.logger import get_logger

chat_api = APIRouter(prefix=f"/v1/api")

logger = get_logger(__name__)

model = SentenceTransformer("sentence-transformers/LaBSE", trust_remote_code=True)

@openlit.trace
def get_embeddings(text):
    return model.encode(text)


@chat_api.post(
    "/embedding",
    summary="Get embedding for text",
    response_description="Return HTTP Status Code 200 OK",
    status_code=status.HTTP_200_OK,
)
async def get_search(payload: EmbeddingPayload):
    try:
        logger.info(f"Received request for search: {payload}")
        res = get_embeddings(text=payload.text).tolist()
        logger.info(f"Res: {res[:10]}")
        return {"embedding": res}
    except HTTPException as http_exc:
        logger.error(f"ERROR occurred: {http_exc}")
        raise http_exc
    except Exception as e:
        logger.error(f"ERROR occurred: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred.",
        )


@chat_api.post(
    "/chat",
    summary="Chat",
    response_description="Return HTTP Status Code 200 OK",
    status_code=status.HTTP_200_OK,
)
async def get_search(payload: ChatPayload):
    try:
        logger.info(f"Received request for search: {payload}")
        res = chat(model=payload.model, message=payload.question)
        return {"answer": res}
    except HTTPException as http_exc:
        logger.error(f"ERROR occurred: {http_exc}")
        raise http_exc
    except Exception as e:
        logger.error(f"ERROR occurred: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An unexpected error occurred.",
        )
