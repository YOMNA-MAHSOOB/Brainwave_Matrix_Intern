import tkinter as tk
from tkinter import messagebox

from Phishing_Link_Scanner import contains_IP, Misspelled_domains, long_url, contains_Suspicious_characters, has_https

def analyze_url():
    url = entry.get().strip()
    dangerLink = 0

    if not url:
        messagebox.showwarning("Input Required", "Please enter a URL before scanning.")
        return

    results = []

    if contains_IP(url):
        results.append("Contains IP address → phishing link")
        dangerLink += 1
    else:
        results.append("No IP address")
     
    if Misspelled_domains(url):
        results.append("Suspicious domain name → possible phishing")
        dangerLink += 1
    else:
        results.append("Domain name looks OK")

    if contains_Suspicious_characters(url):
        results.append("Contains suspicious characters → phishing link")
        dangerLink += 1
    else:
        results.append("No suspicious characters")

    if long_url(url):
        results.append("URL is too long → phishing link")
        dangerLink += 1
    else:
        results.append("Reasonable URL length")

    if not has_https(url):
        results.append("No HTTPS → potential phishing")
        dangerLink += 1
    else:
        results.append("HTTPS is present")

    results.append("Final result:")
    if dangerLink == 0:
        results.append("Safe link")
    else:
        results.append("Phishing link")

    result_text.config(state='normal')
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, "\n".join(results))
    result_text.config(state='disabled')

def clear_fields():
    entry.delete(0, tk.END)
    result_text.config(state='normal')
    result_text.delete("1.0", tk.END)
    result_text.config(state='disabled')
    messagebox.showinfo("Cleared", "Fields cleared!")

# Color Palette
bg_color     = "#D6F3FF"  
entry_bg     = "#F7F7F7" 
btn_color    = "#90CDF4"  
result_bg    = "#FFFFFF"  
font_color   = "#060606"  

root = tk.Tk()
root.title("Phishing Link Scanner")
root.geometry("600x500")
root.configure(bg=bg_color)

title = tk.Label(root, text="Phishing Link Scanner", font=("Arial", 20, "bold"), bg=bg_color, fg=font_color)
title.pack(pady=(20, 5))

label = tk.Label(root, text="Enter URL to scan:", font=("Arial", 13), bg=bg_color, fg=font_color)
label.pack(pady=(10, 0))

entry = tk.Entry(root, font=("Arial", 12), width=55, bg=entry_bg, fg=font_color, relief="groove", bd=2)
entry.pack(pady=5)

button_frame = tk.Frame(root, bg=bg_color)
button_frame.pack(pady=10)

scan_button = tk.Button(button_frame, text="Scan URL", font=("Arial", 12), bg=btn_color, fg=font_color, width=15, command=analyze_url)
scan_button.grid(row=0, column=0, padx=10)

clear_button = tk.Button(button_frame, text="Clear", font=("Arial", 12), bg=btn_color, fg=font_color, width=15, command=clear_fields)
clear_button.grid(row=0, column=1, padx=10)

results_label = tk.Label(root, text="Scan Results:", font=("Arial", 13), bg=bg_color, fg=font_color)
results_label.pack(pady=(15, 5))

result_box = tk.Frame(root, bg=bg_color, padx=10, pady=10)
result_box.pack(fill="both", expand=True)

result_text = tk.Text(result_box, font=("Arial", 12), height=12, bg=result_bg, fg=font_color, wrap="word", relief="groove", bd=2)
result_text.pack(fill="both", expand=True)
result_text.config(state='disabled')

root.mainloop()
