FROM python:3

WORKDIR /code

COPY ./ /code/

RUN apt update && apt install -y git curl vim wget zsh && \
    git config --global core.editor vim && \
    chsh -s /bin/zsh root && \
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended && \
    echo 'alias fastapi-dev="fastapi dev /code/app/main.py --port 8080 --host 0.0.0.0"' >> /root/.zshrc && \
    echo 'alias fastapi-prod="fastapi run /code/app/main.py --port 8080 --host 0.0.0.0"' >> /root/.zshrc

RUN pip install poetry && \
    poetry install --all-extras

CMD ["tail", "-f", "/dev/null"]