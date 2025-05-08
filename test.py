from pynput import keyboard
import pyperclip

pressed_keys = set()

def on_press(key):
    pressed_keys.add(key)
    print(f"Pressed: {key}")
    if (key == keyboard.KeyCode.from_char('a')):
        print("✅ 단축키 a 감지됨!")
        text = pyperclip.paste()
        print(text)
    if(key==keyboard.Key.esc):
        print("❌ Esc 키 눌림. 프로그램 종료.")
        return False

def on_release(key):
    if key in pressed_keys:
        pressed_keys.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("🔍 키보드 감지 시작. a 눌러봐!")
    listener.join()
