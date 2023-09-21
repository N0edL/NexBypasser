import customtkinter as ctk
import requests,re,sys

def find_mega_links():
    website_url = entry.get()
    try:
        # Send a GET request to the provided URL
        response = requests.get(website_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract all URLs starting with "https://mega.nz" using regular expressions
            mega_links = re.findall(r'https://mega\.nz[^\s"\']+', response.text)
            
            if mega_links:
                # Display the found mega.nz links
                result_text.configure(text=mega_links, font=("Arial", 11), text_color="green")
                copy_button.pack(padx=20, pady=10, side=ctk.RIGHT)
            else:
                result_text.configure(text="No Mega.nz links found", font=("Arial", 13), text_color="red")
                copy_button.pack(padx=20, pady=100, side=ctk.RIGHT)
        else:
            result_text.configure(text=f"Failed to fetch URL: {website_url}", font=("Arial", 13), text_color="red")
            copy_button.pack(padx=20, pady=100, side=ctk.RIGHT)

    except requests.exceptions.RequestException as e:
        result_text.configure(text=f"Invalid URL: {website_url}", font=("Arial", 13), text_color="red")
        copy_button.pack(padx=20, pady=100, side=ctk.RIGHT)

def find_pastelink_links():
    website_url = entry.get()
    try:
        # Send a GET request to the provided URL
        response = requests.get(website_url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract all URLs starting with "https://pastelink.net" using regular expressions
            pastelink_links = re.findall(r'https://pastelink\.net[^\s"\']+', response.text)
            
            if pastelink_links :
                # Display the found pastelink.net links
                result_text.configure(text=pastelink_links , font=("Arial", 11), text_color="green")
                copy_button.pack(padx=20, pady=10, side=ctk.RIGHT)
            else:
                result_text.configure(text="No pastelink links found", font=("Arial", 13), text_color="red")
                copy_button.pack(padx=20, pady=100, side=ctk.RIGHT)
        else:
            result_text.configure(text=f"Failed to fetch URL: {website_url}", font=("Arial", 13), text_color="red")
            copy_button.pack(padx=20, pady=100, side=ctk.RIGHT)

    except requests.exceptions.RequestException as e:
        result_text.configure(text=f"Invalid URL: {website_url}", font=("Arial", 13), text_color="red")
        copy_button.pack(padx=20, pady=100, side=ctk.RIGHT)

def paste_clipboard():
    copied_text = window.clipboard_get()
    entry.delete(0, ctk.END)
    entry.insert(0, copied_text)

def copy_to_clipboard():
    copied_text = result_text.cget("text")
    window.clipboard_clear()
    window.clipboard_append(copied_text)
    entry.delete(0, ctk.END)

# window
window = ctk.CTk()
window.title("Nex Bypasser 1.2.1")
window.geometry("420x250")
window.resizable(False, False)
window.bind("<Return>", lambda x: find_button.invoke())
window.iconbitmap("icon.ico")

# appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# widgets
label = ctk.CTkLabel(window,
                    text="Nex Bypasser 1.2.1",
                    font=("Arial", 20),
                    fg_color="#6039fa",
                    text_color="white",
                    corner_radius=5,
                    width=142,
                    height=30
                    )

entry = ctk.CTkEntry(window,
                    font=("Arial", 14),
                    corner_radius=5,
                    width=250,
                    text_color="white",
                    )

past_button = ctk.CTkButton(window,
                            text="Paste",
                            font=("Arial", 16),
                            fg_color="#6642f5",
                            text_color="white",
                            corner_radius=5,
                            width=50,
                            height=30,
                            command=paste_clipboard
                            ).place(x=340, y=50)

find_button = ctk.CTkButton(window,
                            text="Find Mega.nz Link",
                            font=("Arial", 16),
                            fg_color="#6642f5",
                            text_color="white",
                            corner_radius=5,
                            width=250,
                            height=30,
                            command=find_mega_links
                            )

find_button2 = ctk.CTkButton(window,
                            text="Find Pastelink Link",
                            font=("Arial", 16),
                            fg_color="#4e30c2",
                            text_color="white",
                            corner_radius=5,
                            width=250,
                            height=30,
                            command=find_pastelink_links
                            )

copy_button = ctk.CTkButton(window,
                            text="Copy",
                            font=("Arial", 16),
                            fg_color="#6642f5",
                            text_color="white",
                            corner_radius=5,
                            width=50,
                            height=30,
                            command=copy_to_clipboard
                            )

result_text = ctk.CTkLabel(window,
                            font=("Arial", 15),
                            height=200,
                            width=2000,
                            text_color="white",
                            text=""
                            )

# pack widgets
label.pack(padx=20, pady=10, side=ctk.TOP)
entry.pack(pady=0, padx=0)
find_button.pack(pady=9)
find_button2.pack()
copy_button.pack(padx=20, pady=100, side=ctk.RIGHT)
result_text.pack(padx=20, pady=10)

# run the application
window.mainloop()
