import tkinter as tk


class ColorWindow:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("颜色切换窗口")
        self.root.geometry("420x260")
        self.root.attributes("-alpha", 0.9)

        self.colors = ["#F6BD60", "#84A59D", "#F28482", "#6D597A", "#90BE6D"]
        self.color_index = 0

        self.content = tk.Frame(root, bg=self.colors[self.color_index])
        self.content.pack(fill="both", expand=True)

        self.label = tk.Label(
            self.content,
            text="点击按钮切换窗口颜色",
            font=("Arial", 16),
            bg=self.colors[self.color_index],
            fg="white",
        )
        self.label.pack(pady=50)

        self.button = tk.Button(
            self.content,
            text="切换颜色",
            font=("Arial", 24),
            command=self.change_color,
            padx=44,
            pady=24,
        )
        self.button.pack()

        self.alpha_scale = tk.Scale(
            self.content,
            from_=0.3,
            to=1.0,
            resolution=0.1,
            orient="horizontal",
            label="窗口透明度",
            command=self.change_alpha,
            bg=self.colors[self.color_index],
            fg="white",
            highlightthickness=0,
            length=220,
        )
        self.alpha_scale.set(0.9)
        self.alpha_scale.pack(pady=20)

    def change_color(self) -> None:
        self.color_index = (self.color_index + 1) % len(self.colors)
        next_color = self.colors[self.color_index]
        self.content.configure(bg=next_color)
        self.label.configure(bg=next_color)
        self.alpha_scale.configure(bg=next_color)

    def change_alpha(self, value: str) -> None:
        self.root.attributes("-alpha", float(value))


def main() -> None:
    root = tk.Tk()
    ColorWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
