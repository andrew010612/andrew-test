# vulnerable_app.py
import sqlite3
import os

# ❌ 漏洞 1：硬編碼敏感憑證 (Hardcoded Credentials)
# 資安工具或大語言模型應該要能偵測到這組寫死的 API Key
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE-SUPER-SECRET-KEY"
DB_PASSWORD = "AdminPassword123!"

def get_user_data(user_id):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    
    # ❌ 漏洞 2：SQL 注入漏洞 (SQL Injection)
    # 直接使用字串拼接使用者輸入，攻擊者可以傳入 "' OR '1'='1" 來撈出所有資料
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    print(f"Executing query: {query}")
    
    cursor.execute(query)
    return cursor.fetchall()

def ping_host(host_address):
    # ❌ 漏洞 3：命令注入漏洞 (Command Injection)
    # 直接把使用者輸入帶入系統 Shell 執行。
    # 攻擊者可以傳入 "8.8.8.8; rm -rf /" 或 "8.8.8.8 && cat /etc/passwd"
    print(f"Pinging host: {host_address}")
    os.system(f"ping -c 1 {host_address}")

if __name__ == "__main__":
    # 模擬不可信的使用者輸入
    fake_user_input = "1' OR '1'='1"
    fake_host_input = "8.8.8.8; cat /etc/passwd"
    
    get_user_data(fake_user_input)
    ping_host(fake_host_input)