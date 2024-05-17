
import matplotlib.pyplot as plt

def plot_bookings(total_bookings, cancellations_data):
    print('Plotting bookings vs. cancellations...')
    # Extract hotel names, bookings, cancellations, and cancellation ratios
    hotel_names = [list(item[0])[0] for item in total_bookings]
    bookings = [item[1] for item in total_bookings]
    cancellations = [item[1] for item in cancellations_data]
    cancellation_ratios = [round(float(item[2]), 2) for item in cancellations_data]

    # Create a figure and axis
    _, ax1 = plt.subplots(figsize=(12, 6))

    # Plot bookings and cancellations
    ax1.bar(hotel_names, bookings, label='Bookings')
    ax1.bar(hotel_names, cancellations, label='Cancellations(ratio)')
    ax1.set_xlabel('Hotel Type')
    ax1.set_ylabel('Number of Bookings/Cancellations(ratio)')
    ax1.set_title('Bookings vs. Cancellations')
    ax1.legend()

    # Add labels to the top of each bar
    for i, v in enumerate(bookings):
        ax1.text(i, v, str(v), ha='center', va='bottom')
        ax1.text(i, cancellations[i], f"{cancellations[i]} ({cancellation_ratios[i]}%)", ha='center', va='bottom')

    # Show the plot
    plt.tight_layout()
    plt.savefig('./plots/bookings_vs_cancellations.png')

def plot_avg_lead_time(avg_lead_times):
    print('Plotting average lead times...')
    # Extract hotel names and average lead times
    hotel_names = [list(item[0])[0] for item in avg_lead_times]
    avg_lead_times = [int(item[1]) for item in avg_lead_times]  # Round average lead times to integers

    # Create a figure and axis
    _, ax1 = plt.subplots(figsize=(12, 6))

    # Plot average lead times
    ax1.bar(hotel_names, avg_lead_times, label='Average Lead Time')
    ax1.set_xlabel('Hotel Type')
    ax1.set_title('Average Lead Time')
    ax1.set_ylabel('Days to Arrival')
    ax1.legend()

    # Add labels to the top of each bar
    for i, v in enumerate(avg_lead_times):
        ax1.text(i, v, str(v), ha='center', va='bottom')

    # Show the plot
    plt.tight_layout()
    plt.savefig('./plots/avg_lead_times.png')

def plot_avg_length_of_stay(avg_stay_lengths):
    print('Plotting average length of stay...')
    # Extract hotel names and average length of stay
    hotel_names = [list(item[0])[0] for item in avg_stay_lengths]
    avg_stay_lengths = [int(item[1]) for item in avg_stay_lengths]  # Round average length of stay to integers

    # Create a figure and axis
    _, ax1 = plt.subplots(figsize=(12, 6))

    # Plot average length of stay
    ax1.bar(hotel_names, avg_stay_lengths, label='Average Length of Stay')
    ax1.set_xlabel('Hotel Type')
    ax1.set_title('Average Length of Stay')
    ax1.set_ylabel('Days')
    ax1.legend()

    # Add labels to the top of each bar
    for i, v in enumerate(avg_stay_lengths):
        ax1.text(i, v, str(v), ha='center', va='bottom')

    # Show the plot
    plt.tight_layout()
    plt.savefig('./plots/avg_length_of_stay.png')

def plot_revenue(revenue_data):
    print('Plotting revenue...')
    # Extract hotel names and revenue data
    hotel_names = [item[0] for item in revenue_data]
    revenue = [item[1] for item in revenue_data]

    # Create a figure and axis
    _, ax1 = plt.subplots(figsize=(12, 6))

    # Plot revenue
    ax1.bar(hotel_names, revenue, label='Revenue')
    ax1.plot(hotel_names, revenue, marker='o', color='r')
    ax1.set_xlabel('Hotel Type')
    ax1.set_title('Revenue')
    ax1.set_ylabel('Amount in USD')
    ax1.legend()

    # Add labels above the markers
    for hotel, rev in zip(hotel_names, revenue):
        ax1.text(hotel, rev, f'{rev:.0f}', ha='center', va='bottom')

    # Show the plot
    plt.tight_layout()
    plt.savefig('./plots/revenue.png')

def plot_bookings_by_season(bookings_by_month, cancelled_bookings_by_month):
    print('Plotting bookings by season...')
   
    # Group bookings and cancelled bookings by hotel
    hotel_bookings = {}
    for hotel, month, booking in bookings_by_month:
        hotel_name = list(hotel)[0]
        hotel_bookings.setdefault(hotel_name, []).append((list(month)[0], booking))

    hotel_cancelled_bookings = {}
    for hotel, month, booking in cancelled_bookings_by_month:
        hotel_name = list(hotel)[0]
        hotel_cancelled_bookings.setdefault(hotel_name, []).append((list(month)[0], booking))

    # Seasonal colors
    season_colors = {
        'Winter': 'skyblue',
        'Spring': 'lightgreen',
        'Summer': 'gold',
        'Fall': 'orange'
    }

    # Function to assign seasons to months
    def assign_season(month):
        if month in ['December', 'January', 'February']:
            return 'Winter'
        elif month in ['March', 'April', 'May']:
            return 'Spring'
        elif month in ['June', 'July', 'August']:
            return 'Summer'
        else:
            return 'Fall'

    # Plot for each hotel
    for hotel_name, bookings in hotel_bookings.items():
        months, bookings = zip(*bookings)
        seasons = [assign_season(month) for month in months]
        cancelled_bookings = [booking for month, booking in hotel_cancelled_bookings.get(hotel_name, [])]

        _, ax = plt.subplots(figsize=(12, 6))

        # Plot cancelled bookings first with hatch pattern and clear label
        ax.bar(months, cancelled_bookings, color='red', label='Cancelled', hatch='//')

        # Plot regular bookings with seasonal colors and transparency
        bar_plot = ax.bar(months, bookings, label='Bookings', alpha=0.7) 
        for bar, season in zip(bar_plot, seasons):
            bar.set_color(season_colors[season])

        # Add labels, title, and legend
        ax.set_xlabel('Month')
        ax.set_ylabel('Number of Bookings')
        ax.set_title(f'Bookings by Season for {hotel_name}')

        # Add labels on top of both types of bars
        for i, v in enumerate(bookings):
            ax.text(i, v, str(v), ha='center', va='bottom')

        for i, v in enumerate(cancelled_bookings):
            ax.text(i, v, str(v), ha='center', va='bottom', color='black')
 
        # Legend customization
        ax.legend(title='Booking Type', handles=[
            plt.Rectangle((0, 0), 1, 1, color=season_colors[season], label=season) for season in season_colors
        ] + [plt.Rectangle((0, 0), 1, 1, color='red', label='Cancelled', hatch='//')])

        plt.tight_layout()
        plt.savefig(f'./plots/season_booking_{hotel_name}.png')
    
def plot_bookings_by_market_segment(bookings_by_market_segment):
    print('Plotting bookings by market segment...')
    # Create a dictionary to group bookings by hotel
    hotel_bookings = {}
    for hotel, segment, booking in bookings_by_market_segment:
        hotel_name = list(hotel)[0]
        if hotel_name not in hotel_bookings:
            hotel_bookings[hotel_name] = []
        hotel_bookings[hotel_name].append((list(segment)[0], booking))

    # Create a plot for each hotel
    for hotel_name, bookings in hotel_bookings.items():
        segments, bookings = zip(*bookings)

        # Create a figure and axis for this hotel
        _, ax = plt.subplots(figsize=(12, 6))

        # Plot bookings by market segment
        ax.bar(segments, bookings, label='Bookings')
        ax.set_xlabel('Market Segment')
        ax.set_ylabel('Number of Bookings')
        ax.set_title(f'Bookings by Market Segment for {hotel_name}')
        ax.legend()

        # Add labels to the top of each bar
        for i, v in enumerate(bookings):
            ax.text(i, v, str(v), ha='center', va='bottom')

        # Show/save the plot for this hotel
        plt.tight_layout()
        plt.savefig(f'./plots/market_segment_booking_{hotel_name}.png')

def plot_bookings_by_distribution_channel(bookings_by_distribution_channel):
    print('Plotting bookings by distribution channel...')
    # Create a dictionary to group bookings by hotel
    hotel_bookings = {}
    for hotel, channel, booking in bookings_by_distribution_channel:
        hotel_name = list(hotel)[0]
        channel_name = list(channel)[0] if channel else 'NA'
        if hotel_name not in hotel_bookings:
            hotel_bookings[hotel_name] = []
        hotel_bookings[hotel_name].append((channel_name, booking))

    # Create a plot for each hotel
    for hotel_name, bookings in hotel_bookings.items():
        channels, bookings = zip(*bookings)

        # Create a figure and axis for this hotel
        _, ax = plt.subplots(figsize=(12, 6))

        # Plot bookings by distribution channel
        ax.bar(channels, bookings, label='Bookings')
        ax.set_xlabel('Distribution Channel')
        ax.set_ylabel('Number of Bookings')
        ax.set_title(f'Bookings by Distribution Channel for {hotel_name}')
        ax.legend()

        # Add labels to the top of each bar
        for i, v in enumerate(bookings):
            ax.text(i, v, str(v), ha='center', va='bottom')

        # Show/save the plot for this hotel
        plt.tight_layout()
        plt.savefig(f'./plots/distribution_channel_booking_{hotel_name}.png')

def plot_nightly_stay_rates(nightly_stay_rates, mixed_stay_distributions):
    print('Plotting nightly stay rates and mixed stay distributions...')

    # Extract data from nightly_stay_rates
    hotel_names = [list(item[0])[0] for item in nightly_stay_rates]  # Extract strings
    week_nights_rate = [float(item[1]) for item in nightly_stay_rates]
    weekend_nights_rate = [float(item[2]) for item in nightly_stay_rates]
    both_nights_rate = [float(item[3]) for item in nightly_stay_rates]

    # Extract data from mixed_stay_distributions
    mix_1 = [float(item[0]) for item in mixed_stay_distributions]
    mix_2 = [float(item[1]) for item in mixed_stay_distributions]
    mix_3 = [float(item[2]) for item in mixed_stay_distributions]

    # Create subplots
    _, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Bar chart (ax1)
    bar_width = 0.25  # Adjust bar width as needed
    x_positions = range(len(hotel_names))  # Positions for the bars
    
    ax1.bar([p - bar_width for p in x_positions], week_nights_rate, bar_width, label='Weeknight Rate')
    ax1.bar(x_positions, weekend_nights_rate, bar_width, label='Weekend Rate')
    ax1.bar([p + bar_width for p in x_positions], both_nights_rate, bar_width, label='Both Nights Rate')

    ax1.set_xlabel('Hotel Type')
    ax1.set_title('Nightly Stay Rates')
    ax1.set_ylabel('Rate')
    ax1.set_xticks(x_positions)
    ax1.set_xticklabels(hotel_names)
    ax1.legend()

     # Add labels to the top of each bar, with percentages
    for i, v in enumerate(week_nights_rate):
        ax1.text(i - bar_width, v + 0.05, f'{round(v,2)}%', ha='center', va='bottom')  # Slight adjustment for positioning
        ax1.text(i, weekend_nights_rate[i] + 0.05, f'{round(weekend_nights_rate[i],2)}%', ha='center', va='bottom')
        ax1.text(i + bar_width, both_nights_rate[i] + 0.05, f'{round(both_nights_rate[i],2)}%', ha='center', va='bottom')

    # Pie chart (ax2)
    combined_mix = [mix_1[0], mix_2[0], mix_3[0]]  # Combine data for one pie chart
    ax2.pie(combined_mix, labels=['Wkend 1D', 'Wkend 2D', 'Wkend 3D'], autopct='%1.2f%%', startangle=90)
    ax2.set_title('Mixed Stay Distribution')
    ax2.legend()

    # Show and save the plot
    plt.tight_layout()
    plt.savefig('./plots/nightly_stay_rates.png')

def plot_room_type_preferences(room_type_preferences):
    print('Plotting room type preferences...')
    # Create a dictionary to group room type preferences by hotel
    hotel_room_types = {}
    for hotel, room_type, preference in room_type_preferences:
        hotel_name = list(hotel)[0]
        if hotel_name not in hotel_room_types:
            hotel_room_types[hotel_name] = []
        hotel_room_types[hotel_name].append((list(room_type)[0], preference))

    # Create a plot for each hotel
    for hotel_name, room_types in hotel_room_types.items():
        room_type_names, preferences = zip(*room_types)

        # Create a figure and axis for this hotel
        _, ax = plt.subplots(figsize=(12, 6))

        # Plot room type preferences
        ax.bar(room_type_names, preferences, label='Preferences')
        ax.set_xlabel('Room Type')
        ax.set_ylabel('Preference (%)')
        ax.set_title(f'Room Type Preferences for {hotel_name}')
        ax.legend()

        # Add labels to the top of each bar
        for i, v in enumerate(preferences):
            ax.text(i, v, f'{v}', ha='center', va='bottom')

        # Show/save the plot for this hotel
        plt.tight_layout()
        plt.savefig(f'./plots/room_type_preferences_{hotel_name}.png')

def plot_meal_preferences(meal_preferences):
    print('Plotting meal preferences...')
    # Create a dictionary to group meal preferences by hotel
    hotel_meals = {}
    for hotel, meal, preference in meal_preferences:
        hotel_name = list(hotel)[0]
        if hotel_name not in hotel_meals:
            hotel_meals[hotel_name] = []
        if meal is None:
            meal = "NA"
        hotel_meals[hotel_name].append((list(meal)[0], preference))

    # Create a plot for each hotel
    for hotel_name, meals in hotel_meals.items():
        meal_names, preferences = zip(*meals)

        # Create a figure and axis for this hotel
        _, ax = plt.subplots(figsize=(12, 6))

        # Plot meal preferences
        ax.bar(meal_names, preferences, label='Preferences')
        ax.set_xlabel('Meal Type')
        ax.set_ylabel('Preference (%)')
        ax.set_title(f'Meal Preferences for {hotel_name}')
        ax.legend()

        # Add labels to the top of each bar
        for i, v in enumerate(preferences):
            ax.text(i, v, f'{v}', ha='center', va='bottom')

        # Show/save the plot for this hotel
        plt.tight_layout()
        plt.savefig(f'./plots/meal_preferences_{hotel_name}.png')

def plot_special_requests(special_requests):
    print('Plotting special requests...')

    # Create a dictionary to group special requests by hotel
    hotel_requests = {}
    for hotel_set, request, count_of_rows, percentage in special_requests:
        hotel_name = hotel_set.pop()  # Get the single hotel name from the set
        if hotel_name not in hotel_requests:
            hotel_requests[hotel_name] = []
        hotel_requests[hotel_name].append((request, count_of_rows, percentage))

    # Create a plot for each hotel
    for hotel_name, requests in hotel_requests.items():
        request_names, counts, percentages = zip(*requests)  # Unpack data

        # Create a figure and axis for this hotel
        _, ax = plt.subplots(figsize=(12, 6))

        # Plot special requests
        ax.bar(request_names, counts, label='Counts')
        ax.set_xlabel('Special Request Type')
        ax.set_ylabel('Number of Requests')
        ax.set_title(f'Special Requests for {hotel_name}')
        ax.legend()

        # Add labels to the top of each bar
        for i, v in enumerate(counts):
            ax.text(i, v, f'{v} ({percentages[i]:.2f}%)', ha='center', va='bottom')

        # Show/save the plot for this hotel
        plt.tight_layout()
        plt.savefig(f'./plots/special_requests_{hotel_name}.png')

def plot_demographics(demographics):
    print('Plotting demographics...')
    # Create a dictionary to group demographics by hotel
    hotel_demographics = {}
    for hotel, customer_type, count_of_rows in demographics:
        hotel_name = list(hotel)[0]
        if hotel_name not in hotel_demographics:
            hotel_demographics[hotel_name] = []
        hotel_demographics[hotel_name].append((list(customer_type)[0], count_of_rows))

    # Create a plot for each hotel
    for hotel_name, demographics in hotel_demographics.items():
        customer_types, counts = zip(*demographics)

        # Create a figure and axis for this hotel
        _, ax = plt.subplots(figsize=(12, 6))

        # Plot demographics
        ax.bar(customer_types, counts, label='Counts')
        ax.set_xlabel('Customer Type')
        ax.set_ylabel('Number of Customers')
        ax.set_title(f'Demographics for {hotel_name}')
        ax.legend()

        # Add labels to the top of each bar
        for i, v in enumerate(counts):
            ax.text(i, v, f'{v}', ha='center', va='bottom')

        # Show/save the plot for this hotel
        plt.tight_layout()
        plt.savefig(f'./plots/demographics_{hotel_name}.png')

def plot_single_couple_family_bookings(single_couple_family_bookings):
    print('Plotting single, couple, and family bookings...')
    
    # extract data from single_couple_family_bookings
    hotel_names = [list(item[0])[0] for item in single_couple_family_bookings]
    family_rate = [float(item[1]) for item in single_couple_family_bookings]
    single_rate = [float(item[2]) for item in single_couple_family_bookings]
    couple_rate = [float(item[3]) for item in single_couple_family_bookings]

    # Create a figure and axis
    _, ax1 = plt.subplots(figsize=(12, 6))

    # Bar chart (ax1)
    bar_width = 0.25  # Adjust bar width as needed
    x_positions = range(len(hotel_names))  # Positions for the bars

    # Plot single, couple, and family bookings
    ax1.bar([p - bar_width for p in x_positions], family_rate, bar_width, label='Family Rate')
    ax1.bar(x_positions, single_rate, bar_width, label='Single Rate')
    ax1.bar([p + bar_width for p in x_positions], couple_rate, bar_width, label='Couple Rate')

    ax1.set_title('Single, Couple, and Family Bookings')
    ax1.set_xlabel('Hotel Type')
    ax1.set_ylabel('Rate (%)')
    ax1.set_xticks(x_positions)
    ax1.set_xticklabels(hotel_names)
    ax1.legend()

    # Add labels to the top of each bar
    for i, v in enumerate(family_rate):
        ax1.text(i - bar_width, v + 0.05, f'{round(v,2)}%', ha='center', va='bottom')
        ax1.text(i, single_rate[i] + 0.05, f'{round(single_rate[i],2)}%', ha='center', va='bottom')
        ax1.text(i + bar_width, couple_rate[i] + 0.05, f'{round(couple_rate[i],2)}%', ha='center', va='bottom')

    # Show the plot
    plt.tight_layout()
    plt.savefig('./plots/single_couple_family_bookings.png')

def show_plot():
    plt.show()