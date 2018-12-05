import calculator as calc

class TestCalculator:

    def test_add(self):
        assert 9 == calc.add(5, 4)
                
    def test_subtract(self):
        assert 11 == calc.subtract(21, 10)

    def test_multiply(self):
        assert 120 == 10 * 12
        