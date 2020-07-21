# vkaudiotoken-python

Port of [vodka2/vk-audio-token](https://github.com/vodka2/vk-audio-token), originally written in PHP, to Python. This package obtains tokens, that work for VK audio API. Actually there are two versions of the API, one for Kate Mobile, and one for official VK client, each requires a different token.

`vkaudiotoken` is compatible with Python 2.7 and >=3.5. `requests` package is required.

```
pip install vkaudiotoken
```
You can also run examples in the `examples` directory without installing the package

## Getting tokens

The simplest example:

```python
from vkaudiotoken import get_kate_token, get_vk_official_token

login = '+71234567890' # your vk login, e-mail or phone number
password = '12345' # your vk password

# print tokens and corresponding user-agent headers
print(get_kate_token(login, password))
print(get_vk_official_token(login, password))
```

More advanced examples are in the `example` directory. See also examples and README in [vodka2/vk-audio-token](https://github.com/vodka2/vk-audio-token/tree/master/src/examples) repository.

## Using tokens

The simplest example:

```python
import requests

token = '...'
user_agent = '...'

sess = requests.session()
sess.headers.update({'User-Agent': user_agent})

sess.get(
    "https://api.vk.com/method/audio.getById",
    params=[('access_token', token),
            ('audios', '371745461_456289486'),
            ('v', '5.95')]
)
```

See examples in the `example/usage` directory and in [vodka2/vk-audio-token](https://github.com/vodka2/vk-audio-token/tree/master/src/examples/usage). Some VK API documentation, still in progress, is available at [vodka2.github.io/vk-audio-token/](https://vodka2.github.io/vk-audio-token/).

## 2FA

Two factor authorization with SMS is supported, however VK sometimes does not send it. If you don't receive an SMS, you can use `TwoFAHelper` class to force resending. 

It is also possible to create separate passwords in VK account settings and use them instead of your account password.