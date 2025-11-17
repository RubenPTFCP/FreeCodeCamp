from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player

def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    if len(opponent_history) == 0:
        return "P"

    most_frequent_play = {
        "R": opponent_history.count("R"),
        "P": opponent_history.count("P"),
        "S": opponent_history.count("S")
    }

    predicted = max(most_frequent_play, key=most_frequent_play.get)

    counter = {"R": "P", "P": "S", "S": "R"}

    return counter[predicted]

play(player, quincy, 1000)