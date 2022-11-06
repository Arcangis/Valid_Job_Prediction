FROM python:3.10.6

RUN pip install virtualenv
WORKDIR /app                                                                

COPY ["requirements.txt", "./"]

RUN pip install -r /app/requirements.txt

COPY ["*.py", "*.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:9696", "predict:app"]