import asyncio
import os
import random
import string
import time

import requests


def rc(len):
    return os.urandom(len).hex()[len:]


async def createdm(token):
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate',
        'accept-language': 'en-GB',
        'authorization': f"{token}",
        'cookie': f'__dcfduid={rc(43)}; __sdcfduid={rc(96)}; __stripe_mid={rc(18)}-{rc(4)}-{rc(4)}-{rc(4)}-{rc(18)}; locale=en-GB; __cfruid={rc(40)}-{"".join(random.choice(string.digits) for i in range(10))}',
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.9 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-context-properties': 'eyJsb2NhdGlvbiI6IkFkZCBGcmllbmRzIHRvIERNIn0=',
        'x-super-properties': "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2Ojk2LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTYuMCIsImJyb3dzZXJfdmVyc2lvbiI6Ijk2LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTEyMTAyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
    }

    try:
        group = requests.post("https://discord.com/api/v9/users/@me/channels", headers=headers,
                              json={"recipients": [], "name": "poc"})
        if group.status_code == "429":
            print("rate limited")
            time.sleep(10)
            return False
        group_id = group.json()['id']
        open("data/groups.txt", "a+").write(f"{group_id}\n")
        print(f"creted group {group_id}")
        time.sleep(2)
        return group
    except Exception as e:
        time.sleep(5)
        print(e)


async def addusr(token, usrid):
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US',
        'authorization': f"{token}",
        'cookie': f'__dcfduid={rc(43)}; __sdcfduid={rc(96)}; __stripe_mid={rc(18)}-{rc(4)}-{rc(4)}-{rc(4)}-{rc(18)}; locale=en-GB; __cfruid={rc(40)}-{"".join(random.choice(string.digits) for i in range(10))}',
        'content-length': '0',
        'origin': 'https://discord.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.9 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-context-properties': 'eyJsb2NhdGlvbiI6IkFkZCBGcmllbmRzIHRvIERNIn0=',
        'x-super-properties': "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2Ojk2LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTYuMCIsImJyb3dzZXJfdmVyc2lvbiI6Ijk2LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTEyMTAyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
    }

    with open('data/groups.txt', 'r') as temp_file:
        ids = [line.rstrip('\n') for line in temp_file]
        print(ids)
    for id in ids:
        try:
            r = requests.put(f"https://discord.com/api/v9/channels/{id}/recipients/{usrid}", headers=headers)
            if r.status_code == "429":
                print("rate limited")
                time.sleep(10)
                return False
            elif r.status_code == "200":
                print(f"added {usrid} to {id}")
        except Exception as e:
            print(e)
            time.sleep(1)


async def remusr(token, usrid):
    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US',
        'authorization': f"{token}",
        'cookie': f'__dcfduid={rc(43)}; __sdcfduid={rc(96)}; __stripe_mid={rc(18)}-{rc(4)}-{rc(4)}-{rc(4)}-{rc(18)}; locale=en-GB; __cfruid={rc(40)}-{"".join(random.choice(string.digits) for i in range(10))}',
        'content-length': '0',
        'origin': 'https://discord.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.1.9 Chrome/83.0.4103.122 Electron/9.4.4 Safari/537.36',
        'x-debug-options': 'bugReporterEnabled',
        'x-context-properties': 'eyJsb2NhdGlvbiI6IkFkZCBGcmllbmRzIHRvIERNIn0=',
        'x-super-properties': "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJlbi1VUyIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2Ojk2LjApIEdlY2tvLzIwMTAwMTAxIEZpcmVmb3gvOTYuMCIsImJyb3dzZXJfdmVyc2lvbiI6Ijk2LjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTEyMTAyLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==",
    }

    with open('data/groups.txt', 'r') as temp_file:
        ids = [line.rstrip('\n') for line in temp_file]
        print(ids)
    for id in ids:
        try:
            requests.delete(f"https://discord.com/api/v9/channels/{id}/recipients/{usrid}", headers=headers)
            print(f"removed {usrid} from {id}")
        except Exception as e:
            print(e)


def gcspaminit():
    token = input("What token would you like to use? (this function only uses one): ")

    option = input("press 1 for create, 2 for add, 3 for rem: ")
    if option == "1":
        howmany = input("how many gcs would you like to make? ")
        for i in range(int(howmany)):
            asyncio.run(createdm(token=token))
    elif option == "2":
        usrid = input("what userid would you like to spam? ")
        task = asyncio.get_event_loop()
        task.run_until_complete(addusr(token=token, usrid=usrid))
    elif option == "3":
        usrid = input("what userid would you like to remove fron gc's? ")
        task = asyncio.get_event_loop()
        task.run_until_complete(remusr(token=token, usrid=usrid))

