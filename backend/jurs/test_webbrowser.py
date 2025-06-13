import webbrowser

url = "https://www.youtube.com"
print(f"Trying to open {url} ...")

opened = webbrowser.open(url)

if opened:
    print("Browser should have opened the URL.")
else:
    print("Failed to open the browser.")

