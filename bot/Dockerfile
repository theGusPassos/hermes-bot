FROM python:3

ADD . /

RUN pip install requests-async
RUN pip install -U discord.py
RUN pip install -U python-dotenv

CMD [ "python", "bot.py" ]
