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

@patch('utils.pygame.sprite.collide_rect', return_value=True)
@patch('utils.pygame.mixer.Sound')
@patch('utils.os.path.join', return_value='dummy_path')
@patch('utils.random.choice', return_value='dummy_sound.wav')
def test_collided_with_sound(mock_choice, mock_join, mock_sound, mock_collide_rect, worm, bullet):
    assert collided(worm, bullet, sound_option=ON)
    mock_collide_rect.assert_called_once_with(worm, bullet)
    mock_join.assert_called_once_with('sounds/hits', 'dummy_sound.wav')
    mock_sound.assert_called_once_with('dummy_path')
    mock_sound().play.assert_called_once()

@patch('utils.pygame.sprite.collide_rect', return_value=True)
@patch('utils.pygame.mixer.Sound')
@patch('utils.os.path.join', return_value='dummy_path')
@patch('utils.random.choice', return_value='dummy_sound.wav')
def test_collided_without_sound(mock_choice, mock_join, mock_sound, mock_collide_rect, worm, bullet):
    assert collided(worm, bullet, sound_option=OFF)
    mock_collide_rect.assert_called_once_with(worm, bullet)
    mock_join.assert_not_called()
    mock_sound.assert_not_called()

@patch('utils.pygame.sprite.collide_rect', return_value=False)
def test_not_collided(mock_collide_rect, worm, bullet):
    assert not collided(worm, bullet, sound_option=ON)
    mock_collide_rect.assert_called_once_with(worm, bullet)

def test_bullet_shooted_by_same_worm(worm, bullet_by_same_worm):
    assert not collided(worm, bullet_by_same_worm, sound_option=ON)