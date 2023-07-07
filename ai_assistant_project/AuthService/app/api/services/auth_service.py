from LoginStrategy import LoginStrategy
class AuthService:
    def __init__(self, strategy: LoginStrategy):
        self.strategy = strategy

    def login(self, code: str) -> str:
        try:
            return self.strategy.login(code)
        except Exception as e:
            # 这里可以处理异常，例如转换为你自定义的异常类型
            raise e
