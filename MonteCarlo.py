# from random import randint
import random

# MonteCarlo.py
# This program uses a Monte Carlo approach to estimate the probability of winning the dice game "Approach" with different
# "hold" values.
# Recall that approach works like this:
# Both players agree on a limit n.
# Player 1 rolls first. They go until they either exceed n or hold.
# Then player 2 rolls. They go until they either exceed n or beat player 1's score.
# The player who is closest to n without going over wins.
# Note:
# We can reduce this to the problem of player 1 choosing the best value at which to hold.
# This is called a policy; once we know the best number to hold at, we can act optimally.

# To estimate the best number to hold at, we'll try to estimate the probability of winning
# for each possible hold value between n-5 and n.
# Once we have this, we will know which hold value to use for our strategy.

# This function should try each possible hold value 1000000 times. For each time, play a random
# game. If Player 1 wins, increment the appropriate value in the win_table dictionary.

# n is the limit.

def monte_carlo_approach(n) :
    win_table = {}
    for i in range(n-5,n+1) :
        win_table[i] = 0
    
    # updated_win_table = {}

    for i in range(1000000) :
        ## you do this part. My solution is under 20 lines of code. Yours can be longer, but if it's getting
        ## really big, take a step back and rethink.
        
        ## player 1 plays
        for item in win_table.keys():
            hold = item
            s_player1 = 0
            while(s_player1<hold):
                die = random.randint(1,6)
                s_player1+=die
            
            if(s_player1>n):
                continue
            elif(s_player1>=hold and s_player1<=n):
                s_player2=0
                while(s_player2<=s_player1):
                    die = random.randint(1,6)
                    s_player2+=die
                
                if(s_player2>s_player1 and s_player2<=n):
                    continue
                elif(s_player2>n):
                    win_table[hold] += 1

    # for item, value in updated_win_table.items():
    #     win_table[item] = value

    for item in win_table.keys() :
        print("%d: %f" % (item, win_table[item]/1000000))

monte_carlo_approach(10)
