from ..constants import MINIMUM_AUDIO_LEVEL, validate_level
from math import sin, pi
from typing import Self


class SineWave:
    def __init__(
            self,
            amplitude: float,
            frequency: float,
            samplerate: int
    ) -> None:
        self.amplitude = amplitude
        self.frequency = frequency
        self.samplerate = samplerate

    # ==================================================================================================================
    # Generator Methods
    # ==================================================================================================================
    def __iter__(self) -> Self:
        self.__value: float = MINIMUM_AUDIO_LEVEL
        return self
    
    def __next__(self) -> float:
        sample: float = self.__calculate_sample()
        self.__value += self.__sine_angle
        return sample

    # ==================================================================================================================
    # Sample Calculator
    # ==================================================================================================================
    def __calculate_sample(self) -> float:
        return self.amplitude * sin(self.__value)

    # ==================================================================================================================
    # Properties
    # ==================================================================================================================
    @property
    def __sine_angle(self) -> float:
        return 2 * pi * self.frequency / self.samplerate

    # ------------------------------------------------------------------------------------------------------------------
    # Amplitude
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def amplitude(self) -> float:
        return self.__amplitude
    
    @amplitude.setter
    def amplitude(
            self,
            value: float
    ) -> None:
        self.__amplitude: float = validate_level(value)

    # ------------------------------------------------------------------------------------------------------------------
    # Frequency
    # ------------------------------------------------------------------------------------------------------------------
    @property
    def frequency(self) -> float:
        return self.__frequency
    
    @frequency.setter
    def frequency(
            self,
            value: float
    ) -> None:
        self.__frequency: float = abs(value)

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
