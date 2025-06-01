# shortcut_server.py
from flask import Flask, jsonify
from pynput import keyboard
import threading
import pyperclip
import requests
import json


app = Flask(__name__)
detected_shortcuts = []
searching_results = []

pressed_keys = set()

def on_press(key):
    pressed_keys.add(key)
    if (key == keyboard.Key.alt_l):
        print("단축키 감지")
        detected_shortcuts.clear()
        text = pyperclip.paste()
        detected_shortcuts.append(text)
        
        # 검색 API 호출
        try:
            response = requests.post('http://localhost:5001/search/', json={'keyword': text})
            if response.status_code == 200:
                result = response.json()
                searching_results.append(result)
            else:
                print(f"검색 API 오류: {response.text}")
        except Exception as e:
            print(f"검색 API 호출 중 오류 발생: {str(e)}")

        # URL 저장 API 호출
    elif (key == keyboard.KeyCode.from_char('s')):
        detected_shortcuts.clear()
        text = pyperclip.paste()
        detected_shortcuts.append(text)

        try:
            response = requests.post('http://localhost:5001/url/', json={'url': text})
        except Exception as e:
            print(f"URL 저장 중 오류 발생: {str(e)}")


def on_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)


@app.route('/')
def home():
    return


@app.route('/results', methods=['GET'])
def results():
    data = list(searching_results)
    searching_results.clear()
    return jsonify(data)

def start_keyboard_listener():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

def start_flask():
    app.run(port=5000)

if __name__ == "__main__":
    t1 = threading.Thread(target=start_keyboard_listener)
    t1.daemon = True
    t1.start()

    start_flask()