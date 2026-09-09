import sys
import json
from client import RankOrderEncoder

def handle_request(req):
    method = req.get("method")
    params = req.get("params", {})
    if method == "encode":
        enc = RankOrderEncoder(params.get("window_ms", 50.0))
        return enc.encode(params.get("features", [0.2, 0.8, 0.5]))
    return {"error": "Unknown method"}

def main():
    for line in sys.stdin:
        if not line.strip():
            continue
        req = json.loads(line)
        res = handle_request(req)
        print(json.dumps(res))
        sys.stdout.flush()

if __name__ == "__main__":
    main()
