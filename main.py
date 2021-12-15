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
    "https://media.giphy.com/media/hMKjvTYlSaFCU/giphy.gif": "gif_url",
    "https://media.giphy.com/media/MRxJqmk3MNta8/giphy.gif": "gif_url",
    "https://media.giphy.com/media/rFPH6jKnrAKU8/giphy.gif": "gif_url",
    "https://media.giphy.com/media/UT2HdKPXukBJjypvwy/giphy.gif": "gif_url",
    "https://media.giphy.com/media/83AmaPcShmpjHJ43qC/giphy.gif": "gif_url",
    "https://media.giphy.com/media/BSYBVqUdNvhAy3hWnO/giphy.gif": "gif_url",
    "https://media.giphy.com/media/DuI2l5zEDiGzoWfYdL/giphy.gif": "gif_url",
    "https://media.giphy.com/media/qcLaYD4EIPJabpN16c/giphy.gif": "gif_url",
    "wolf of wall street chest bump": "gif_random",
    "Satoshi would be proud of us :smiling_face_with_tear:": "string",
    "Abachi has bigger balls than Jupiter :ringed_planet:": "string",
    "(3,3) 4 lyf baby": "string",
    "Abachi to the moooon. :rocket:": "string",
    ":913098305012109334:": "string",
    ":pepe_holding__abachi: :pepe_holding__abachi: :pepe_holding__abachi:": "string",
    "Abachi, You’re that “Nothing” when people ask me what I’m thinking about.": "string",
    "You look great today ohmie's. :heart:": "string",
    "Abachi, you have impeccable manners.": "string",
    "Abachi, I like your style.": "string",
    "Abachi, You have the best laugh.": "string",
    "I appreciate you and you appreciate me too.": "string",
    "Abachi, You are the most perfect you there is.": "string",
    "Our system of inside jokes is so advanced that only you and I (all the ohmie's of the world) get it. And I like that.": "string",
    "Abachi, Your perspective is refreshing.": "string",
    "Abachi, You’re an awesome friend.": "string",
    "You’re more helpful than you realize.": "string",
    "Abachi, Is that your picture next to “charming” in the dictionary?": "string",
    "On a scale from 1 to 10, you’re an Abachi.": "string",
    "Yes abachi, I want to be on your wl, your wife list.": "string",
    "You’re a great listener.": "string",
    "How is it that you always look great, even in sweatpants?": "string",
    "Everything would be better if more people were like you!": "string",
    "I bet you sweat ohms.": "string",
    "90's hair gel < hipsters < abachi": "string",
    "Abachi, Hanging out with you is always a blast.": "string",
    "When you say, “I meant to do that,” I totally believe you Abacih.": "string",
    "When you’re not afraid to be yourself is when you’re most incredible Abachi baby.": "string",
    "Colors seem brighter when you’re around.": "string",
    "Someone is getting through something hard right now because you’ve got their back.": "string",
    "You have the best ideas.": "string",
    "Everyone gets knocked down sometimes, but you always get back up and keep going.": "string",
    "You’re a candle in the darkness.": "string",
    "Being around you is like being on a happy little vacation.": "string",
    "If someone based an Internet meme on you, it would have impeccable grammar.": "string",
    "Who raised you? They deserve a medal for a job well done.": "string",
    "Abachi, You’re like a breath of fresh air.": "string",
    "You’re so thoughtful.": "string",
    "Your creative potential seems limitless.": "string",
    "Abachi, You’re irresistible when you blush.": "string",
    "Abachu, Your ass deserves its own Instagram account.": "string",
    "Abachi, I need your naked body more than I need oxygen right now.": "string",
    "Oh Abachi, You make me want to be so fucking naughty.": "string",
    "Oh Abachi, Do you realize what you do to me?": "string",
    "Where are we going? To the mooooooon baby! :rocket:": "string",
    "It's all over guys :cry: , read this document and you'll understand why: https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley": "string",
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
