import pandas as pd
import numpy as np

def combinations(n, k):
    x = np.math.factorial(n)
    y = np.math.factorial(k)
    z = np.math.factorial(n - k)
    return x / (y * z)

def formatting(x):
    return round(x * 100, 0)

def create_deck(symbols, suits):
    deck = pd.DataFrame()
    deck['symbol'] = symbols * 4
    deck['suit'] = np.sort(suits * 10)
    deck['value'] = [i for i in range(1, len(symbols) + 1)] * 4
    deck['card'] = deck['symbol'] + ' of ' + deck['suit']
    return deck[['card', 'symbol', 'suit', 'value']]

def shuffle(deck):
    return deck.sample(frac=1)

def set_cards_owners(deck, n_players, n_cards):
    owner = []
    for i in range(1, n_players + 1):
        owner = owner + [f'Player {i}'] * n_cards
    owner = owner + ['Turned']
    owner = owner + ['Deck'] * (len(deck) - len(owner))
    deck['owner'] = owner

def set_card_status(deck, n_players, n_cards):
    status = ['Playable'] * (n_cards * n_players) + ['Turned'] + ['Deck'] * (len(deck) - (n_cards * n_players + 1))
    deck['status'] = status

def set_wildcards(deck):
    turned_value = deck[deck['owner'] == 'Turned']['value'].iloc[0]
    if turned_value == 10:
        wildcard_value = 1
    else:
        wildcard_value = turned_value + 1
    deck['wildcard'] = deck['value'].map(lambda x: 1 if x == wildcard_value else 0)