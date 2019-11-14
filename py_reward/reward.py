""" Our DeepRacer training code """

SPEED_THRESHOLD = 3
def reward_function(params):
    """ Reward function for training our deep racer """
    reward = 1
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']

    if speed < SPEED_THRESHOLD:
        reward *= 0.8

    marker_1 = 0.1 * track_width
    marker_2 = 0.5 * track_width

    if distance_from_center <= marker_1:
        reward *= 1.2
    elif distance_from_center <= marker_2:
        reward *= 0.5

    if all_wheels_on_track:
        reward *= 1.2
    else:
        reward *= 0.01
    return float(reward)
