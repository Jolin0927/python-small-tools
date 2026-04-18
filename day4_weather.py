import requests
def get_weather(city):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        res = requests.get(url,timeout=10)
        res.raise_for_status()
        data = res.json()
        current = data["current_condition"][0]
        print(f"\n[{city}]")
        print(f"天气:{current['weatherDesc'][0]['value']}")
        print(f"温度:{current['temp_C']}℃")
        print(f"湿度:{current['humidity']}%")
    except requests.exceptions.RequestException:
        print("查询失败，请检查网络或城市名")
def main():
    print("===Day4 天气查询工具 ===")
    while True:
        city = input("\n输入城市名（q退出）：").strip()
        if city.lower() == "q":
            print("再见")
            break
        if city:
            get_weather(city)
if __name__ == "__main__":
    main()