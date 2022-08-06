from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine

from app.config import MONGO_DB_NAME, MONGO_URL


class MongoDB:
    def __init__(self):
        self.client = None
        self.engine = None

    def connect(self):
        self.client = AsyncIOMotorClient(MONGO_URL)
        self.engine = AIOEngine(
            motor_client=self.client, database=MONGO_DB_NAME)
        print("DB 연결에 성공했습니다.")

    def close(self):
        self.client.close()
        print("DB 연결을 종료했습니다.")


mongodb = MongoDB()
