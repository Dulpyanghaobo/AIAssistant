from AuthService.app.api.services.AuthTokenStrategy.AuthTokenStrategy import AuthTokenStrategy

class AuthService:
    def __init__(self, strategy: AuthTokenStrategy):
        self.strategy = strategy

    def authtoken(self, code: str) -> str:
        try:
            return self.strategy.authtoken(code)
        except Exception as e:
            # 这里可以处理异常，例如转换为你自定义的异常类型
            raise e
    def verifytoken(self, token: str) -> str:
        try:
            return self.strategy.verifytoken(token)
        except Exception as e:
            # 这里可以处理异常，例如转换为你自定义的异常类型
            raise e