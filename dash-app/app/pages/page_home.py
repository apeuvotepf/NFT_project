import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output
from app.app_test import app

import sys
sys.path.append('../')
sys.path.append('../../')

pg = 'Duck Project - NFT'



def layout():
    return html.Div([dbc.Row(dbc.Col(dbc.Card(children=[
        dbc.CardHeader(html.H4(f'{pg.title()} ', style={'textAlign': 'center'})),

        dbc.Row([
            # dbc.Toast(
            #     [

            #         dbc.Label("Enter the movie you want to search for :"),
            #         dbc.Input(placeholder="Enter a movie here", type="text", id="movie_to_search_for"),
            # ],
            #     header="Movie search : ",
            #     header_class_name="bi bi-search",
            #     is_open=True,
            #     dismissable=False,
            # ),
            

            dbc.Row([

                html.H5('Our collection of NFT regroups 3 types of ducks :',
                    style={"margin":"30px"}
                    ),
                ],
            ),

            dbc.Row(
                dbc.ListGroup(
                    [
                    dbc.ListGroupItem(
                            [
                            html.Div(
                                [
                                    html.P("A lot of rare ducks", className="mb-1"),
                                    html.Small("Damn!", className="text-danger"),
                                ],
                                className="d-flex w-100 justify-content-between",
                            ),
                            html.Small("These ducks have been generated with an IA, they have mysterious features...", className="text-muted"),
                        ],
                    ),
                    dbc.ListGroupItem(
                        [
                            html.Div(
                                [
                                    html.P("Some super rare ducks", className="mb-1"),
                                    html.Small("WOOOH!", className="text-danger"),
                                ],
                                className="d-flex w-100 justify-content-between",
                            ),
                            html.Small("These ducks have been designed by a genius of drawing who goes by the name of BOB.\nThese ducks evolved in goose.", className="text-muted"),
                        ],
                    ),
                    dbc.ListGroupItem(
                        [
                        html.Div(
                            [
                                html.P("A few legendary ducks", className="mb-1"),
                                html.Small("No fucking way!", className="text-danger"),
                            ],
                            className="d-flex w-100 justify-content-between",
                        ),
                        html.Small("Low are your chances of getting these ducks but high will be your fame if you success.", className="text-muted"),
                    ],
                    ),
                    ],
                    flush=True,
                ),
                style={"margin":"30px"},
            ),

            dbc.Row(
                dbc.Toast(
                    [
                    dbc.Col(
                        html.P(["Nothing easier !",
                                html.Br(), 
                                "You just need to send at least 0.005ETH to the address of our smart contract and you will receive on your wallet a duck chosen randomly from our collection.",
                                html.Br(),
                                "Here is the address of the smart contract : "
                                ], 
                                className="mb-0"),
                        # width=3,
                    ),
                    
                    
                    # dbc.Col(
                    #     dbc.Card(
                    #     [
                    #         dbc.CardImg(src="https://media.istockphoto.com/id/941339880/fr/vectoriel/bo%C3%AEte-en-carton-magique-avec-la-lumi%C3%A8re.jpg?s=612x612&w=0&k=20&c=d5wknkBpoydpbwWiu75FOjiZW7Zt-C_ClLStYjINfmE=", 
                    #         top=True,
                    #         style={"width":"200px", "height":"200px"}
                    #         ),
                    #         dbc.CardBody(
                    #             [
                    #                 html.H5("Get your own duck", className="card-title"),
                    #                 dbc.Button("Open Mystery Box", id="open_mystery_box", outline=True, color="primary", className="me-1", style={"width":"30%"}),
                    #             ]
                    #         ),
                    #     ],
                    #     # style={"width": "100%"},
                    # ),
                    # width=4,
                    # )
                    ],
                     header="How to get your own duck ?",
                     style={"width":"100%"}
                ),
            # style={"display":"flex", "justify-content":"space-around", "width":"100%"}         
            ),
                


            dbc.Row(
                html.H5('Here are some examples of our collection :'),
                style={"margin":"30px"}
            ),

            dbc.Row(
                [
                dbc.Card(
                [
                    dbc.CardImg(src="https://gateway.pinata.cloud/ipfs/QmTue2nCLt7EkERnqAe6hFeN5JNj6AatMuphFt74K6NeUT/33.png", 
                    top=True,
                    style={"width":"200px", "height":"200px"}
                    ),
                    dbc.CardBody(
                        [
                            html.H4("Burglar duck", className="card-title"),
                            html.P(
                                "Rare",
                                className="card-text",
                            ),
                        ]
                    ),
                ],
                style={"width": "250px"},
            ),

            dbc.Card(
                [
                    dbc.CardImg(src="https://gateway.pinata.cloud/ipfs/QmTue2nCLt7EkERnqAe6hFeN5JNj6AatMuphFt74K6NeUT/58.png", 
                    top=True,
                    style={"width":"200px", "height":"200px"}
                    ),
                    dbc.CardBody(
                        [
                            html.H4("Oiegre", className="card-title"),
                            html.P(
                                "Super Rare",
                                className="card-text",
                            ),
                        ]
                    ),
                ],
                style={"width": "250px"},
            ),

            dbc.Card(
                [
                    dbc.CardImg(src="https://gateway.pinata.cloud/ipfs/QmTue2nCLt7EkERnqAe6hFeN5JNj6AatMuphFt74K6NeUT/54.png", 
                    top=True,
                    style={"width":"200px", "height":"200px"}
                    ),
                    dbc.CardBody(
                        [
                            html.H4("Quackamole", className="card-title"),
                            html.P(
                                "Legendary",
                                className="card-text",
                            ),
                        ]
                    ),
                ],
                style={"width": "250px"},
            ),
        ],
        style={"display":"flex", "justify-content":"space-around", "width":"100%"}
        ),

        dbc.Row(
            html.P(['You can check the full collection here : ',
                dcc.Link('Full collection', href='https://testnets.opensea.io/collection/ticket-event-dnsr90hwfp', target="_blank")
                ])
        )
            
        ],style={'margin': '2%'}
        ),

        


    ]),
        width={"size": 10, "offset": 1}))])


# @app.callback(
#     Output("movies", "children"),
#     Input('movie_to_search_for', 'value'),
# )
# def select_date_range(movie_to_search_for):

    
#     card_list = []
    
#     if movie_to_search_for is not None:
#         movies = MovieFacade.get_movies(movie_to_search_for)
#         print(movies)
#         for movie in movies:
#             # assert isinstance(movie, Movie)
#             card = dbc.Card(
#                     [
#                         dbc.CardImg(src=movie.poster_url, top=True),
#                         dbc.CardBody(
#                             [
#                                 html.H4(movie.title, className="card-title"),
#                                 html.P(
#                                     movie.description + "\n" + movie.mean_rate + "/100",
#                                     className="card-text",
#                                 ),
#                             ]
#                         ),
#                     ],
#                     style={"width": "18rem"},
#                 )
#             card_list.append(card)
#         return card_list
    
#     else:
#         return []