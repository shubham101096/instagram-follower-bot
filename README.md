# instagram-follower-bot
A python program used to automate sending follow request to people who follow an account of our interest. For example, user has an Instagram account which tells people about latest movies on the OTT platform. So he can enter keyword like "appleTV" or "netflix" as input to the program.
The program automatically logins to his insta account, searches for the entered keyword and goes to that page.
It then opens the list of followers of that page.
First the bot scrolls down the page multiple times so that around 50 followers can be loaded.
It then starts sending them follow request.
As people who follow 'appleTV' are likely to be interested in his Insta account, so they may follow back and so the user can increase the popularity of his insta account. 
This automation is done with help of Selenium.
 
 User enters the keyword:
![alt text](https://github.com/shubham101096/instagram-follower-bot/blob/master/screenshots/input.png)

Instagram-bot starts sending request to the people who follow the account user entered:
![alt text](https://github.com/shubham101096/instagram-follower-bot/blob/master/screenshots/insta_follow.gif)
