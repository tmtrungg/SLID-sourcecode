from fastapi import APIRouter


from app.api.eth_liquidity import eth_liquidity_routers
from app.api.eth_slow_liqall import eth_slowliq_routers

api_v1_routers = APIRouter(
    prefix="/v1",
    responses={404: {"description": "Not found"}},
)

api_v1_routers.include_router(eth_liquidity_routers.router)
api_v1_routers.include_router(eth_slowliq_routers.router)

# RAG
# api_v1_routers.include_router(rag_routers.router)
