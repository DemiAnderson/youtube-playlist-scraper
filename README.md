# YouTube Playlist Scraper

Этот проект использует Selenium для сбора информации о видео из плейлиста YouTube.

## Установка и запуск

1. Клонируйте репозиторий:
   ```
   git clone https://github.com/your-username/youtube-playlist-scraper.git
   cd youtube-playlist-scraper
   ```

2. Создайте виртуальное окружение и активируйте его:
   ```
   python -m venv venv

   Windows: `venv\Scripts\activate`
   macOS/Linux: `source venv/bin/activate`
   ```

3. Установите зависимости:
   ```
   pip install -r requirements.txt
   ```

4. Запустите скрипт:
   ```
   python main.py <URL плейлиста>
   ```

   Например:
   ```
   python main.py https://www.youtube.com/playlist?list=PLlfVHEB1pHYb0ORhWxdECbIjmutbVO-Q1
   ```

5. Результаты будут сохранены в файле `output.txt` и `output.csv`.

## Линтер

Этот проект использует [ruff](https://github.com/astral-sh/ruff) для проверки кода. Чтобы запустить проверку, выполните:

```
ruff check .
```

