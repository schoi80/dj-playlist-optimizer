"""DJ Playlist Optimizer - Harmonic mixing with Google OR-Tools."""

from dj_playlist_optimizer.bpm import bpm_compatible, get_bpm_difference
from dj_playlist_optimizer.camelot import (
    get_compatible_keys,
    is_harmonic_compatible,
    parse_camelot_key,
)
from dj_playlist_optimizer.models import (
    HarmonicLevel,
    PlaylistResult,
    PlaylistStatistics,
    Track,
    TransitionInfo,
)
from dj_playlist_optimizer.optimizer import PlaylistOptimizer

__version__ = "0.1.0"

__all__ = [
    "HarmonicLevel",
    "PlaylistOptimizer",
    "PlaylistResult",
    "PlaylistStatistics",
    "Track",
    "TransitionInfo",
    "bpm_compatible",
    "get_bpm_difference",
    "get_compatible_keys",
    "is_harmonic_compatible",
    "parse_camelot_key",
]
