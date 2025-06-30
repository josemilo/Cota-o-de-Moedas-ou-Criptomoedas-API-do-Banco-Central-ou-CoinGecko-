def transform_data(df):
    df = df[[
        'id',
        'symbol',
        'name',
        'current_price',
        'market_cap',
        'total_volume',
        'price_change_percentage_24h',
        'last_updated'
    ]]
    df.columns = [
        'id',
        'simbolo',
        'nome',
        'preco_atual_usd',
        'market_cap',
        'volume_total',
        'variacao_24h_percentual',
        'data_atualizacao'
    ]
    return df