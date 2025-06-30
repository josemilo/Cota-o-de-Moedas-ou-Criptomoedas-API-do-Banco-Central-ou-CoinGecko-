from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

def run_pipeline():
    df = extract_data()
    df_transformado = transform_data(df)
    load_data(df_transformado)

if __name__ == "__main__":
    run_pipeline()
