# Redbus Data Scraping and Filtering with Streamlit Application
## Project Overview
Aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. 
By utilizing **Selenium** for web scraping, this project automates web browser interactions, the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability
By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the
transportation industry.

This project involves 
   - Scraping bus route and schedule data from the RedBus website using Selenium and Python.
   - The scraped data is then processed, cleaned, and stored in MySQL database tables.
   - Create a web application that allow users to browse and filter bus routes and schedules for various state transport corporations (RTCs) in India.

The project leverages Python, Streamlit, and MySQL to achieve this.
Here's a breakdown of the project components and how to use them.

## Requirements 

- Python 3.12.3 
- Selenium
- pandas
- MySQL Connector for Python
- Chrome WebDriver (for Selenium)

Install the required packages using `pip`:
```bash
pip install selenium pandas mysql-connector-python
```

## Setup
   
1. **MySQL Database**: Ensure you have MySQL installed and create a database named `Redbus_Project`. Adjust the database connection details (`host`, `user`, `password`) in the code as per your MySQL setup.

2. **Python Environment**: Set up a virtual environment (optional but recommended).

## Running the Code

1. **Collection**: scrapes data from the RedBus website:
   - **get_into_rtc_wise**: Collects links to specific RTCs (Road Transport Corporations).
   - **get_bus_route_link_pagewise**: Collects route links for each RTC.
   - **get_bus_details_route_wise**: Scrapes detailed bus information for each route.
   
   Execute the collection cell to collect and save individual RTC-wise and route-wise CSV files.

2. **Extraction & Cleaning**: cleans and combines scraped CSV data:
   - **classify_bus**: Categorizes bus operators into Government or Private.
   - **classify_bus_type**: Categorizes bus types into Sleeper or Seater.
   - **classify_ac_type**: Categorizes bus types into AC or Non-AC.
   
   Run the extraction_cleaning cell to clean and merge RTC-specific CSV files into a consolidated `RedBus_Data.csv`.

3. **Storage**: establishes a connection to MySQL and inserts cleaned data:
   - Creates a table `bus_routes` in the `Redbus_Project` database.
   - Inserts cleaned data from `RedBus_Data.csv` into MySQL.

   Execute the storage cell to create the database table and populate it with the cleaned data.

# RedBus Imitation Streamlit App

This Streamlit application mimics the functionality of RedBus, allowing users to view and filter bus routes and details from various state transport corporations.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-repo/redbus-imitation.git
   cd redbus-imitation
   ```

2. **Install dependencies & setup :**

   Install all the requirements as specified above.

3. **Database Setup:**

   - Make sure MySQL is installed and running on your local machine or server.
   - Create a MySQL database named `Redbus_Project`.
   - Modify the connection settings in `app.py` to match your MySQL configuration (`host`, `user`, `password`).

4. **Run the Streamlit app:**

   Start the Streamlit server by running the following command:

   ```bash
   streamlit run app.py
   ```

   This command will launch the Streamlit application in your default web browser.

## Usage

- Upon running the Streamlit app, you will see a page resembling RedBus with available state transport buses listed.
- Use the navigation buttons (`< Previous`, `Next >`) to navigate through the list of state transport corporations.
- Click on `View Buses [RTC Name]` button to view detailed routes for the selected state transport corporation.
- You can filter buses based on amenities, departure time, arrival time, bus type, and operator type using the filters on the sidebar.
- The filtered bus details will be displayed in a table format.

## Features

- **Dynamic Content:** Displays bus details dynamically fetched from a MySQL database.
- **Filtering:** Allows filtering of bus routes based on various criteria such as amenities, time of departure and arrival, bus type, and operator type.
- **Navigation:** Supports navigation through a list of state transport corporations with next and previous buttons.

## File Structure

- `app.py`: Main Streamlit application file containing the code for fetching data from MySQL and displaying it using Streamlit components.
- `requirements.txt`: Lists all Python dependencies required to run the application.
- `README.md`: Markdown file providing instructions and information about the application.

## Dependencies

- **Python Packages:**
  - `pandas`: Data manipulation and analysis library.
  - `streamlit`: Web application framework for Python.
  - `mysql-connector-python`: MySQL driver for Python.
  - `numpy`: Numerical computing library (used indirectly through `pandas`).

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

### Notes:

- Customize the paths, dependencies, and installation steps based on your project structure and requirements.
- Include additional sections or details as needed, such as troubleshooting tips, known issues, or future enhancements.

This README file provides a structured overview of your Streamlit application, guiding users on how to set up and use the application effectively. Adjust it further to fit specific details and nuances of your project.
