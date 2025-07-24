import requests
from src import exception
from src import utils
import json

class SaveData:
    def __init__(self):
        self.origin_data = {}
        self.custom_data = {}
    def load_data(self, code, password, country, game_version):
        """
        이어하기 코드로 세이브 데이터를 불러옵니다.

        :param code: 이어하기 코드
        :type code: str
        :param password: 인증번호
        :type password: str
        :param country: 국가코드(en, ja, kr, tw)
        :type country: str
        :param game_version: 게임 버전(13.0.1)
        :type game_version: str
        :return: 결과를 반환합니다.
        :rtype: dict
        :raises RequestException: request요청중 오류 발생시
        :raises UnknownTypeError: response값이 기대한 형식과 일치하지 않을시
        """
        try:
            url = utils.get_url("save") + "/v2/transfers/" + code + "/reception"
            data = {
                "clientInfo": {
                    "client": {
                        "countryCode": country,
                        "version": utils.str_to_gv(game_version),
                    },
                    "device": {
                        "model": "SM-G955F",
                    },
                    "os": {
                        "type": "android",
                        "version": "9",
                    },
                },
                "nonce": utils.random_hex_string(32),
                "pin": password
            }
            data = json.dumps(data).replace(" ", "")
            headers = {
                "content-type": "application/json",
                "accept-encoding": "gzip",
                "connection": "keep-alive",
                "user-agent": "Dalvik/2.1.0 (Linux; U; Android 9; SM-G955F Build/N2G48B)",
            }
            response = requests.post(url, headers=headers, data=data)
        except requests.exceptions.RequestException as e:
            raise exception.RequestException(f'세이브 데이터 로딩중 오류 발생\n {e}')
        except Exception as e:
            raise exception.RequestException(e)
        if response.status_code != 200:
            raise exception.RequestException(
                f'세이브 데이터 로딩중 오류 발생\n{response}, {response.status_code}')
        if response.headers.get('content-type', "") != 'application/octet-stream':
            raise exception.UnknownTypeError(
                f'세이브 데이터 로딩중 오류 발생(비정상적인 content-type)\n{response}, {response.status_code}')
        save_data = response.content
        try:
            save_data = json.loads(save_data)
        except (json.decoder.JSONDecodeError, UnicodeDecodeError):
            raise exception.UnknownTypeError(
                f'올바르지 않은 세이브 데이터 형식\n{save_data}\n{response}'
            )
        # headers = response.headers
        # start_parse = parse_save
        # save_stats = parse_save.start_parse(save_data, country_code) #json을 dict로
        # save_stats["token"] = headers["nyanko-password-refresh-token"]
        # info = user_info.UserInfo(save_stats["inquiry_code"])
        # info.set_password(headers["nyanko-password"])
        # save_data = serialise_save.start_serialize(save_stats)
        # save_data = patcher.patch_save_data(save_data, country_code)
        # path = helper.save_file(
        #     "Save save data",
        #     helper.get_save_file_filetype(),
        #     helper.get_save_path_home(),
        # )
        # if path is None:
        #     return None
        # helper.write_file_bytes(path, save_data)
        # return path