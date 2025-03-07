import logging
import requests


class WebhookHandler(logging.Handler):
    def __init__(self, webhook_url):
        super().__init__()
        self.webhook_url = webhook_url

    def emit(self, record):
        log_entry = self.format(record)
        payload = {"message": log_entry}
        try:
            requests.post(self.webhook_url, json=payload)
        except requests.exceptions.RequestException as e:
            print(f"Failed to send log to webhook: {e}")


def SetupLogging(webhook_url):
    """设置日志处理器"""
    webhook_handler = WebhookHandler(webhook_url)
    webhook_handler.setLevel(logging.ERROR)  # 只发送ERROR级别的日志
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    webhook_handler.setFormatter(formatter)

    # 添加处理器到日志记录器
    logger = logging.getLogger()
    logger.addHandler(webhook_handler)

