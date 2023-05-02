import discord
import os
import giphy_client
from giphy_client.rest import ApiException
import random

api_instance = giphy_client.DefaultApi()

gif_query = ""
giphy_token = ""
discord_api_key = ""

async def search_gifs(query):
    try:
        response = api_instance.gifs_search_get(giphy_token, query, limit=3, rating="g")
        lst = list(response.data)
        gif = random.choices(lst)

        return gif[0].url

    except ApiException as e:
        return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e


client = discord.Client()

praises = {
    "You look good today": "string",
    "You're the best": "string",
}

list_phrases = list(praises.items())


def pick_praise(praises):
    praise = random.choice(praises)
    print(praise)
    return praise


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("abachi praise"):
        praise = pick_praise(list_phrases)

        if praise[1] == "string":
            await message.channel.send(praise[0])
        elif praise[1] == "gif_random":
            gif = await search_gifs(praise[0])
            await message.channel.send("Gif URL : " + gif)
        elif praise[1] == "gif_url":
            await message.channel.send(praise[0])

    if message.content.startswith("abachi bump"):
        await message.channel.send("https://media.giphy.com/media/MRxJqmk3MNta8/giphy.gif")

client.run(discord_api_key)
