from dash import Output, Input
from app.app_test import app
from app.pages import page_home

@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    """
    Route l'utilisateur en fonction de l'URL
    """
    if pathname == "/":
        return page_home.layout()
    else:
        return "404"


if __name__ == '__main__':
    app.run_server(debug=True, port=5000, host="localhost")
