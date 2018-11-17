import requests
import xml.etree.ElementTree as ET
import pandas as pd
import argparse


endpoint = r'http://dd.weather.gc.ca/citypage_weather/xml/QC/s0000635_f.xml'


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("output", help="Path of the CSV file you wish to create", default="MontrealTemps.csv")
    args = parser.parse_args()


    payload = requests.get(endpoint)
    tree = ET.fromstring(payload.text)
    hourlies = tree.find('hourlyForecastGroup').findall('hourlyForecast')

    times = []
    temps = []

    for forecast in hourlies:
        times.append(pd.to_datetime(forecast.attrib["dateTimeUTC"]))
        temps.append(int(forecast.find("temperature").text))

    res = pd.DataFrame({"Temperature":temps}, index=times)
    res.index.name = "Time"

    res.to_csv(args.output)

