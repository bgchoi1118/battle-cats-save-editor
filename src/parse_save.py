"""받아온 데이터를 파싱"""
from typing import Optional

#파싱을 bcps에서 할지, BCSFE_Python에서 할지 확인 필요(버전별 임포트 차이)
#그냥 BCSFE_Python 그대로 사용 결정
def parse_save(save_data: bytes, country_code: str, dst: Optional[bool] = None):
    """
    Parse the save data.

    :param save_data:
    :type save_data: bytes
    :param country_code:
    :type country_code: str
    :param dst:
    :type dst: bool
    :return: 파싱된 세이브 데이터
    :rtype: dict[str, Any]
    """
    print(save_data, country_code, dst)
