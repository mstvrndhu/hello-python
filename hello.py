import sys
from datetime import datetime

# Ensure UTF-8 encoding (and handle UTF-8 BOM if present on Windows)
if sys.platform == "win32":
    try:
        sys.stdin.reconfigure(encoding="utf-8-sig")
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Ask language before printing anything
lang = input("Choose language / 選擇語言 (en / zh-tw): ").strip().lower().replace("\ufeff", "")

hour = datetime.now().hour
today_str = datetime.now().strftime("%Y/%m/%d")

if lang in ["zh-tw", "zh", "tw"]:
    print("你好！我是 GitHub 使用者 mstvrndhu。")
    name = input("請輸入您的姓名：")
    if hour < 12:
        greeting = f"早安，{name}！"
    elif hour < 18:
        greeting = f"午安，{name}！"
    else:
        greeting = f"晚安，{name}！"
    print(greeting)
    print(f"今天是 {today_str}")
else:
    print("Hello! I am GitHub user mstvrndhu.")
    name = input("Enter your name: ")
    if hour < 12:
        greeting = f"Good morning, {name}!"
    elif hour < 18:
        greeting = f"Good afternoon, {name}!"
    else:
        greeting = f"Good evening, {name}!"
    print(greeting)
    print(f"Today is {today_str}")
