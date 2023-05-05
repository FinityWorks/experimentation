import asyncio

import polars as pl
from fastapi import FastAPI
from fin_tools.aggregations import BarMaker
from fin_tools.clients import Binance
from fin_tools.formatting import df_to_dict

app = FastAPI()


@app.get("/")
async def get_bars():
    binance = Binance()

    df = await binance.pull_data("BTC/USDT")
    await binance.close()

    df = df.with_columns(pl.col("id").str.parse_int(10).diff().alias("id_diff"))
    df = df.drop_nulls()

    bar_maker = BarMaker()

    df = bar_maker.create_imbalance_bars(df, "amount", 1)

    return df_to_dict(df, sort="amount_imbal_bar_id")
