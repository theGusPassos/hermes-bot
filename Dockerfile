FROM python:3

ADD bot.py /

RUN pip install -U discord.py
RUN pip install -U python-dotenv

CMD [ "python", "bot.py" ]
