# shortcut_server.py
from flask import Flask, jsonify
from pynput import keyboard
import threading
import pyperclip
import requests
import json


app = Flask(__name__)
copied_text = []
pressed_keys = set()

def on_press(key):
    pressed_keys.add(key)

def on_release(key):
    print("현재 저장된 keyboard 입력:", pressed_keys)
    if (keyboard.Key.alt_l in pressed_keys and keyboard.KeyCode.from_char('f') in pressed_keys):
        print("단축키 감자")

    elif (keyboard.Key.alt_l in pressed_keys and keyboard.KeyCode.from_char('s') in pressed_keys):
        print("단축키 감지")
    text = pyperclip.paste()
    print("현재 클립보드 내용:", text)
    pressed_keys.clear()  # 모든 키 해제
    # print("현재 저장된 keyboard 입력 초기화됨.")















@app.route('/')
def home():
    return '서버는 정상적으로 작동 중입니다.'

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
