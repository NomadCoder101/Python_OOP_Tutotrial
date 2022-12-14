import random


suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two', 'Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Qween','King','Ace')
values = {'Two':2, 'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10, 'Jack':11,'Qween':12,'King':13,'Ace':14}


class Card:
    def __init__(self,suit,rank):
        self.suit =suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " +  self.suit


'''
two_heart = Card('Hearts','Two')

print(two_heart.suit)
print(two_heart.rank)
print(two_heart.value)
#print(values[two_heart.rank])

three_of_clubs = Card('Clubs','Three')

print(three_of_clubs.rank)
print(three_of_clubs.suit)
print(three_of_clubs.value)

print(two_heart.value < three_of_clubs.value)
print(two_heart.value == three_of_clubs.value)
print(two_heart.value > three_of_clubs.value)

'''

class Deck():
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    def shuffle(self):

        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()



class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards) 
        else:
            self.all_cards.append(new_cards)
        

    def __str__(self):
        return f" Plaeyer {self.name} has {len(self.all_cards)} cards."






'''

# testing code 
new_deck = Deck()
#print(new_deck.all_cards)
#first_card = new_deck.all_cards[0]
#print(first_card)
#bottom_card = new_deck.all_cards[-1]
#print(bottom_card)

#for card_objects in new_deck.all_cards:
   # print(card_objects)
new_deck.shuffle()
first_card = new_deck.all_cards[0]
print(first_card)
bottom_card = new_deck.all_cards[-1]
print(bottom_card)

my_card = new_deck.deal_one()
print(my_card)
print(len(new_deck.all_cards))


new_player = Player('Jose')
print(new_player)
new_player.add_cards(my_card)
print(new_player)

new_player.add_cards([my_card,my_card,my_card])
print(new_player)

new_player.remove_one()
print(new_player)

'''

# Game Logic

# Game setup

player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()

for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

#print(player_one.all_cards[0])
#print(len(player_one.all_cards))
#print(player_two.all_cards[0])
#print(len(player_two.all_cards))

game_on = True

round_num = 0 
# while game on
while game_on:
    round_num +=1
    print(f'Round {round_num}')

    if len(player_one.all_cards)==0:
        print('Player one out of cards ! Player two wins')
        game_on = False
        break
    if len(player_two.all_cards)==0:
        print('Player two out of cards ! Player one wins')
        game_on = False
        break
    # Start new round

    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())


    # While at_war
    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value :
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False
        
        elif player_one_cards[-1].value < player_two_cards[-1].value :
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False
        
        else:
            print('War !')

            if len(player_one.all_cards) < 5:
                print('Player one Unable to Declare war ')
                print('Player  Two Wins')
                game_on = False
                break
            if len(player_two.all_cards) < 5:
                print('Player two Unable to Declare war ')
                print('Player  one Wins')
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())


            
        





    

