class RankOrderEncoder:
    """Rank-Order Coding (ROC) temporal spike converter."""
    def __init__(self, time_window_ms: float = 50.0):
        self.time_window = time_window_ms

    def encode(self, features: list[float]) -> dict:
        if not features:
            return {"spikes": []}

        # Sort indices by feature strength in descending order
        sorted_pairs = sorted(enumerate(features), key=lambda x: x[1], reverse=True)
        N = len(features)

        spike_events = []
        for rank, (channel_id, value) in enumerate(sorted_pairs):
            # Earliest spike for highest value, linear rank-delay mapping
            spike_time = (rank / max(1, N - 1)) * self.time_window
            spike_events.append({
                "channel": channel_id,
                "spike_time_ms": round(spike_time, 2),
                "rank": rank,
                "intensity": round(value, 4)
            })

        return {
            "channels_count": N,
            "window_duration_ms": self.time_window,
            "spikes_sequence": spike_events
        }
