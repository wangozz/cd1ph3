def clockConverter(hour, minute, period):
    if period == "am":
        if hour == 12:
            hour_24 = 0
        else:
            hour_24 = hour
    else:  # period == "pm"
        if hour == 12:
            hour_24 = 12
        else:
            hour_24 = hour + 12
            
    return f"{hour_24:02d}{minute:02d}"
