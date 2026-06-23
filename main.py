# main.py
import datetime

def main():
    print("====================================")
    print("Hello, GitHub Actions!")
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"目前執行時間 (UTC): {current_time}")
    print("====================================")

if __name__ == "__main__":
    main()