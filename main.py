import smtplib, ssl
import os
from dotenv import load_dotenv

load_dotenv()

smt_server = os.getenv('SMTP_SERVER')
port = os.getenv('SMTP_PORT')

login = os.getenv('LOGIN')
password = os.getenv('PASSWORD')

sender = os.getenv('LOGIN')
receiver = os.getenv('RECEIVER')

website = '%website%'
friend_name = '%friend_name%'
my_name = '%my_name%'

message = f'''\
From: {sender}
To: {receiver}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''

message = message.replace(website, 'https://dvmn.org/profession-ref-program/idov555/AUWFk/').replace(friend_name, 'Виктор').replace(my_name, 'Ольга')
message = message.encode("UTF-8")

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smt_server, port, context=context) as server:
    server.login(login, password)
    server.sendmail(sender, receiver, message)