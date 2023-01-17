import zipfile
import pandas as pd


def get_dataframe_from_zip_file(file_path: str) -> pd.DataFrame:
    with zipfile.ZipFile(file_path) as z:
        with z.open("GlobalLandTemperaturesByMajorCity.csv") as f:
            df_initial = pd.read_csv(f, parse_dates=["dt"])
    return df_initial
