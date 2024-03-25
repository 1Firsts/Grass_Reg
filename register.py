import requests
from faker import Faker
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import string
import time
from colorama import init, Fore

init(autoreset=True)

def generate_random_email():
    domain = "tempmailo.com"
    username_length = 10
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=username_length))
    return f"{username}@{domain}"

def manual_input():
    email = input("Masukkan alamat email manual: ")
    return email

def register_with_grass(email, referral_code, output_file):
    # Generate random username and password
    faker = Faker()
    username = faker.user_name()
    password = faker.password(length=12)

    # Confirmation password is the same as password
    confirmation_password = password

    # Update data with generated email, username, and password
    grass_register_url = 'https://app.getgrass.io/register/'

    headers = {
        'authority': 'app.getgrass.io',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json;charset=UTF-8',
        'referer': 'https://app.getgrass.io/',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Google Chrome";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': UserAgent().random
    }

    data = {
        'email': email,
        'password': password,
        'referralCode': referral_code
    }

    try:
        # Register with generated data
        response = requests.post(grass_register_url, json=data, headers=headers)
        print(Fore.CYAN + "=== Status Registrasi ===")
        if response.status_code == 200:
            print(Fore.GREEN + "Registrasi berhasil!")
            print(Fore.YELLOW + "Username:", username)
            print(Fore.YELLOW + "Email:", email)
            print(Fore.YELLOW + "Password:", password)
            # Tulis hasil registrasi ke dalam file
            with open(output_file, 'a') as file:
                file.write(f"Registrasi berhasil!\nUsername: {username}\nEmail: {email}\nPassword: {password}\n\n")
        else:
            print(Fore.RED + "Registrasi gagal.")
            print(Fore.YELLOW + "Response Content:", response.text)
    except Exception as e:
        print(Fore.RED + "Terjadi kesalahan:", str(e))

# Tampilan menu
print(Fore.CYAN + "=== Registrasi dengan Grass ===")
print(Fore.YELLOW + "Menu:")
print("1. Gunakan Email Acak dari Temp Mail")
print("2. Input Manual")

menu_choice = input(Fore.GREEN + "Pilih menu (1/2): ")

if menu_choice == '1':
    email = generate_random_email()
elif menu_choice == '2':
    email = manual_input()
else:
    print(Fore.RED + "Pilihan tidak valid.")
    exit(1)

referral_code = input(Fore.GREEN + "Masukkan referral code: ")
output_file = input(Fore.GREEN + "Masukkan nama file untuk menyimpan hasil registrasi (misal: hasil_registrasi.txt): ")

# Registrasi berulang kali dengan jeda 3 detik
while True:
    register_with_grass(email, referral_code, output_file)
    time.sleep(3)
