from rest_framework.throttling import UserRateThrottle

class EmonRateThrottle(UserRateThrottle):
    scope = 'emon'
    