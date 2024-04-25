import unittest
from contextlib import ExitStack
from unittest.mock import patch, Mock

from shared.live_session import LiveTradingSession

#TODO: edge cases
class TestLiveTradingSession(unittest.TestCase):    
    def setUp(self) -> None:
        self.mock_parameters = {
                                "strategy_name": "cointegrationzscore", 
                                "capital": 100000, 
                                "data_type": "BAR", 
                                "train_start": "2020-05-18", 
                                "train_end": "2024-01-01", 
                                "test_start": "2024-01-02", 
                                "test_end": "2024-01-19", 
                                "tickers": ["HE", "ZC"], 
                                "benchmark": ["^GSPC"]
                            }
        self.mock_acount = [{
                                "start_BuyingPower": "2557567.234", 
                                "currency": "USD", 
                                "start_ExcessLiquidity": "767270.345", 
                                "start_FullAvailableFunds": "767270.4837", 
                                "start_FullInitMarginReq": "282.3937", 
                                "start_FullMaintMarginReq": "282.3938", 
                                "start_FuturesPNL": "-464.883", 
                                "start_NetLiquidation": "767552.392", 
                                "start_TotalCashBalance": "-11292.332", 
                                "start_UnrealizedPnL": "0", 
                                "start_timestamp": "2024-04-11T11:40:09.861731", 
                                "end_BuyingPower": "2535588.9282", 
                                "end_ExcessLiquidity": "762034.2928", 
                                "end_FullAvailableFunds": "760676.292", 
                                "end_FullInitMarginReq": "7074.99", 
                                "end_FullMaintMarginReq": "5716.009", 
                                "end_FuturesPNL": "-487.998", 
                                "end_NetLiquidation": "767751.998", 
                                "end_TotalCashBalance": "766935.99", 
                                "end_UnrealizedPnL": "-28.99", 
                                "end_timestamp": "2024-04-11T11:42:17.046984"
                            }]
        self.mock_trades =  [
                                {"timestamp": "2024-04-11T15:41:00+00:00", "ticker": "HE", "quantity": "1", "cumQty": "1", "price": "91.45", "AvPrice": "91.45", "action": "SELL", "cost": "0", "currency": "USD", "fees": "2.97"}, 
                                {"timestamp": "2024-04-11T15:41:00+00:00", "ticker": "ZC", "quantity": "1", "cumQty": "1", "price": "446.25", "AvPrice": "446.25", "action": "BUY", "cost": "0", "currency": "USD", "fees": "2.97"}
                            ]
        self.mock_signals =  [
                                {
                                    "timestamp": "2024-04-11T15:41:00+00:00", 
                                    "trade_instructions": [
                                        {"ticker": "HE", "order_type": "MKT", "action": "SHORT", "trade_id": 1, "leg_id": 1, "weight": "-0.8689"}, 
                                        {"ticker": "ZC", "order_type": "MKT", "action": "LONG", "trade_id": 1, "leg_id": 2, "weight": "0.1311"}
                                    ]
                                }, 
                                {
                                    "timestamp": "2024-04-11T15:41:05+00:00", 
                                    "trade_instructions": [
                                        {"ticker": "HE", "order_type": "MKT", "action": "SHORT", "trade_id": 1, "leg_id": 1, "weight": "-0.8689"}, 
                                        {"ticker": "ZC", "order_type": "MKT", "action": "LONG", "trade_id": 1, "leg_id": 2, "weight": "0.1311"}
                                    ]
                                }, 
                                {
                                    "timestamp": "2024-04-11T15:41:10+00:00", 
                                    "trade_instructions": [
                                        {"ticker": "HE", "order_type": "MKT", "action": "SHORT", "trade_id": 1, "leg_id": 1, "weight": "-0.8689"}, 
                                        {"ticker": "ZC", "order_type": "MKT", "action": "LONG", "trade_id": 1, "leg_id": 2, "weight": "0.1311"}
                                    ]
                                }
                            ]


        self.session = LiveTradingSession(parameters = self.mock_parameters,
                                          account_data = self.mock_acount,
                                          trade_data = self.mock_trades,
                                          signal_data = self.mock_signals)

    # Basic Validation
    def test_to_dict_valid(self):
        # test
        session_dict = self.session.to_dict()

        # validate
        self.assertEqual(session_dict['parameters'], self.mock_parameters)
        self.assertEqual(session_dict['account_data'], self.mock_acount)
        self.assertEqual(session_dict['signals'], self.mock_signals)
        self.assertEqual(session_dict['trades'], self.mock_trades)

    def test_type_constraints(self):
        with self.assertRaisesRegex(ValueError, "parameters must be a dictionary"):
            LiveTradingSession(parameters = "self.mock_parameters,",
                                          account_data = self.mock_acount,
                                          trade_data = self.mock_trades,
                                          signal_data = self.mock_signals)
            
        with self.assertRaisesRegex(ValueError,"trade_data must be a list of dictionaries" ):
            LiveTradingSession(parameters = self.mock_parameters,
                                        account_data = self.mock_acount,
                                        trade_data = "self.mock_trades",
                                        signal_data = self.mock_signals)
            
        with self.assertRaisesRegex(ValueError,"account_data must be a list of dictionaries" ):
            LiveTradingSession(parameters = self.mock_parameters,
                                        account_data = "self.mock_acount",
                                        trade_data = self.mock_trades,
                                        signal_data = self.mock_signals)
            
        with self.assertRaisesRegex(ValueError, "signal_data must be a list of dictionaries"):
            LiveTradingSession(parameters = self.mock_parameters,
                                        account_data = self.mock_acount,
                                        trade_data = self.mock_trades,
                                        signal_data = "self.mock_signals")
            

if __name__ == "__main__":
    unittest.main()
