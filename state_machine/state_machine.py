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



