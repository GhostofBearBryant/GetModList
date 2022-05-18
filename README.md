# GetModList
Add co-moderators to a log subreddit for the bot's actions.

GetModList.py is a script that runs once a month as a linux cronjob.  

It has several functions.

1. It checks the shared mod lists for each subreddit for which the bot is a mod and makes a list of all co-moderators.
2. The next step is to compare that list to the list of approved users for a private log subreddit that is used to log all of the bot's actions.  That way all mods can review the bot's actions.  The private subreddit also makes it easier to review any actions taken by the bot from mobile.
3. The bot then checks the list of approved users and removes any reddit accounts that are no longer on a shared modlist with the submanager bot.
4. The last function is that the bot compliles a multireddit string of all of the subs of which it is a mod.  This list can then be passed to the main script for use as the main "subreddit name" when defining which subreddits the bot patrols.
