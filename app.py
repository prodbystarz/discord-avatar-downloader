import os
import requests
from PIL import Image
from io import BytesIO

def download_and_resize_avatar(user_id, output_folder='avatars', size=(3000, 3000)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    base_url = f"https://cdn.discordapp.com/avatars/{user_id}"
    avatar_url = f"{base_url}/a_hash.png?size=1024"

    try:
        user_info_url = f"https://discord.com/api/v9/users/{user_id}"
        headers = {
            "Authorization": "Bot 'bot_token'" #insert bot token there
        }
        response = requests.get(user_info_url, headers=headers)
        if response.status_code != 200:
            print(f"Failed to fetch user information: {response.status_code}")
            return

        user_data = response.json()
        avatar_hash = user_data.get("avatar")
        if not avatar_hash:
            print(f"User {user_id} does not have an avatar.")
            return

        avatar_url = f"{base_url}/{avatar_hash}.png?size=1024"

        response = requests.get(avatar_url)
        response.raise_for_status()

        img = Image.open(BytesIO(response.content))
        img = img.resize(size, Image.LANCZOS)

        output_path = os.path.join(output_folder, f"{user_id}_avatar.png")
        img.save(output_path)
        print(f"Avatar saved to {output_path}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch avatar: {e}")

if __name__ == "__main__":
    user_id = input("Enter the Discord user ID: ")
    download_and_resize_avatar(user_id)
