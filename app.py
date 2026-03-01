import tkinter as tk
from tkinter import ttk


class ColorWindow:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("炫彩控制台")
        self.root.geometry("560x420")
        self.root.minsize(520, 380)
        self.root.attributes("-alpha", 0.95)
        self.root.configure(bg="#0F172A")

        self.theme_pairs = [
            ("#4F46E5", "#06B6D4"),
            ("#EC4899", "#8B5CF6"),
            ("#F97316", "#EAB308"),
            ("#10B981", "#14B8A6"),
            ("#3B82F6", "#22D3EE"),
        ]
        self.theme_index = 0

        self.content = tk.Canvas(self.root, highlightthickness=0, bd=0)
        self.content.pack(fill="both", expand=True, padx=20, pady=20)
        self.content.bind("<Configure>", self.redraw_background)

        self.panel = tk.Frame(self.content, bg="#111827", bd=0)
        self.panel_window = self.content.create_window(
            0, 0, window=self.panel, anchor="center", width=460, height=300
        )

        self.title_label = tk.Label(
            self.panel,
            text="✨ 霓虹窗口控制器",
            font=("Segoe UI", 22, "bold"),
            bg="#111827",
            fg="#E2E8F0",
        )
        self.title_label.pack(pady=(25, 6))

        self.label = tk.Label(
            self.panel,
            text="点击按钮切换主题配色",
            font=("Segoe UI", 12),
            bg="#111827",
            fg="#94A3B8",
        )
        self.label.pack(pady=(0, 18))

        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Neon.TButton",
            font=("Segoe UI", 14, "bold"),
            foreground="#F8FAFC",
            background="#6366F1",
            borderwidth=0,
            padding=(20, 12),
        )
        style.map(
            "Neon.TButton",
            background=[("active", "#818CF8"), ("pressed", "#4F46E5")],
        )

        self.button = ttk.Button(
            self.panel,
            text="切换主题",
            command=self.change_color,
            style="Neon.TButton",
        )
        self.button.pack(pady=6)

        self.alpha_scale = tk.Scale(
            self.panel,
            from_=0.4,
            to=1.0,
            resolution=0.05,
            orient="horizontal",
            label="窗口透明度",
            command=self.change_alpha,
            bg="#111827",
            fg="#E2E8F0",
            activebackground="#6366F1",
            troughcolor="#1E293B",
            highlightthickness=0,
            length=280,
            bd=0,
            font=("Segoe UI", 10),
        )
        self.alpha_scale.set(0.95)
        self.alpha_scale.pack(pady=(16, 22))

        self.redraw_background()

    def redraw_background(self, _event: tk.Event | None = None) -> None:
        width = self.content.winfo_width()
        height = self.content.winfo_height()

        if width <= 1 or height <= 1:
            return

        self.content.delete("bg")
        color1, color2 = self.theme_pairs[self.theme_index]
        r1, g1, b1 = self.hex_to_rgb(color1)
        r2, g2, b2 = self.hex_to_rgb(color2)

        for i in range(height):
            ratio = i / max(height - 1, 1)
            r = int(r1 + (r2 - r1) * ratio)
            g = int(g1 + (g2 - g1) * ratio)
            b = int(b1 + (b2 - b1) * ratio)
            self.content.create_line(0, i, width, i, fill=f"#{r:02x}{g:02x}{b:02x}", tags="bg")

        self.content.tag_lower("bg")
        self.content.coords(self.panel_window, width / 2, height / 2)

        glow_color = self.brighten(color1, 0.35)
        self.panel.configure(highlightbackground=glow_color, highlightthickness=2)

    def change_color(self) -> None:
        self.theme_index = (self.theme_index + 1) % len(self.theme_pairs)
        self.redraw_background()

    def change_alpha(self, value: str) -> None:
        self.root.attributes("-alpha", float(value))

    @staticmethod
    def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
        hex_color = hex_color.lstrip("#")
        return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))

    @staticmethod
    def brighten(hex_color: str, factor: float) -> str:
        r, g, b = ColorWindow.hex_to_rgb(hex_color)
        r = min(255, int(r + (255 - r) * factor))
        g = min(255, int(g + (255 - g) * factor))
        b = min(255, int(b + (255 - b) * factor))
        return f"#{r:02x}{g:02x}{b:02x}"


def main() -> None:
    root = tk.Tk()
    ColorWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
