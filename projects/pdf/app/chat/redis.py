from redis import Redis
from os import environ

client = Redis.from_url(
    environ['REDIS_URI'],
    decode_responses=True
)