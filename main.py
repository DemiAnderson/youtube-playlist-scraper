import csv
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def process_playlist(playlist_url):
    # Инициализация веб-драйвера
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(playlist_url)

    # Прокрутка страницы 5 раз для загрузки всех видео
    for _ in range(5):
        driver.execute_script("window.scrollBy(0, 1000)")

    wait = WebDriverWait(driver, 10)
    videos = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ytd-playlist-video-renderer")))

    # Собираем данные
    video_data = []
    for video in videos:
        title = video.find_element(By.CSS_SELECTOR, "#video-title").text
        duration = video.find_element(By.CSS_SELECTOR, "ytd-thumbnail-overlay-time-status-renderer div.thumbnail-overlay-badge-shape div.badge-shape-wiz__text").text
        
        views_xpath = './/yt-formatted-string[@class="style-scope ytd-video-meta-block"]'
        views = WebDriverWait(video, 20).until(EC.presence_of_element_located((By.XPATH, views_xpath))).text.split("•")[1]
        
        video_data.append((title, duration, views))

    driver.quit()
    return video_data

def save_data(video_data):
    # Сохраняем данные в txt файл
    with open('output.txt', 'w', encoding='utf-8') as f:
        for title, duration, views in video_data:
            f.write(f"Название: {title}\nДлительность: {duration}\nПросмотры: {views}\n\n")
    print("Данные успешно сохранены в файл output.txt")

    # Сохраняем данные в csv файл
    with open('output.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Название', 'Длительность', 'Просмотры'])  # Заголовки столбцов
        writer.writerows(video_data)
    print("Данные успешно сохранены в файл output.csv")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Пожалуйста, укажите URL плейлиста в качестве аргумента.")
        print("Пример: python test.py https://www.youtube.com/playlist?list=...")
        sys.exit(1)

    playlist_url = sys.argv[1]
    video_data = process_playlist(playlist_url)
    save_data(video_data)
