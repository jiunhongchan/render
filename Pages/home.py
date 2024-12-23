from dash import html
from WebEngine import dash_page_base

class HomePage(dash_page_base.DashPageBase):
    
    def __init__(self):
        super().__init__('Home')

    def get_initial_layout(self, memory):
        content = html.H2('Welcome JH')
        return content
    
    def register_callback(self, app):
        return super().register_callback(app)