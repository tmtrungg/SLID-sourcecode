from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.eth_slow_liqall import eth_slowliq_crud as crud
from app.api.eth_slow_liqall.eth_slowliq_schemas import (TokenSlowLiquidity,
                                                   TokenSlowLiquidityCreate)
from app.db import get_db
from typing import List

router = APIRouter(
    prefix="/eth-slowrugpull-liquidity",
    tags=["eth-slowrugpull-liquidity"],
    responses={404: {"description": "Not found"}},
    include_in_schema=True,
)


@router.get(
    "/",
    response_model=list[TokenSlowLiquidity],
    summary="Get slow rug-pull tokens liquidity eth",
    description="Get slow rug-pull tokens liquidity eth",
)
def read_eth_slowtokenliq(db: Session = Depends(get_db)):
    eth_tokenliq = crud.get_slowtokens(db)
    return eth_tokenliq

@router.post(
    "/",
    response_model=TokenSlowLiquidity,
    summary="Add slow rug-pull tokens liquidity",
    description="Add slow rug-pull tokens liquidity",
)
def create_eth_slowtokenliq(
        eth_tokenliq: TokenSlowLiquidityCreate, db: Session = Depends(get_db)
):
    db_eth_slowtokenliq = crud.create_eth_slowtokenliq(db, eth_tokenliq)
    return db_eth_slowtokenliq

@router.post(
    "/bulk",
    response_model=List[TokenSlowLiquidity],
    summary="Add slow rug-pull tokens liquidity in bulk",
    description="Add slow rug-pull tokens liquidity in bulk",
)
def add_new_slowtokens_liquidity_bulk(eth_tokenliqs: list[TokenSlowLiquidityCreate], db: Session = Depends(get_db)):
    try:
        db_eth_slowtokenliqs = crud.create_eth_slowtokenliq_bulk(db, eth_tokenliqs)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return db_eth_slowtokenliqs