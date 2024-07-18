# Import required libraries
import pandas as pd
import streamlit as st
import mysql.connector

# Establishes connection to MySQL
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "MySql_Password",
    database = "Redbus_Project"
)
# creating cursor object where SQL queries are returned as dictionaries, where the keys are the column names
cursor = connection.cursor(dictionary=True)     

# list of RTC's
rtc_items = ["KSRTC", "KTCL", "RSRTC", "HRTC", "ASTC", "PEPSU", "NBSTC", "BSRTC", "KAAC", "JKSRTC"]

# Details of all RTC's
rtc_item_details = {
    "KSRTC": """<b>കേരള സ്റ്റേറ്റ് റോഡ് ട്രാൻസ്പോർട്ട് കോർപ്പറേഷൻ</b><br>
                    Kerala State Road Transport Corporation<br>
                    <b>Rating:</b> 3.85<br>
                    <b>Services:</b> 940 services including Swift, AC Multiaxle and more""",
    "KTCL": """<b>कदंब येरादारी म्हामंडळ</b><br>
                    Kadamba Transport Corporation Limited<br>
                    <b>Rating:</b> 3.83<br>
                    <b>Services:</b> 60 services including Volvo Bus, AC & Non AC Bus and more""",
    "RSRTC": """<b>राजस्थान स्टेट रोड ट्रांसपोर्ट कॉर्पोरेशन</b><br>
                    Rajasthan State Road Transport Corporation<br>
                    <b>Rating:</b> 3.71<br>
                    <b>Services:</b> 6000 services including Deluxe, Ordinary and more""",
    "HRTC": """<b>हिमाचल रोड ट्रान्सपोर्ट कॉर्पोरेशन</b><br>
                    Himachal Road Transport Corporation<br>
                    <b>Rating:</b> 3.98<br>
                    <b>Services:</b> 480 services including Himgaurav, Himmani and more""",
    "ASTC": """<b>অসম ৰাজ্যিক পৰিবহন নিগম</b><br>
                    Assam State Transport Corporation<br>
                    <b>Rating:</b> 4.02<br>
                    <b>Services:</b> 200 services including Volvo Bus, AC & Non AC Bus and more""",
    "PEPSU": """<b>ਪੈਪਸੂ ਰੋਡ ਟਰਾਂਸਪੋਰਟ ਕਾਰਪੋਰੇਸ਼ਨ</b><br>
                    Punjab Roadways Pepsu Road Transport Corporation<br>
                    <b>Rating:</b> 3.83<br>
                    <b>Services:</b> 100 services including Volvo Bus, AC & Non AC Bus and more""",
    "NBSTC": """<b>উত্তরবঙ্গ রাজ্য পরিবহন কর্পোরেশন</b><br>
                    North Bengal State Transport Corporation<br>
                    <b>Rating:</b> 3.93<br>
                    <b>Services:</b> 30 services including Volvo Bus, AC & Non AC Bus and more""",
    "BSRTC": """<b>बिहार राज्य रोड ट्रान्सपोर्ट कॉर्पोरेशन</b><br>
                    Bihar State Road Transport Corporation<br>
                    <b>Rating:</b> 3.91<br>
                    <b>Services:</b> 220 services including Volvo Bus, AC & Non AC Bus and more""",
    "KAAC": """<b>কাৰ্বি আংলং স্বায়ত্ত শাসিত পৰিষদ পৰিবহণ</b><br>
                    Karbi Anglong Autonomous Council Transport<br>
                    <b>Rating:</b> 3.71<br>
                    <b>Services:</b> 10 services including AC & Non AC Bus and more""",
    "JKSRTC": """<b>जम्मू और कश्मीर सड़क परिवहन निगम</b><br>
                    Jammu & Kashmir State Road Transport Corporation<br>
                    <b>Rating:</b> 3.85<br>
                    <b>Services:</b> 16 services including Volvo Bus, AC & Non AC Bus and more"""
}

# Page Congfiguration 
st.set_page_config(
    page_title="RedBus Imitation",
    layout='wide',
    page_icon='page_icon.png',
    initial_sidebar_state='collapsed'
)

# Navigation Functions
def next_item():
    st.session_state.index = (st.session_state.index + 1) % len(rtc_items)

def prev_item():
    st.session_state.index = (st.session_state.index - 1) % len(rtc_items)
    if st.session_state.index < 0:
        st.session_state.index += len(rtc_items)

# Page Header
st.markdown("<h1 style='background-color:#EF7878;text-align:center;color:white;'>RedBus</h1>", unsafe_allow_html=True)

# Session State Initialization
if 'index' not in st.session_state:
    st.session_state.index = 0

if 'selected_item' not in st.session_state:
    st.session_state.selected_item = None

# Function to split time range
def get_time_range_limits(time_range):
    if time_range == '6 AM to 12 PM':
        return '06:00:00', '12:00:00'
    elif time_range == '12 PM to 6 PM':
        return '12:00:00', '18:00:00'
    elif time_range == '6 PM to 12 AM':
        return '18:00:00', '23:59:59'
    elif time_range == '12 AM to 6 AM':
        return '00:00:00', '06:00:00'
    else:
        return '00:00:00', '23:59:59'

# Creating list of items to display 
start_index = st.session_state.index
end_index = start_index + 3
current_items = rtc_items[start_index:end_index] if end_index <= len(rtc_items) else rtc_items[start_index:] + rtc_items[:end_index - len(rtc_items)]

# Displaying RTC's
with st.container():
    st.subheader('Available State Transport Buses:')
    col1, col2, col3 = st.columns(3)
    for i, item in enumerate(current_items):
        with [col1, col2, col3][i]:
            with st.container(border=True):
                st.markdown(f"<h2 style='text-align:center;color:red;'>{item}</h2>", unsafe_allow_html=True)
                st.markdown(f"<p style='text-align:center;'>{rtc_item_details[item]}</p>", unsafe_allow_html=True)
                view_buses_button = st.button(f'View Buses {item}', key=f'{item}', use_container_width=True)
                if view_buses_button:
                    st.session_state.selected_item = item

    # Navigation through RTC's
    col1, col2, col3 = st.columns(3)
    with col2:
        if start_index > 0:
            if st.button('< Previous', use_container_width=True):
                prev_item()
        if st.button('Next >', use_container_width=True):
            next_item()

# After selecting RTC - displaying the routes & buses with filters
if st.session_state.selected_item:
    selected_rtc = st.session_state.selected_item
    st.subheader(f"Routes for {selected_rtc}")
    # Query to collect the routes of the RTC selected
    cursor.execute("""
    SELECT 
        Bus_Route_Name,
        MIN(Departing_Time) AS First_Bus_Time,
        MAX(Departing_Time) AS Last_Bus_Time,
        COUNT(*) AS Number_of_Buses
    FROM 
        bus_routes 
    WHERE 
        RTC_Name = %s 
    GROUP BY 
        Bus_Route_Name""", (selected_rtc,))
    
    route_data = cursor.fetchall()

    # Converts the data as DataFrame
    df_routes = pd.DataFrame(route_data)
    
    # loops through each route & displays required data of each route
    for index, row in df_routes.iterrows():
        with st.container(border=True):
            st.subheader(f'{row["Bus_Route_Name"]}')
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.write(f'{row["Number_of_Buses"]} buses')
            with col2:
                first_bus_time = row['First_Bus_Time'].strftime('%H:%M:%S') if row['First_Bus_Time'] else None
                st.write(f'First Bus: {first_bus_time}')
            with col3:
                last_bus_time = row['Last_Bus_Time'].strftime('%H:%M:%S') if row['Last_Bus_Time'] else None
                st.write(f'Last Bus: {last_bus_time}')
            with col4:
                view_buses = st.checkbox('View Buses', key=f'{row["Bus_Route_Name"]}')
            
            # after clicking the view buses - displayes the bus data
            if view_buses:
                # Query to collect bus details of each route
                sql_query = """SELECT Bus_Name, Bus_Type, Departing_Time, Reaching_Time, Duration, Availability, Star_Rating, Price, Boarding_Points, Reaching_Points, Amenities
                FROM bus_routes 
                WHERE RTC_Name = %s 
                AND Bus_Route_Name = %s"""

                # Filters
                st.sidebar.title("Filter by")

                time_ranges = ['All', '6 AM to 12 PM', '12 PM to 6 PM', '6 PM to 12 AM', '12 AM to 6 AM']
                bus_types = ['All', 'Sleeper', 'Seater', 'AC', 'NON AC']
                operator_types = ['All', 'Government', 'Private']

                selected_filter1 = st.sidebar.checkbox("Bus Departure Time from Source")
                selected_filter2 = st.sidebar.checkbox("Bus Arrival Time at Destination")
                selected_filter3 = st.sidebar.checkbox("Bus Type")
                selected_filter4 = st.sidebar.checkbox("Bus Operator")

                filters = []

                if selected_filter1:
                    selected_departure_time_range = st.sidebar.selectbox('Departure Time Range', time_ranges, key=1)
                    if selected_departure_time_range != 'All':
                        start_time, end_time = get_time_range_limits(selected_departure_time_range)
                        filters.append(f"TIME(Departing_Time) BETWEEN '{start_time}' AND '{end_time}'")

                if selected_filter2:
                    selected_arrival_time_range = st.sidebar.selectbox('Arrival Time Range', time_ranges, key=2)
                    if selected_arrival_time_range != 'All':
                        start_time, end_time = get_time_range_limits(selected_arrival_time_range)
                        filters.append(f"TIME(Reaching_Time) BETWEEN '{start_time}' AND '{end_time}'")

                if selected_filter3:
                    selected_bus_type = st.sidebar.selectbox('Bus Type', bus_types, key=3)
                    if selected_bus_type and selected_bus_type != 'All':
                        filters.append(f"(Bus_Type1 = '{selected_bus_type}' OR Bus_Type2 = '{selected_bus_type}')")

                if selected_filter4:
                    selected_operator_type = st.sidebar.selectbox('Operator Type', operator_types, key=4)
                    if selected_operator_type != 'All':
                        filters.append(f"Operator_Type = '{selected_operator_type}'")

                if filters:
                    # Updating the query to include the filters
                    sql_query += " AND " + " AND ".join(filters)

                # sort
                st.sidebar.title("Sort by")

                sort_options = ['None', 'Price - High to Low', 'Price - Low to High', 'Best Rating First', 'Early Departure', 'Late Departure', 'Early Arrival', 'Late Arrival']
                selected_sort_by = st.sidebar.radio('Sort By', sort_options)                
                
                sort_by_price = ""
                sort_by_rating = ""
                sort_by_departing_time = ""
                sort_by_reaching_time = ""

                if selected_sort_by == 'Price - High to Low':
                    sort_by_price = "Price DESC"
                elif selected_sort_by == 'Price - Low to High':
                    sort_by_price = "Price ASC"

                if selected_sort_by == 'Best Rating First':
                    sort_by_rating = "Star_Rating DESC"

                if selected_sort_by == 'Early Departure':
                    sort_by_departing_time = "Departing_Time ASC"
                elif selected_sort_by == 'Late Departure':
                    sort_by_departing_time = "Departing_Time DESC"

                if selected_sort_by == 'Early Arrival':
                    sort_by_reaching_time = "Reaching_Time ASC"
                elif selected_sort_by == 'Late Arrival':
                    sort_by_reaching_time = "Reaching_Time DESC"

                sort_clauses = [clause for clause in [sort_by_price, sort_by_rating, sort_by_departing_time, sort_by_reaching_time] if clause]
                if sort_clauses:
                    # updating query to include sorts
                    sql_query += " ORDER BY " + ", ".join(sort_clauses)

                # Executes the query after filters & sorts
                cursor.execute(sql_query, (st.session_state.selected_item, row["Bus_Route_Name"]))
                detailed_data = cursor.fetchall()
                df_detailed = pd.DataFrame(detailed_data)

                # Amenities Filter
                st.sidebar.title("Filter by Amenities")

                df_detailed['Amenities'] = df_detailed['Amenities'].apply(lambda x: x.split(', ') if pd.notna(x) else [])
                unique_amenities = set(amenity for sublist in df_detailed['Amenities'] for amenity in sublist)
                unique_amenities = list(unique_amenities)
                selected_amenities = st.sidebar.multiselect("Select Amenities", unique_amenities)

                if selected_amenities:
                    df_detailed = df_detailed[df_detailed['Amenities'].apply(lambda x: any(item in selected_amenities for item in x))]
                
                if df_detailed.empty:
                    st.warning("No buses found for the selected filters.")
                else:
                    try: 
                        # taking only the time
                        df_detailed['Departing_Time'] = df_detailed['Departing_Time'].dt.time   
                        df_detailed['Reaching_Time'] = df_detailed['Reaching_Time'].dt.time
                        # spliting the points with ','
                        df_detailed['Boarding_Points'] = df_detailed['Boarding_Points'].apply(lambda x: x.split(', ') if pd.notna(x) else [])  
                        df_detailed['Reaching_Points'] = df_detailed['Reaching_Points'].apply(lambda x: x.split(', ') if pd.notna(x) else [])

                        st.dataframe(df_detailed)
                    except Exception:
                        st.warning("No buses found for the selected filters.")
