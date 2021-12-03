import seaborn as sns
import pandas as pd
import numpy as np

from matplotlib import pyplot as plt


def draw_monthly(data):
    plt.figure(figsize=(7,7),dpi=100)
    sns_monthly = sns.histplot(data=data,multiple="stack",stat="density",legend=True,binwidth=0.1)
    sns_monthly.legend(handles=sns_monthly.legend_.legendHandles, labels=[t.get_text() for t in sns_monthly.legend_.texts],
                        title=sns_monthly.legend_.get_title().get_text(),
                        fontsize=14)
    plt.title("Average windspeed over monthly intervals", fontsize=18)
    plt.xlabel("Windspeed (m/s)",fontsize=16)
    plt.ylabel("Density", fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    sns_monthly.figure.savefig("monthly.png")
    return


def draw_hourly(data):
    plt.figure(figsize=(7,7),dpi=100)
    sns_hour = sns.histplot(data=data, 
                            multiple="stack",
                            stat="density",
                            binwidth=0.5)
    sns_hour.legend(handles=sns_hour.legend_.legendHandles, labels=[t.get_text() for t in sns_hour.legend_.texts],
                        title=sns_hour.legend_.get_title().get_text(),
                        fontsize=14)
    plt.title("Average windspeed over hourly intervals", fontsize=18)
    plt.xlabel("Windspeed (m/s)",fontsize=16)
    plt.ylabel("Density", fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    sns_hour.figure.savefig("hourly.png")
    return


def draw_val(data):
    wp_s = sorted(list(data.wp))
    mean_E_s = sorted(list(data.mean_E))
    mean_E_s10 = sorted(list(data.mean_E[:10]))

    wp_E_s = sorted(list(data.wp[:10]))
    prc_95_E_sorted = sorted(list(data.prc_95_E[:10]))
    prc_5_E_sorted = sorted(list(data.prc_5_E[:10]))

    fig, ax = plt.subplots()
    sns.lineplot(x=wp_s, y=mean_E_s)
    ax.fill_between(wp_E_s, prc_5_E_sorted, prc_95_E_sorted, alpha=0.3)
    #sns.lineplot(x=wp_E_s, y=prc_95_E_sorted, label="95%")
    #sns.lineplot(x=wp_E_s, y=prc_5_E_sorted, label="5%")

    plt.scatter(x=data.wp, y=data.energy, c="black", marker="x", s=10)

    plt.title("")
    plt.xlabel("Windspeed (m/s)",fontsize=16)
    plt.ylabel("Normalised energy [MW/GW]", fontsize=16)
    #plt.legend(fontsize=14)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.savefig("regressio.png")
    return


def draw_histogram(data):
    plt.figure()
    sns.histplot(data=data["theta"], stat="density")
    
    plt.xlabel(r"$\theta$", fontsize=16)
    plt.ylabel("Density", fontsize=16)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.savefig("histogrammi.png")
    pass


def main():
    sns.set_style("darkgrid")

    maar = pd.read_csv("maarianhamina.csv")
    kok  = pd.read_csv("kokkola.csv")
    kemi = pd.read_csv("kemijarvi.csv")
    datacsv = pd.read_csv("data_csv_23112021.csv")

    hourly = pd.DataFrame()
    hourly["Maarianhamina"] = maar["Tuulen nopeus (m/s)"]
    hourly["Kokkola"] = kok["Tuulen nopeus (m/s)"]
    hourly["Kemijärvi"] = kemi["Tuulen nopeus (m/s)"]
    #hourly["Avg"] = data.mean(axis=1)

    monthly = pd.DataFrame()
    monthly["Maarianhamina"] = datacsv["keskinopeus_maar"]
    monthly["Kokkola"] = datacsv["keskinopeus_kok"]
    monthly["Kemijärvi"] = datacsv["keskinopeus_kemi"]
    #monthly["Avg"] = data.mean(axis=1)


    val_data = pd.read_csv("python_data.csv")

    #draw_hourly(hourly)
    #draw_monthly(monthly)
    draw_val(val_data)
    draw_histogram(val_data)

    return


if __name__=="__main__":
    main()