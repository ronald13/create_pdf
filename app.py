import jinja2
import pdfkit
from  num2words import num2words
from datetime import datetime


##########################

     # VARIABLES

##########################
invoice_number = ''
today_date = datetime.today().strftime("%d %b, %Y")
day = datetime.today().strftime("%d")
month = datetime.today().strftime("%B")
year = datetime.today().strftime("%Y")
customer_name = "Frank Andrade"
dogovor_number = str(day)+'/'+month+' от '+str(today_date)
final_price_text = num2words(325.5, lang='ru')
print(datetime.today())

context = {'invoice_number':'invoice_number', 'today_date': today_date, 'month':month,
           'customer_name':customer_name, 'dogovor_number':dogovor_number, 'final_price_text':final_price_text

           }

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'invoice.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf='/usr/bin/wkhtmltopdf')
output_pdf = 'invoice.pdf'

options = {
    'page-size': 'Letter',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'no-outline': None
}

pdfkit.from_string(output_text, output_pdf, configuration=config, css='style.css', options=options)