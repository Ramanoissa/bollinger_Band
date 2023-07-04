import unittest
import pandas as pd
import numpy as np
from ta.volatility import BollingerBands
class BollingerBandsTest(unittest.TestCase):
    def setUp(self):
        # Set up the test data
        np.random.seed(42)
        dates = pd.date_range(start='2023-01-01', periods=100)
        close_prices = np.random.uniform(low=100, high=200, size=(100,))
        self.df = pd.DataFrame({'date': dates, 'close': close_prices}, dtype=np.float64)
    def test_bollinger_bands(self):
        # Initialize the Bollinger Bands indicator
        indicator_bb = BollingerBands(close=self.df['close'], window=20, window_dev=2)
        # Compute the upper, middle, and lower bands
        self.df['bb_upperband'] = indicator_bb.bollinger_hband()
        self.df['bb_middleband'] = indicator_bb.bollinger_mavg()
        self.df['bb_lowerband'] = indicator_bb.bollinger_lband()
        # Verify the dimensions of the bands
        self.assertEqual(len(self.df), len(self.df['bb_upperband']))
        self.assertEqual(len(self.df), len(self.df['bb_middleband']))
        self.assertEqual(len(self.df), len(self.df['bb_lowerband']))
        # Verify that the middle band is within the upper and lower bands
        self.assertTrue(all(self.df['bb_lowerband'] <= self.df['bb_middleband']))
        self.assertTrue(all(self.df['bb_middleband'] <= self.df['bb_upperband']))
    # Add more test cases for edge cases or specific scenarios
if __name__ == '__main__':
    unittest.main()
