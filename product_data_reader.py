import pandas
from pprint import pprint


def read_product_data():
    excel_data_df = pandas.read_excel("wine.xlsx", sheet_name="Лист1")
    product_data = excel_data_df.to_dict(orient="records")
    return product_data

def read_new_product_data():
    excel_data_df = pandas.read_excel("wine2.xlsx", sheet_name="Лист1" )
    excel_data_df = excel_data_df.fillna("")

    grouped_products = {}
    for category, group in excel_data_df.groupby("Категория"):
        grouped_products[category] = group.to_dict(orient="records")

    return grouped_products

if __name__ == "__main__":
    product_data = read_new_product_data()
    pprint(product_data)