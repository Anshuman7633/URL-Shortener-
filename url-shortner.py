import tkinter as tk
import pyshorteners


class URLShortener:
    def __init__(self, master):
        self.master = master
        master.title("URL Shortener")

        # Create the URL entry widget
        self.url_entry = tk.Entry(master, width=50)
        self.url_entry.grid(row=0, column=0, padx=10, pady=10)

        # Create the Shorten button
        self.shorten_button = tk.Button(master, text="Shorten", command=self.shorten_url)
        self.shorten_button.grid(row=0, column=1, padx=10, pady=10)

        # Create the output label
        self.output_label = tk.Label(master, text="", fg="blue", cursor="hand2")
        self.output_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Bind the label to the short URL
        self.output_label.bind("<Button-1>", lambda e: self.copy_to_clipboard())

    def shorten_url(self):
        # Get the long URL from the entry widget
        long_url = self.url_entry.get()

        # Shorten the URL using the Bitly API
        s = pyshorteners.Shortener(api_key='cff418e731a07f1b48c0014a0b14015d7cfcbb6c')
        short_url = s.bitly.short(long_url)

        # Update the output label with the short URL
        self.output_label.config(text=short_url)

    def copy_to_clipboard(self):
        # Copy the short URL to the clipboard
        self.master.clipboard_clear()
        self.master.clipboard_append(self.output_label.cget("text"))
        self.master.update()  # required to update clipboard contents

        # Update the label to show that the URL has been copied
        self.output_label.config(fg="green", text="Copied to clipboard!")


if __name__ == "__main__":
    root = tk.Tk()
    url_shortener = URLShortener(root)
    root.mainloop()