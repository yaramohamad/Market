import sys  
from PyQt5 import QtWidgets  
from supermarket_app_ui import Ui_Form  # Import the generated UI file  


class SupermarketApp(QtWidgets.QWidget):  
    def __init__(self):  
        super(SupermarketApp, self).__init__()  

        # Set up the UI  
        self.ui = Ui_Form()  
        self.ui.setupUi(self)  

        # Prices  
        self.prices = {  
            "Apple": 0.5,  
            "Mango": 0.75,  
            "Guava": 0.6,  
            "Banana": 0.3  
        }  

        # Counts  
        self.counts = {fruit: 0 for fruit in self.prices}  

        # Connect buttons to methods  
        self.ui.apple_button.clicked.connect(lambda: self.add_fruit("Apple"))  
        self.ui.mango_button.clicked.connect(lambda: self.add_fruit("Mango"))  
        self.ui.guava_button.clicked.connect(lambda: self.add_fruit("Guava"))  
        self.ui.banana_button.clicked.connect(lambda: self.add_fruit("Banana"))  
        self.ui.checkout_button.clicked.connect(self.checkout)  

    def add_fruit(self, fruit):  
        # Update fruit count  
        self.counts[fruit] += 1  
        # Update the respective label  
        getattr(self.ui, f"{fruit.lower()}_count_label").setText(f"{fruit} Count: {self.counts[fruit]}")  
        # Update total cost  
        self.update_total_cost()  

    def update_total_cost(self):  
        total_cost = sum(self.counts[fruit] * self.prices[fruit] for fruit in self.prices)  
        self.ui.total_cost_label.setText(f"Total Cost: ${total_cost:.2f}")  

    def checkout(self):  
        # Reset counts and total cost  
        for fruit in self.counts:  
            self.counts[fruit] = 0  
            getattr(self.ui, f"{fruit.lower()}_count_label").setText(f"{fruit} Count: {self.counts[fruit]}")  
        self.ui.total_cost_label.setText("Total Cost: $0.00")  


if __name__ == "__main__":  
    app = QtWidgets.QApplication(sys.argv)  
    window = SupermarketApp()  
    window.show()  
    sys.exit(app.exec_())