from pynput import keyboard
import pyperclip

pressed_keys = set()

def on_press(key):
    pressed_keys.add(key)
    print(f"Pressed: {key}")

    # Alt + s 감지
    if keyboard.Key.alt_l in pressed_keys and keyboard.KeyCode.from_char('s') in pressed_keys:
        print("✅ Alt + S 단축키 감지됨!")
        print("현재 저장된 keyboard 입력:", pressed_keys)
    elif keyboard.Key.alt_l in pressed_keys and keyboard.KeyCode.from_char('f') in pressed_keys:
        print("✅ Alt + F 단축키 감지됨!")
        print("현재 저장된 keyboard 입력:", pressed_keys)
    # Esc 키로 종료
    if key == keyboard.Key.esc:
        print("❌ Esc 키 눌림. 프로그램 종료.")
        return False

def on_release(key):
    print(f"Released: {key}")
    pressed_keys.clear()  # 모든 키 해제
    print("현재 저장된 keyboard 입력 초기화됨.")
    print("현재 저장된 keyboard 입력:", pressed_keys)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("🔍 키보드 감지 시작. Alt + S를 눌러봐!")
    listener.join()
