def event_format(year, race_number):
    match year:
        case 2023:
            if race_number in [5, 11, 14, 19, 20, 22]:
                return 'sprint_qualifying'
            else:
                return 'conventional'
        case 2024:
            if race_number in [5, 6, 11, 19, 21, 23]:
                return 'sprint_qualifying'
            else:
                return 'conventional'
        case 2025:
            if race_number in [2, 5, 13, 19, 21, 23]:
                return 'sprint_qualifying'
            else:
                return 'conventional'

def quali_session_range(session_laps):
    quali_session_last_minute = int((max(session_laps.Time) - min(session_laps.Time)).total_seconds()//60) +1
    quali_range = range(0, quali_session_last_minute)
    return quali_range