# shortcut_server.py
from flask import Flask, jsonify
from pynput import keyboard
import threading

app = Flask(__name__)
detected_shortcuts = []

pressed_keys = set()

def on_press(key):
    print(f"Pressed: {key}")  # 어떤 키를 눌렀는지 출력
    pressed_keys.add(key)
    if (key == keyboard.KeyCode.from_char('a')):
        print("단축키 a 감지됨")
        detected_shortcuts.append("a")

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
