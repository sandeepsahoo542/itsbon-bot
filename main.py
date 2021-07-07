import discord
import os
from replit import db
import requests
import json
import random
from alive import keep_alive

client = discord.Client() 

bad_words_eng = ['dick','cunt','fuck','titties','fucker','asshole']

bad_words_hin = ['katwa','madarchod','bhsdk','randi','gandu','lund','lodu','tmkc','bhosdike']

bad_replies_eng = [
"stop saying these bad words",
"bad actions are not tolerated",
"hey i think you dropped your brain - sincerely itsbon",
"seems like someone lacks formal education"
]

bad_replies_hin = [
  "chal hat na be ",
  "apne papa ko bolna school mein bharti karade phirse",
  "tameez hai hi nahi ",
  "tumko ab kon sikhaye"
]


simp_activities = [
"you are beautiful",
"kitna acha bol rahi ho",
"han tum jo bol rahi wahi karenge"                
]


stories = [

  "You are stranded in an island where all you can eat is coconut and everywhere you look coconut trees and you are with ",
  "You go into a strip club just to see your ex strip teasing there and your ex was ",
  "You go into a place where all you can eat is for 500 bucks but you cant use the toilet and your stomach is half full how much would you eat and for how long and you have gone with ",
  "you get the chance to go meet your favourite celebrity and the person going with you is ",
  "you were pushed to the toilet of the opposite gender what would be your reaction if you saw "


]

names = [
   'ABHIK  KONER',
   'ABHISHEK  KUMAR',
   'ADITYA  MEENA',
   'AKANKSHA SINGH',
   'AKSHITA  SAH',
   'ANIKET  KUMAR',
   'ANIKET  VERMA',
   'ANIRUDDHA  BHAGAWATI',
   'ANISH  ANMOL',
    'ANJALI  BHAWANI',
    'ANKIT  PATEL',
    'ANMOL  NARAYAN',
    'ANUJ  ANAND',
    'ANURAG  KANUNGO',
    'ARKA  MUKHERJEE',
    'ASHMIT  SINGH',
   'ASHUTOSH  KUMAR',
   'ATUL  ARYA',
    'ATUL  DUBEY',
    'AYUSH CHAKRABORTY',
    'BHASKAR  GUPTA',
    'BISWARUP  GUHA',
   'CHINMAY  SHARMA',
    'CHIRAG  KAR',
    'DEBDEEP  PAL',
    'DEBRAJ  DEY',
   'DEVANSH  SRIVASTAVA',
   'DEVYANSH  RAWAT',
   'GAURAV  RAJ',
    'HIMANSHU  HIMSURYA',
    'JOY  MAJUMDAR',
    'MONJIMA  MAJUMDAR',
    'NARAYAN BANDYOPADHYAY',
    'NITISH  NIRMAL' ,
    'NITYA TRRIPURARI SINGH',
    'P  RUPSA',
   'PRANAV  MATHUR',
    'PRANAV  PANT',
    'PRASHANT  PUROHIT',
    'PRIYAM  MITRA',
   'PRIYANSHU  JHA',
   'RISHI  AGARWAL',
    'ROHIT KUMAR PANI',
    'SAHIL KUMAR SINGH',
    'SANDEEP SUBHANKAR SAHOO',
    'SAPTANGSHU  KAVIRAJ',
    'SASWATA  SARKAR',
    'SATYAPRIYA  MISHRA',
    'SHEETAL  MOHANTY',
    'SHIBASISH  KAR',
    'SHISHIR  SAURAV',
    'SHRIMOY  MOHANTY',
    'SMEET  SINGH',
    'SOHAN  DANDAPAT',
    'SOUMALYA  MUNSI',
    'SOURAV  SARKAR',
   'SUBHRANGSHU  GHOSH',
   'SUMIT  PANWAR',
   'SWASTIK  CHATTERJEE',
   'TANMOY  ROY',
   'TRYAMBAK  DEY',
   'UTKARSH  GARG',
    'VIBHAKAR  YASHASVI',
    'VINAYAK  TRIPATHI',
   'ROSHNI  DAS'

]

dirty_talk = [
   "My ceiling is so boring, I wish I could see you on top of me instead!",
   "I’m always in the mood for you.",
   "You make me want to sin.",
   "I had the wildest dream last night, and guess what, you were in it!",
   "You’re going to scream my name tonight.",
   "I miss you… on top of me!",
   "I am going to bring out the animal in you, tonight!"
]

task = [
  "Take your vehicle and go goof around",
  ""
]
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
