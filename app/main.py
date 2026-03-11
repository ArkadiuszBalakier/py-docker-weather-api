from dotenv import load_dotenv
import os
import requests


def get_weather() -> None:
    load_dotenv()

    API_KEY = os.getenv("API_KEY")
    URL = os.getenv("URL")
    FILTERING = os.getenv("FILTERING")

    if not all([API_KEY, URL, FILTERING]):
        print("Missing environment variables. Check -e flags.")
        return

    response = requests.get(f"{URL}/current.json?key={API_KEY}&q={FILTERING}")
    print(response.json())


if __name__ == "__main__":
    get_weather()
