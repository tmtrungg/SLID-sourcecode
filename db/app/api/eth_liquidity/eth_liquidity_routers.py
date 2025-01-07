from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.eth_liquidity import eth_liquidity_crud as crud
from app.api.eth_liquidity.eth_liquidity_schemas import (TokenLiquidity,
                                                   TokenLiquidityCreate)
from app.db import get_db
from typing import List

router = APIRouter(
    prefix="/eth-alltokens-liquidity",
    tags=["eth-alltokens-liquidity"],
    responses={404: {"description": "Not found"}},
    include_in_schema=True,
)


@router.get(
    "/",
    response_model=list[TokenLiquidity],
    summary="Get all tokens liquidity eth",
    description="Get all tokens liquidity eth",
)
def read_eth_tokenliq(db: Session = Depends(get_db)):
    eth_tokenliq = crud.get_tokens(db)
    return eth_tokenliq

@router.post(
    "/",
    response_model=TokenLiquidity,
    summary="Add new tokens liquidity",
    description="Add new tokens liquidity",
)
def create_eth_tokenliq(
        eth_tokenliq: TokenLiquidityCreate, db: Session = Depends(get_db)
):
    db_eth_tokenliq = crud.create_eth_tokenliq(db, eth_tokenliq)
    return db_eth_tokenliq

@router.post(
    "/bulk",
    response_model=List[TokenLiquidity],
    summary="Add new tokens liquidity in bulk",
    description="Add new tokens liquidity in bulk",
)
def add_new_tokens_liquidity_bulk(eth_tokenliqs: list[TokenLiquidityCreate], db: Session = Depends(get_db)):
    try:
        db_eth_tokenliqs = crud.create_eth_tokenliq_bulk(db, eth_tokenliqs)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return db_eth_tokenliqs