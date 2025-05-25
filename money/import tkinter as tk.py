import tkinter as tk
import math
python canvas_quadrant.py

class QuadrantCanvas:
    def __init__(self, root):
        self.root = root
        self.root.title("Roue du Quadrant dans le 8")
        
        # Canvas dimensions
        self.canvas_width = 800
        self.canvas_height = 600
        self.center_x = self.canvas_width // 2
        self.center_y = self.canvas_height // 2

        # Default parameters
        self.radius = 100
        self.center_distance = 200

        # Create canvas
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        # Control panel
        self.create_controls()

        # Initial draw
        self.draw()

    def create_controls(self):
        controls_frame = tk.Frame(self.root)
        controls_frame.pack()

        # Radius control
        tk.Label(controls_frame, text="Radius:").grid(row=0, column=0)
        self.radius_var = tk.Scale(controls_frame, from_=50, to=200, orient=tk.HORIZONTAL, command=self.update)
        self.radius_var.set(self.radius)
        self.radius_var.grid(row=0, column=1)

        # Center distance control
        tk.Label(controls_frame, text="Center Distance:").grid(row=1, column=0)
        self.distance_var = tk.Scale(controls_frame, from_=100, to=400, orient=tk.HORIZONTAL, command=self.update)
        self.distance_var.set(self.center_distance)
        self.distance_var.grid(row=1, column=1)

        # Toggle axes
        self.show_axes_var = tk.BooleanVar(value=True)
        tk.Checkbutton(controls_frame, text="Show Axes", variable=self.show_axes_var, command=self.draw).grid(row=2, column=0, columnspan=2)

    def draw(self):
        self.canvas.delete("all")  # Clear canvas

        # Get parameters
        radius = self.radius_var.get()
        center_distance = self.distance_var.get()

        # Compute circle centers
        left_center = (self.center_x - center_distance // 2, self.center_y)
        right_center = (self.center_x + center_distance // 2, self.center_y)

        # Draw circles
        self.draw_circle(left_center, radius, "blue", "Circle 1")
        self.draw_circle(right_center, radius, "green", "Circle 2")

        # Draw tangency points
        self.draw_tangent_points(left_center, right_center)

        # Draw axes
        if self.show_axes_var.get():
            self.draw_axes()

    def draw_circle(self, center, radius, color, label):
        x, y = center
        self.canvas.create_oval(
            x - radius, y - radius, x + radius, y + radius,
            outline=color, width=2
        )
        self.canvas.create_text(x, y - radius - 10, text=label, fill=color)

        # Draw quadrants
        self.canvas.create_line(x, y - radius, x, y + radius, fill=color, dash=(4, 2))
        self.canvas.create_line(x - radius, y, x + radius, y, fill=color, dash=(4, 2))

    def draw_tangent_points(self, left_center, right_center):
        lx, ly = left_center
        rx, ry = right_center

        # Tangent points are horizontally aligned
        tangent_y = self.center_y
        self.canvas.create_oval(
            lx - 5, tangent_y - 5, lx + 5, tangent_y + 5,
            fill="red", outline="red"
        )
        self.canvas.create_oval(
            rx - 5, tangent_y - 5, rx + 5, tangent_y + 5,
            fill="red", outline="red"
        )

        self.canvas.create_text(lx, tangent_y + 10, text="T1", fill="red")
        self.canvas.create_text(rx, tangent_y + 10, text="T2", fill="red")

    def draw_axes(self):
        # Draw symmetry axes
        self.canvas.create_line(
            0, self.center_y, self.canvas_width, self.center_y,
            fill="black", dash=(4, 2), width=1
        )
        self.canvas.create_line(
            self.center_x, 0, self.center_x, self.canvas_height,
            fill="black", dash=(4, 2), width=1
        )

    def update(self, event=None):
        self.draw()

# Create the Tkinter app
root = tk.Tk()
app = QuadrantCanvas(root)
root.mainloop()

