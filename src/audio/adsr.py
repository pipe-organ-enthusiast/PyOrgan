from ..constants import ADSR_PHASES, MINIMUM_AUDIO_LEVEL, MAXIMUM_AUDIO_LEVEL, validate_level
from typing import Self


class ADSR:
    def __init__(
            self,
            attack_time: float,
            decay_time: float,
            sustain_level: float,
            release_time: float,
            samplerate: int
    ) -> None:
        self.attack_time = attack_time
        self.decay_time = decay_time
        self.sustain_level = sustain_level
        self.release_time = release_time
        self.samplerate = samplerate

    # ==================================================================================================================
    # Generator Methods
    # ==================================================================================================================
    def __iter__(self) -> Self:
        self.__value: float = MINIMUM_AUDIO_LEVEL
        self.__phase: ADSR_PHASES = ADSR_PHASES.ATTACK
        return self

    def __next__(self) -> float:
        modifier: float = self.__value
        self.__update_value()
        return modifier

    # ==================================================================================================================
    # ADSR Phase Control
    # ==================================================================================================================
    def __update_value(self) -> None:
        match self.__phase:
            case ADSR_PHASES.ATTACK:
                self.__value += self.__attack_modifier
                self.__check_upper_limit(
                    limit=MAXIMUM_AUDIO_LEVEL, 
                    new_phase=ADSR_PHASES.DECAY
                )
            case ADSR_PHASES.DECAY:
                self.__value -= self.__decay_modifier
                self.__check_lower_limit(
                    limit=self.sustain_level,
                    new_phase=ADSR_PHASES.SUSTAIN
                )
            case ADSR_PHASES.SUSTAIN:
                self.__value = self.sustain_level
            case ADSR_PHASES.RELEASE:
                self.__value -= self.__release_modifier
                self.__check_lower_limit(
                    limit=MINIMUM_AUDIO_LEVEL,
                    new_phase=ADSR_PHASES.COMPLETE
                )
            case ADSR_PHASES.COMPLETE:
                self.__value = MINIMUM_AUDIO_LEVEL

    def __check_upper_limit(
            self,
            limit: float,
            new_phase: ADSR_PHASES
    ) -> None:
        if self.__value >= limit:
            self.__update_phase(limit, new_phase)

    def __check_lower_limit(
            self,
            limit: float,
            new_phase: ADSR_PHASES
    ) -> None:
        if self.__value <= limit:
            self.__update_phase(limit, new_phase)

    def __update_phase(
            self,
            limit: float,
            new_phase: ADSR_PHASES
    ) -> None:
        self.__value = limit
        self.__phase = new_phase

    def start_release_phase(self) -> None:
        self.__phase = ADSR_PHASES.RELEASE

    # ==================================================================================================================
    # Properties
    # ==================================================================================================================
    # ------------------------------------------------------------------------------------------------------------------
    # Value Modifiers
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def __attack_modifier(self) -> float:
        return MAXIMUM_AUDIO_LEVEL / (self.attack_time * self.samplerate)

    @property
    def __decay_modifier(self) -> float:
        return (MAXIMUM_AUDIO_LEVEL - self.sustain_level) / (self.decay_time * self.samplerate)

    @property
    def __release_modifier(self) -> float:
        return self.sustain_level / (self.release_time * self.samplerate)

    # ------------------------------------------------------------------------------------------------------------------
    # Attack Time
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def attack_time(self) -> float:
        return self.__attack_time

    @attack_time.setter
    def attack_time(
            self,
            value: float
    ) -> None:
        self.__attack_time: float = abs(value)

    # ------------------------------------------------------------------------------------------------------------------
    # Decay Time
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def decay_time(self) -> float:
        return self.__decay_time

    @decay_time.setter
    def decay_time(
            self,
            value: float
    ) -> None:
        self.__decay_time: float = abs(value)

    # ------------------------------------------------------------------------------------------------------------------
    # Sustain Level
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def sustain_level(self) -> float:
        return self.__sustain_level

    @sustain_level.setter
    def sustain_level(
            self,
            value: float
    ) -> None:
        self.__sustain_level: float = validate_level(value)

    # ------------------------------------------------------------------------------------------------------------------
    # Release Time
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def release_time(self) -> float:
        return self.__release_time

    @release_time.setter
    def release_time(
            self,
            value: float
    ) -> None:
        self.__release_time: float = abs(value)

    # ------------------------------------------------------------------------------------------------------------------
    # Samplerate
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def samplerate(self) -> int:
        return self.__samplerate

    @samplerate.setter
    def samplerate(
            self,
            value: int
    ) -> None:
        self.__samplerate: int = abs(value)
