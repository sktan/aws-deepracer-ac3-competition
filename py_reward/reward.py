""" Our DeepRacer training code """

SPEED_THRESHOLD = 3
ABS_STEERING_THRESHOLD = 20.0

def reward_function(params):
    """ Reward function for training our deep racer """
    # Initialise rewards
    reward = 1

    # Deepracer parameters
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    steering = abs(params['steering_angle'])

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
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    # Penalise heavily if wheels go off track
    if all_wheels_on_track:
        reward *= 1.2
    else:
        reward *= 0.01
    return float(reward)
