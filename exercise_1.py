def direction(facing, turn):
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    try:
        turning = turn // 45
        final_direction = (directions.index(facing) + turning) % len(directions)
        return directions[final_direction]
    except Exception as err:
        return f'The error {err} occurred'
