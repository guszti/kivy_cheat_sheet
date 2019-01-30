from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.core.window import Window

class MyListButton(ListItemButton):
    pass

class Stuff(GridLayout):
    d = ['a   =>   \@_',
        'b   =>   \@_',
        'c   =>   \@_',
        'd   =>   \@_']

    def change_bg(self, i):
        if i.background_color == [1.0, 0.0, 0.0, 1.0]:
            i.background_color = 1, 1, 1, 1
        else:
            i.background_color = 1.0, 0.0, 0.0, 1.0

    def remove_item(self):
        if self.ids.data_list.adapter.selection:
            self.d.remove(self.ids.data_list.adapter.selection[0].text)
            self.ids.data_list.adapter.data.remove(self.ids.data_list.adapter.selection[0].text)
            self.ids.data_list._trigger_reset_populate()

class StuffApp(App):
    def build(self):
        st = Stuff()
        return st


if __name__ == '__main__':
    Window.size = (500, 500)
    StuffApp().run()
