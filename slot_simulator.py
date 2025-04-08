
import random

symbols = {
    "7": "7️⃣",
    "Grapes": "🍇",
    "Watermelon": "🍉",
    "Bell": "🔔",
    "Plum": "🍑",
    "Orange": "🍊",
    "Lemon": "🍋",
    "Cherry": "🍒",
    "$": "💰",
    "★": "⭐",
    "Wild": "👑"
}

# Reel strip for each reel
reel_strip = ["7"]*2 + ["Grapes"]*4 + ["Watermelon"]*4 + ["Bell"]*3 + ["Plum"]*3 +              ["Orange"]*3 + ["Lemon"]*3 + ["Cherry"]*3 + ["$"]*2 + ["★"]*2 + ["Wild"]*2

# Reels: only put Wild on reels 2, 3, 4
reels = []
for i in range(5):
    strip = reel_strip[:]
    if i not in [1, 2, 3]:  # Wilds only on reels 2, 3, 4
        strip = [s for s in strip if s != "Wild"]
    reels.append(strip)

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
    "7": {2: 5, 3: 25, 4: 125, 5: 2500},
    "Grapes": {3: 20, 4: 60, 5: 350},
    "Watermelon": {3: 20, 4: 60, 5: 350},
    "Bell": {3: 10, 4: 20, 5: 100},
    "Plum": {3: 5, 4: 15, 5: 75},
    "Orange": {3: 5, 4: 15, 5: 75},
    "Lemon": {3: 5, 4: 15, 5: 75},
    "Cherry": {3: 5, 4: 15, 5: 75},
    "$": {3: 25, 4: 100, 5: 500},
    "★": {3: 100}
}

def spin_reels():
    return [[random.choice(reel) for _ in range(3)] for reel in reels]

def evaluate_spin(grid, bet):
    total_win = 0
    scatter_count = {"$": 0, "★": 0}

    # Count scatter symbols
    for idx, col in enumerate(grid):
        for row_idx, s in enumerate(col):
            if s in scatter_count:
                if s == "★" and idx in [0, 2, 4]:  # Star scatter only valid on 1, 3, 5
                    scatter_count[s] += 1
                elif s == "$":
                    scatter_count[s] += 1

    # Scatter payouts
    for scatter, count in scatter_count.items():
        payout = paytable.get(scatter, {}).get(count, 0)
        total_win += payout * bet / 5  # scale by bet

    # Line wins
    for line in paylines:
        line_syms = [grid[i][line[i]] for i in range(5)]
        base = line_syms[0]
        count = 1
        for s in line_syms[1:]:
            if s == base or s == "Wild":
                count += 1
            else:
                break
        if base in paytable and count >= 2:
            payout = paytable[base].get(count, 0)
            total_win += payout * bet / 5

    return round(total_win, 2), scatter_count

def display_grid(grid):
    return "\n".join(" ".join(symbols[s] for s in row) for row in zip(*grid))

def simulate(spins, bet):
    total_win = 0
    total_bet = spins * bet
    wins = 0
    scatters_dollar = 0
    scatters_star = 0
    max_single_win = 0
    for _ in range(spins):
        grid = spin_reels()
        win, scatters = evaluate_spin(grid, bet)
        total_win += win
        if win > 0:
            wins += 1
        max_single_win = max(max_single_win, win)
        scatters_dollar += scatters["$"]
        scatters_star += scatters["★"]
    rtp = total_win / total_bet
    hit_rate = wins / spins
    avg_win_per_hit = total_win / wins if wins else 0
    avg_spins_per_hit = spins / wins if wins else 0
    return {
        "spins": spins,
        "bet": bet,
        "total_bet": total_bet,
        "total_win": total_win,
        "net": total_win - total_bet,
        "rtp": rtp,
        "hit_rate": hit_rate,
        "scatters_dollar": scatters_dollar,
        "scatters_star": scatters_star,
        "max_single_win": max_single_win,
        "avg_win_per_hit": avg_win_per_hit,
        "avg_spins_per_hit": avg_spins_per_hit
    }
