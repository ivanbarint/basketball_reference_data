def show(season):
    import pandas as pd
    url = f"https://www.basketball-reference.com/leagues/NBA_{season}_play-by-play.html"
    site = pd.read_html(url)
    df = site[0]
    df = df.fillna("0")
    return df