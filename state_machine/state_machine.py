# State machine code: picks the next state based on the current state and the input event. 
# It also handles transitions and actions associated with each state.

from dataclasses import dataclass
from enum import Enum

class State(Enum):
    IDLE = "IDLE"
    TRACKING = "TRACKING"
    HOVERING = "HOVERING"
    DOCKING_UNIT = "DOCKING_UNIT"
    DOCKING_APPROACH = "DOCKING_APPROACH"
    DOCKED = "DOCKED"
    ABORT = "ABORT"
    EMERGENCY_LAND = "EMERGENCY_LAND"


@dataclass
class Bird:
    type: str | None = None
    detected: bool = False
    distance_m: float | None = None


@dataclass
class Battery:
    percentage: float = 100.0
    low: bool = False

@dataclass
class Safety:
    people_nearby: bool = False
    cart_moving: bool = False
    weather: str = "CLEAR"
    camera_ok: bool = True
    comm_ok: bool = True

@dataclass
class Docking:
    should_dock: bool = False
    reason: str | None = None
    aborted: bool = False

@dataclass
class Observation:
    bird: Bird | None = None
    battery: Battery | None = None
    safety: Safety | None = None
    docking: Docking | None = None

def step(state: State, observation: Observation) -> tuple[State, str | None]:
    # Placeholder logic for state transition
    if state == State.IDLE:
        if observation.bird and observation.bird.detected:
            return State.TRACKING, "Bird detected"
    elif state == State.TRACKING:
        if not observation.bird or not observation.bird.detected:
            return State.IDLE, "Bird not detected"
    # Add more state transition logic as needed
    return state, None