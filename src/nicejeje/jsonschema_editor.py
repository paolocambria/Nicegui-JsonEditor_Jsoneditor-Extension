from nicegui.element import Element
from pathlib import Path
from typing import Optional, Callable, Any
from nicegui.events import GenericEventArguments, JsonEditorChangeEventArguments, handle_event
from typing_extensions import Self

lib_abs_path = Path(__file__).parent / "lib/jsoneditor.js"


class JsonSchemaEditor(Element, component="jsonschema_editor.js", libraries=[lib_abs_path]):

    def __init__(self, settings,
                 on_change: Optional[Callable] = None,
                 on_add: Optional[Callable] = None,
                 on_switch: Optional[Callable] = None,
                 on_add_row: Optional[Callable] = None,
                 on_delete_row: Optional[Callable] = None,
                 on_delete_all_rows: Optional[Callable] = None,
                 ) -> None:
        super().__init__()
        self.settings = settings
        self._props['settings'] = self.settings

        if on_change:
            self.on_change(on_change)

        if on_change:
            self.on_change(on_change)

        if on_add:
            self.on_add(on_add)

        if on_switch:
            self.on_switch(on_switch)

        if on_add_row:
            self.on_add_row(on_add_row)

        if on_delete_row:
            self.on_delete_row(on_delete_row)

        if on_delete_all_rows:
            self.on_delete_all_rows(on_delete_all_rows)

    def on_change(self, callback: Callable[..., Any]) -> Self:
        """Add a callback to be invoked when the content changes."""
        def handle_on_change(e: GenericEventArguments) -> None:
            content = e.args.get('content', None)
            errors = e.args.get('errors', None)
            handle_event(callback, JsonEditorChangeEventArguments(
                sender=self, client=self.client, content=content, errors=errors))
        self.on('change', handle_on_change)
        return self

    def on_add(self, callback: Callable[..., Any]) -> Self:
        """Add a callback to be invoked when a property is added."""
        def handle_on_add(e: GenericEventArguments) -> None:
            type = e.args.get('type', None)
            path = e.args.get('path', None)
            key = e.args.get('key', None)
            data = {
                "type": type,
                "path": path,
                "key": key
            }

            handle_event(callback, data)
        self.on('add', handle_on_add)
        return self

    def on_switch(self, callback: Callable[..., Any]) -> Self:
        """Add a callback to be invoked when switching occurs."""
        def handle_on_switch(e: GenericEventArguments) -> None:
            type = e.args.get('type', None)
            path = e.args.get('path', None)
            data = {
                "type": type,
                "path": path,
            }
            handle_event(callback, data)
        self.on('switch', handle_on_switch)
        return self

    def on_add_row(self, callback: Callable[..., Any]) -> Self:
        """Add a callback to be invoked when a row is added."""
        def handle_on_add_row(e: GenericEventArguments) -> None:
            print("e")
            editor = e.args.get('editor', None)
            handle_event(callback, editor)
        self.on('addRow', handle_on_add_row)
        return self

    def on_delete_row(self, callback: Callable[..., Any]) -> Self:
        """Add a callback to be invoked when a row is deleted."""
        def handle_on_delete_row(e: GenericEventArguments) -> None:
            handle_event(callback, e.args)
        self.on('deleteRow', handle_on_delete_row)
        return self

    def on_delete_all_rows(self, callback: Callable[..., Any]) -> Self:
        """Add a callback to be invoked when all rows are deleted."""
        def handle_on_delete_all_rows(e: GenericEventArguments) -> None:
            handle_event(callback, e.args)
        self.on('deleteAllRows', handle_on_delete_all_rows)
        return self

    def update_settings(self) -> None:
        return self.run_method('run_update_settings', self.settings)

    def update_schema(self, schema) -> None:
        return self.run_method('run_update_schema', schema)

    def reset(self) -> None:
        self.run_method('reset')
