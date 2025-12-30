import numpy as np
import matplotlib.pyplot as plt
import urllib.request
from PIL import Image
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.patches import RegularPolygon
from fetcher import getPlayerId, getPlayerShotCharts
from court import drawCourt

def add_player_photo(ax, player_id, x_pos=-210):
    url = f"https://ak-static.cms.nba.com/wp-content/uploads/headshots/nba/latest/260x190/{player_id}.png"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            img = Image.open(response).convert('RGBA') 
            
        imagebox = OffsetImage(img, zoom=0.4)
        ab = AnnotationBbox(imagebox, (x_pos, 360), frameon=False)
        ax.add_artist(ab)
    except Exception as e:
        print(f"Error photo ID {player_id}: {e}")

def draw_hybrid_hexbin(ax, df, grid_size=25):
    hb_count = ax.hexbin(df['LOC_X'], df['LOC_Y'], gridsize=grid_size, mincnt=1, alpha=0)
    hb_eff = ax.hexbin(df['LOC_X'], df['LOC_Y'], C=df['SHOT_MADE_FLAG'], 
                       reduce_C_function=np.mean, gridsize=grid_size, mincnt=1, alpha=0)
    
    offsets = hb_count.get_offsets()
    counts = hb_count.get_array()
    efficiencies = hb_eff.get_array()
    max_count = np.max(counts)
    cmap = plt.get_cmap('RdYlGn')

    for coll in ax.collections:
        coll.remove()

    for i in range(len(offsets)):
        x, y = offsets[i]
        scaling_factor = np.sqrt(counts[i] / max_count)
        size = (250 / grid_size) * 0.9 * scaling_factor
        
        poly = RegularPolygon((x, y), numVertices=6, radius=size, orientation=0,
                              facecolor=cmap(efficiencies[i]), edgecolor='#444444', lw=0.5)
        ax.add_patch(poly)
    
    return cmap

def compare_players(player1_name, player2_name, season='2025-26'):
    plt.style.use('dark_background')
    gris_fondo = '#333333'
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(22, 12), facecolor=gris_fondo)
    
    for ax, name in zip([ax1, ax2], [player1_name, player2_name]):
        ax.set_facecolor(gris_fondo)
        
        p_id = getPlayerId(name)
        if not p_id: continue
        
        df = getPlayerShotCharts(p_id, season=season)
        if df.empty: continue
            
        drawCourt(ax, color='#bbbbbb', lw=1.2)
        draw_hybrid_hexbin(ax, df)
        add_player_photo(ax, p_id)
        
        ax.set_xlim(-250, 250)
        ax.set_ylim(-52, 418)
        
        ax.set_title(f"{name.upper()}", fontsize=18, color='white', fontweight='bold', pad=10)
        ax.axis('off')

    fig.suptitle(f"NBA COMPARISON | SEASON {season}\nSize = Frequency | Color = Efficiency", 
                 fontsize=22, color='white', fontweight='bold', y=0.96)

    sm = plt.cm.ScalarMappable(cmap=plt.get_cmap('RdYlGn'), norm=plt.Normalize(vmin=0, vmax=1))
    cb_ax = fig.add_axes([0.93, 0.25, 0.015, 0.5])
    cb = fig.colorbar(sm, cax=cb_ax)
    cb.set_label('Efficiency (% Made)', color='white', size=14)
    cb.ax.set_yticklabels(['{:.0f}%'.format(x*100) for x in cb.get_ticks()], color='white')

    fig.text(0.1, 0.05, 'Data: nba.com | Visual: Omar Brizuela', color='#888888', fontsize=12)

    plt.tight_layout(rect=[0, 0.03, 0.92, 0.91])
    plt.show()

if __name__ == "__main__":
    compare_players("Stephen Curry", "devin booker")