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
    if (keyboard.Key.alt_l in pressed_keys and keyboard.KeyCode.from_char('f') in pressed_keys):
        print("단축키 감지")
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


    elif (keyboard.Key.alt_l in pressed_keys and keyboard.KeyCode.from_char('s') in pressed_keys):
        print("단축키 감지")
        detected_shortcuts.clear()
        text = pyperclip.paste()
        detected_shortcuts.append(text)
        # URL 저장 API 호출
        try:
            response = requests.post('http://localhost:5001/url/', json={'url': text})
            if response.status_code == 200:
                print(f"URL 저장 성공: {text}")
            else:
                print(f"URL 저장 실패: {response.text}")
        except Exception as e:
            print(f"URL 저장 중 오류 발생: {str(e)}")


def on_release(key):
    pressed_keys.clear()  # 모든 키 해제
    print("현재 저장된 keyboard 입력 초기화됨.")
    print("현재 저장된 keyboard 입력:", pressed_keys)



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
