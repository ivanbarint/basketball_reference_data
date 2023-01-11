def show(season):
    import pandas as pd
    url = f"https://www.basketball-reference.com/leagues/NBA_{season}_advanced.html"
    site = pd.read_html(url)
    df = site[0]
    df = df.fillna("0")
    df = df.drop(['Rk'], axis=1)
    return df