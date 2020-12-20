import pyryver
import asyncio
import urllib.request
import requests
import urllib
import time
from pyryver.objects import Creator
from pyryver.objects import Topic
from pyryver import ryver
import random
from pyryver.util import retry_until_available


print("Welcome to the Python secret santa!")
print("-----------------------------------")
botname = input("Before we start, please pick a name for me: ")
botpfp = input("Also, I'm going to need a profile picture. Send an image address here, or say pfp for default: ")
if botpfp == "pfp":
    botpfp = "https://previews.123rf.com/images/gmast3r/gmast3r1411/gmast3r141100257/33643405-santa-claus-cartoon-profile-flat-icon-christmas-holiday.jpg"
botpfp=str(botpfp)
creator = Creator(
    name=botname,
    avatar=botpfp,
)

async def main():
    
    time.sleep(.5)

    print("Thanks for that! I'm going to help you set up a great secret santa with your friends!")

   
    input("Ready? (Y) ")
    time.sleep(.25)
    done = input("Do you already have a Ryver ogranization with your secret santa group? (Y/N) ")
    if done != "Y":
        print("No worries! First, visit https://signup.ryver.com/ and fill out the info on the form.")
        input("Say done when you've finished that: ")
        print("-----------------------------------")
        print("Perfect! Now make sure you press the create organization button. Once that's done, check the email you provided to start your Ryver org.")
        input("Say done once you pressed the link from your email and finished the signup process: ")
        print("-----------------------------------")
    
    org = input("What's the name (not whole URL) of your Ryver organization? ")
    print("Checking...")
    orgurl = str("https://"+org+".ryver.com")
    print(orgurl)
    time.sleep(.5)
    r = requests.get(orgurl)
    time.sleep(.5)
                    
    statuscode = r.status_code
    time.sleep(.5)
                    
    if statuscode == 404:
        print("Uh oh. That's not a real organization. Please try again.")
        
                           
    if statuscode == 200:
                                
        print("Thanks for giving me a valid organization!")
        print("-----------------------------------")
        username = input("What is your username on Ryver? Don't include the @. (It should say in the top left corner): ")
    
        password = input("What is your Ryver password? (I need this to send messages in Ryver. It won't be shared with anyone.): ")
    
        print("-----------------------------------")
        print("I'm making a SecretSanta forum quickly to keep everything organized, please wait.")
        
        
        
       
       
        time.sleep(2)
    
        # Connect to ryver
        async with pyryver.Ryver(org, username, password) as ryver:
        # Load all chats
            await ryver.load_chats()
        # Find users and forums/teams
            
            await ryver.create_forum("SecretSanta")
            forum_or_team = ryver.get_groupchat(name="SecretSanta")
            print("I just created the forum, please hold for a few seconds...")
            time.sleep(5)
        # Send a message
            code = random.randint(11111,99999)
            code = str(code)
            await forum_or_team.send_message("Your verification code is: [["+code+"]]",creator)
            
        
            while True:
                verify = input("Please enter the verification code: ")
                if verify == code:
                    break
            
            
           
              
           
                
                   
                    
         
            
            
            
 
            
            
            print("-----------------------------------")
            print("Time for the gifting, I'm going to make an announcement in +SecretSanta about the gift exchange so everyone can sign up!")
            input("Press return to start it. Check back here once I post the topic.")
            
            subject = "Secret Santa"
            body = "@team - Hey everyone! Someone in your Ryver organization has set up a secret santa for all of you! You'll recieve a message from me shortly with info. Have fun!" 
            stickied = False
            await forum_or_team.create_topic(subject, body, stickied, creator)
            ss = []
            ad = []
            amount = input("How many people are playing? ")
            price = input("Choose amount to be gifted ($): ")
            date = input("When should all gifts be given by? DD/MM/YYYY: ")
            amount = int(amount)
            
            
            while True:
                adduser = input("Particpant Username: ")
                address = input("Above user's adress for gifting: ")
                
                
                
                ss.append(adduser)
                ad.append(address)
                amount -= 1
                if amount == 0:
                    break
            
            
            ss_order = ss[:]
            ad_order = ss[:]
            random.shuffle(ss_order)
            ada = 0
            up = 0 
            for item in ss:
                
                iteminlist = ss[up]
                iteminad = ad[ada]
                up += 1
                ada += 1
                my_friend = ryver.get_user(username=iteminlist)
                
                
                random.shuffle(ss_order)
                send = ss_order.pop()
               
                    
                
                sendad = str(ad)
                print("Shuffling list and sending...")
                
                
                
              
            
                        
                      
                        
               
                    
                
               
            
           
                     
                
                await my_friend.send_message("Hey there! You've been invited to the secret santa! Please gift **`"+send+"`** a gift worth around $"+price+". You can send their gift to the address: `"+iteminad+"`. Please get this done by "+date+". Thanks! If you have any questions, you can message the organizer: `"+username+"`",creator)
               
                
                await my_friend.send_message("**Super secret info above - please do not look Secret Santa host! :santa:**",creator)
                
                                   
            print("Please try not to look sat the secret santa results in DM's. I have provided all neccesary info to the users and you should be good to go!")
            await forum_or_team.send_message("I just messaged everyone participating with their neccesary info! See you all later! :santa:",creator)      

                
                
            
                
            
           
            

asyncio.get_event_loop().run_until_complete(main())

    
        
    
    




