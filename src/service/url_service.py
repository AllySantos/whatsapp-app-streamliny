
BASE_URL = 'https://wa.me/'

def create_new_url(phone_number):
    url = f'{BASE_URL}{phone_number}'
    return url