def lon_lat_to_coords(lat, lon):
    return (int((lat+90.0)/.5), int((lon+180)/.625))

