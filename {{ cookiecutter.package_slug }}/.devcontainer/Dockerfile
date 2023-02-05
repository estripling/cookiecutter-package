FROM {{ cookiecutter.docker_base_image }}

# configurations
ENV PYTHONUNBUFFERED=on \
    PYTHONFAULTHANDLER=on \
    PYTHONHASHSEED=random \
    PYTHONDONTWRITEBYTECODE=on \
    # pip:
    PIP_NO_CACHE_DIR=on \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=120 \
    # poetry:
    POETRY_VERSION={{ cookiecutter.poetry_version }} \
    POETRY_NO_ANSI=on \
    POETRY_NO_INTERACTION=on \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME="/opt/poetry" \
    PATH="${POETRY_HOME}/bin:${PATH}"

# install additional system packages
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install --no-install-recommends -y \
    gcc \
    make \
    python-dev \
    ## cleanup
    && apt-get clean -y \
    && apt-get autoclean -y \
    && apt-get autoremove --purge  -y \
    && rm -rf /var/lib/apt/lists/*

# install poetry
RUN python3 -m pip install poetry==${POETRY_VERSION}

# create workspace
WORKDIR /workspaces/{{ cookiecutter.package_slug }}

# install project dependencies
COPY . .
RUN poetry install \
    && rm -rf ~/.cache/pypoetry/{cache,artifacts}
