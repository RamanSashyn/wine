import pandas
import os
import argparse
from collections import defaultdict


def read_new_product_data(file_path):
    excel_data_df = pandas.read_excel(file_path, sheet_name="Лист1" )
    excel_data_df = excel_data_df.fillna("")

    grouped_products = defaultdict(list)
    for _, row in excel_data_df.iterrows():
        grouped_products[row["Категория"]].append(row.to_dict())

    return grouped_products


def get_file_path():
    parser = argparse.ArgumentParser(description="Process product data.")
    parser.add_argument(
        "--file",
        default=os.getenv("WINE_FILE_PATH", "wine3.xlsx"),  # Дефолтное значение
        help="Path to the Excel file with product data"
    )
    args = parser.parse_args()
    return args.file