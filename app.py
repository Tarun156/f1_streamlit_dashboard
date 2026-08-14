import streamlit as st
import pandas as pd
import datetime as dt

from src.f1_data import get_qualifying_session
from src.f1_data import get_season_schedule
from src.utilities import PROJECT_ROOT, ensure_directory_exists

# Define the path to the data directory
data_path = PROJECT_ROOT / "data"

# Current year
current_year = dt.datetime.now().year

st.markdown("#### 🏎️ Formula 1 Qualifying Analytics Dashboard")

# Select the year for the F1 season
year = st.selectbox("Select Year", list(range(2021, current_year + 1)), index=current_year - 2021)

# Fetch the season schedule for the selected year and save it to a CSV file
schedule = get_season_schedule(int(year))
grand_prix_schedule = pd.DataFrame(schedule, columns=["Grand Prix"])
schedule_path = data_path / "schedules" / str(year) / "grand_prix_schedule.csv"
ensure_directory_exists(schedule_path.parent)
grand_prix_schedule.to_csv(schedule_path, index=False)


# Read the grand prix options from the CSV file
grandprix_options = pd.read_csv(schedule_path)["Grand Prix"].tolist()

grandprix = st.selectbox(
    "Select Grand Prix",
    ["Select Grand Prix"] + grandprix_options,
)

# Select the grand prix for the qualifying session
if st.button("Load Qualifying Session Data"):

    with st.spinner("Fetching Qualifying Session Data..."):
        session = get_qualifying_session(year, grandprix)

        session_results = session.results
        qualifying_results_path = data_path / "qualifying_results" / f"{year}_{grandprix}_qualifying_results.csv"
        ensure_directory_exists(qualifying_results_path.parent)
        session_results.to_csv(qualifying_results_path, index=False)
        saved_session_results = pd.read_csv(qualifying_results_path)
        st.success("Qualifying Session Data Loaded Successfully!")

        # Display session data
        st.subheader(f"Qualifying Session Data for {grandprix} ({year})")
        st.write(saved_session_results)