import pyautogui
import time
import keyboard
import threading

# CONFIG
TARGET_CPS = 60
IS_RUNNING = False
click_x, click_y = None, None

def safe_click():
    """Ultra-fast click with position lock"""
    if click_x is not None and click_y is not None:
        pyautogui.click(click_x, click_y, duration=0)
    else:
        pyautogui.click(duration=0)

def autoclicker_loop():
    """Busy loop - NO SLEEP = MAXIMUM SPEED"""
    global IS_RUNNING
    clicks = 0
    start_time = time.time()
    
    while True:
        if IS_RUNNING:
            safe_click()
            clicks += 1
            
            # Print CPS every second
            elapsed = time.time() - start_time
            if elapsed >= 1.0:
                cps = clicks / elapsed
                print(f"\rCPS: {cps:.1f} | ]:Toggle | F1:Exit     ", end="")
                clicks = 0
                start_time = time.time()
        else:
            print("\rAutoclicker: STOPPED | ]:Start | F1:Exit     ", end="")
            time.sleep(0.1)

def set_click_position():
    """Set exact click position""" 
    global click_x, click_y
    click_x, click_y = pyautogui.position()
    print(f"\n✅ Click position locked: ({click_x}, {click_y})")
    print("💡 Move mouse there and press [ to start!")

def toggle():
    """Toggle autoclicker"""
    global IS_RUNNING
    IS_RUNNING = not IS_RUNNING
    status = "STARTED" if IS_RUNNING else "STOPPED"
    print(f"\n🚀 Autoclicker {status}!")

# SAFETY FIRST
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0  # Zero delay between clicks

print("🔥 ULTRA-FAST AUTOCLICKER (60+ CPS)")
print("=" * 40)
print("🎮 INSTRUCTIONS:")
print("1. Position mouse where you want to click")
print("2. Press [ to LOCK POSITION")
print("3. Press ] to START/STOP")
print("4. Press F1 to EXIT")
print("5. Drag to corner for EMERGENCY STOP")
print("-" * 40)

# Hotkeys
keyboard.add_hotkey('[', set_click_position)
keyboard.add_hotkey(']', toggle)
keyboard.add_hotkey('f1', lambda: exit(0))

# Start clicking thread
threading.Thread(target=autoclicker_loop, daemon=True).start()

try:
    while True:
        time.sleep(0.01)
except KeyboardInterrupt:
    print("\n👋 Goodbye!")