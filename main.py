from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape

from company_age_calculator import calculate_company_age
from word_form_generator import get_year_word_form
from product_data_reader import read_product_data


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

wine_data = read_product_data()

rendered_page = template.render(
    store_age=calculate_company_age(),
    word_form=get_year_word_form(),
    wines=wine_data,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()