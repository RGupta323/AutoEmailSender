import smtplib, ssl
import urllib, re
from googlesearch import search
from urllib.request import Request, urlopen

def main():
    n=input("Enter a number: ")
    e=emails(int(n))
    count=0
    print(e) #list of emails 
    for email in e:
        send("johnhan234@gmail.com","asdfjkl;",email)
        count+=1
    print("Just sent {} emails".format(count))
    
def send(sender_email, sender_password, receiver_email): 
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
##    sender_email = "guptarohan323@gmail.com"  # Enter your address
##    receiver_email = "shyboyrey@gmail.com"  # Enter receiver address
##    password = "Koopatroopa123"
    message = """\
    Subject: Hi there

    Subscribe to my YouTube Channel https://www.youtube.com/watch?v=cDe6AFuN5hQ
    This message is sent from Python."""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message)
def emails(n):
    terms=list()
    urls=list()
    e=list() #list of email addresses 
    #assembling a list of terms to search
    while(True):
        query=input("Please enter a search term to scrape email addresses: ")
        if(query=='done'):
            break
        terms.append(query)
    #searching the internet using those queries
    for t in terms:
        j=search(t, tld='com', lang='en', num=n, start=0, stop=10, pause=2.0)
        for url in j:
            urls.append(url)
    for url in urls:
        f=openUrl(url)
        s=str(f)
        emails=re.findall(r"[A-Za=-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}",s)
        for em in emails:
            if(em not in e): 
                e.append(em)
    return e;
#functio to open a url
def openUrl(url):
##    req=urllib.request.Request(url)
##    with urllib.request.urlopen(req) as response:
##        return response.read()
    req=Request(url, headers={"User-agent": "Mozilla/5.0"})
    webpage=urlopen(req).read()
    return webpage
        
    
