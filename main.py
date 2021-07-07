import discord
import os
from replit import db
import requests
import json
import random
from alive import keep_alive
from assets import *

client = discord.Client() 


def update_cuss(word):
  if "cuss" in db.keys():
    cuss = db["cuss"]
    cuss.append(word)
    db["cuss"] = cuss
  else:
    db["cuss"] = [word]

def delete_cuss(index):
  cuss = db["cuss"]
  if len(cuss) > index:
    del cuss[index]
    db ["cuss"] = cuss
  

     

@client.event
async def on_ready():
  print('Hi there I am a bot and my name is {0.user}'.format(client))


@client.event
async def on_message(msg):
  if msg.author == client.user:
    return

  if any(word in msg.content for word in bad_words_eng):
    await msg.channel.send(random.choice(bad_replies_eng))  

  if any(word in msg.content for word in bad_words_hin):
    await msg.channel.send(random.choice(bad_replies_hin))

  if any(word in msg.content for word in simp_activities):
    await msg.channel.send('simp alert')    

  if msg.content.startswith('.it'):
    await msg.channel.send('hello bimtch')
    
  if msg.content.startswith('.help'):
    await msg.channel.send(' hello friends i am itsbon bot currently being developed so i dont have much command so here is the list of a few \n .it - to make me say hello \n .help - to make me display all the commands \n .every - to ping everyone and ask them to play any game \n .gali,hindi - to make me say hindi gali \n .gali,english - to make me say english gali \n .dirty - to make me talk dirty \n to give a story and a name and you decide what to do ') 

  if msg.content.startswith('.every'):
    await msg.channel.send('@everyone lets play a game together')

  if msg.content.startswith('.debu'):
    await msg.channel.send('hemlo sexy') 
 

  if msg.content.startswith('.addgali'):
    cuss = msg.content.split(".addgali",1)[1] 
    update_cuss(cuss) 
    await msg.channel.send("New gali added")

  if msg.content.startswith('.gali,hindi'): 
     await msg.channel.send(random.choice(bad_words_hin))

  if msg.content.startswith('.gali,english'): 
     await msg.channel.send(random.choice(bad_words_eng))  

  if msg.content.startswith('.story'):
    await msg.channel.send(random.choice(stories)+(random.choice(names)))   
  if msg.content.startswith('.dirty'): 
     await msg.channel.send(random.choice(dirty_talk))  

  if msg.content.startswith('.dedicate_music'):
    await msg.channel.send("Dedicate a music for " + random.choice(names))   



keep_alive() 
client.run(os.environ['TOKEN']) 
