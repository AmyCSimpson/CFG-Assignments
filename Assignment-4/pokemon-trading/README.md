**API Usage Guide**

<u>What is the API for?</u>

This API is designed to track Pokémon trading cards. You can use it to view all cards, add new cards, and remove cards by their unique ID.
Required Packages

Before running the code, you need to install the following Python packages:
- flask: A lightweight web framework for building web applications.
- mysql-connector-python: A library for connecting to a MySQL database.
- requests: A library to make HTTP requests to the API from the client-side.

You can install these packages in PyCharm by hovering over the writing and waiting for the drop down, or by going directly to packages.

<u>Changing Credentials in config.py</u>

Open the config.py file in your project. You will see variables like USER, PASSWORD, HOST, and DATABASE.
Change these values to match your MySQL database credentials. For example:
- USER = 'your_username'  # Your MySQL username
- PASSWORD = 'your_password'  # Your MySQL password
- HOST = 'localhost'  # Usually 'localhost' for local development
- DATABASE = 'pokemon_trading'  # The name of your database

<u>Order to Run the Files</u>

1.  run app.py. This will start the Flask server and make the API available.
2.  run main.py. This file will interact with the API to allow you to add, view, or delete cards.

<u>How to Interact with the API</u>

To view all Pokémon cards, run main.py and select option A when prompted.

To add a new Pokémon card:
When prompted in the console, select option C.
You will be asked to enter the card’s name, type, and PSA rating.
After entering this information, the card will be added to the database, and you will see a confirmation message.

To remove a card:
Select option B in main.py.
You will see a list of all cards. Enter the ID of the card you want to remove.
The card will be deleted, and you will see a confirmation message.

<u>Additional Notes</u>

Make sure your MySQL database is running and the pokemon_trading database exists with the appropriate tables before starting the server.

The API runs on http://127.0.0.1:5000/, which is the local address for accessing it through your web browser or the client-side application.
