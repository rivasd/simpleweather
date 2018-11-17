import requests
import xml.etree.ElementTree as ET
import pandas as pd
import argparse
import datetime
import sys
import os.path
import errno


endpoint = r'http://dd.weather.gc.ca/citypage_weather/xml/QC/s0000635_f.xml'


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--output", "-o", help="Path to the directory where you wish to save the csv file. Will be created if does not exist. Do not include file name as it will be auto-generated", default=".")
    args = parser.parse_args()


    payload = requests.get(endpoint) # hit the weather service server and download the http response

    if not payload.status_code == 200:      # error handling ...
        print("Could not get a response from Canada weather service, HTTP code %s" % payload.status_code)
        sys.exit(1)


    tree = ET.fromstring(payload.text)      # Parse the XML response
    hourlies = tree.find('hourlyForecastGroup').findall('hourlyForecast') # find the elements representing the hourly forecasts

    times = []
    temps = []

    for forecast in hourlies:
        times.append(pd.to_datetime(forecast.attrib["dateTimeUTC"]))
        temps.append(int(forecast.find("temperature").text))

    res = pd.DataFrame({"Temperature":temps}, index=times)      # create a pandas DataFrame with our data
    res["TagName"] = "TIT-1000"                                 # add the required static column
    res.index.name = "Time"                                     # Give a pretty name to the index column
    res.index = res.index - pd.Timedelta(5, "h")                # Adjust UTC time to Montreal's time zone

    curr_time = datetime.datetime.now()                         
    out_name = "Previsions_Montreal_{}.csv".format(curr_time.strftime("%Y-%m-%d_%H:%M"))

    if not os.path.isdir(args.output):          # create the output folder if it does not exist

        try:
            os.makedirs(args.output)
        except OSError as e:
            if e.errno == errno.EACCES:
                print("You do not have write permissions to create the directory %s" % args.output)
                sys.exit(1)
            raise

    

    res.to_csv(os.path.join(args.output, out_name))     # Write in csv format

