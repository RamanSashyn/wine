import pandas
from collections import defaultdict


def read_new_product_data():
    excel_data_df = pandas.read_excel("wine3.xlsx", sheet_name="Лист1" )
    excel_data_df = excel_data_df.fillna("")

    grouped_products = defaultdict(list)
    for _, row in excel_data_df.iterrows():
        grouped_products[row["Категория"]].append(row.to_dict())

    return grouped_products