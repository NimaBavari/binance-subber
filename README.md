# Binance Subber

_by Tural Mahmudov <nima.bavari@gmail.com>_

**Time taken: 2 hour**

Simple Binance live data stream subscription and reporting client.

## Requirements

### Prerequisites

- No binance/crypto related libraries allowed
- Execute below tasks on main-net (api.binance.com & wss://stream.binance.com)
- Unit tests/any form of testing for the below tasks is completely optional
- SPOT documentation available at https://binance-docs.github.io/apidocs/spot/en/#change-log

### Task

1. Open 1 "empty" websocket and then LIVE SUB-scribe to 2 trade streams, 2 aggTrade streams and 2 kline streams
2. Measure websocket event time => client receive time latency for each specific stream and print min/avg/max to console every 1 min (optimize code for high message rate/minimum processing time)

## Scripts

### Dev Scripts

Run

```sh
chmod +x ./lint.sh
./lint.sh
```

to lint and format the code in the directory of this project.

### Usage

Run `docker-compose up subber` to start the application.