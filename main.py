from fastapi import FastAPI, HTTPException
from fastapi.responses import Response


app = FastAPI()

BALANCE = {}


@app.get('/health')
def health_check():
    return Response(status_code=200)


@app.get('/balance')
def get_balance(wallet_name: str | None = None):
    if wallet_name is None:
        return {'total_balance': sum(BALANCE.values())}
    if wallet_name not in BALANCE:
        raise HTTPException(
            status_code=404,
            detail=f'Кошелек {wallet_name} не найден!'
        )
    return {'Кошелек': wallet_name, 'balance': BALANCE[wallet_name]}


@app.post('/wallets/{name}')
def recive_money(name: str, amount: int):
    if name not in BALANCE:
        BALANCE[name] = 0
    BALANCE[name] += amount
    return {
        'message': f'Добавлено {amount} в кошелек {name}',
        'wallet': name,
        'new_balance': BALANCE[name]
    }
