from .constants import *
from dataclasses import dataclass, field


# ######################################################################################################################
# Organ Editing
# ######################################################################################################################
@dataclass
class OrganSettings:
    number_divisions: int = MINIMUM_DIVISIONS
    number_couplers: int = MINIMUM_COUPLERS
    number_generals: int = MINIMUM_GENERALS
    include_crescendo: bool = False


@dataclass
class DivisionSettings:
    division_number: int = 1
    division_name: str = DIVISION_NAMES[0]
    number_stops: int = MINIMUM_STOPS
    number_divisional_couplers: int = MINIMUM_DIVISIONAL_COUPLERS
    number_divisionals: int = MINIMUM_DIVISIONALS
    include_tremulant: bool = False
    include_enclosure: bool = False


@dataclass
class StopSettings:
    division_name: str = DIVISION_NAMES[0]
    stops: list[str] = field(default_factory=list[str])


@dataclass
class DivisionalCouplerSettings:
    division_name: str = DIVISION_NAMES[0]
    coupler_number: int = 1
    coupler_type: str = DIVISIONAL_COUPLER_TYPES[0]


@dataclass
class TremulantSettings:
    division_name: str = DIVISION_NAMES[0]
    depth: float = MINIMUM_AUDIO_LEVEL
    rate: float = MINIMUM_RATE


@dataclass
class EnclosureSettings:
    division_name: str = DIVISION_NAMES[0]
    minimum_volume: float = MINIMUM_AUDIO_LEVEL
    maximum_volume: float = MAXIMUM_AUDIO_LEVEL


# ######################################################################################################################
# Stop Editing
# ######################################################################################################################
@dataclass
class StopInformation:
    stop_name: str
    stop_family: str = STOP_FAMILIES[0]
    number_ranks: int = MINIMUM_RANKS


@dataclass
class RankInformation:
    rank_number: int = 1
    rank_size: str = RANK_SIZES[0]
    number_pipes: int = NUMBER_PIPES_LIST[0]
    starting_note: str = NOTES[0]


@dataclass
class PipeInformation:
    pipe_construction: str = PIPE_CONSTRUCTION_TYPES[0]
    pipe_type: str = PIPE_TYPES[0]
    number_harmonics: int = MINIMUM_HARMONICS


@dataclass
class AdsrSettings:
    attack_time: float = MINIMUM_TIME
    decay_time: float = MINIMUM_TIME
    sustain_level: float = MINIMUM_TIME
    release_time: float = MINIMUM_TIME


@dataclass
class HarmonicInformation:
    harmonic_number: int = 1
    amplitude: float = MINIMUM_AUDIO_LEVEL
    adsr: AdsrSettings = AdsrSettings()


@dataclass
class PipeSettings:
    pipe_number: int = 1
    note: str = NOTES[0]
    harmonics: list[HarmonicInformation] = field(default_factory=list[HarmonicInformation()])
    adsr: AdsrSettings = AdsrSettings()


# ######################################################################################################################
# Application Settings
# ######################################################################################################################
@dataclass
class GeneralConsoleSettings:
    number_manuals: int
    include_pedals: bool
    number_thumb_pistons: int
    number_toe_studs: int
    number_swell_shoes: int
    number_stop_controls: int


@dataclass
class AudioSettings:
    audio_device: str
    number_channels: int
    block_size: int
    latency: str | float


@dataclass
class MetronomeSettings:
    number_beats: int
    beats_minute: int


@dataclass
class MidiDevices:
    input_devices: list[str] = field(default_factory=list[str])
    output_devices: list[str] = field(default_factory=list[str])


@dataclass
class DivisionMidiSettings:
    division_name: str
    midi_device: str
    midi_channel: int
    lowest_note: int
    highest_note: int
    note_off: int
    note_on: int


@dataclass
class ControlMidiSettings:
    control: str
    midi_device: str
    midi_channel: int
    midi_note: int
    note_off: int
    note_on: int
