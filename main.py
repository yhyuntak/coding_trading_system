import os
from dotenv import load_dotenv
import pyupbit

# .env 파일만 로드
load_dotenv()


def main():
    # 환경변수에서 API 키 불러오기 (시세 조회는 키 없이도 가능)
    access_key = os.getenv("UPBIT_ACCESS_KEY")
    secret_key = os.getenv("UPBIT_SECRET_KEY")

    # 리플(XRP), 이더리움(ETH) 시세 조회 (KRW 마켓)
    xrp_price = pyupbit.get_current_price("KRW-XRP")
    eth_price = pyupbit.get_current_price("KRW-ETH")

    print(f"리플(XRP) 현재가: {xrp_price} KRW")
    print(f"이더리움(ETH) 현재가: {eth_price} KRW")

if __name__ == "__main__":
    main()
