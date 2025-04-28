import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime


def parse_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        headers = soup.find_all('h1')

        links = soup.find_all('a')

        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f'parsed_data_{timestamp}.csv'

        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Тип', 'Текст'])

            for header in headers:
                writer.writerow(['Заголовок', header.text.strip()])

            for link in links:
                writer.writerow(['Ссылка', f"{link.text.strip()} - {link.get('href', '')}"])

        print(f"Данные успешно сохранены в файл: {filename}")

    except requests.RequestException as e:
        print(f"Ошибка при запросе: {e}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


if __name__ == "__main__":
    url = "https://example.com" 
    parse_website(url)
