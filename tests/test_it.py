import unittest


class TestCallerPackage(unittest.TestCase):
    def _callFUT(self, *arg, **kw):
        from path import caller_package

        return caller_package(*arg, **kw)

    def test_level_3(self):
        assert unittest == self._callFUT(3)

    def test_level_2(self):
        import tests

        assert tests == self._callFUT(2)
