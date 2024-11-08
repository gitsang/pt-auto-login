# PT Auto Login

python script for m-team(only support m-team now) auto login

## How to use

### Login Once

```bash
docker run --rm -e "BASE_URL=xxxxx" -e "USERNAME=xxxxx" -e "PASSWORD=xxxxx" -e "TOTP_SEC=xxxxx" gitsang/pt-auto-login:latest
```

### Use crontab to schedule

```bash
crontab -e
```

Crontab example (auto login at 0:00 every day):

```bash
0 0 * * * docker run --rm -e "BASE_URL=xxxxx" -e "USERNAME=xxxxx" -e "PASSWORD=xxxxx" -e "TOTP_SEC=xxxxx" gitsang/pt-auto-login:latest
```

> Visit https://crontab.guru for more details about crontab

### Why not use python cron?

Just laziness

## License

MIT
