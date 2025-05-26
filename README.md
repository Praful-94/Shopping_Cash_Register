# Shopping_Cash_Register

The Python Cash Register System is a terminal-based application designed to simulate a real-world point-of-sale (POS) system for retail environments. It allows users to manage a shopping cart, apply discounts, calculate GST (Goods and Services Tax), and generate itemized invoices. This project was developed with educational and small business use cases in mind, offering a hands-on example of how core programming concepts can be applied to solve practical business problems.

The program is entirely built in Python and runs in a command-line interface or Jupyter Notebook. It provides users with interactive control using text commands, such as add, view cart, update, remove, checkout, and invoices. Each function is modular, making the system easy to maintain and extend. The system makes use of built-in Python data structures like lists and dictionaries to manage cart items, store invoice data, and perform calculations.

The system starts with a menu display that guides the user through available operations. The add_item() function collects item details such as name, price, quantity, and discount rate. Input validation ensures users do not mistakenly enter commands while in the middle of item entry. Users can also update or remove specific items from the cart, making the cart management flexible and realistic.

The view_bill() function calculates the subtotal of all items in the cart, factoring in discounts, and displays the result in a clean format. During checkout, the program prompts the user to input the GST rate, calculates the final amount after applying GST and discounts, and displays a full breakdown of charges. The transaction is then stored as an invoice using deepcopy() to prevent reference issues and saved in a global list named daily_invoices.

Invoices can be reviewed at any time during the session using the view_invoices() command. Users can also clear the entire invoice history with the clear_invoices() function if needed. Each invoice includes a complete breakdown of items, subtotal, total discount, GST applied, and the final amount payable.

One of the system’s strengths lies in its simplicity and clarity, making it ideal for beginners in Python programming. It demonstrates the use of functions, conditionals, loops, input handling, formatting, and basic error checking. The program also makes good use of the IPython.display module to enhance visual output when run in notebooks.
