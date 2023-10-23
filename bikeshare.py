import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york': 'new_york_city.csv',
    'washington': 'washington.csv'
}

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June']

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        str (city), str (month), str (day): City name, month, and day of the week for analysis
    """
    print("\nWelcome to the Bike Share Data Analysis tool!\n")

    while True:
        city = input("Would you like to see data for Chicago, New York, or Washington? ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid input. Please choose a valid city.")

    while True:
        time_filter = input("Would you like to filter the data by month, day, or not at all? ").lower()
        if time_filter in ['month', 'day', 'none']:
            break
        else:
            print("Invalid input. Please choose 'month', 'day', or 'none'.")

    month = 'all'
    day = 'all'

    if time_filter == 'month':
        while True:
            month = input("Which month - January, February, March, April, May, or June? ").capitalize()
            if month in MONTHS:
                break
            else:
                print("Invalid month. Please choose a valid month.")
    elif time_filter == 'day':
        while True:
            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ").capitalize()
            if day in DAYS:
                break
            else:
                print("Invalid day of the week. Please choose a valid day.")

    print('-' * 40)

    return city, month, day

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter

    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """

    try:
        df = pd.read_csv(CITY_DATA[city])
    except FileNotFoundError:
        print("File not found. Please make sure the data file exists.")
        return None

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['Day of Week'] = df['Start Time'].dt.strftime('%A')
    df['Hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month_num = MONTHS.index(month) + 1
        df = df[df['Month'] == month_num]

    if day != 'all':
        df = df[df['Day of Week'] == day]

    return df

def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    """
    print("\nCalculating the most frequent times of travel...\n")

    common_month = df['Month'].mode()[0]
    print("Most common month:", MONTHS[common_month - 1])

    common_day = df['Day of Week'].mode()[0]
    print("Most common day of the week:", common_day)

    common_hour = df['Hour'].mode()[0]
    print("Most common start hour:", common_hour)
def station_stats(df):
    """
    Displays statistics on the most popular stations and trips.
    """
    print("\nCalculating the most popular stations and trips...\n")

    common_start_station = df['Start Station'].mode()[0]
    print("Most common start station:", common_start_station)

    common_end_station = df['End Station'].mode()[0]
    print("Most common end station:", common_end_station)

    df['Trip'] = df['Start Station'] + ' to ' + df['End Station']
    common_trip = df['Trip'].mode()[0]
    print("Most common trip:", common_trip)

def trip_duration_stats(df):
    """
    Displays statistics on trip duration.
    """
    print("\nCalculating trip duration statistics...\n")

    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time (seconds):", total_travel_time)

    average_travel_time = df['Trip Duration'].mean()
    print("Average travel time (seconds):", average_travel_time)

def user_stats(df, city):
    """
    Displays statistics on user types, gender, and birth year (if available).
    """
    print("\nCalculating user statistics...\n")

    user_types = df['User Type'].value_counts()
    print("Counts of each user type:")
    for user_type, count in user_types.items():
        print(f"{user_type}: {count}")

    if 'Gender' in df.columns and 'Birth Year' in df.columns:
        genders = df['Gender'].value_counts()
        print("\nCounts of each gender:")
        for gender, count in genders.items():
            print(f"{gender}: {count}")

        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        common_birth_year = int(df['Birth Year'].mode()[0])

        print("\nBirth year statistics:")
        print("Earliest birth year:", earliest_birth_year)
        print("Most recent birth year:", most_recent_birth_year)
        print("Most common birth year:", common_birth_year)
    else:
        print("\nGender and birth year data not available for", city.title())

def display_raw_data(df):
    """
    Displays 5 lines of raw data upon user request.
    """
    raw_data_display = input("Would you like to see 5 lines of raw data? Enter 'yes' or 'no': ").lower()
    if raw_data_display == 'yes':
        i = 0
        while i < len(df):
            print(df.iloc[i:i+5])
            i += 5
            raw_data_display = input("Would you like to see the next 5 lines of raw data? Enter 'yes' or 'no': ").lower()
            if raw_data_display != 'yes':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        if df is not None:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df, city)
            display_raw_data(df)

        restart = input("\nWould you like to restart? Enter 'yes' or 'no': ").lower()
        if restart != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
