from fastapi import FastAPI
from pydantic import BaseModel
from predict import predict

app = FastAPI(title="Prediction API")

class InputData(BaseModel):
    risk_factor: float
    first_tx_timestamp: float
    max_eth_ever: float
    min_eth_ever: float
    risk_factor_above_threshold_daily_count: float
    repay_amount_avg_eth: float
    liquidation_amount_sum_eth: float
    time_since_last_liquidated: float
    total_balance_eth: float
    risky_sum_outgoing_amount_eth: float
    liquidation_count: float
    risky_first_last_tx_timestamp_diff: float
    total_available_borrows_avg_eth: float
    avg_weighted_risk_factor: float
    market_atr: float
    borrow_repay_diff_eth: float
    outgoing_tx_sum_eth: float
    total_available_borrows_eth: float
    wallet_age: float
    incoming_tx_sum_eth: float
    deposit_count: float
    market_adxr: float
    borrow_amount_avg_eth: float
    market_fastk: float
    market_fastd: float
    market_correl: float
    market_dx: float
    incoming_tx_count: float
    market_cmo: float
    market_adx: float
    incoming_tx_avg_eth: float
    market_max_drawdown_365d: float
    risky_tx_count: float
    unique_borrow_protocol_count: float
    market_aroonosc: float
    avg_gas_paid_per_tx_eth: float
    outgoing_tx_avg_eth: float
    risky_unique_contract_count: float
    hash_19: float
    hash_5: float
    hash_8: float
    hash_30: float
    hash_2: float
    hash_14: float
    hash_16: float
    hash_17: float
    hash_31: float
    hash_27: float
    hash_12: float
    hash_28: float
    hash_25: float
    hash_13: float

@app.post("/predict")
def get_prediction(data: InputData):
    data_dict = data.dict()
    score = predict(data_dict)
    return {"probability": score}