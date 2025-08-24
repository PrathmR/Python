from flask import Flask, render_template, request
import threading
import time
from plyer import notification

app = Flask(__name__)

def start_notifications():
    while True:
        notification.notify(
            title="**Please Drink Water Now!!",
            message="The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            timeout=12
        )
        time.sleep(5)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_notifications', methods=['POST'])
def start_notifications_route():
    thread = threading.Thread(target=start_notifications)
    thread.start()
    return "Notification process started!"

if __name__ == '__main__':
    app.run(debug=True)
