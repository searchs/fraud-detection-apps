import subprocess

import pytest

from mysiri.commands import Commander


def test_discover_name(monkeypatch, capsys):
    called = {}

    def fake_call(args, *a, **k):
        # record the response text passed to say
        if isinstance(args, list):
            called["args"] = args
        else:
            called["args"] = args

    monkeypatch.setattr(subprocess, "call", fake_call)

    cmd = Commander()
    cmd.discover("what is your name")

    # capture printed output to ensure respond printed
    captured = capsys.readouterr()
    assert (
        "My name is Python commander" in captured.out
        or "You haven't told me your name yet" in captured.out
    )


def test_discover_open_app(monkeypatch):
    ran = {}

    def fake_run(args, check=False):
        ran["args"] = args

    monkeypatch.setattr(subprocess, "run", fake_run)
    monkeypatch.setattr(subprocess, "call", lambda *a, **k: None)

    cmd = Commander()
    cmd.discover("please open TextEdit")

    assert "args" in ran
    # because discover lowercases input, expect textedit.app
    assert ran["args"] == ["open", "-a", "textedit.app"]
