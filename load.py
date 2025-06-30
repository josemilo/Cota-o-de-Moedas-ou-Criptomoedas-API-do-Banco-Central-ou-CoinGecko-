import os
from datetime import datetime

def load_data(df):
    os.makedirs('dados', exist_ok=True)
    data = datetime.now().strftime('%Y-%m-%d_%H-%M')
    file_path = f'dados/cripto_{data}.csv'
    df.to_csv(file_path, index=False)
    print(f'Dados salvos em {file_path}')