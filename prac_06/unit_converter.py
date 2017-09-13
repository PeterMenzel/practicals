from kivy.app import App
from kivy.lang import Builder


class UnitConverter(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('unit_converter.kv')
        return self.root

    def handle_increment(self, value, increment):
        value += increment
        self.root.ids.input_number.text = str(value)

    def handle_convert_miles_to_km(self, value):
        self.root.ids.output_number.text = str(value * 1.609344)


UnitConverter().run()