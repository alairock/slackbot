import os

os.environ['SMACKBOT_TEST'] = 'true'
ALIASES = ",".join(["!", "$"])

def load_driver_settings():
    KEYS = (
        'testbot_apitoken',
        'testbot_username',
        'driver_apitoken',
        'driver_username',
        'test_channel',
        'test_private_channel',
    )

    _private_group_patch = 'SMACKBOT_TEST_GROUP'

    for key in KEYS:
        envkey = 'SMACKBOT_' + key.upper()

        # Backwards compatibility patch for TravisCI env variables
        if 'PRIVATE_CHANNEL' in envkey and os.environ.get(_private_group_patch):
            globals()[key] = os.environ.get(_private_group_patch, None)
        else:
            globals()[key] = os.environ.get(envkey, None)

load_driver_settings()

try:
    from smackbot_test_settings import * # pylint: disable=wrong-import-position
except ImportError:
    pass
