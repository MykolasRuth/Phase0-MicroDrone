from state_machine.state_machine import step, State, Observation, Bird, Battery, Safety, Docking

def test_idle_to_tracking():
    observation = Observation(bird=Bird(detected=True))
    new_state, reason = step(State.IDLE, observation)
    assert new_state == State.TRACKING
    assert reason == "Bird detected"

def test_tracking_to_idle():
    observation = Observation(bird=Bird(detected=False))
    new_state, reason = step(State.TRACKING, observation)
    assert new_state == State.IDLE
    assert reason == "Bird not detected"

def make_observation(bird = None, battery = None, safety = None, docking = None): 
    # Makes observations for testing purposes
    return Observation(
        bird=bird or Bird(detected=False),
        battery=battery or Battery(),
        safety=safety or Safety(),
        docking=docking or Docking()
    )

def test_idle_to_detected_bird():
    observation = make_observation(bird=Bird(type="sparrow", detected=True, distance_m=5))
    assert step(State.IDLE, observation) == (State.TRACKING, "Bird detected")

def test_lost_bird_to_idle():
    observation = make_observation(bird=Bird(detected=False))
    assert step(State.TRACKING, observation) == (State.IDLE, "Bird not detected")