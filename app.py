import sys
import os
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(f'parent dir {parent_dir}')
sys.path.insert(0, parent_dir)

import logging
import Pages
from WebEngine import dash_engine
import os 

parent_dir = os.path.dirname(os.getcwd())

pages = []
pages.append(Pages.HomePage())

eng = dash_engine.DashEngine('Dashboard', 'Dashboard', pages, logging_level= logging.ERROR)
server = eng.server