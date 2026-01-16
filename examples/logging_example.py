"""Example demonstrating logging configuration for the SDK."""

import logging

from dj_playlist_optimizer import PlaylistOptimizer, Track, HarmonicLevel

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

tracks = [
    Track(id="track_001", key="8A", bpm=128),
    Track(id="track_002", key="8B", bpm=130),
    Track(id="track_003", key="9A", bpm=125),
    Track(id="track_004", key="7A", bpm=132),
    Track(id="track_005", key="8A", bpm=64),
]

optimizer = PlaylistOptimizer(
    bpm_tolerance=10,
    allow_halftime_bpm=True,
    max_violation_pct=0.10,
    harmonic_level=HarmonicLevel.STRICT,
)

result = optimizer.optimize(tracks)

print("\nOptimized Playlist:")
for i, track in enumerate(result.playlist, 1):
    print(f"{i}. {track.id} ({track.key}, {track.bpm} BPM)")

if result.statistics:
    print(f"\nStatistics:")
    print(f"  Coverage: {result.statistics.coverage_pct:.1f}%")
    print(f"  Harmonic transitions: {result.statistics.harmonic_pct:.1f}%")
