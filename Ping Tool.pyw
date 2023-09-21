import tkinter as tk
import subprocess

devices = {
    "POS Server": "xxxxx.pos.chick-fil-a.com",
    "Router": "xxxxx.rtr.chick-fil-a.com",
    "CFA PC": "xxxxx.pc.chick-fil-a.com",
    "MICR": "micr.xxxxx.chick-fil-a.com",
    "Smart Safe": "loomis.xxxxx.chick-fil-a.com",
    "DMZ": "dmz.xxxxx.chick-fil-a.com",
    "3rd Party Printer": "printer.xxxxx.chick-fil-a.com",
    "SW1": "xxxxx.SW1.chick-fil-a.com",
    "SW2": "xxxxx.SW2.chick-fil-a.com",
    "SW3": "xxxxx.SW3.chick-fil-a.com",
    "SW4": "xxxxx.SW4.chick-fil-a.com",
    "CradlePoint (WAN2)": "cfaxxxxxcp.cbescpe.com",
    "Fiber (WAN1)": "cfaxxxxx.cfamsp.com"
}

def ping_device(store_number, device_address):
    device_address = device_address.replace('xxxxx', store_number)
    cmd = f"ping {device_address} -t"
    subprocess.Popen(["start", "cmd", "/k", cmd], shell=True)

def ping_selected_devices(event=None):
    selected_devices = [device_listbox.get(idx) for idx in device_listbox.curselection()]
    store_number = store_number_entry.get()

    if not selected_devices:
        error_label.config(text="Please select at least one device.")
    elif not store_number.isdigit() or len(store_number) != 5:
        error_label.config(text="Please enter a valid 5-digit store number.")
    else:
        error_label.config(text="")
        for device in selected_devices:
            ping_device(store_number, devices[device])

# Create the main window
root = tk.Tk()
root.title("Ping Tool")

# Set the width and height of the window
window_width = 220
window_height = 290
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (window_width / 2)
y_coordinate = (screen_height / 2) - (window_height / 2)
root.geometry(f"{window_width}x{window_height}+{int(x_coordinate)}+{int(y_coordinate)}")

# Create a listbox for device selection with a fixed height
listbox_height = 13
device_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE, height=listbox_height)
for device in devices:
    device_listbox.insert(tk.END, device)
device_listbox.pack()

# Create a store number entry field
store_number_label = tk.Label(root, text="Enter 5-digit store number:")
store_number_label.pack()
store_number_entry = tk.Entry(root)
store_number_entry.pack()
store_number_entry.focus_set()  # Set focus to this entry field

# Create a ping button
ping_button = tk.Button(root, text="Ping", command=ping_selected_devices)
ping_button.pack()

# Bind the Enter key to trigger the "Ping" button
root.bind("<Return>", ping_selected_devices)

# Error label to display validation errors
error_label = tk.Label(root, text="", fg="red")
error_label.pack()

root.mainloop()
