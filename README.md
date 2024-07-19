# Redbus Data Scraping and Filtering with Streamlit Application

## Problem Statement

Aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analyzing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates web browser interactions, the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.

## Introduction

The purpose of this project is to scrape the data using **selenium**, clean and structure the data, store it in a **MySQL** database, and visualize the information using a **Streamlit** web app.

This project involves 
   - Scraping bus route and schedule data from the RedBus website using Selenium and Python.
   - The scraped data is then processed, cleaned, and stored in MySQL database tables.
   - Create a web application that allow users to browse and filter bus routes and schedules for various state transport corporations (RTCs) in India.

The project leverages Python, Streamlit, and MySQL to achieve this.  
Here's a breakdown of the project components and how to use them.

## Requirements 
- Python 3.12.3 
- `selenium`: Automate Web Scrapping
- `pandas`: Data manipulation and analysis library.
- `mysql-connector-python` : MySQL Connector for Python
- `streamlit`: Web application framework for Python.

There is no need to download the chromedriver manually, Selenium's new in-built tool Selenium Manager will automatically download and manage the drivers for you. 

Install the required packages using `pip`:
```bash
pip install selenium pandas mysql-connector-python streamlit
```

## Setup
1. **MySQL Database**: Ensure you have MySQL installed and create a database. Adjust the database connection details (`host`, `user`, `password`) in the code as per your MySQL setup.

2. **Python Environment**: Set up a virtual environment (optional but recommended).

## Running the Code

1. **Collection**: scrapes data from the RedBus website:
   - **get_into_rtc_wise**: Collects links to specific RTCs (Road Transport Corporations).
   - **get_bus_route_link_pagewise**: Collects route links for each RTC.
   - **get_bus_details_route_wise**: Scrapes detailed bus information for each route.
   
   Execute the collection cell to collect and save individual RTC-wise and route-wise CSV files.

2. **Extraction & Cleaning**: cleans and combines scraped CSV data:
   - Convert collected data into appropriate formats.
   - **classify_bus**: Categorizes bus operators into Government or Private.
   - **classify_bus_type**: Categorizes bus types into Sleeper or Seater.
   - **classify_ac_type**: Categorizes bus types into AC or Non-AC.
   
   Run the extraction_cleaning cell to clean and merge RTC-specific CSV files into a consolidated `RedBus_Data.csv`.

4. **Storage**:
   - Establishes a connection to MySQL and inserts cleaned data:
   - Creates a table `bus_routes` in the `Redbus_Project` database.
   - Inserts cleaned data from `RedBus_Data.csv` into MySQL.

   Execute the storage cell to create the database table and populate it with the cleaned data.

5. **Streamlit Visualization**:
   - Establishes a connection to MySQL
   - Displays the RTC available
   - **Navigation:** Supports navigation through a list of state transport corporations with next and previous buttons.
   - Displays routes available under each RTC
   - Displays the bus details under each route
   - **Dynamic Content:** Displays bus details dynamically fetched from a MySQL database.
   - **Filtering:** Allows filtering of bus routes based on various criteria such as amenities, time of departure and arrival, bus type, and operator type.





