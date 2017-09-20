
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Label
from kivy.properties import StringProperty


class NameIterator(App):
    status_text = StringProperty()

    def __init__(self, **kwargs):
        """
        Construct main app
        """
        super().__init__(**kwargs)
        # basic data example - dictionary of names: phone numbers
        # self.phonebook = {"Bob Brown": "0414144411", "Cat Cyan": "0441411211", "Oren Ochre": "0432123456"}
        self.names = {"Bob Brown", "Cat Cyan", "Oren Ochre"}

    def build(self):
        """
        Build the Kivy GUI
        :return: reference to the root Kivy widget
        """
        self.title = "Name Iterator"
        self.root = Builder.load_file('name_iterator.kv')
        self.create_widgets()
        # self.names = {"Bob Brown", "Cat Cyan", "Oren Ochre"}
        return self.root

    def create_widgets(self):
        """
        Create buttons from dictionary entries and add them to the GUI
        :return: None
        """
        for name in self.names:
            # create a button for each phonebook entry
            temp_label = Label(text=name)
            # temp_label.bind(on_release=self.press_entry)
            # add the button to the "entriesBox" using add_widget()
            self.root.ids.entriesBox.add_widget(temp_label)

    # def press_entry(self, instance):
    #     """
    #     Handler for pressing entry buttons
    #     :param instance: the Kivy button instance
    #     :return: None
    #     """
    #     # update status text
    #     name = instance.text
        # self.status_text = "{}'s number is {}".format(name, self.phonebook[name])

    def clear_all(self):
        """
        Clear all of the widgets that are children of the "entriesBox" layout widget
        :return:
        """
        self.root.ids.entriesBox.clear_widgets()

NameIterator().run()
