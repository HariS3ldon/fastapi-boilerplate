FROM python:3

WORKDIR /code

COPY ./ /code/

RUN apt update && apt install -y git curl vim wget zsh && \
    git config --global core.editor vim && \
    chsh -s /bin/zsh root && \
    sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended && \
    echo 'alias fastapi-dev="poetry run uvicorn fa_ms_auth.main:app --reload --host 0.0.0.0 --port 8080 --reload-exclude var --log-level debug' >> /root/.zshrc && \
    echo 'alias fastapi-prod="poetry run uvicorn fa_ms_auth.main:app --reload --host 0.0.0.0 --port 8080 --reload-exclude var --log-level error' >> /root/.zshrc

RUN pip install poetry && \
    poetry install --all-extras && \
    poetry run alembic upgrade head

CMD ["tail", "-f", "/dev/null"]