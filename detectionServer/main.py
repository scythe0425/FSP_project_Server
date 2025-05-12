# shortcut_server.py
from flask import Flask, jsonify
from pynput import keyboard
import threading
import pyperclip
import requests
import json


app = Flask(__name__)
detected_shortcuts = []

pressed_keys = set()

def on_press(key):
    pressed_keys.add(key)
    if (key == keyboard.KeyCode.from_char('f')):
        detected_shortcuts.clear()
        text = pyperclip.paste()
        detected_shortcuts.append(text)
        
        # 검색 API 호출
        try:
            response = requests.post('http://localhost:5001/search/', json={'keyword': text})
            if response.status_code == 200:
                result = response.json()
                # JSON 형식으로 결과 출력
                print(f"\n === {text}에 대한 검색 결과 ===")
                print(json.dumps(result, indent=2, ensure_ascii=False))
            else:
                print(f"검색 API 오류: {response.text}")
        except Exception as e:
            print(f"검색 API 호출 중 오류 발생: {str(e)}")

    elif (key == keyboard.KeyCode.from_char('o')):
        detected_shortcuts.clear()
        text = pyperclip.paste()
        detected_shortcuts.append(text)
        # 브라우저 열기 API 호출
        try:
            response = requests.post('http://localhost:5001/chrome/open', json={'url': text})
            if response.status_code == 200:
                print(f"브라우저 열기 성공: {text}")
            else:
                print(f"브라우저 열기 실패: {response.text}")
        except Exception as e:
            print(f"브라우저 열기 중 오류 발생: {str(e)}")  

    elif (key == keyboard.KeyCode.from_char('s')):
        detected_shortcuts.clear()
        text = pyperclip.paste()
        detected_shortcuts.append(text)
        # URL 저장 API 호출
        try:
            response = requests.post('http://localhost:5001/db/', json={'url': text})
            if response.status_code == 200:
                print(f"URL 저장 성공: {text}")
            else:
                print(f"URL 저장 실패: {response.text}")
        except Exception as e:
            print(f"URL 저장 중 오류 발생: {str(e)}")


def on_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)


@app.route('/')
def home():
    return '서버는 정상적으로 작동 중입니다.'


@app.route("/shortcuts", methods=["GET"])
def get_shortcuts():
    return jsonify(detected_shortcuts)

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
