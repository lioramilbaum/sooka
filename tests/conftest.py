#!/usr/bin/env python3

import pytest

from zapata import create_app
from zapata.routes import configure_routes


@pytest.fixture()
def test_client():
    app = create_app()

    configure_routes(app)

    testing_client = app.test_client()

    ctx = app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()