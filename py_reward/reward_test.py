import pylint
import reward

def test_reward_straight_track_success():
  """ Test to see if a straight track results in rewarding 2x """
  params = {
    'waypoints': [
      [0, 1], [1, 2], [2, 3], [3, 4]
    ],
    'closest_waypoints': [1, 2],
    'steering_angle': 0
  }
  assert reward.reward_straight_track(params) == 2

def test_reward_straight_track_end():
  """ Test to see if a straight track results in rewarding 2x """
  params = {
    'waypoints': [
      [0, 1], [1, 2], [2, 3], [3, 4]
    ],
    'closest_waypoints': [2, 3],
    'steering_angle': 0
  }
  assert reward.reward_straight_track(params) == 1

def test_reward_straight_track_oversteer():
  """ Test to see if a straight track results in rewarding 2x """
  params = {
    'waypoints': [
      [0, 1], [1, 2], [2, 3], [3, 4]
    ],
    'closest_waypoints': [1, 2],
    'steering_angle': 15
  }
  assert reward.reward_straight_track(params) == 0.8

def test_reward_straight_track_fail():
  """ Test to see if a non-straight track results in rewarding 1x """
  params = {
    'waypoints': [
      [0, 1], [0, 2], [0, 3], [0, 15]
    ],
    'closest_waypoints': [1, 2],
    'steering_angle': 0
  }
  assert reward.reward_straight_track(params) == 1
