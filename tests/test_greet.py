from src.greet import hello

def test_hello():
    assert hello('Jim') == 'hello, Jim'