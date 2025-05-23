from email.message import EmailMessage  # пакет email модуль message
import smtplib  # модуль
from string import Template
from pathlib import Path
# с помощью smtplib мы будет отправлять имэйл сконструированный классом EmailMessage

# загhужаем b читаем из папки шаблон html
html_template = Template(Path("templates/index.html").read_text())
# метод substitute позволяет заменить значения с $
html_content = html_template.substitute({'name': 'Vika', 'date': 'tommorow'})


my_email = EmailMessage()  # новый экземпляр класса
# с помощью EmailMessage мы будем конструировать имэйл

my_email['from'] = 'Vika'
my_email['to'] = 'test@gmail.com'
my_email['subject'] = 'let\'s go out'
my_email.set_content(html_content, 'html')

# порт указываем тот на котором у нас открыт докер
with smtplib.SMTP(host='localhost', port=2525) as smtp_server:
    smtp_server.ehlo()  # ehlo - метод который устранавливает связь с smtp сервером
    # smtp_server.starttls()  # передача данных в зашифрованном виде
    # smtp_server.login('username', 'password')  # для авторизации
    smtp_server.send_message(my_email)
    print('email was sent!')
