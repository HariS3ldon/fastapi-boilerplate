FROM python:3

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN apt update && apt install -y git curl vim wget zsh && \
    git config --global core.editor vim && \
    chsh -s /bin/zsh root && \
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["fastapi", "run", "app/main.py", "--port", "8080"]