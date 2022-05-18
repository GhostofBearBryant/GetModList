
#  Get mod list from r/mod and store it in a text file.  Mod list is used in the sub manager bot for post approval.

import praw
import time
     

 

sub_name = "ghostofbearbryant"
dontAdd = ["assistantbot1", "repostsleuthbot", "botdefense", "botterminator", "flair_helper", "assistantBot", "moderatelyhelpfulbot", "duplicatedestroyer"]


def get_mod_list():

    modList = []

    #f = open("/home/pi/bots/submanager/modList.txt", "w+")

    for subreddit in reddit.redditor(sub_name).moderated():
        for moderator in reddit.subreddit(subreddit.display_name).moderator():

            if moderator in dontAdd:
                break
            else:    
                 modList.append(str(moderator))
       
    #f.write(f"{modList}")
    print("Done compiling mod list.")
    #print(modList)
    #f.close()
    return modList

def get_contributors():

    contributors = []

    #q = open("/home/pi/bots/submanager/contributors.txt", "w+")
        
    for contributor in reddit.subreddit(sub_name).contributor(limit=None):
        if contributor in dontAdd:
            break
        else:
            contributors.append(str(contributor))

    #q.write(f"{contributors}") 
    print("All done with submitters.")  
    #q.close()
    return contributors   

def get_difference(modList, contributors):

    #modList = open('/home/pi/bots/submanager/modList.txt').read()
    #contributors = open('/home/pi/bots/submanager/contributors.txt').read()

    mod_set = set(modList)
    contrib_set = set(contributors)
    

    add_contributors = mod_set.difference(contrib_set)

    remove_contributors = contrib_set.difference(mod_set)

    #  Code to remove names from the approved users list 
    #add_contributors = contrib_set.difference(mod_set)
    
    for contributor in add_contributors:
       reddit.subreddit("ghostofbearbryant").contributor.add(contributor)    
       print(f'added {contributor}')

    for contributor in remove_contributors:
        reddit.subreddit("ghostofbearbryant").contributor.remove(contributor)    
        print(f'remove {contributor}')

    #print(mod_set)
    #print(contrib_set)

def get_master_list():
    with open("/home/pi/bots/submanager/master_list.txt", "w+") as f:

        master_list = []
        for subreddit in reddit.user.moderator_subreddits(limit=None):
            print(str(subreddit)) 
            master_list.append(str(subreddit))
        f.write(f"{master_list}")
        return master_list   



#Create all subreddit objects and return multisub for comment stream
def get_multisub(master_list):
    sub_list = []
    multisub_str = ""
    # Read subreddit names from master list
    #master_list = open("subreddit_master_list.txt", "r", )
    for sub_name in master_list:
        sub_name = sub_name.replace("\n", "")
        #sub_list.append(Subreddit(sub_name, r))
        multisub_str += sub_name + "+"

    # Remove trailing '+'
    return reddit.subreddit(multisub_str[:-1]) 


if __name__ == '__main__':

    reddit = praw.Reddit(
                    client_id="",
                    client_secret="",
                    user_agent="Get Mod List and Add to Log Sub Bot v.2 by /u/ghostofbearbryant",
                    username="",
                    password=""
                    )

    print(f'Logged in as: {reddit.user.me()}')

    modList = get_mod_list()
    #time.sleep(3)
    master_list = get_master_list()
    subreddit_multiname = get_multisub(master_list)
    time.sleep(1)
    print(subreddit_multiname)
    contributors = get_contributors()
    time.sleep(3)
    get_difference(modList, contributors)



     

