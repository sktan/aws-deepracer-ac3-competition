""" Our DeepRacer training code """

SPEED_THRESHOLD = 5
ABS_STEERING_THRESHOLD = 20.0
TOTAL_NUM_STEPS = 250

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
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

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
