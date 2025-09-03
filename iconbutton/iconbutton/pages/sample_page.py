from __future__ import annotations

from dataclasses import KW_ONLY, field
import typing as t

import rio

@rio.page(
    name="Sample Page",
    url_segment="",
)
class SplitPopup(rio.Component):
    is_open: bool = False
    def on_button_press(self):
        self.is_open = not self.is_open
    def build(self) -> rio.Component:
        grid=rio.Grid(row_spacing=0,column_spacing=0,align_y=0.5)
        ixr=0;ixc=0
        grid.add(rio.Text("First"),
                    row=ixr,column=ixc);ixc+=1
        grid.add(rio.Text("Second"),
                    row=ixr,column=ixc);ixc+=1
        grid.add(rio.Text("Third"),
                    row=ixr,column=ixc);ixc+=1
        grid.add(rio.IconButton(icon="material/close",style='minor'),
                    row=ixr,column=ixc);ixc+=1
        #grid.add(rio.Button('X'),
        #            row=ixr,column=ixc);ixc+=1
        #grid.add(rio.Icon('material/close'),
        #            row=ixr,column=ixc);ixc+=1
        ixr+=1
        ixc=0
        grid.add(rio.Text("Content1"),
                    row=ixr,column=ixc);ixc+=1
        grid.add(rio.Text("Content2"),
                    row=ixr,column=ixc);ixc+=1
        grid.add(rio.Text("Content3"),
                    row=ixr,column=ixc);ixc+=1

        return rio.Popup(
            anchor=rio.Button(
                "Popup",
                on_press=self.on_button_press),
            content=rio.Card(
                content=grid
            ),
            is_open=self.is_open,
            position="bottom"
            )

class SamplePage(rio.Component):
    """
    This is an example Page. Pages are identical to other Components and only
    differ in how they're used.
    """

    def build(self) -> rio.Component:
        return rio.Column(
            rio.Text("Example IconButton App", style="heading2"),
            SplitPopup(),
            spacing=2,
            margin=2,
            align_x=0,
            align_y=0,
        )

