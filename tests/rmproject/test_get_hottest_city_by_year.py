import os
from pathlib import Path

import pandas as pd
import pytest

from rmproject.get_dataframe_from_zip_file import get_dataframe_from_zip_file
from rmproject.get_hottest_city_by_year import get_hottest_city_by_year


@pytest.fixture()
def data_path() -> str:
    return os.path.join(Path(__file__).parent.parent, "data/archive.zip")


def test_get_dataframe_by_zip_file(data_path):
    df = get_dataframe_from_zip_file(data_path)
    assert isinstance(df, pd.DataFrame)


def test_get_hottest_city_by_year(data_path):
    df = get_dataframe_from_zip_file(data_path)
    hottest_city = get_hottest_city_by_year(df, 1950)
    assert hottest_city == "Umm Durman"
