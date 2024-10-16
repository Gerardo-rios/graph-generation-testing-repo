import pytest
from unittest.mock import Mock, patch
from utils import collided
from defaults import ON, OFF
from game_classes import Worm, Bullet

@pytest.fixture
def worm():
    return Worm(name="worm1")

@pytest.fixture
def bullet():
    return Bullet(shooted_by="worm2")

@pytest.fixture
def bullet_by_same_worm(worm):
    return Bullet(shooted_by=worm.name)