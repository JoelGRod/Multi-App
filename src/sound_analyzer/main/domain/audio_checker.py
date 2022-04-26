import pathlib

import numpy
from pydub import AudioSegment
from scipy import signal
from mutagen.mp3 import MP3

from sound_analyzer.main.domain.song import Song

class AudioChecker:

    bitrate_to_min_max_freq = {
                0: 0,
                16: 4000,
                64: 10000,
                128: 15000,
                192: 16000,
                320: 18000,
    }

    def _get_result(self, filename, frequency) -> Song:
        filename = pathlib.Path(filename)
        if filename.suffix in [".wav", ".flac"]:
            return self._analyze_uncompressed(filename, frequency)          
        elif filename.suffix == ".mp3":
            return self._analyze_compressed(filename, frequency)
        return f"Don't know what to expect for {filename}."

    def _analyze_compressed(self, filename, frequency) -> Song:
        mp3_file = MP3(filename)
        bitrate = int(mp3_file.info.bitrate / 1000)
        is_valid = False
        
        for key, val in self.bitrate_to_min_max_freq.items():
            if bitrate < key: break
            expected_max_freq = val
        if frequency > expected_max_freq:
            is_valid = True
        return Song(pathlib.Path(
                filename).stem, filename, is_valid, bitrate, f"{frequency:.0f}"
            )

    def _analyze_uncompressed(self, filename, frequency) -> Song:
        is_valid = False
        if frequency > 19000: is_valid = True
        return Song(pathlib.Path(
                filename).stem, filename, is_valid, 19000, f"{frequency:.0f}"
            )

    def check_file(self, filename, window_length_s: float = 0.05, channel: int = 0) -> Song:
        track = AudioSegment.from_file(filename)

        assert track.channels is not None
        out = numpy.array(track.get_array_of_samples()).reshape(-1, track.channels)
        nperseg = (None if window_length_s is None 
                        else int(round(window_length_s * track.frame_rate)))

        # Use the first channel by default
        f, _, Sxx = signal.spectrogram(
            out[:, channel],
            fs=track.frame_rate,
            scaling="spectrum",
            mode="magnitude",
            # nperseg=window_length_samples
            nperseg=nperseg,
            # noverlap=noverlap
        )
        # Make sure all values are positive for the log scaling
        smallest_positive = numpy.min(Sxx[Sxx > 0])
        Sxx[Sxx < smallest_positive] = smallest_positive
        # Which row surpasses the average first?
        log_Sxx = numpy.log10(Sxx)
        avg_log_Sxx = numpy.average(log_Sxx)
        count = numpy.sum(log_Sxx > avg_log_Sxx, axis=1)
        k = numpy.where(count > log_Sxx.shape[1] / 8)[0][-1]

        # What do we expect?
        return self._get_result(filename, f[k])
        


