import tkinter as tk


class ColorWindow:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("颜色切换窗口")
        self.root.geometry("420x260")

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
            font=("Arial", 14),
            command=self.change_color,
            padx=18,
            pady=10,
        )
        self.button.pack()

    def change_color(self) -> None:
        self.color_index = (self.color_index + 1) % len(self.colors)
        next_color = self.colors[self.color_index]
        self.content.configure(bg=next_color)
        self.label.configure(bg=next_color)


def main() -> None:
    root = tk.Tk()
    ColorWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
