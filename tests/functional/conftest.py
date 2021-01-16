#!/usr/bin/env python3

import os

import pytest


@pytest.fixture
def firefox_options(firefox_options):
    firefox_options.headless = True
    return firefox_options


@pytest.fixture(autouse=True)
def env_setup(monkeypatch):
    if os.getenv("GITHUB_ACTIONS"):
        guest_home = os.getenv("GITHUB_WORKSPACE")
    else:
        guest_home = "/Users/liora/src/github.com/lioramilbaum/zapata"
    monkeypatch.setenv("GUEST_HOME", guest_home)