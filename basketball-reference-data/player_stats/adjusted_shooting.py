## Still needs to be improved and fixed

def show(season):
    import pandas as pd
    url = f"https://www.basketball-reference.com/leagues/NBA_{season}_adj_shooting.html"
    site = pd.read_html(url)
    df = site[0]
    df = df.fillna("0")
    df = df.drop(['Rk'], axis=1)
    return df
