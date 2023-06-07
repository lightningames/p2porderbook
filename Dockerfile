# TODO: add mongodb install and setup with the dbtools.py file
FROM python:3.9

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# set environment variables
CMD [ "python", "./tgbot.py" ]
