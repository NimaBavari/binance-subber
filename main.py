import json
from datetime import datetime

import websocket

WS_API_URL = "wss://stream.binance.com:9443/stream?streams=%s"

stream_list = [
    "btcusdt@trade",
    "ethusdt@trade",
    "btcusdt@aggTrade",
    "ethusdt@aggTrade",
    "btcusdt@kline_1m",
    "ethusdt@kline_1m",
]
stream_str = "/".join(stream_list)
ws = websocket.create_connection(WS_API_URL % stream_str)

payload_str = json.dumps(
    {
        "method": "SUBSCRIBE",
        "params": stream_list,
        "id": 1,
    }
)
ws.send(payload_str)

report_mapping = {
    "btcusdt@trade": {"last_seen": None, "latencies": [], "restart_time": None},
    "ethusdt@trade": {"last_seen": None, "latencies": [], "restart_time": None},
    "btcusdt@aggTrade": {"last_seen": None, "latencies": [], "restart_time": None},
    "ethusdt@aggTrade": {"last_seen": None, "latencies": [], "restart_time": None},
}
for msg in ws:
    resp = json.loads(msg)
    stream = resp.get("stream", None)
    if stream in report_mapping:
        if not report_mapping[stream]["latencies"]:
            report_mapping[stream]["restart_time"] = datetime.now().timestamp()
        if datetime.now().timestamp() - report_mapping[stream]["restart_time"] > 60:
            report_mapping[stream]["restart_time"] = datetime.now().timestamp()
            stale_latencies = report_mapping[stream]["latencies"]
            min_ = min(stale_latencies) / 1000
            max_ = max(stale_latencies) / 1000
            avg = (sum(stale_latencies) / len(stale_latencies)) / 1000
            print("Stream name: %s" % stream)
            print("Min latency: %s" % min_)
            print("Avg latency: %s" % avg)
            print("Max latency: %s" % max_)
            print("\n")
            report_mapping[stream]["latencies"] = []
        if report_mapping[stream]["last_seen"] is not None:
            latency = resp["data"]["T"] - report_mapping[stream]["last_seen"]
            report_mapping[stream]["latencies"].append(latency)
        report_mapping[stream]["last_seen"] = resp["data"]["T"]
ws.close()
