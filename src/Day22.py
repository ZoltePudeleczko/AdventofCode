from collections import deque


def play_game(player1Deck, player2Deck):
    while len(player1Deck) > 0 and len(player2Deck) > 0:
        player1Card = player1Deck.popleft()
        player2Card = player2Deck.popleft()

        if player1Card > player2Card:
            player1Deck.append(player1Card)
            player1Deck.append(player2Card)
        else:
            player2Deck.append(player2Card)
            player2Deck.append(player1Card)

    if len(player1Deck) == 0:
        return player2Deck
    else:
        return player1Deck


def play_game_recursive(player1Deck, player2Deck, player1History=[], player2History=[]):
    while len(player1Deck) > 0 and len(player2Deck) > 0:
        if player1Deck in player1History and player2Deck in player2History:
            return (1, player1Deck)
        player1History.append(player1Deck.copy())
        player2History.append(player2Deck.copy())

        player1Card = player1Deck.popleft()
        player2Card = player2Deck.popleft()

        if len(player1Deck) >= player1Card and len(player2Deck) >= player2Card:
            newPlayer1Deck = []
            for i in range(player1Card):
                newPlayer1Deck.append(player1Deck[i])
            newPlayer2Deck = []
            for i in range(player2Card):
                newPlayer2Deck.append(player2Deck[i])

            if play_game_recursive(deque(newPlayer1Deck), deque(newPlayer2Deck), [], [])[0] == 1:
                player1Deck.append(player1Card)
                player1Deck.append(player2Card)
            else:
                player2Deck.append(player2Card)
                player2Deck.append(player1Card)
        else:    
            if player1Card > player2Card:
                player1Deck.append(player1Card)
                player1Deck.append(player2Card)
            else:
                player2Deck.append(player2Card)
                player2Deck.append(player1Card)

    if len(player1Deck) == 0:
        return (2, player2Deck)
    else:
        return (1, player1Deck)


def score_calculate(deck):
    multiply = 1
    score = 0
    while len(deck) > 0:
        score += deck.pop() * multiply
        multiply += 1
    return score


with open('../inputs/day22.txt') as f:
    player1 = []
    player2 = []
    readingPlayer1 = False
    for line in f.readlines():
        line = line.strip()
        if line == 'Player 1:':
            readingPlayer1 = True
        elif line == 'Player 2:':
            readingPlayer1 = False
        elif line == '':
            continue
        else:
            if readingPlayer1:
                player1.append(int(line))
            else:
                player2.append(int(line))

print(f"22-1: {score_calculate(play_game(deque(player1), deque(player2)))}")
print(f"22-2: {score_calculate(play_game_recursive(deque(player1), deque(player2))[1])}")
