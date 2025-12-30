import gspread
from google.oauth2.service_account import Credentials
import pandas as pd

def upload_dataframe_to_gsheet(df):
    scopes = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive"
    ]

    creds = Credentials.from_service_account_file(
        "service_account.json",
        scopes=scopes
    )

    client = gspread.authorize(creds)
    spreadsheet = client.open("Crypto_Market_Analytics")

    try:
        worksheet = spreadsheet.worksheet("crypto_data")
    except gspread.WorksheetNotFound:
        worksheet = spreadsheet.add_worksheet(
            title="crypto_data",
            rows=1000,
            cols=50
        )

    existing_data = worksheet.get_all_values()


    df = df.astype(str)

    if len(existing_data) == 0:
        worksheet.update(
            [df.columns.tolist()] + df.values.tolist()
        )
        print("✅ First load: headers + data uploaded")
        return

    headers = existing_data[0]

    if "load_date" not in headers:
        worksheet.clear()
        worksheet.update(
            [df.columns.tolist()] + df.values.tolist()
        )
        print("⚠️ load_date not found → sheet reset & full load done")
        return

    existing_df = pd.DataFrame(existing_data[1:], columns=headers)

    last_load_date = existing_df["load_date"].max()

    incremental_df = df[df["load_date"] > last_load_date]

    if incremental_df.empty:
        print("⚠️ No new data to load")
        return

    worksheet.append_rows(incremental_df.values.tolist())
    print(f"✅ Incremental load: {len(incremental_df)} new rows added")
