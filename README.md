# Montreal Weather Fetcher
Have you ever wished you could get Environment Canada's hourly forecasts for Montreal in a nice, simple csv file? Well, wish no more!

## Installation
1. Find a way to install Python 3.whatever
2. Make sure you add this installation's directory to your PATH, or better yet use [virtual environments](https://docs.python.org/3/tutorial/venv.html)
3. Clone or dowload this repo and navigate to it on command line
4. Install the dependencies with pip:
```bash
$ pip install -r requirements.txt
```
5. Profit !

## Usage
Make sure you can call your python installation from the command line by adding its installation directory to your PATH variable. You can now use ```python``` on the command line !

to run this awesome tool, just navigate to where you downloaded or clone this repo and do
```bash
$ python fetchweather.py
```

By default the output will be saved to your current directory. Pass the ```-o``` flag to specify another location
```bash
$ python fetchweather.py -o "C:\Users\myname\Documents\forecasts\"
```

Have fun!
