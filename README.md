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
    -e "BARK_PUSH=https://api.day.app/xxx" \
    gitsang/pt-auto-login:latest
```

### Notification-related Environment Variables
The notification usage method is consistent with that of the Qinglong panel. Configuring the following environment variables will enable notifications.

| 变量名称                | 类型      | 默认值   | 用途说明                                                                 |
|-------------------------|-----------|----------|--------------------------------------------------------------------------|
| HITOKOTO                | Boolean   | `True`   | 启用一言（随机句子）                                                     |
| BARK_PUSH               | String    | 空       | Bark推送的IP或设备码（例如：`https://api.day.app/DxHcxxxxxRxxxxxxcm/`）  |
| BARK_ARCHIVE            | String    | 空       | Bark推送是否存档（填写 `true`/`false`）                                  |
| BARK_GROUP              | String    | 空       | Bark推送分组名称                                                         |
| BARK_SOUND              | String    | 空       | Bark推送提示音（例如：`chime`）                                          |
| BARK_ICON               | String    | 空       | Bark推送自定义图标URL                                                    |
| BARK_LEVEL              | String    | 空       | Bark推送时效性（`active`/`timeSensitive`/`passive`）                      |
| BARK_URL                | String    | 空       | Bark推送跳转链接                                                         |
| CONSOLE                 | Boolean   | `False`  | 启用控制台输出                                                           |
| DD_BOT_SECRET           | String    | 空       | 钉钉机器人的Secret密钥                                                   |
| DD_BOT_TOKEN            | String    | 空       | 钉钉机器人的Access Token                                                 |
| FSKEY                   | String    | 空       | 飞书机器人的Webhook Key                                                  |
| GOBOT_URL               | String    | 空       | go-cqhttp推送URL（例如：`http://127.0.0.1/send_private_msg`）             |
| GOBOT_QQ                | String    | 空       | go-cqhttp推送目标（用户ID或群ID）                                        |
| GOBOT_TOKEN             | String    | 空       | go-cqhttp的访问Token                                                     |
| GOTIFY_URL              | String    | 空       | Gotify服务地址（例如：`https://push.example.de:8080`）                    |
| GOTIFY_TOKEN            | String    | 空       | Gotify消息应用的Token                                                    |
| GOTIFY_PRIORITY         | Integer   | `0`      | Gotify推送消息优先级（0-10）                                             |
| IGOT_PUSH_KEY           | String    | 空       | iGot聚合推送的Key                                                        |
| PUSH_KEY                | String    | 空       | Server酱的推送Key（兼容旧版和Turbo版）                                   |
| DEER_KEY                | String    | 空       | PushDeer的推送Key                                                         |
| DEER_URL                | String    | 空       | PushDeer自定义服务地址                                                   |
| CHAT_URL                | String    | 空       | Synology Chat的Webhook URL                                               |
| CHAT_TOKEN              | String    | 空       | Synology Chat的Token                                                     |
| PUSH_PLUS_TOKEN         | String    | 空       | Push+微信推送的用户Token                                                 |
| PUSH_PLUS_USER          | String    | 空       | Push+微信推送的群组编码                                                   |
| WE_PLUS_BOT_TOKEN       | String    | 空       | 微加机器人的Token                                                        |
| WE_PLUS_BOT_RECEIVER    | String    | 空       | 微加机器人消息接收者标识                                                 |
| WE_PLUS_BOT_VERSION     | String    | `pro`    | 微加机器人接口版本（默认`pro`）                                          |
| QMSG_KEY                | String    | 空       | Qmsg酱的推送Key                                                          |
| QMSG_TYPE               | String    | 空       | Qmsg酱推送类型（例如：`group`/`user`）                                   |
| QYWX_ORIGIN             | String    | 空       | 企业微信代理地址                                                         |
| QYWX_AM                 | String    | 空       | 企业微信应用参数（需组合使用）                                           |
| QYWX_KEY                | String    | 空       | 企业微信机器人Webhook Key                                                |
| TG_BOT_TOKEN            | String    | 空       | Telegram机器人的Token（例如：`140xxxxxx:AAG9rt-6RDaaX0HBLZQq0laNOh8xxxxx`）|
| TG_USER_ID              | String    | 空       | Telegram用户/群组ID                                                      |
| TG_API_HOST             | String    | 空       | Telegram代理API地址                                                      |
| TG_PROXY_AUTH           | String    | 空       | Telegram代理认证参数                                                     |
| TG_PROXY_HOST           | String    | 空       | Telegram代理服务器地址                                                   |
| TG_PROXY_PORT           | String    | 空       | Telegram代理服务器端口                                                   |
| AIBOTK_KEY              | String    | 空       | 智能微秘书的API Key                                                      |
| AIBOTK_TYPE             | String    | 空       | 智能微秘书推送目标类型（`room`或`contact`）                              |
| AIBOTK_NAME             | String    | 空       | 智能微秘书推送目标名称（群名或好友昵称）                                 |
| SMTP_SERVER             | String    | 空       | SMTP邮件服务器地址（例如：`smtp.exmail.qq.com:465`）                     |
| SMTP_SSL                | String    | `false`  | SMTP是否启用SSL（`true`/`false`）                                        |
| SMTP_EMAIL              | String    | 空       | SMTP收发件邮箱地址                                                       |
| SMTP_PASSWORD           | String    | 空       | SMTP登录密码或授权码                                                     |
| SMTP_NAME               | String    | 空       | SMTP收发件人显示名称                                                     |
| PUSHME_KEY              | String    | 空       | PushMe服务的推送Key                                                      |
| PUSHME_URL              | String    | 空       | PushMe自定义服务地址                                                     |
| CHRONOCAT_QQ            | String    | 空       | Chronocat推送的QQ号                                                      |
| CHRONOCAT_TOKEN         | String    | 空       | Chronocat的Token                                                         |
| CHRONOCAT_URL           | String    | 空       | Chronocat服务地址                                                        |
| WEBHOOK_URL             | String    | 空       | 自定义Webhook请求地址                                                    |
| WEBHOOK_BODY            | String    | 空       | 自定义Webhook请求体模板                                                  |
| WEBHOOK_HEADERS         | String    | 空       | 自定义Webhook请求头（JSON格式）                                          |
| WEBHOOK_METHOD          | String    | 空       | 自定义Webhook请求方法（例如：`POST`/`GET`）                              |
| WEBHOOK_CONTENT_TYPE    | String    | 空       | 自定义Webhook的Content-Type（例如：`application/json`）                  |

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
