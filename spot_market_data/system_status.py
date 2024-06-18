import requests


def get_system_status():
    # URL of API
    url = "https://api.kraken.com/0/public/SystemStatus"
    # Requesting data from API
    resp = requests.get(url)
    # Checking for errors
    resp.raise_for_status()
    # Extracting data from response
    data = resp.json()
    # Extracting system status
    system_status = data["result"]["status"]
    return system_status


if __name__ == "__main__":
    print(get_system_status())
