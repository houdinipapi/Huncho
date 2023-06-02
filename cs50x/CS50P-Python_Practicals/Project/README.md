# Wine Database Web Application
- This is a simple web application that allows you to manage a wine database.
- The application enables you to track different types of wines,
	their capacities, outlets that retail teh wines, and the stock and
	sales information.

## Features
- Add new wines to the database, including their names and capacities.
- Add new outlets to the database, including their names and stock levels.
- Record wine sales by selecting a wine, an outlet, and specifying
	the quantity sold.
- View the list of wines, outlets, and sales recorded in the database.

## Technologies Used
- Python
- Flask (a web framework)
- SQLite ( alightweight database system)
- HTML
- CSS

## Getting Started
1. Clone the repository to your local machine:
	`git clone https://github.com/your-username/wine-database-web-app.git`

2. Install the required dependencies. It's recommended to set
	up a virtual environment before installing the dependencies:
	```
	cd wine-database-web-app
	python -m venv venv
	source venv/bin/activate  # Activating the virtual environment
	pip install -r requirements.txt
	```

3. Create the wine database:
	`python app.py`

4. Access the application by opening a web browser and navigating to
	`http://localhost:5000`.

## Usage
- On the home page, you will see the list of wines, outlets, and sales
	recorded in the database.
- To add a new wine, click on the "Add Wine" section and fill out the
	wine name and capacity.
- To add a new outlet, click on the "Add Outlet" section and provide the
	outlet name and stock level.
- To record a sale, go to "Record Sale" section, select the wine, outlet,
	and enter teh quantity sold.
- The data will be updated in real-time, and you can view the changes on
	the home page.

## Cutomization
- You can customize the appearance of the web application by modifying the CSS
	in the `index.html` file.
- If you need to extend the functionality or modify the database schema,
	yo can edit the Python code in `app.py`.

## License
This project is licensed under the [MIT License]().
Feel free to modify and use the code according to your requirements.

## Acknowledgements
This project was inspired by the need to create a simple wine database
and was built using Flask and SQLite.

## Contact
If you have any questions or suggesstions regarding this project,
feel free to contact me at ochiengcliff.co@gmail.com.
