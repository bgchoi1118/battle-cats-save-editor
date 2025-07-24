from src import exception
import os

t = {'clientInfo': {'client': {'countryCode': 'tw', 'version': 120200},
                    'device': {'model': 'SM-G955F'},
                    'os': {'type': 'android', 'version': '9'}},
        'nonce': '1fa77822898f533ed9b1cf14923f9c6b',
        'pin': '3'}
def get_url(kind: str):
    """
    서버 URL을 불러옵니다

    :param kind: 불러올 서버 URL의 종류를 성택합니다.(save, auth, backup, managed-item, aws)
    :type kind: str
    :return: 해당 URL의 링크
    :rtype: str
    :raises UnknownTypeError: 인자 kind가 옳지 못한 경우에 발생
    """
    url = f"{ServerHandler.save_url}/v2/transfers/{transfer_code}/reception"  # type: ignore
    if kind == "save":
        return "https://nyanko-save.ponosgames.com"
    elif kind == "auth":
        return "https://nyanko-auth.ponosgames.com"
    elif kind == "backup":
        return "https://nyanko-backups.ponosgames.com"
    elif kind == "managed-item":
        return "https://nyanko-managed-item.ponosgames.com"
    elif kind == "aws":
        return "https://nyanko-service-data-prd.s3.amazonaws.com"
    else:
        raise exception.UnknownTypeError(kind+'는 알 수 없는 타입입니다.')


def str_to_gv(game_version: str):
    """
    게임 버전을 정수로 변경합니다

    :param game_version: 게임 버전(12.0.6등)
    :type game_version: str
    :return: 포메팅된 게임 버전
    :rtype: str
    """

    split_gv = game_version.split(".")
    if len(split_gv) == 2:
        split_gv.append("0")
    final = ""
    for split in split_gv:
        final += split.zfill(2)

    return final.lstrip("0")

def random_hex_string(length: int):
    """
    지정한 길이만큼의 랜덤 16진수 문자열을 생성합니다.

    :param length: 길이
    :type length: int
    :return: 랜덤 16진수 문자열
    :rtype: str
    """
    return os.urandom((length + 1) // 2).hex()[:length]
