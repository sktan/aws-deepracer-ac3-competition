""" Our DeepRacer training code """

SPEED_THRESHOLD = 5
ABS_STEERING_THRESHOLD = 20.0
TOTAL_NUM_STEPS = 200

def reward_straight_track(params):
    """ Determines if a track is going straight for the next x waypoints """
    waypoints = params['waypoints']
    closest_waypoints = params['closest_waypoints']

    # Make sure we dont go out of bounds for our waypoints array
    if closest_waypoints[1] + 1 < len(waypoints):
        prev_point = waypoints[closest_waypoints[0]]
        next_point = waypoints[closest_waypoints[1]]
        next_point2 = waypoints[closest_waypoints[1] + 1]

        ydiff1 = next_point[0] - prev_point[0]
        ydiff2 = next_point2[0] - prev_point[0]
        xdiff1 = next_point[1] - prev_point[1]
        xdiff2 = next_point2[1] - prev_point[1]

        slope1 = 0
        slope2 = 0
        if xdiff1 == 0:
            slope1 = ydiff1
        elif ydiff1 == 0:
            slope1 = xdiff1
        else:
            slope1 = ydiff1 / xdiff1
        if xdiff2 == 0:
            slope2 = ydiff2
        elif ydiff2 == 0:
            slope2 = xdiff2
        else:
            slope2 = ydiff2 / xdiff2

        # If is a straight line and we're not steering too much
        # we'll give a reward
        if slope1 == slope2 and abs(params['steering_angle']) < 5:
            return 2
        # Otherwise if it's a straight line, and we're oversteering
        # punish the model a bit
        if slope1 == slope2 and abs(params['steering_angle']) > 5:
            return 0.8
    # Otherwise, we'll just not modify our rewards
    return 1

def reward_function(params):
    """ Reward function for training our deep racer """
    # Initialise rewards
    reward = 1

    # Deepracer parameters
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steps = params['steps']
    progress = params['progress']

    # Penalise if car moves too slowly
    if speed < SPEED_THRESHOLD:
        reward *= 0.8

    marker_1 = 0.1 * track_width
    marker_2 = 0.5 * track_width

    # Penalise if too far away from the centre
    if distance_from_center <= marker_1:
        reward *= 1.2
    elif distance_from_center <= marker_2:
        reward *= 0.5

    # Penalise if steering too much
    reward *= reward_straight_track(params)

    # Give additional reward if the car pass every 50 steps faster than expected
    if (steps % 50) == 0 and progress > (steps / TOTAL_NUM_STEPS) * 100:
        reward += 10.0

    # Give more rewards the further my car goes
    if progress >= 90:
        reward *= 1.4
    elif progress >= 80:
        reward *= 1.3
    elif progress >= 70:
        reward *= 1.2
    elif progress >= 60:
        reward *= 1.1

    # Penalise heavily if wheels go off track
    if all_wheels_on_track:
        reward *= 1.2
    else:
        reward *= 0.01
    return float(reward)
