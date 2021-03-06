import matplotlib.pyplot as plt 
import numpy as np

def ewp(port_rets):
    df = port_rets.copy()
    no_assets = len(df.columns)
    weights = [1/no_assets for i in range(no_assets)]
    df["EWP"] = df.dot(weights)
    return df


def ewp_contribs(port_rets):
    df = port_rets.copy()
    no_assets = len(df.columns)
    weights = [1/no_assets for i in range(no_assets)]
    equal_contrib = df.mul(weights, axis="columns")
    return equal_contrib


def _ewp_stats(port_rets):
    contrib = ewp(port_rets)
    stats = contrib.agg(["mean","std"]).T
    return stats


def ewp_expected(port_rets):
    stats = _ewp_stats(port_rets)
    stats.columns=['er','vol']
    stats['er'] = stats['er'] * 252
    stats['vol'] = stats['vol'] * np.sqrt(250)  #BUG: annualize the vol as well
    return stats


def display_ewp(port_rets):
    summary = ewp_expected(port_rets)
    summary.plot(kind="scatter",x="vol",y="er",figsize=(13,9), s=50, fontsize=15)
    for i in summary.index:
        plt.annotate(i, xy=(summary.loc[i, "vol"], summary.loc[i,"er"]), size=15)
    plt.xlabel("Annual Volatility(std)",fontsize=15)
    plt.ylabel("Expected Return")
    plt.title("Expected Return / Volatility")
    plt.show()


