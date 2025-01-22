from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from company_age_calculator import calculate_company_age
from word_form_generator import get_year_word_form
from product_data_reader import read_new_product_data


def render_page():
    grouped_wine_data = read_new_product_data()

    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    rendered_page = template.render(
        store_age=calculate_company_age(),
        word_form=get_year_word_form(),
        grouped_wines=grouped_wine_data,
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)


def start_server():
    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    render_page()
    start_server()