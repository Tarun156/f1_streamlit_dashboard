import fastf1

def get_qualifying_session(year, grand_prix):
    """
    Fetches the qualifying session data for a given year and grand prix.

    Parameters:
    year (int): The year of the Formula 1 season.
    grand_prix (str): The name of the grand prix.

    Returns:
    fastf1.Qualifying: The qualifying session data.
    """
    session = fastf1.get_session(year, grand_prix, 'Q')

    session.load()

    return session


def get_season_schedule(year):
    """
    Fetches the season schedule for a given year.

    Parameters:
    year (int): The year of the Formula 1 season.

    Returns:
    list: A list of grand prix names for the specified year.
    """
    schedule = fastf1.get_event_schedule(year)
    return schedule["EventName"].tolist()