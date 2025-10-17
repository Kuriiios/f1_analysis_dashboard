🏁 F1 2025 Race Data Dashboard - README

This repository hosts the code for an interactive Formula 1 Data Analysis Dashboard built using Streamlit and powered by the fastf1 library. The project's primary goal is to provide a real-time (or post-session) analytical view of F1 sessions, with a strong focus on the 2025 season, enabling detailed teammate performance comparison and race strategy analysis.

🚨 PROJECT STATUS: PROTOTYPE & ACTIVE DEVELOPMENT 🚧

This is currently a foundational prototype for a much larger project.

The code presented here is the first major iteration and is under active, heavy development. The primary focus is on data accuracy, establishing the core data ingestion and transformation logic, and validating the visualization components.

    Non-Final State: Expect frequent changes, refactoring, and potentially incomplete features or styling.

    Focus: Prioritizing backend integrity (data fetching/cleaning with fastf1) over final front-end polish.

🚀 Getting Started

Prerequisites

    Python 3.x

    Streamlit

    fastf1

    Pandas

    NumPy

    Matplotlib/Seaborn (for chart components, assumed from component names)

Installation

    Clone the repository (assuming this code is the core of a larger project):
    Bash

git clone [repository-url]
cd [repository-name]

Install dependencies:
Bash

pip install -r requirements.txt # (Assuming you have a requirements.txt file)
# or install the core libraries:
pip install streamlit fastf1 pandas numpy

Run the Streamlit App:
Bash

    streamlit run main_app.py # (Assuming the main file is named main_app.py based on imports)

📊 Dashboard Features

The dashboard is structured into three main views, allowing for comprehensive data exploration and visual analysis.

1. Main Dashboard View (render_dashboard)

This view provides an extensive, multi-panel snapshot of the selected session up to a specific lap or minute, ideal for live monitoring or post-session review.
Section	Chart Component	Description
Current Performance	get_last_laps	Timing data for the most recent laps (all drivers).
	get_track_status	Visualizes the current track status (Green, Yellow, Red flags).
	get_last_laps_per_driver (x2)	Detailed lap analysis for each of the selected team's two drivers.
Contextual Data	get_team_radio_chart	Visual representation/timeline of team radio messages.
	get_weather_info	Displays current or historical weather conditions.
	get_race_control_message	Logs and displays messages from Race Control.
	get_lap_and_tyre	Visualizes lap numbers and corresponding tyre compound usage.
Best Performance & Track	get_map	Interactive or static map showing car location or track delta (requires telemetry).
	get_best (x5)	Shows the current best times for Sector 1, Sector 2, Sector 3, Lap Time, and Theoretical Best (calculated from best sectors) across the session.

2. Race Recap View (render_race_recap)

Focuses on in-depth post-race analysis, particularly strategy and pace comparison between teammates.
Chart Component	Description
show_pace_comp (x2)	Comparison of overall race pace for the two selected drivers.
show_laptime_scatterplot	Scatter plot comparing all valid lap times between the two drivers.
show_laptime_comp	Lap time trend comparison plot (e.g., delta time over race distance).
show_tyre_strategy	Detailed visualization of tyre strategies, including stint length and compound choice.

3. Home/Overview View (render_home)

Serves as the project's landing page, providing an overview of its goals, status, and author information.

⚙️ Data and Logic

The dashboard uses a structured data pipeline:

    fastf1 Library: Used for fetching and processing raw F1 session data (telemetry, timing, etc.).

    data.fetch_data: Handles the retrieval of session data.

    logic.transform: Contains functions for data manipulation, such as identifying the session type (event_format) and handling qualifying time ranges (quali_session_range).

    logic.sidebar: Manages the Streamlit sidebar, allowing users to select the Year (2023-2025 supported), Race, Session (Practice, Qualifying, Race, Sprint), Team, and control the visualization parameters like Lap/Minute selection and Chart Height.

Key Data Handling Functionality

    Session Selection: Supports both Conventional and Sprint Qualifying weekends, adapting the available sessions accordingly (e.g., 2025 sprint races are at rounds 2, 5, 13, 19, 21, 23).

    Data Styling: The style_lap_df function provides visual enhancements to data tables:

        Driver Colors: Applies F1 team colors to driver names.

        Personal Bests: Highlights personal best sector/lap times in green.

        Overall Bests: Highlights the overall session fastest times in purple.

        Tyre Colors: Applies background colors to match tyre compounds (Soft-Red, Medium-Yellow, Hard-White, etc.).

    Time Formatting: Custom functions (microseconds_to_mmss, seconds_to_mmss) ensure lap times are displayed in the standard M:SS format.

⚠️ Project Status

This project is under active development.

The primary focus is currently on data accuracy, backend logic, and the creation of core visualizations.

Next Steps & Planned Enhancements:

    Full implementation and styling of all components within dashboard_charts and race_recap_charts.

    Introduction of a dedicated Driver Comparison page/dashboard.

    Major UI/UX improvements, including integrating team logos, smoother data loading, and interactive chart filtering.

    More in-depth telemetry analysis (e.g., G-force, steering angle plots).

👨‍💻 Author

Cyril Leconte 📍 Créteil, France

📧 cyril.leconte@proton.me

🔗 LinkedIn | GitHub