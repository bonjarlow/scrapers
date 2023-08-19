import sys
import os
import configs
import requests
import json
from pathlib import Path
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm

p = Path(__file__).resolve().parents[5]
sys.path.insert(1, str(p))
from scrapers_library.data_portals.crimegraphics import crimegraphics_clery


save_dir = "./data/daily_bulletins/"
data = []

if not os.path.exists(save_dir):
    os.makedirs(save_dir)

crimegraphics_clery(configs, save_dir, configs_file=True)
