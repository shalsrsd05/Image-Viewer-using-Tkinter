
import tkinter as tk
from PIL import Image, ImageTk
import os
from tkinter import messagebox

root = tk.Tk()
root.title("Image Viewer")
root.geometry("600x500")

IMAGE_DIR = "images"

if not os.path.exists(IMAGE_DIR):
    messagebox.showerror("Error", "Images folder not found")
    root.destroy()

images = [img for img in os.listdir(IMAGE_DIR)
          if img.lower().endswith(("png", "jpg", "jpeg", "bmp"))]

if not images:
    messagebox.showerror("Error", "No supported images found")
    root.destroy()

index = 0

image_label = tk.Label(root)
image_label.pack(expand=True)

def show_image():
    global img
    img_path = os.path.join(IMAGE_DIR, images[index])
    img = Image.open(img_path)
    img = img.resize((450, 350))
    img = ImageTk.PhotoImage(img)
    image_label.config(image=img)

def next_image():
    global index
    if index < len(images) - 1:
        index += 1
        show_image()

def prev_image():
    global index
    if index > 0:
        index -= 1
        show_image()

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Previous", command=prev_image, width=10).grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Next", command=next_image, width=10).grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Exit", command=root.quit, width=10).grid(row=0, column=2, padx=10)

show_image()
root.mainloop()
