# Image2Discord Bot

This Discord bot is designed to automate the process of uploading a grid of images to a specified Discord channel. After successfully uploading the images, the bot will delete them from the filesystem, ensuring that your working directory remains clean and organized.

## Features

- Uploads images in batches to a Discord channel.
- Supports common image formats such as PNG, JPG, JPEG, GIF, and MP4 video format.
- Checks and respects Discord's maximum file size limit for uploads.
- Deletes images and videos from the filesystem after successful upload.
- Utilizes discord.py with full intents for comprehensive Discord interactions.

## Requirements

- Python 3.6 or higher
- discord.py
- tqdm

## Setup

1. Clone the Repository:

git clone https://github.com/MadeBySaints/Image2Discord.git

2. Navigate into the project directory:

cd Image2Discord.

3. Install Dependencies:

pip install discord.py tqdm.

5. Discord Bot Token and Permissions:

Create a bot on the Discord Developer Portal and obtain your bot's token. Invite the bot to your server with the appropriate permissions (at least Send Messages and Attach Files). Enable all intents for your bot in the Discord Developer Portal.

7. Configuration:

Edit Config.json to use your bot token and channel ID for discord.

## Usage

8. Run the bot:

python dumper.py

The bot will log in to Discord, upload all eligible images and video from the bot's working directory to the specified channel automatically, and delete them from the folder afterward.

## Contributing

Contributions are welcome! Feel free to submit a pull request or open an issue for any improvements or suggestions.

## License

This project is licensed under the MIT License. See the LICENSE file in the repository for more information.
