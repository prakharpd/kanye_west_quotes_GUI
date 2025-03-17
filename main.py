from tkinter import *
import requests


def get_quote():
    url = "https://waifu.it/api/v4/quote"
    response = requests.get(url, headers={
        "Authorization": "MTE4ODE1MjY2MDA4NDQwODQ2MA--.MTcwMzM0ODU0OA--.da8bf2cc9c8f",
    })
    data = response.json()

    anime_name = data['anime']

    quote = data["quote"] +" ---> " + anime_name
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Anime Quotes...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 190, text="Anime Quote Goes HERE", width=250, font=("Arial", 12, "bold"),
                                fill="white")
canvas.grid(row=0, column=0)

anime_img = PhotoImage(file="try3.png")
anime_button = Button(image=anime_img, highlightthickness=0, command=get_quote)
anime_button.grid(row=1, column=0)

window.mainloop()
