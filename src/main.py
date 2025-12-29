import matplotlib.pyplot as plt
from fetcher import getPlayerId, getPlayerShotCharts
from court import drawCourt

def create_visual(player_name, season='2025-26'):
    id_player = getPlayerId(player_name)
    if not id_player:
        print("Jugador no encontrado")
        return

    df = getPlayerShotCharts(id_player, season=season)

    fig, ax = plt.subplots(figsize=(12, 11))
    
    drawCourt(ax, color='black', lw=2)

    made = df[df['SHOT_MADE_FLAG'] == 1]
    missed = df[df['SHOT_MADE_FLAG'] == 0]

    ax.scatter(made['LOC_X'], made['LOC_Y'], c='green', s=25, alpha=0.6, label='Anotado')
    ax.scatter(missed['LOC_X'], missed['LOC_Y'], c='red', s=25, alpha=0.4, label='Fallado')

    ax.set_xlim(-250, 250)
    ax.set_ylim(-52, 418)
    ax.set_title(f"Shot Chart: {player_name} ({season})", fontsize=18)
    ax.axis('off')
    plt.legend(loc='upper right')
    
    plt.show()

if __name__ == "__main__":
    create_visual("Stephen Curry")