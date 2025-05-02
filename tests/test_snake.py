
import animalsounds
import pytest

def test_snake():
    ans = animalsounds.snakeSpeak(3)
    assert len(ans) == 3

def test_snake_zero():
    ans = animalsounds.snakeSpeak(0)
    assert len(ans) == 0

def test_snake_neg():
    with pytest.raises(ValueError) as e_info:
        animalsounds.snakeSpeak(-1)
