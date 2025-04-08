
import random

symbols = {
    "7": "7️⃣",
    "Bell": "🔔",
    "Watermelon": "🍉",
    "Grapes": "🍇",
    "Plum": "🍑",
    "Orange": "🍊",
    "Lemon": "🍋",
    "Cherry": "🍒",
    "Wild": "⭐",
    "Crown": "👑"
}

reel_strip = ["7"]*2 + ["Bell"]*3 + ["Watermelon"]*3 + ["Grapes"]*4 + ["Plum"]*4 +              ["Orange"]*4 + ["Lemon"]*4 + ["Cherry"]*5 + ["Wild"]*2 + ["Crown"]*1

reels = [reel_strip[:] for _ in range(5)]

paylines = [
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [2, 2, 2, 2, 2],
    [0, 1, 2, 1, 0],
    [2, 1, 0, 1, 2],
    [0, 1, 1, 1, 0],
    [2, 1, 1, 1, 2],
    [1, 2, 2, 2, 1],
    [1, 0, 0, 0, 1],
    [0, 1, 2, 2, 2]
]

paytable = {
    "7": {3: 50, 4: 200, 5: 1000},
    "Bell": {3: 20, 4: 50, 5: 200},
    "Watermelon": {3: 15, 4: 40, 5: 150},
    "Grapes": {3: 15, 4: 40, 5: 150},
    "Plum": {3: 10, 4: 30, 5: 100},
    "Orange": {3: 10, 4: 30, 5: 100},
    "Lemon": {3: 5, 4: 15, 5: 50},
    "Cherry": {3: 5, 4: 15, 5: 50},
    "Crown": {3: 20, 4: 100, 5: 500}
}

def spin_reels():
    return [[random.choice(reel) for _ in range(3)] for reel in reels]

def evaluate_spin(grid):
    total_win = 0
    scatter_count = sum(col.count("Crown") for col in grid)
    if scatter_count >= 3:
        total_win += paytable["Crown"].get(scatter_count, 0)
    for line in paylines:
        line_symbols = [grid[i][line[i]] for i in range(5)]
        first = line_symbols[0]
        count = 1
        for sym in line_symbols[1:]:
            if sym == first or sym == "Wild":
                count += 1
            else:
                break
        if first in paytable and count >= 3:
            total_win += paytable[first].get(count, 0)
    return total_win, scatter_count

def display_grid(grid):
    return "\n".join(" ".join(symbols[s] for s in row) for row in zip(*grid))

def simulate(spins=10000):
    total_win = 0
    total_bet = 5 * spins
    wins = 0
    scatters_hit = 0
    max_single_win = 0
    for _ in range(spins):
        grid = spin_reels()
        win, scatters = evaluate_spin(grid)
        if win > 0:
            wins += 1
        total_win += win
        scatters_hit += scatters
        max_single_win = max(max_single_win, win)
    rtp = total_win / total_bet
    hit_rate = wins / spins
    avg_win_per_hit = total_win / wins if wins > 0 else 0
    avg_spins_per_hit = spins / wins if wins > 0 else 0
    return {
        "spins": spins,
        "total_win": total_win,
        "total_bet": total_bet,
        "net": total_win - total_bet,
        "rtp": rtp,
        "hit_rate": hit_rate,
        "scatters_hit": scatters_hit,
        "max_single_win": max_single_win,
        "avg_win_per_hit": avg_win_per_hit,
        "avg_spins_per_hit": avg_spins_per_hit
    }
