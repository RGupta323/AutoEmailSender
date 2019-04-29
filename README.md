# AutoEmailSender
This is a project I worked on for a bit. 
Basically I use it uses whats called queries or search terms, to scrape different urls and from there gets any emails if any from the website 
and then sends an email to those emails. 

In order to run this successfully, all you have to do is type in main() to the python shell. 

You enter in a number, which is the number of urls per search query. Then the program asks continously for a search terms, and when you're done 
simply type 'done', and it will terminate. 

After that, the search queries or terms are stored into a list which are then used to search through urls, and then those urls are webscraped 
via regular expressions. 

And then a message is sent to these emails via an SMTP server. 
