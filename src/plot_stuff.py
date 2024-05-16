
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt

def plot_bookings(total_bookings, cancellations_data):
    print('Plotting bookings vs. cancellations...')
    # Extract hotel names, bookings, cancellations, and cancellation ratios
    hotel_names = [list(item[0])[0] for item in total_bookings]
    bookings = [item[1] for item in total_bookings]
    cancellations = [item[1] for item in cancellations_data]
    cancellation_ratios = [round(float(item[2]), 2) for item in cancellations_data]

    # Create a figure and axis
    fig, ax1 = plt.subplots(figsize=(12, 6))

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
    fig, ax1 = plt.subplots(figsize=(12, 6))

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
    fig, ax1 = plt.subplots(figsize=(12, 6))

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
    fig, ax1 = plt.subplots(figsize=(12, 6))

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

def plot_bookings_by_season(bookings_by_month):
    print('Plotting bookings by season...')
    # Create a dictionary to group bookings by hotel
    hotel_bookings = {}
    for hotel, month, booking in bookings_by_month:
        hotel_name = list(hotel)[0]
        if hotel_name not in hotel_bookings:
            hotel_bookings[hotel_name] = []
        hotel_bookings[hotel_name].append((list(month)[0], booking))

    # Define seasonal colors
    season_colors = {
        'Winter': 'skyblue',
        'Spring': 'lightgreen',
        'Summer': 'gold',
        'Fall': 'orange'
    }

    # Assign seasons to months
    def assign_season(month):
        if month in ['December', 'January', 'February']:
            return 'Winter'
        elif month in ['March', 'April', 'May']:
            return 'Spring'
        elif month in ['June', 'July', 'August']:
            return 'Summer'
        else:
            return 'Fall'

    # Create a plot for each hotel
    for hotel_name, bookings in hotel_bookings.items():
        months, bookings = zip(*bookings)
        seasons = [assign_season(month) for month in months]

        # Create a figure and axis for this hotel
        fig, ax = plt.subplots(figsize=(12, 6))

        # Plot bookings with seasonal colors
        bar_plot = ax.bar(months, bookings, label='Bookings')
        for bar, season in zip(bar_plot, seasons):
            bar.set_color(season_colors[season])

        # Add labels, title, and legend
        ax.set_xlabel('Month')
        ax.set_ylabel('Number of Bookings')
        ax.set_title(f'Bookings by Season for {hotel_name}')

        # Add labels to the top of each bar
        for i, v in enumerate(bookings):
            ax.text(i, v, str(v), ha='center', va='bottom')
        ax.legend(title='Season', handles=[plt.Rectangle((0,0),1,1, color=season_colors[season], label=season) for season in season_colors])
        # Show/save the plot for this hotel
        plt.tight_layout()
        plt.savefig(f'./plots/season_booking_{hotel_name}.png')
    
def plot_bookings_by_market_segment(bookings_by_market_segment):
    pass

def plot_bookings_by_distribution_channel(bookings_by_distribution_channel):
    pass



def show_plot():
    plt.show()