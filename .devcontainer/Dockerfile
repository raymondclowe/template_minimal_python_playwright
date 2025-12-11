# Minimal Python dev container for Playwright with Chrome
FROM mcr.microsoft.com/devcontainers/python:3.11

# Install dependencies needed for Playwright and Chrome
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    libnss3 \
    libnspr4 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libdbus-1-3 \
    libxkbcommon0 \
    libxcomposite1 \
    libxdamage1 \
    libxfixes3 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libatspi2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*
