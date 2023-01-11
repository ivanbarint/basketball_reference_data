def show(season):    
    import pandas as pd
    import datetime

    url = f"https://www.basketball-reference.com/leagues/NBA_{season}_standings.html"
    site = pd.read_html(url)
    df = site[0]

    current_year = datetime.date.today().year
    current_month = 11
    current_season = False

    if season == current_year:
        current_season = True
    elif season - current_year == -1 and current_month > 10:
        current_season = True

    if current_season == True:
        df = df.rename(columns={"Eastern Conference": "Team"})
        
        team_names = []
        for i, row in df.iterrows():
            splitted = row['Team'].split('\xa0')
            team_name = splitted[0]
            team_names.append(team_name)
        for i in range(len(team_names)):
            df['Team'][i] = team_names[i]
            
    if season >= 2016:
        df = df.rename(columns={"Eastern Conference": "Team"})
        team_names = []

        for i, row in new_df.iterrows():
            if row['Team'][-1:] == "*":
                team_names.append(row['Team'][:-1])
            else:
                team_names.append(row['Team'])
        for i in range(len(team_names)):
            df['Team'][i] = team_names[i]
                
    return df