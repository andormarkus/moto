from moto.core.exceptions import JsonRESTError


class GreengrassClientError(JsonRESTError):
    code = 400


class IdNotFoundException(GreengrassClientError):
    def __init__(self, msg):
        self.code = 404
        super().__init__("IdNotFoundException", msg)


class InvalidContainerDefinitionException(GreengrassClientError):
    def __init__(self, msg):
        self.code = 400
        super().__init__("InvalidContainerDefinitionException", msg)


class VersionNotFoundException(GreengrassClientError):
    def __init__(self, msg):
        self.code = 404
        super().__init__("VersionNotFoundException", msg)
