import requests, json, time, os
amount = int(input("How many webhooks to use? (Minimum = 1, Maximum = 10): "))
avatar = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDYsuOLXrjLmzJTCM-AOwdZGQso5Nkt0cJ_Q&s"; webhooks = []
for i in range(amount):
    url_input = input(f"Webhook URL {i+1}: "); webhooks.append(url_input)
name = input("Name To Use: ")
text = input("Text To Spam: ")
os.system("cls")
while True:
    for url in webhooks:
        response = requests.post(url, data={"avatar_url": avatar, "content": text, "username": name}); time.sleep(0.5)
        if response.status_code != 429: 
            print(f"Failed to send: RATELIMITED"); time.sleep(1)

