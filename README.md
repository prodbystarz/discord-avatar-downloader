# discord-avatar-downloader

a simple script to download and resize discord user avatars.

## prerequisites

- python 3.x
- pip (python package installer)
- requests library
- pillow library

## setup

### windows

1. clone the repository:
    ```sh
    git clone https://github.com/prodbystarz/discord-avatar-downloader.git
    cd discord-avatar-downloader
    ```

2. install the required libraries:
    ```sh
    pip install requests pillow
    ```

3. create a discord bot and get your bot token. replace `bot_token` in `app.py` with your actual bot token.

4. run the script:
    ```sh
    python app.py
    ```

### mac

1. clone the repository:
    ```sh
    git clone https://github.com/prodbystarz/discord-avatar-downloader.git
    cd discord-avatar-downloader
    ```

2. install the required libraries:
    ```sh
    pip3 install requests pillow
    ```

3. create a discord bot and get your bot token. replace `bot_token` in `app.py` with your actual bot token.

4. run the script:
    ```sh
    python3 app.py
    ```

## usage

1. when prompted, enter the discord user id of the user whose avatar you want to download and resize.
2. the avatar will be saved in the `avatars` folder as `<user_id>_avatar.png`.

## notes

- ensure your bot has the necessary permissions to read user information.
- avatars will be resized to 3000x3000 pixels.

## license

this project is licensed under the mit license.
