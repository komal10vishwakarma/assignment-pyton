import tkinter as tk
from itertools import cycle
from PIL import Image, ImageTk

def image_application():

    root = tk.Tk()
    root.title("IMAGE SLIDESHOW VIEWER")

    # List of image paths
    image_path = [
        r"C:\batch19\python project\game_pro\img\Nezuko _3.jfif",
        r"C:\batch19\python project\game_pro\img\L kira laughing.jfif",
        r"C:\batch19\python project\game_pro\img\Eren Mikasa.jfif",
        r"C:\batch19\python project\game_pro\img\download.jfif",
        r"C:\batch19\python project\game_pro\img\download (10).jfif",
        r"C:\batch19\python project\game_pro\img\download (9).jfif",
        r"C:\batch19\python project\game_pro\img\download (8).jfif",
        r"C:\batch19\python project\game_pro\img\download (7).jfif",
        r"C:\batch19\python project\game_pro\img\download (6).jfif",
        r"C:\batch19\python project\game_pro\img\download (5).jfif",
        r"C:\batch19\python project\game_pro\img\download (4).jfif",
        r"C:\batch19\python project\game_pro\img\download (3).jfif",
        r"C:\batch19\python project\game_pro\img\download (2).jfif",
        r"C:\batch19\python project\game_pro\img\download (1).jfif",
        r"C:\batch19\python project\game_pro\img\Death note.jfif",
        r"C:\batch19\python project\game_pro\img\anime character well paper.jfif"
    ]

    # Resize images
    image_size = (1000, 1000)

    images = [
        Image.open(path).resize(image_size)
        for path in image_path
    ]

    # Convert images for Tkinter
    photo_images = [
        ImageTk.PhotoImage(image)
        for image in images
    ]

    label = tk.Label(root)
    label.pack(pady=20)

    # Create slideshow cycle
    slideshow = cycle(photo_images)

    def start_slideshow():
        photo_image = next(slideshow)

        label.config(image=photo_image)

        label.after(3000, start_slideshow)

    # Play button
    play_button = tk.Button(
        root,
        text="Play Slideshow",
        command=start_slideshow
    )

    play_button.pack(pady=10)

    root.mainloop()




