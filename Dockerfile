# Используем официальный образ Selenium Chrome
FROM selenium/standalone-chrome:latest

# Переключаемся на root для установки пакетов
USER root

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Вариант 2: Жёстко указанный репозиторий (раскомментировать при необходимости)
RUN git clone https://github.com/art-kovalev-93/Sprint_6.git /app/repo

# Переходим в директорию проекта
WORKDIR /app/repo

# Устанавливаем зависимости Python
RUN pip3 install --no-cache-dir -r requirements.txt

# Устанавливаем pytest если его нет в requirements.txt
RUN pip3 install pytest

# Запускаем тесты
CMD ["pytest", "-v", "--tb=short"]