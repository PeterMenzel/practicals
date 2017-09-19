from kivy.app import App
from kivy.lang import Builder


class UnitConverter(App):
    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('unit_converter.kv')
        return self.root

    def handle_increment(self, input_value, increment):
        value = self.error_check(input_value)
        value += increment
        self.root.ids.input_number.text = str(value)

    def handle_convert_miles_to_km(self, input_value):
        value = self.error_check(input_value)
        self.root.ids.output_number.text = str(value * 1.609344)

    def error_check(self, input_value):
        try:
            value = float(input_value)
        except:
            value = float(0)
            self.root.ids.output_number.text = str("0.0")
        return value


UnitConverter().run()