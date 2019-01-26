import urllib.request

def takeInput() :
    user_input = input("Enter the Text : ")
    type(user_input)
    profanityCheck(user_input)
    
def profanityCheck(user_input) :
    res = urllib.request.urlopen("https://www.purgomalum.com/service/containsprofanity?text="+user_input)
    html = res.read()
    
    if b'true' in html :
        print("PROFANITY ALERT !!! ")
    elif b'false' in html :
        print("NO CURSE WORD FOUND.")
    else :
        print("ERROR !!!")
   
takeInput()
