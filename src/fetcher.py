from nba_api.stats.static import players;
from nba_api.stats.endpoints import shotchartdetail

HEADERS = {
    'Host': 'stats.nba.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://stats.nba.com/',
    'Connection': 'keep-alive'
}

def getPlayerId(fullName):
    playerDict = players.get_players()
    
    player = [p for p in playerDict if p['full_name'].lower() == fullName.lower()]
    
    if player:
        return player[0]['id']
    else:
        return None

def getPlayerShotCharts(player_id, season='2025-26'):
    shotData = shotchartdetail.ShotChartDetail(
        team_id=0,
        player_id=player_id,
        context_measure_simple='FGA',
        season_nullable=season,
        season_type_all_star='Regular Season',
        headers=HEADERS
    )
    
    df = shotData.get_data_frames()[0]
    return df






if __name__ == "__main__":
    nombre = "Stephen Curry"
    playerId = getPlayerId(nombre)
    if playerId:
        (f"Obteniendo datos para {nombre}...")
        df_tiros = getPlayerShotCharts(playerId)
        print(df_tiros[['PLAYER_NAME', 'LOC_X', 'LOC_Y', 'EVENT_TYPE', 'SHOT_MADE_FLAG']].head())
        print(f"\nTotal de tiros encontrados: {len(df_tiros)}")
    else:
        print("Jugador no encontrado.")