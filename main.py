import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from company_age_calculator import calculate_company_age
from word_form_generator import get_year_word_form
from product_data_reader import read_new_product_data


def render_page(foundation_year, today):
    company_age = calculate_company_age(foundation_year, today)
    word_form = get_year_word_form(company_age)

    grouped_wine_data = read_new_product_data()

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        store_age=company_age,
        word_form=word_form,
        grouped_wines=grouped_wine_data,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


def start_server():
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


def main():
    foundation_year = datetime.datetime(year=1920, month=1, day=21)
    today = datetime.date.today()

    render_page(foundation_year, today)
    start_server()


if __name__ == '__main__':
    main()