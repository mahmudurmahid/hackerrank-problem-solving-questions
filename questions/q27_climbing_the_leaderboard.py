def climbing_leaderboard(ranked, player):
    # ranked_scores = dict(sorted(enumerate(ranked), key=lambda x: x[1], reverse=True))

    # player_rankings = []

    # for i in range(len(player)):
    #     for j in range(len(ranked_scores)):
    #         if player[i] > ranked_scores[j]:
    #             player_rankings.append([player[i], ranked_scores[key]])

    # return player_rankings

    # Step 1: Remove duplicates and sort descending
    unique_ranks = sorted(set(ranked), reverse=True)

    player_rankings = []
    index = len(unique_ranks) - 1  # Start from the bottom of the leaderboard

    # Step 2: For each player's score
    for score in player:
        # Move up the leaderboard while player score >= leaderboard score
        while index >= 0 and score >= unique_ranks[index]:
            index -= 1
        # Rank is index + 2 (since index is 0-based and we passed one higher)
        player_rankings.append(index + 2)

    return player_rankings

ranked = [100, 100, 50, 40, 40, 20, 10]
player = [5, 25, 50, 120]
result = climbing_leaderboard(ranked, player)
print(result)