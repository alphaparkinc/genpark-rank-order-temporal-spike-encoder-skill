from client import RankOrderEncoder

def main():
    print("=== Rank Order Temporal Spike Encoder ===")
    encoder = RankOrderEncoder(time_window_ms=20.0)
    features = [0.15, 0.92, 0.44, 0.78]

    res = encoder.encode(features)
    print("Encoded Spikes:", res["spikes_sequence"])
    # Channel 1 (0.92) must spike first at 0.0ms
    assert res["spikes_sequence"][0]["channel"] == 1
    assert res["spikes_sequence"][0]["spike_time_ms"] == 0.0

    print("Rank Order Temporal Spike Encoder verified successfully!")

if __name__ == "__main__":
    main()
