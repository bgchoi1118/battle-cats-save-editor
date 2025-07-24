class PackageException(Exception):
    """패키지 예외 클래스"""
class RequestException(PackageException):
    """request 요청 실패"""
class UnknownTypeError(PackageException):
    """알 수 없는 타입"""