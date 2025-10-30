import types

import pytest

from mysiri.get_answers import Fetcher


class DummyResp:
    def __init__(self, status_code=200, text=""):
        self.status_code = status_code
        self.text = text


def test_lookup_returns_meta_description(monkeypatch):
    html = '<html><head><meta name="description" content="Meta description here"><title>Page Title</title></head><body><p>Hello</p></body></html>'

    def fake_get(url, headers=None, timeout=None):
        return DummyResp(status_code=200, text=html)

    monkeypatch.setattr("requests.get", fake_get)

    f = Fetcher("http://example.local")
    out = f.lookup()
    assert out == "Meta description here"


def test_lookup_falls_back_to_title(monkeypatch):
    html = "<html><head><title>Only Title</title></head><body></body></html>"

    def fake_get(url, headers=None, timeout=None):
        return DummyResp(status_code=200, text=html)

    monkeypatch.setattr("requests.get", fake_get)

    f = Fetcher("http://example.local")
    out = f.lookup()
    assert out == "Only Title"


def test_lookup_handles_errors(monkeypatch):
    def fake_get(url, headers=None, timeout=None):
        raise RuntimeError("boom")

    monkeypatch.setattr("requests.get", fake_get)
    f = Fetcher("http://example.local")
    out = f.lookup()
    assert out == "I don't know"
