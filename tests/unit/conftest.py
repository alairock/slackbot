import pytest


@pytest.fixture(scope='function', autouse=True)
def mock_settings(monkeypatch):
    class Settings:
        ALIASES = ''

        def __getattr__(self, item):
            return None

    settings = Settings()
    monkeypatch.setattr('smackbot.settings', settings)
    monkeypatch.setattr('smackbot.dispatcher.settings', settings)
