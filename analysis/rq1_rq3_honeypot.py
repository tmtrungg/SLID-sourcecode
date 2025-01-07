import asyncio
from loguru import logger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import datetime
import time
import tasks
import tasks.eth
import pandas as pd
import aiohttp
from handlers.goplus_handlers import get_goplus_api
from handlers.transpose_handlers import get_transpose_api 
import requests

async def honeypot_verification():
    async with aiohttp.ClientSession() as session:
        df = pd.read_excel('slow.xlsx')
        fields = ['buy_tax', 'sell_tax', 'cannot_buy', 'cannot_sell_all', 'slippage_modifiable', 'is_honeypot', 'transfer_pausable', 'personal_slippage_modifiable', 'trading_cooldown']

        print(df.head())

        # for index, row in df.iterrows():
        address = row['unverified_token']
        pool_address = row['pool_address']
        print(f"Unverified Token: {address}, Pool Address: {pool_address}")
        
        try:
            result = await get_goplus_api(session, address.lower())
            return_data = {key: result['result'][address.lower()].get(key, 0) for key in fields}
            if 'buy_tax' in return_data:
                if return_data['buy_tax'] ==  '':
                    return_data['buy_tax'] = 0
            
            if 'sell_tax' in return_data:
                if return_data['sell_tax'] == '':
                    return_data['sell_tax'] = 0
                    
            print(return_data)
            time.sleep(1)
        except Exception as e:
            logger.error(f"Error at goplus: {e}")
        df.to_excel('slowrug_updated_1.xlsx', index=False)


async def honeypot_check():
    await honeypot_verification()

if __name__ == "__main__":
    logger.info("Starting scheduler")
    scheduler = AsyncIOScheduler()
    scheduler.add_job(honeypot_check)
    scheduler.start()
    asyncio.get_event_loop().run_forever()
