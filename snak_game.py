import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import os
import winsound  # sound effect (Windows only)

# Constants for snake game
WIDTH = 700
HEIGHT = 600
SIZE = 20
INITIAL_SNAKE_LENGTH = 3
LEVEL_THRESHOLDS = [5, 10, 20]

USERS_FILE = "users.txt"

# Load users from file
def load_users():
    users = {}
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    phone, name, password = line.split(",")
                    users[phone] = {"name": name, "password": password}
    return users

# Save users to file
def save_users(users):
    with open(USERS_FILE, "w") as f:
        for phone, data in users.items():
            f.write(f"{phone},{data['name']},{data['password']}\n")

users_db = load_users()

class LoginRegisterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login / Register")
        self.root.geometry("350x480")
        self.root.configure(bg="#222222")

        self.current_frame = None
        self.show_login_ui()

    def clear_frame(self):
        if self.current_frame:
            self.current_frame.destroy()

    def toggle_password(self, entry, toggle_btn):
        if entry.cget('show') == '':
            entry.config(show='*')
            toggle_btn.config(text='👁️')
        else:
            entry.config(show='')
            toggle_btn.config(text='🙈')

    def show_login_ui(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg="#222222")
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        # Shadab Logo (Top)
        tk.Label(self.current_frame, text=" Bite & grow  🐍", font=("Helvetica", 20, "bold"),
                 fg="#00FFAA", bg="#222222").pack(pady=5)

        tk.Label(self.current_frame, text="Login", font=("Helvetica", 18, "bold"),
                 fg="white", bg="#222222").pack(pady=10)

        tk.Label(self.current_frame, text="Phone Number:", fg="white", bg="#222222").pack(anchor='w')
        self.login_phone_entry = tk.Entry(self.current_frame, font=("Helvetica", 14))
        self.login_phone_entry.pack(fill=tk.X, pady=5)

        tk.Label(self.current_frame, text="Password:", fg="white", bg="#222222").pack(anchor='w')
        pwd_frame = tk.Frame(self.current_frame)
        pwd_frame.pack(fill=tk.X, pady=5)
        self.login_password_entry = tk.Entry(pwd_frame, font=("Helvetica", 14), show="*")
        self.login_password_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.login_toggle_btn = tk.Button(pwd_frame, text="👁️", width=3,
                                          command=lambda: self.toggle_password(self.login_password_entry, self.login_toggle_btn))
        self.login_toggle_btn.pack(side=tk.LEFT, padx=5)

        login_btn = tk.Button(self.current_frame, text="Login", font=("Helvetica", 14, "bold"),
                              bg="#4CAF50", fg="white", command=self.login)
        login_btn.pack(fill=tk.X, pady=10)

        forgot_btn = tk.Button(self.current_frame, text="Forgot Password?", font=("Helvetica", 10),
                               bg="#222222", fg="#FF6666", bd=0, command=self.forgot_password)
        forgot_btn.pack()

        switch_reg_btn = tk.Button(self.current_frame, text="No account? Register here",
                                   font=("Helvetica", 10), bg="#222222", fg="#66ccff", bd=0,
                                   command=self.show_register_ui)
        switch_reg_btn.pack(pady=5)

        # Footer Logo
        tk.Label(self.current_frame, text="© Shadab 🐍", font=("Helvetica", 10, "italic"),
                 fg="#AAAAAA", bg="#222222").pack(side=tk.BOTTOM, pady=10)

    def show_register_ui(self):
        self.clear_frame()
        self.current_frame = tk.Frame(self.root, bg="#222222")
        self.current_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tk.Label(self.current_frame, text="★ Shadab ★ 🐍", font=("Helvetica", 20, "bold"),
                 fg="#00FFAA", bg="#222222").pack(pady=5)

        tk.Label(self.current_frame, text="Register", font=("Helvetica", 18, "bold"),
                 fg="white", bg="#222222").pack(pady=10)

        tk.Label(self.current_frame, text="Name:", fg="white", bg="#222222").pack(anchor='w')
        self.name_entry = tk.Entry(self.current_frame, font=("Helvetica", 14))
        self.name_entry.pack(fill=tk.X, pady=5)

        tk.Label(self.current_frame, text="Phone Number:", fg="white", bg="#222222").pack(anchor='w')
        self.phone_entry = tk.Entry(self.current_frame, font=("Helvetica", 14))
        self.phone_entry.pack(fill=tk.X, pady=5)

        tk.Label(self.current_frame, text="Password:", fg="white", bg="#222222").pack(anchor='w')
        pwd_frame1 = tk.Frame(self.current_frame)
        pwd_frame1.pack(fill=tk.X, pady=5)
        self.password_entry = tk.Entry(pwd_frame1, font=("Helvetica", 14), show="*")
        self.password_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.pwd_toggle_btn = tk.Button(pwd_frame1, text="👁️", width=3,
                                        command=lambda: self.toggle_password(self.password_entry, self.pwd_toggle_btn))
        self.pwd_toggle_btn.pack(side=tk.LEFT, padx=5)

        tk.Label(self.current_frame, text="Re-enter Password:", fg="white", bg="#222222").pack(anchor='w')
        pwd_frame2 = tk.Frame(self.current_frame)
        pwd_frame2.pack(fill=tk.X, pady=5)
        self.re_password_entry = tk.Entry(pwd_frame2, font=("Helvetica", 14), show="*")
        self.re_password_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
        self.repwd_toggle_btn = tk.Button(pwd_frame2, text="👁️", width=3,
                                          command=lambda: self.toggle_password(self.re_password_entry, self.repwd_toggle_btn))
        self.repwd_toggle_btn.pack(side=tk.LEFT, padx=5)

        register_btn = tk.Button(self.current_frame, text="Register", font=("Helvetica", 14, "bold"),
                                 bg="#2196F3", fg="white", command=self.register)
        register_btn.pack(fill=tk.X, pady=15)

        switch_login_btn = tk.Button(self.current_frame, text="Already have account? Login here",
                                     font=("Helvetica", 10), bg="#222222", fg="#66ccff", bd=0,
                                     command=self.show_login_ui)
        switch_login_btn.pack()

    def forgot_password(self):
        phone = simpledialog.askstring("Forgot Password", "Enter your Phone Number:")
        if not phone:
            return
        user = users_db.get(phone)
        if not user:
            messagebox.showerror("Error", "User not found!")
            return
        new_pass = simpledialog.askstring("Reset Password", "Enter your New Password:", show="*")
        if new_pass:
            users_db[phone]["password"] = new_pass
            save_users(users_db)
            messagebox.showinfo("Success", "Password updated successfully!")

    def login(self):
        phone = self.login_phone_entry.get().strip()
        password = self.login_password_entry.get().strip()

        if not phone or not password:
            messagebox.showerror("Error", "Phone number and password cannot be empty")
            return

        user = users_db.get(phone)
        if not user:
            messagebox.showerror("Error", "User not found. Please register first.")
            return
        if user["password"] != password:
            messagebox.showerror("Error", "Incorrect password.")
            return

        messagebox.showinfo("Success", f"Welcome back, {user['name']}!")
        self.root.withdraw()
        self.open_snake_game()

    def register(self):
        name = self.name_entry.get().strip()
        phone = self.phone_entry.get().strip()
        password = self.password_entry.get().strip()
        re_password = self.re_password_entry.get().strip()

        if not name or not phone or not password or not re_password:
            messagebox.showerror("Error", "All fields are required!")
            return

        if password != re_password:
            messagebox.showerror("Error", "Passwords do not match!")
            return

        if phone in users_db:
            messagebox.showerror("Error", "Phone number already registered")
            return

        # OTP verification
        otp = str(random.randint(1000, 9999))
        entered_otp = simpledialog.askstring("OTP Verification", f"Enter the OTP sent to your phone:\n(OTP: {otp})")
        if entered_otp != otp:
            messagebox.showerror("Error", "Invalid OTP! Registration failed.")
            return

        users_db[phone] = {"name": name, "password": password}
        save_users(users_db)
        messagebox.showinfo("Registration Success", f"User '{name}' registered successfully! You can now login.")
        self.show_login_ui()

    def open_snake_game(self):
        snake_root = tk.Toplevel()
        snake_root.title("🐍 Snake Game")
        snake_app = SnakeGame(snake_root, self)
        snake_root.protocol("WM_DELETE_WINDOW", self.root.destroy)

    def logout(self, game_window):
        game_window.destroy()
        self.root.deiconify()


class SnakeGame:
    def __init__(self, root, login_app):
        self.root = root
        self.login_app = login_app
        self.root.configure(bg="#101820")

        self.speed = 150

        self.score_label = tk.Label(root, text="Score: 0", font=("Helvetica", 16, "bold"),
                                    fg="white", bg="#101820")
        self.score_label.pack(pady=(10, 0))

        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="#1e1e2f",
                                highlightthickness=5, highlightbackground="#00FFAA")
        self.canvas.pack(pady=(5, 10))

        button_frame = tk.Frame(root, bg="#2c2c2c")
        button_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        button_style = {"font": ("Helvetica", 14, "bold"), "fg": "white", "bd": 0, "padx": 10, "pady": 5}

        self.start_button = tk.Button(button_frame, text="▶ Start", command=self.start_game,
                                      bg="#4CAF50", activebackground="#388E3C", **button_style)
        self.start_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        self.pause_button = tk.Button(button_frame, text="⏸️ Pause", command=self.toggle_pause,
                                      bg="#FFC107", activebackground="#FFA000", **button_style)
        self.pause_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        self.reset_button = tk.Button(button_frame, text="🔄 Reset", command=self.reset,
                                      bg="#2196F3", activebackground="#1976D2", **button_style)
        self.reset_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        self.logout_button = tk.Button(button_frame, text="🔓 Logout", command=lambda: self.login_app.logout(self.root),
                                       bg="#9C27B0", activebackground="#7B1FA2", **button_style)
        self.logout_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        self.exit_button = tk.Button(button_frame, text="❌ Exit", command=root.quit,
                                     bg="#F44336", activebackground="#D32F2F", **button_style)
        self.exit_button.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=5)

        # Footer
        tk.Label(root, text="© Shadab 🐍 Snake Game", font=("Helvetica", 10, "italic"),
                 fg="#AAAAAA", bg="#101820").pack(side=tk.BOTTOM, pady=5)

        self.snake = []
        self.food = None
        self.direction = 'Right'
        self.next_direction = 'Right'
        self.running = False
        self.paused = False
        self.score = 0

        self.root.bind("<Key>", self.change_direction)
        self.reset()

    def reset(self):
        self.canvas.delete("all")
        self.snake = []
        self.direction = 'Right'
        self.next_direction = 'Right'
        self.running = False
        self.paused = False
        self.score = 0
        self.speed = 150
        self.score_label.config(text="Score: 0")
        self.canvas.delete("gameover")

        for i in range(INITIAL_SNAKE_LENGTH):
            x = 100 - i * SIZE
            y = 100
            rect = self.create_snake_segment(x, y, i)
            self.snake.append(rect)

        self.spawn_food()

    def create_snake_segment(self, x, y, index):
        shade = 200 - (index * 10)
        color = f'#00{shade:02x}00' if shade >= 0 else '#006600'
        return self.canvas.create_rectangle(x, y, x+SIZE, y+SIZE, fill=color, outline="#650C1B")

    def start_game(self):
        if not self.running:
            self.running = True
            self.paused = False
            self.move()

    def toggle_pause(self):
        if self.running:
            self.paused = not self.paused
            self.pause_button.config(text="▶ Resume" if self.paused else "⏸️ Pause")
            if not self.paused:
                self.move()

    def spawn_food(self):
        while True:
            x = random.randint(0, (WIDTH - SIZE) // SIZE) * SIZE
            y = random.randint(0, (HEIGHT - SIZE) // SIZE) * SIZE
            overlap = any(self.canvas.coords(part) == [x, y, x+SIZE, y+SIZE] for part in self.snake)
            if not overlap:
                break
        self.food = self.canvas.create_oval(x, y, x+SIZE, y+SIZE, fill="red")

    def change_direction(self, event):
        key = event.keysym
        opposites = {'Up': 'Down', 'Down': 'Up', 'Left': 'Right', 'Right': 'Left'}
        if key in opposites and opposites[key] != self.direction:
            self.next_direction = key

    def move(self):
        if not self.running or self.paused:
            return

        self.direction = self.next_direction
        head_coords = self.canvas.coords(self.snake[0])
        x1, y1, x2, y2 = head_coords

        if self.direction == "Up":
            y1 -= SIZE; y2 -= SIZE
        elif self.direction == "Down":
            y1 += SIZE; y2 += SIZE
        elif self.direction == "Left":
            x1 -= SIZE; x2 -= SIZE
        elif self.direction == "Right":
            x1 += SIZE; x2 += SIZE

        if x1 < 0 or y1 < 0 or x2 > WIDTH or y2 > HEIGHT:
            self.game_over(); return

        for part in self.snake[1:]:
            if self.canvas.coords(part) == [x1, y1, x2, y2]:
                self.game_over(); return

        new_head = self.create_snake_segment(x1, y1, 0)
        self.snake = [new_head] + self.snake

        if self.canvas.coords(new_head) == self.canvas.coords(self.food):
            self.canvas.delete(self.food)
            self.spawn_food()
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.adjust_speed()
            winsound.Beep(1000, 150)  # 👈 Eating sound effect
        else:
            self.canvas.delete(self.snake[-1])
            self.snake.pop()

        self.root.after(self.speed, self.move)

    def adjust_speed(self):
        if self.score >= LEVEL_THRESHOLDS[2]:
            self.speed = 60
        elif self.score >= LEVEL_THRESHOLDS[1]:
            self.speed = 80
        elif self.score >= LEVEL_THRESHOLDS[0]:
            self.speed = 100

    def game_over(self):
        self.running = False
        winsound.Beep(400, 400)  # game over sound
        self.canvas.create_text(WIDTH/2, HEIGHT/2,
                                text=f"Game Over!\nScore: {self.score}",
                                fill="white", font=("Arial", 24), tags="gameover")


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginRegisterApp(root)
    root.mainloop()
