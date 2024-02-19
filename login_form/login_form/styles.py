# general stylesheets for components

general_stylesheet = {
    "width": ["100%", "100%", "70%", "50%", "35%"],
    "padding": ["0em 2em"],
    "transition": "all 550ms ease",
    "display": "flex",
    "justify_content": "center",
    "align_items": "start",
}

input_stylesheet = {
    **general_stylesheet,
}

button_stylesheet = {
    **general_stylesheet,
    "height": "2em",
}

auth_pages_stylesheet = {
    "width": "100%",
    "height": "100vh",
    "display": "flex",
    "align_items": "center",
}
