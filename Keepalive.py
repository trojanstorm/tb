from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

# اگر این فایل جدا اجرا شود، مستقیم سرور بالا می‌آید
if __name__ == "__main__":
    run()
