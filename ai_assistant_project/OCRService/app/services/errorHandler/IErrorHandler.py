class IErrorHandler:
    def handle_error(self, func, *args, **kwargs):
        raise NotImplementedError


class RetryErrorHandler(IErrorHandler):
    def __init__(self, max_retries):
        self.max_retries = max_retries

    def handle_error(self, func, *args, **kwargs):
        for _ in range(self.max_retries):
            try:
                return func(*args, **kwargs)
            except Exception:
                continue
        raise


class ImmediateFailureErrorHandler(IErrorHandler):
    def handle_error(self, func, *args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception:
            # 在这里你可以发送警报，例如发送邮件或者短信
            raise
