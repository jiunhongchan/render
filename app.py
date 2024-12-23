import logging
import Pages
from WebEngine import dash_engine

pages = []
pages.append(Pages.HomePage())

eng = dash_engine.DashEngine('Dashboard', 'Dashboard', pages, logging_level= logging.ERROR)
server = eng.server