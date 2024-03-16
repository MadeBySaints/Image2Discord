import discord
import json
import os
from tqdm import tqdm

# Define intents
intents = discord.Intents.all()

# Initialize Discord client with intents
client = discord.Client(intents=intents)

# Function to check if a file is an image
def is_image(filename):
    return filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.mp4'))

# Function to check if an image size is within Discord's limit
def is_within_size_limit(filename):
    return os.path.getsize(filename) <= 8388608  # Discord's maximum file size is 8 MB

# Function to upload a grid of images to Discord channel and then delete them
async def upload_image_grid(files, channel):
    files_to_send = []
    for image_file in files:
        if is_image(image_file) and is_within_size_limit(image_file):
            discord_file = discord.File(image_file)
            files_to_send.append(discord_file)
    
    if files_to_send:
        await channel.send(files=files_to_send)
        # After successfully sending the files, delete them
        for image_file in files:
            os.remove(image_file)
    else:
        await channel.send("No images left to upload.")

# Main function to handle image uploading
async def handle_image_upload(client):
    folder = os.getcwd()  # Get current directory
    files = [f for f in os.listdir(folder) if is_image(f)]
    
    grid_size = 9

    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    
    channel_id = int(config['channel_id'])
    channel = client.get_channel(channel_id)
    
    if channel is None:
        print("Channel not found or bot doesn't have access to it.")
        return

    # Initialize the progress bar
    pbar = tqdm(total=len(files), desc="Uploading images")

    for i in range(0, len(files), grid_size):
        batch_files = files[i:i+grid_size]
        await upload_image_grid(batch_files, channel)
        # Update the progress bar
        pbar.update(len(batch_files))

    # Close the progress bar after completion
    pbar.close()

# Event handler for when the bot is ready
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await handle_image_upload(client)

# Run the bot
if __name__ == "__main__":
    with open('config.json', 'r') as config_file:
        config = json.load(config_file)
    token = config['token']
    client.run(token)
