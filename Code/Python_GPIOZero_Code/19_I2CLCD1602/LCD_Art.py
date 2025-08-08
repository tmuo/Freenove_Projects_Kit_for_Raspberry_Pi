#!/usr/bin/env python3
########################################################################
# Filename    : LCD_Art.py
# Description : Create ASCII art and animations on LCD1602 display
# Author      : GitHub Copilot
# modification: 2025/08/08
########################################################################
import time
from LCD1602 import CharLCD1602

class LCDArt:
    def __init__(self):
        self.lcd = CharLCD1602()
        self.lcd.init_lcd()
        
    def clear_display(self):
        """Clear the LCD display"""
        self.lcd.clear()
        
    def display_frame(self, line1, line2, duration=1):
        """Display two lines on LCD for specified duration"""
        self.lcd.clear()
        self.lcd.write(0, 0, line1[:16])  # Limit to 16 characters
        self.lcd.write(0, 1, line2[:16])  # Limit to 16 characters
        time.sleep(duration)
    
    def scrolling_text(self, text, cycles=3):
        """Scroll long text across the display"""
        text = "  " + text + "  "  # Add padding
        for cycle in range(cycles):
            for i in range(len(text) - 15):
                self.display_frame(text[i:i+16], " " * 16, 0.3)
    
    def bouncing_ball(self, duration=10):
        """Animate a bouncing ball using 'o' character"""
        start_time = time.time()
        position = 0
        direction = 1
        row = 0
        
        while time.time() - start_time < duration:
            # Create the display lines
            line1 = " " * 16
            line2 = " " * 16
            
            if row == 0:
                line1 = " " * position + "o" + " " * (15 - position)
            else:
                line2 = " " * position + "o" + " " * (15 - position)
            
            self.display_frame(line1, line2, 0.2)
            
            # Update position
            position += direction
            if position >= 15:
                direction = -1
                row = 1 - row  # Switch rows
            elif position <= 0:
                direction = 1
                row = 1 - row  # Switch rows
    
    def heart_beat(self, beats=5):
        """Animate a heart beating"""
        small_heart = [
            "   <3 LOVE <3   ",
            "  RASPBERRY PI  "
        ]
        
        big_heart = [
            " <3> LOVE <3>  ",
            " >RASPBERRY PI< "
        ]
        
        for beat in range(beats):
            # Small heart
            self.display_frame(small_heart[0], small_heart[1], 0.3)
            # Big heart
            self.display_frame(big_heart[0], big_heart[1], 0.3)
    
    def snake_game(self, duration=8):
        """Simple snake-like animation"""
        snake = "===>"
        start_time = time.time()
        position = 0
        
        while time.time() - start_time < duration:
            line1 = " " * 16
            line2 = " " * 16
            
            # Place snake on alternating rows
            if (position // 13) % 2 == 0:
                start_pos = position % 13
                line1 = " " * start_pos + snake + " " * (16 - start_pos - len(snake))
            else:
                start_pos = 12 - (position % 13)
                line2 = " " * start_pos + snake + " " * (16 - start_pos - len(snake))
            
            self.display_frame(line1, line2, 0.3)
            position += 1
    
    def progress_bar(self, label="Loading", duration=5):
        """Animated progress bar"""
        steps = 14  # 14 characters for progress bar (16 - 2 for brackets)
        
        for i in range(steps + 1):
            progress = "=" * i + " " * (steps - i)
            line1 = f"{label}..."[:16]
            line2 = f"[{progress}]"[:16]
            self.display_frame(line1, line2, duration / steps)
    
    def digital_rain(self, duration=10):
        """Matrix-style digital rain effect"""
        import random
        
        characters = "01"
        start_time = time.time()
        
        while time.time() - start_time < duration:
            line1 = ""
            line2 = ""
            
            for i in range(16):
                line1 += random.choice(characters)
                line2 += random.choice(characters)
            
            self.display_frame(line1, line2, 0.2)
    
    def wave_animation(self, duration=8):
        """Create a wave-like pattern"""
        wave_chars = ["_", "~", "^", "~"]
        start_time = time.time()
        offset = 0
        
        while time.time() - start_time < duration:
            line1 = ""
            line2 = ""
            
            for i in range(16):
                char_index = (i + offset) % len(wave_chars)
                line1 += wave_chars[char_index]
                line2 += wave_chars[(char_index + 2) % len(wave_chars)]
            
            self.display_frame(line1, line2, 0.3)
            offset += 1
    
    def countdown_timer(self, seconds=10):
        """Display a countdown timer"""
        for i in range(seconds, -1, -1):
            minutes = i // 60
            secs = i % 60
            time_str = f"{minutes:02d}:{secs:02d}"
            
            line1 = f"  COUNTDOWN TIMER "
            line2 = f"     {time_str}     "
            
            self.display_frame(line1, line2, 1)
        
        # Final message
        self.display_frame("   TIME'S UP!   ", "  *** DONE ***  ", 2)
    
    def pong_game(self, duration=15):
        """Simple Pong-like animation"""
        ball_x = 8
        ball_y = 0
        dx = 1
        dy = 1
        paddle1_y = 0
        paddle2_y = 0
        start_time = time.time()
        
        while time.time() - start_time < duration:
            # Create display
            line1 = [" "] * 16
            line2 = [" "] * 16
            
            # Place paddles
            line1[0] = "|" if paddle1_y == 0 else " "
            line2[0] = "|" if paddle1_y == 1 else " "
            line1[15] = "|" if paddle2_y == 0 else " "
            line2[15] = "|" if paddle2_y == 1 else " "
            
            # Place ball
            if ball_y == 0:
                line1[ball_x] = "o"
            else:
                line2[ball_x] = "o"
            
            self.display_frame("".join(line1), "".join(line2), 0.3)
            
            # Update ball position
            ball_x += dx
            ball_y += dy
            
            # Bounce off top/bottom
            if ball_y < 0 or ball_y > 1:
                dy = -dy
                ball_y += dy
            
            # Bounce off paddles or sides
            if ball_x <= 1 or ball_x >= 14:
                dx = -dx
                # Move paddles randomly
                paddle1_y = 1 - paddle1_y if ball_x <= 1 else paddle1_y
                paddle2_y = 1 - paddle2_y if ball_x >= 14 else paddle2_y
    
    def run_art_show(self):
        """Run a complete art show with various animations"""
        try:
            print("Starting LCD Art Show...")
            
            # Welcome message
            self.display_frame("  LCD ART SHOW  ", "   STARTING...  ", 2)
            
            # 1. Scrolling text
            self.scrolling_text("Welcome to the amazing LCD1602 Art Gallery! Enjoy the show!", 2)
            
            # 2. Heart beat
            self.heart_beat(4)
            
            # 3. Bouncing ball
            self.display_frame("  BOUNCING BALL ", "                ", 1)
            self.bouncing_ball(6)
            
            # 4. Progress bar
            self.progress_bar("Art Loading", 3)
            
            # 5. Digital rain
            self.display_frame("  DIGITAL RAIN  ", "                ", 1)
            self.digital_rain(5)
            
            # 6. Wave animation
            self.display_frame("    WAVE DEMO   ", "                ", 1)
            self.wave_animation(6)
            
            # 7. Snake game
            self.display_frame("  SNAKE MOVING  ", "                ", 1)
            self.snake_game(6)
            
            # 8. Pong game
            self.display_frame("   PONG DEMO    ", "                ", 1)
            self.pong_game(8)
            
            # 9. Countdown
            self.display_frame("  COUNTDOWN TO  ", "   SHOW END!    ", 2)
            self.countdown_timer(5)
            
            # Final message
            self.display_frame(" THANKS FOR     ", " WATCHING! :)   ", 3)
            
        except Exception as e:
            print(f"Error during art show: {e}")
        finally:
            self.clear_display()

def main():
    """Main function to run the LCD Art demonstrations"""
    art = LCDArt()
    
    print("LCD Art Controller")
    print("==================")
    print("1. Run complete art show")
    print("2. Bouncing ball")
    print("3. Heart beat")
    print("4. Digital rain")
    print("5. Wave animation")
    print("6. Pong game")
    print("7. Progress bar")
    print("8. Countdown timer")
    print("9. Scrolling text")
    
    try:
        choice = input("\nEnter your choice (1-9) or press Enter for full show: ").strip()
        
        if choice == "" or choice == "1":
            art.run_art_show()
        elif choice == "2":
            art.bouncing_ball(15)
        elif choice == "3":
            art.heart_beat(8)
        elif choice == "4":
            art.digital_rain(15)
        elif choice == "5":
            art.wave_animation(15)
        elif choice == "6":
            art.pong_game(20)
        elif choice == "7":
            art.progress_bar("Processing", 8)
        elif choice == "8":
            art.countdown_timer(15)
        elif choice == "9":
            text = input("Enter text to scroll: ") or "Hello LCD World!"
            art.scrolling_text(text, 5)
        else:
            print("Invalid choice!")
            
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        art.clear_display()
        print("Program ended.")

if __name__ == '__main__':
    main()
