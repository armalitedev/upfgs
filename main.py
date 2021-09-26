import os
import sys
from web3 import Web3
from time import sleep
import random
import json


clear = lambda: os.system('clear')
clear()
#clears the terminal ^^

def check():
  print("Looking for config.json file...")
  try:
    with open("config.json") as conf:
      data = json.load(conf)
    print("Found config file.")
    web3 = Web3(Web3.HTTPProvider(data['web3keys']))
    print("Connecting to Web3 API...")
    if web3.isConnected()==True:
      print("Connection established.")
      print(" ")
      print("Skipped setup.")
      print("Entering casino...")
      sys.exit()
    else:
      print("Error: Invalid Web3 API key.")
      sys.exit()
  except FileNotFoundError:
    global webkey
    print("Not found.")
    webkey=input("Enter your Web3 API key...\n")
    web3 = Web3(Web3.HTTPProvider(webkey))
    print("Connecting to Web3 API...")
    if web3.isConnected()==True:
      print("Connection established.")
      sleep(1.6)
      clear()
      confexist=True
    else:
      print("Error: Invalid Web3 key.")
      sys.exit()
#checks for a config.json file and ensures a connection with web3
      
check()

def printer():
  print("  ")
  sleep(0.4)
  print("                           __           ")
  sleep(0.4)
  print("              _   _ _ __  / _| __ _ ___ ")
  sleep(0.4)
  print("             | | | | '_ \| |_ / _` / __|   ⇆ https://github.com/armalitedev/upfgs")
  sleep(0.4)
  print('             | |_| | |_) |  _| (_| \__ \ ')
  sleep(0.4)
  print("              \__,_| .__/|_|  \__, |___/")
  sleep(0.4)
  print("                   |_|        |___/     ")
  sleep(0.4)
  print("      universal provability-fair gambling system")
  sleep(0.4)
  print("                    by armalitedev")
printer()
#shows banner

def priva(add):
  sleep(0.4)
  print(" ")
  priv=input("Enter your "+add+" private address:\n")
  choice1=input("Are you sure? [y/n/b] ")
  if choice1=="y":
    sleep(1)
    dict = {
      "privkey":priv,
      "network":ba,
      "web3keys":webkey
    }
    print("   ")
    open("config.json", 'w')
    with open("config.json", "w") as outfile:
      json.dump(dict, outfile)
    print("Preferences saved as config.json.")
    print("Entering casino...")
  elif choice1=="n":
    priva(ba)
  elif choice1=="b":
    net()
  else:
    print("Error: "+choice1+" not an option.")
    sys.exit()
#creates a config.json file and makes you enter your private key
    
def net():
  sleep(0.4)
  print(" ")
  global ba
  print("Select a blockchain network:")
  print("[1] Ethereum network")
  print("[2] BSC network")
  nets=input("[3] Ropsten testnet network\n")
  if nets=="1":
    ba="Ethereum network"
    priva(ba)
  elif nets=="2":
    ba="BSC network"
    priva(ba)
  elif nets=="3":
    ba="Ropsten testnet network"
    priva(ba)
  else:
    print("Error: "+nets+" not an option.")
    sys.exit()
#network selection
    
net()
