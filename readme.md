# NiceJEJE, a Json-Editor Renderer for NiceGUI

This project integrates `[json-editor/json-editor](https://github.com/json-editor/json-editor)`, a JSON Schema Based Editor, to render schemas as input and labels in NiceGUI. 
It provides mappings for various events within NiceGUI environment.

## Event Mappings

| Event               | Description                            |
|---------------------|----------------------------------------|
| On Add              | Notifies when an item is added.        |
| On Switch           | Notifies when switching items.         |
| On Delete Row       | Notifies when deleting a row.          |
| On Delete All Rows  | Notifies when deleting all rows.       |
| On Change           | Notifies when any change occurs.       |

## Usage

To use this project, follow the steps below:

1. Import nicejeje JsonSchemaEditor
   ```python
   from nicejeje.jsonschema_editor import JsonSchemaEditor
   """)

2. Import additional required libraries such as Bootstrap, FontAwesome etc..

3. Define your JSON schema and settings.

   ```python
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
   ```

4. Use `JsonSchemaEditor` within a NiceGUI card context with event mappings.

   ```python
   with ui.card():
       schema1 = JsonSchemaEditor(
           settings,
           on_add=lambda e: ui.notify(f'added: {e}'),
           on_switch=lambda e: ui.notify(f'switched: {e}'),
           on_delete_row=lambda e: ui.notify(f'deleted: {e}'),
           on_delete_all_rows=lambda e: ui.notify(f'all: {e}'),
           on_change=lambda e: ui.notify(f'Change: {e}'),
       )
   ```

5. Run the NiceGUI application.

   ```python
   ui.run()
   ```


