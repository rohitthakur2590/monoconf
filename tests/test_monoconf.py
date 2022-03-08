# import pytest
from monoconf.netmapper import display


def test_display():
    assert "netmapper monitor" in display()
