FROM python:3

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apt update && apt install -y git curl vim wget && \
    git config --global core.editor vim
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["fastapi", "run", "app/main.py", "--port", "8080"]