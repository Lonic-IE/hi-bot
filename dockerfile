FROM python:3.11


RUN pip install --upgrade pip
RUN pip install discord.py


WORKDIR /main.py

CMD [ "python","./main.py" ]