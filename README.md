# PT Auto Login

python script for m-team(only support m-team now) auto login

## How to use

### Login Once

```bash
docker run --rm \
    -e "BASE_URL=xxxxx" \
    -e "USERNAME=xxxxx" \
    -e "PASSWORD=xxxxx" \
    -e "TOTP_SEC=xxxxx" \
    gitsang/pt-auto-login:latest
```

### Use crontab to schedule

```bash
crontab -e
```

Crontab example (auto login at 0:00 every day):

```bash
0 0 * * * /path/to/pt-auto-login.sh
```

> Visit https://crontab.guru for more details about crontab

### Why not use python cron?

Just laziness

## Contribute

### Init Python Environment

Create Environment

```bash
conda create -p .venv python=3.12
```

Activate Environment

```bash
conda activate ./.venv
```

### Install Requirements

```bash
make init
```

### Run

```bash
make run
```

To display on browser, comment out `--headless` agument in [utils/driver_utils.py](./utils/driver_utils.py)

```diff
- options.add_argument("--headless")
+ # options.add_argument("--headless")
```

## License

MIT
