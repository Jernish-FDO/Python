import time
import sys

def pomodoro(minutes):
    seconds = minutes * 60
    print(f"⏳ Timer started for {minutes} minutes. Get to work, buddy!")
    
    try:
        while seconds > 0:
            mins, secs = divmod(seconds, 60)
            timer = f"{mins:02d}:{secs:02d}"
            print(f"\rTime left: {timer}", end="")
            time.sleep(1)
            seconds -= 1
        
        print("\n\n🔔 Time's up! Take a 5-minute break. You earned it! 🤜🤛")
    except KeyboardInterrupt:
        print("\n👋 Timer stopped. Catch you later!")

if __name__ == "__main__":
    work_time = 25
    pomodoro(work_time)
