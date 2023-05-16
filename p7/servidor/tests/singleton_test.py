from singleton import Singleton

def test_singleton_implements_pattern():
    class TestSingleton(metaclass=Singleton):
        pass

    singleton_1 = TestSingleton()
    singleton_2 = TestSingleton()

    assert singleton_1 == singleton_2