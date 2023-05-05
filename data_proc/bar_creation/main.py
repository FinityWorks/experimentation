from fastapi import FastAPI
from fin_tools.aggregations import BarMaker
from fin_tools.clients import Binance
from fin_tools.formatting import df_to_dict

app = FastAPI()


@app.get("/bars")
def get_bars():
    return {}
