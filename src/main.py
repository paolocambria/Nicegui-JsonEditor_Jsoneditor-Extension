from nicejeje.jsonschema_editor import JsonSchemaEditor

from nicegui import ui


ui.markdown('''
#### Demo
this is a demo
''')
ui.add_head_html("""  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
   <link href='https://use.fontawesome.com/releases/v5.6.1/css/all.css' rel="stylesheet" />
   <script src="https://cdnjs.cloudflare.com/ajax/libs/lz-string/1.4.4/lz-string.min.js"></script>
                 <style>
                 .je-ready [type=button], .je-ready [type=reset], .je-ready [type=submit], .je-ready button {
    -webkit-appearance: button;
    background-color: #2196f3 !important;
    background-image: none;
}
                 </style>
 """)


schema = {
    "type": "object",
            "properties": {
                "possible_colors": {
                    "type": "array",
                    "items": {
                        "type": "string"
                    }
                },
                "primary_color": {
                    "type": "string"
                }
            }
}

settings = {
    "iconlib": "fontawesome5",
    "object_layout": "normal",
    "show_errors": "interaction",
    "theme": "bootstrap5",
    "schema": schema
}

with ui.card():
    schema1 = JsonSchemaEditor(
        settings,
        on_add=lambda e: ui.notify(f'added: {e}'),
        on_switch=lambda e: ui.notify(f'switched: {e}'),
        on_delete_row=lambda e: ui.notify(f'deleted: {e}'),
        on_delete_all_rows=lambda e: ui.notify(f'all: {e}'),
        on_change=lambda e: ui.notify(f'Change: {e}'),
    )


ui.run()
