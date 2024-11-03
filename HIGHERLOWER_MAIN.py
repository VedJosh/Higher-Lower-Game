from HIGHERLOWER_ART import logo,vs, game_over
from HIGHERLOWER_DATA import data
from random import choice
import time

def higherlower():
    print(logo)
    game_end=False
    score=0
    data_last=choice(data)
    while not game_end:
        data1=data_last
        data.remove(data1)
        data2=choice(data)
        
        name1=data1['name']
        description1=data1['description']
        countryname1=data1['country']
        follower_count1=data1['follower_count']
        
        name2=data2['name']
        description2=data2['description']
        countryname2=data2['country']
        follower_count2=data2['follower_count']

        if follower_count1>follower_count2:
            answer='A'
        else:
            answer='B'
        
        print(f"Compare A: {name1},a {description1}, from {countryname1}.")
        print(vs)
        print(f"Against B: {name2}, a {description2}, from {countryname2}.")
        guess=input("Who has more followers? Type 'A' or 'B': ").upper()

        if guess==answer:
            score+=1
            print(f"You're right! Current score: {score}.")
            data_last=data2
        else:
            print(f"Sorry, that's wrong. Final score: {score}.")
            game_end=True
            print(game_over)
            time.sleep(5)
higherlower()
