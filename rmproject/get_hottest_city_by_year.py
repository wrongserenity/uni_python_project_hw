import pandas as pd


def get_hottest_city_by_year(df: pd.DataFrame, year: int) -> str:
    df_target_year = df.copy().loc[df.dt.dt.year == year]
    df_target_year = df_target_year.groupby("City").mean()
    df_target_year = df_target_year.loc[df_target_year["AverageTemperature"].idxmax()]
    return df_target_year.name
