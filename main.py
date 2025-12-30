from extract import fetch_crypto_data
from transform import transform_crypto_data
from upload_to_gsheets import upload_dataframe_to_gsheet

print("🚀 Crypto pipeline started")

df = fetch_crypto_data()
df = transform_crypto_data(df)

upload_dataframe_to_gsheet(df)

print("Pipeline finished successfully")

