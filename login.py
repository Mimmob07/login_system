#!/usr/bin/python
#imports
import ast
import os
from colorama import Fore, Style
import sys
import tkinter as tk
import requests
import time
import getpass
import webbrowser
#other stuff
os.system('clear')
f = open("login_info.txt", "r")
contents = f.read()
f.close()
users = ast.literal_eval(contents) #empty dictionary
#variables
stuff = ""
status = ""
newlist = []
login = ""
inp = ("| => ")

def interface():#main page after login
    os.system("clear")
    print(Fore.CYAN + """
    ██╗░░░░░██╗████████╗██╗░░██╗██╗██╗░░░██╗███╗░░░███╗
    ██║░░░░░██║╚══██╔══╝██║░░██║██║██║░░░██║████╗░████║
    ██║░░░░░██║░░░██║░░░███████║██║██║░░░██║██╔████╔██║
    ██║░░░░░██║░░░██║░░░██╔══██║██║██║░░░██║██║╚██╔╝██║
    ███████╗██║░░░██║░░░██║░░██║██║╚██████╔╝██║░╚═╝░██║
    ╚══════╝╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░╚═════╝░╚═╝░░░░░╚═╝
    """)
    print(Fore.RED + """
    ░██████╗██╗░░░██╗░██████╗████████╗███████╗███╗░░░███╗░██████╗
    ██╔════╝╚██╗░██╔╝██╔════╝╚══██╔══╝██╔════╝████╗░████║██╔════╝
    ╚█████╗░░╚████╔╝░╚█████╗░░░░██║░░░█████╗░░██╔████╔██║╚█████╗░
    ░╚═══██╗░░╚██╔╝░░░╚═══██╗░░░██║░░░██╔══╝░░██║╚██╔╝██║░╚═══██╗
    ██████╔╝░░░██║░░░██████╔╝░░░██║░░░███████╗██║░╚═╝░██║██████╔╝
    ╚═════╝░░░░╚═╝░░░╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░░░░╚═╝╚═════╝░
    """)
    print(Style.RESET_ALL)
    print("||=================================================||")
    print("|| create = create a new file then save text to it ||")
    print("|| read = see the contents of an existing file     ||")
    print("|| edit = edit an existing file                    ||")
    print("|| client = join chatroom                          ||")
    print("|| server = start chatroom server                  ||")
    print("|| weather = get weather                           ||")
    print("|| hack = switch to hacker mode                    ||")
    print("|| crypt = encrypt/decrypt text                    ||")
    print("|| fun = get fun perks                             ||")
    print("|| quit = quit/exits program                       ||")
    print("||=================================================||\n")
    cf = input(inp)
    if cf == "create" or cf == "Create":
        createfile()
    elif cf == "read" or cf == "Read":
        readfile()
    elif cf == "edit" or cf == "Edit":
        editfile()
    elif cf == "client" or cf == "Client":
        client()
    elif cf == "server" or cf == "Server":
        server()
    elif cf == "weather" or cf == "Weather":
        weather()
    elif cf == "hack" or cf == "Hack":
            os.system("clear")
            hacker_mode()
    elif cf == "quit" or cf == "Quit":
        sys.exit()
    elif cf == "crypt" or cf == "Crypt":
        os.system("python3 encryption.py")
    elif cf == "fun" or cf =="Fun":
        funmode()
    else:
        print("\nanswer not recognized\n")
        time.sleep(1)
        interface()
def createfile():
    os.system("clear")
    print("""
    ░█████╗░██████╗░███████╗░█████╗░████████╗███████╗  ███████╗██╗██╗░░░░░███████╗
    ██╔══██╗██╔══██╗██╔════╝██╔══██╗╚══██╔══╝██╔════╝  ██╔════╝██║██║░░░░░██╔════╝
    ██║░░╚═╝██████╔╝█████╗░░███████║░░░██║░░░█████╗░░  █████╗░░██║██║░░░░░█████╗░░
    ██║░░██╗██╔══██╗██╔══╝░░██╔══██║░░░██║░░░██╔══╝░░  ██╔══╝░░██║██║░░░░░██╔══╝░░
    ╚█████╔╝██║░░██║███████╗██║░░██║░░░██║░░░███████╗  ██║░░░░░██║███████╗███████╗
    ░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝  ╚═╝░░░░░╚═╝╚══════╝╚══════╝
    """)
    print("what is the name of the text file you would like to create?(do not include the .txt)")
    nm = input(inp);
    print('enter any text you want saved')
    f = open(nm, "a+")
    x = input(inp);
    f.write(x)
    f.close()
    interface()
def readfile():
    os.system("clear")
    print("""
    ██████╗░███████╗░█████╗░██████╗░  ███████╗██╗██╗░░░░░███████╗
    ██╔══██╗██╔════╝██╔══██╗██╔══██╗  ██╔════╝██║██║░░░░░██╔════╝
    ██████╔╝█████╗░░███████║██║░░██║  █████╗░░██║██║░░░░░█████╗░░
    ██╔══██╗██╔══╝░░██╔══██║██║░░██║  ██╔══╝░░██║██║░░░░░██╔══╝░░
    ██║░░██║███████╗██║░░██║██████╔╝  ██║░░░░░██║███████╗███████╗
    ╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═════╝░  ╚═╝░░░░░╚═╝╚══════╝╚══════╝
    """)
    print("what is the name of the file you would like to read?")
    rd = input(inp)
    f = open(rd, "r")
    contentamos = f.read()
    print(contentamos)
    f.close()
    interface()
def editfile():
    os.system("clear")
    print("""
    ███████╗██████╗░██╗████████╗  ███████╗██╗██╗░░░░░███████╗
    ██╔════╝██╔══██╗██║╚══██╔══╝  ██╔════╝██║██║░░░░░██╔════╝
    █████╗░░██║░░██║██║░░░██║░░░  █████╗░░██║██║░░░░░█████╗░░
    ██╔══╝░░██║░░██║██║░░░██║░░░  ██╔══╝░░██║██║░░░░░██╔══╝░░
    ███████╗██████╔╝██║░░░██║░░░  ██║░░░░░██║███████╗███████╗
    ╚══════╝╚═════╝░╚═╝░░░╚═╝░░░  ╚═╝░░░░░╚═╝╚══════╝╚══════╝
    """)
    print("what is the name of the file you would like to edit?\n(make sure the file is in the folder that this program is in)")
    ed = input(inp)
    f = open(ed, "w")
    contentamis = f.read()
    print("contents of the file:")
    print(contentamis + "\n")
    print(Fore.RED + "wrighting anything here will overide the contents of the file")
    print("press ^c to quit")
    print(Style.RESET_ALL)
    print("what is it you would like to replace the existing text with?")
    replace = input(inp)
    f.write(replace)
    f.close()
    interface()
def client():
    os.system("clear")
    print("what is the hosts ip?")
    ip = input(inp)
    print("what is the port number you would like to use")
    port = input(inp)
    print("""
    ░█████╗░██╗░░██╗░█████╗░████████╗  ██████╗░░█████╗░░█████╗░███╗░░░███╗
    ██╔══██╗██║░░██║██╔══██╗╚══██╔══╝  ██╔══██╗██╔══██╗██╔══██╗████╗░████║
    ██║░░╚═╝███████║███████║░░░██║░░░  ██████╔╝██║░░██║██║░░██║██╔████╔██║
    ██║░░██╗██╔══██║██╔══██║░░░██║░░░  ██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║
    ╚█████╔╝██║░░██║██║░░██║░░░██║░░░  ██║░░██║╚█████╔╝╚█████╔╝██║░╚═╝░██║
    ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░  ╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝
    """)
    time.sleep(1)
    os.system("python client.py " + ip + " " + port)
    interface()
def server():
    os.system("clear")
    print("what is the hosts ip?")
    ipa = input(inp)
    print("what is the port number you would like to use")
    porta = input(inp)
    print("""
    ░█████╗░██╗░░██╗░█████╗░████████╗  ██████╗░░█████╗░░█████╗░███╗░░░███╗
    ██╔══██╗██║░░██║██╔══██╗╚══██╔══╝  ██╔══██╗██╔══██╗██╔══██╗████╗░████║
    ██║░░╚═╝███████║███████║░░░██║░░░  ██████╔╝██║░░██║██║░░██║██╔████╔██║
    ██║░░██╗██╔══██║██╔══██║░░░██║░░░  ██╔══██╗██║░░██║██║░░██║██║╚██╔╝██║
    ╚█████╔╝██║░░██║██║░░██║░░░██║░░░  ██║░░██║╚█████╔╝╚█████╔╝██║░╚═╝░██║
    ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░  ╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝
        """)
    time.sleep(1)
    os.system("python chat_server.py " + ipa + " " + porta)
    interface()
def weather():
    HEIGHT = 500
    WIDTH = 600

    def test_function(entry):
        print("This is the entry:", entry)

    # api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
    # a4aa5e3d83ffefaba8c00284de6ef7c3

    def format_response(weather):
        try:
            name = weather['name']
            desc = weather['weather'][0]['description']
            temp = weather['main']['temp']

            final_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
        except:
            final_str = 'There was a problem retrieving that information'

        return final_str

    def get_weather(city):
        weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'APPID': weather_key, 'q': city, 'units': 'imperial'}
        response = requests.get(url, params=params)
        weather = response.json()

        label['text'] = format_response(weather)

    root = tk.Tk()

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    background_image = tk.PhotoImage(file='landscape.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

    entry = tk.Entry(frame, font=40)
    entry.place(relwidth=0.65, relheight=1)

    button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
    button.place(relx=0.7, relheight=1, relwidth=0.3)

    lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
    lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

    label = tk.Label(lower_frame)
    label.place(relwidth=1, relheight=1)

    root.mainloop()
    interface()
def funmode():
    os.system("clear")
    print("""
    ███████╗██╗░░░██╗███╗░░██╗  ███╗░░░███╗░█████╗░██████╗░███████╗
    ██╔════╝██║░░░██║████╗░██║  ████╗░████║██╔══██╗██╔══██╗██╔════╝
    █████╗░░██║░░░██║██╔██╗██║  ██╔████╔██║██║░░██║██║░░██║█████╗░░
    ██╔══╝░░██║░░░██║██║╚████║  ██║╚██╔╝██║██║░░██║██║░░██║██╔══╝░░
    ██║░░░░░╚██████╔╝██║░╚███║  ██║░╚═╝░██║╚█████╔╝██████╔╝███████╗
    ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝  ╚═╝░░░░░╚═╝░╚════╝░╚═════╝░╚══════╝
    """)
    print("||=================================================||")
    print("|| rickroll = play never gonna give you up         ||")
    print("|| back = go back                                  ||")
    print("|| quit = quit the program                         ||")
    print("||=================================================||")
    fumo = input(inp)
    if fumo == "rickroll" or fumo == "Rickroll" or fumo == "RickRoll":
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    elif fumo == "back" or fumo == "Back":
        interface()
    elif fumo == "quit" or fumo =="Quit":
        sys.exit()
def hacker_mode():
    os.system("clear")
    print("""
    ██╗░░██╗░█████╗░░█████╗░██╗░░██╗███████╗██████╗░  ███╗░░░███╗░█████╗░██████╗░███████╗
    ██║░░██║██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗  ████╗░████║██╔══██╗██╔══██╗██╔════╝
    ███████║███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝  ██╔████╔██║██║░░██║██║░░██║█████╗░░
    ██╔══██║██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗  ██║╚██╔╝██║██║░░██║██║░░██║██╔══╝░░
    ██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║  ██║░╚═╝░██║╚█████╔╝██████╔╝███████╗
    ╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝  ╚═╝░░░░░╚═╝░╚════╝░╚═════╝░╚══════╝
    """)
    print("||=================================================||")
    print("|| raven = runs ravenstorm program                 ||")
    print("|| msf = msfconsole                                ||")
    print("|| ssh = connect to server using secure shell      ||")
    print("|| back = go back                                  ||")
    print("|| quit = quit/exits program                       ||")
    print("||=================================================||\n")
    hm = input(inp)
    if hm == "raven" or hm == "Raven":
        print("""
    ██████╗░░█████╗░██╗░░░██╗███████╗███╗░░██╗  ░██████╗████████╗░█████╗░██████╗░███╗░░░███╗
    ██╔══██╗██╔══██╗██║░░░██║██╔════╝████╗░██║  ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗████╗░████║
    ██████╔╝███████║╚██╗░██╔╝█████╗░░██╔██╗██║  ╚█████╗░░░░██║░░░██║░░██║██████╔╝██╔████╔██║
    ██╔══██╗██╔══██║░╚████╔╝░██╔══╝░░██║╚████║  ░╚═══██╗░░░██║░░░██║░░██║██╔══██╗██║╚██╔╝██║
    ██║░░██║██║░░██║░░╚██╔╝░░███████╗██║░╚███║  ██████╔╝░░░██║░░░╚█████╔╝██║░░██║██║░╚═╝░██║
    ╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚══╝  ╚═════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝
        """)
        time.sleep(1)
        os.system("./Raven-Storm")
    elif hm == "msf" or hm == "Msf" or hm == "MSF" or hm =="msfconsole" or hm =="Msfconsole" or hm =="MSFconsole":
        os.system("msfconsole")
    elif hm == "ssh" or hm == "SSH":
        ssh()
    elif hm == "back" or hm == "Back":
        interface()
    elif hm == "quit" or hm == "Quit":
        sys.exit()
    else:
        print("\nanswer not recognized\n")
        time.sleep(1)
        hacker_mode()
def ssh():
    os.system("clear")
    print("""
    ░██████╗███████╗░█████╗░██╗░░░██╗██████╗░███████╗  ░██████╗██╗░░██╗███████╗██╗░░░░░██╗░░░░░
    ██╔════╝██╔════╝██╔══██╗██║░░░██║██╔══██╗██╔════╝  ██╔════╝██║░░██║██╔════╝██║░░░░░██║░░░░░
    ╚█████╗░█████╗░░██║░░╚═╝██║░░░██║██████╔╝█████╗░░  ╚█████╗░███████║█████╗░░██║░░░░░██║░░░░░
    ░╚═══██╗██╔══╝░░██║░░██╗██║░░░██║██╔══██╗██╔══╝░░  ░╚═══██╗██╔══██║██╔══╝░░██║░░░░░██║░░░░░
    ██████╔╝███████╗╚█████╔╝╚██████╔╝██║░░██║███████╗  ██████╔╝██║░░██║███████╗███████╗███████╗
    ╚═════╝░╚══════╝░╚════╝░░╚═════╝░╚═╝░░╚═╝╚══════╝  ╚═════╝░╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝
    """)
    print("what is the host ip?")
    ipo = input(inp)
    print("what is the password?")
    sshpassw = input(inp)
    print("what is the username(leave blank if you dont have a user)?")
    userss = input(inp)
    if userss == "":
        os.system("sshpass -p '" + sshpassw + "' ssh " + ipo)
    else:
        os.system("sshpass -p '" + sshpassw + "' ssh " + userss +"@"+ ipo)

while status != "q": #while status is not equal to q or "quit"
    os.system("clear")
    print("""
    ██╗░░░░░░█████╗░░██████╗░██╗███╗░░██╗
    ██║░░░░░██╔══██╗██╔════╝░██║████╗░██║
    ██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║
    ██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║
    ███████╗╚█████╔╝╚██████╔╝██║██║░╚███║
    ╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝
    """)
    status = input("press ^c to quit\nare you a registered user? y/n press q to quit: ")

    if status == "n" : #create new login
        createlogin = input("Create login name: ")

        if createlogin in users: #check if login name exist in the dictionary
            print (Fore.RED + "\nLogin name alredy exsist!\n")
            print(Style.RESET_ALL)
            sys.exit()
        else:
            createpassw = getpass.getpass("Create password: ")
            users[createlogin] = createpassw #add login and password
            print("\nUser created!\n")
            interface()
            stuff = contents.split('}',1)
            newlist = ', "' + createlogin + '" : "' + createpassw + '"}'
            print(newlist)
            f = open("login_info.txt","w")
            for element in stuff:
                f.write(element)
            f.write(newlist)
            f.close()
            login = createlogin
            
    elif status == "y": #login the user
        login = input("Enter username: ")

        if login in users:
            passw = getpass.getpass("Enter password: ")

            if passw == users[login]: #login matches password
                print ("\nlogin successful!\n")
                time.sleep(1)
                interface()
            else:
                print(Fore.RED + "\nYou entered the wrong password!\n")
                print(Style.RESET_ALL)
                sys.exit()
        else:
            print(Fore.RED + "\nUser dosent exist!\n")
            print(Style.RESET_ALL)
            sys.exit()
    else:
        print("\nanswer not recognized\ntry again\n")
        time.sleep(1)
        os.system("clear")
