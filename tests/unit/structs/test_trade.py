import random
import unittest

from midastrader.structs.trade import Trade


class TestTrade(unittest.TestCase):
    def setUp(self) -> None:
        # Mock trade data
        self.trade_id = 1
        self.leg_id = 2
        self.timetamp = 16555000000000000
        self.instrument = 1
        self.quantity = 10
        self.avg_price = 85.98
        self.trade_value = 900.90
        self.trade_cost = 400
        self.action = random.choice(["BUY", "SELL"])
        self.fees = 9.87

        # Creaet trade object
        self.trade_obj = Trade(
            trade_id=self.trade_id,
            leg_id=self.leg_id,
            timestamp=self.timetamp,
            instrument=self.instrument,
            quantity=self.quantity,
            avg_price=self.avg_price,
            trade_value=self.trade_value,
            trade_cost=self.trade_cost,
            action=self.action,
            fees=self.fees,
        )

    # Basic Validation
    def test_construction(self):
        # Test
        trade = Trade(
            trade_id=self.trade_id,
            leg_id=self.leg_id,
            timestamp=self.timetamp,
            instrument=self.instrument,
            quantity=self.quantity,
            avg_price=self.avg_price,
            trade_value=self.trade_value,
            trade_cost=self.trade_cost,
            action=self.action,
            fees=self.fees,
        )
        # Validate
        self.assertEqual(trade.trade_id, self.trade_id)
        self.assertEqual(trade.leg_id, self.leg_id)
        self.assertEqual(trade.timestamp, self.timetamp)
        self.assertEqual(trade.instrument, self.instrument)
        self.assertEqual(trade.quantity, self.quantity)
        self.assertEqual(trade.avg_price, self.avg_price)
        self.assertEqual(trade.trade_value, self.trade_value)
        self.assertEqual(trade.trade_cost, self.trade_cost)
        self.assertEqual(trade.action, self.action)
        self.assertEqual(trade.fees, self.fees)

    # Type Validation
    def test_type_validation(self):
        with self.assertRaisesRegex(
            TypeError, "'trade_id' field must be of type int."
        ):
            Trade(
                trade_id="1",
                leg_id=self.leg_id,
                timestamp=self.timetamp,
                instrument=self.instrument,
                quantity=self.quantity,
                avg_price=self.avg_price,
                trade_value=self.trade_value,
                trade_cost=self.trade_cost,
                action=self.action,
                fees=self.fees,
            )

        with self.assertRaisesRegex(
            TypeError, "'leg_id' field must be of type int."
        ):
            Trade(
                trade_id=self.trade_id,
                leg_id="2",
                timestamp=self.timetamp,
                instrument=self.instrument,
                quantity=self.quantity,
                avg_price=self.avg_price,
                trade_value=self.trade_value,
                trade_cost=self.trade_cost,
                action=self.action,
                fees=self.fees,
            )

        with self.assertRaisesRegex(
            TypeError, "'timestamp' field must be of type int."
        ):
            Trade(
                trade_id=self.trade_id,
                leg_id=self.leg_id,
                timestamp="2022-08-08",
                instrument=self.instrument,
                quantity=self.quantity,
                avg_price=self.avg_price,
                trade_value=self.trade_value,
                trade_cost=self.trade_cost,
                action=self.action,
                fees=self.fees,
            )

        with self.assertRaisesRegex(
            TypeError, "'instrument' field must be of type int."
        ):
            Trade(
                trade_id=self.trade_id,
                leg_id=self.leg_id,
                timestamp=self.timetamp,
                instrument="1",
                quantity=self.quantity,
                avg_price=self.avg_price,
                trade_value=self.trade_value,
                trade_cost=self.trade_cost,
                action=self.action,
                fees=self.fees,
            )

        with self.assertRaisesRegex(
            TypeError, "'quantity' field must be of type float or int."
        ):
            Trade(
                trade_id=self.trade_id,
                leg_id=self.leg_id,
                timestamp=self.timetamp,
                instrument=self.instrument,
                quantity="1234",
                avg_price=self.avg_price,
                trade_value=self.trade_value,
                trade_cost=self.trade_cost,
                action=self.action,
                fees=self.fees,
            )

        with self.assertRaisesRegex(
            TypeError, "'avg_price' field must be of type float or int."
        ):
            Trade(
                trade_id=self.trade_id,
                leg_id=self.leg_id,
                timestamp=self.timetamp,
                instrument=self.instrument,
                quantity=self.quantity,
                avg_price="90.9",
                trade_value=self.trade_value,
                trade_cost=self.trade_cost,
                action=self.action,
                fees=self.fees,
            )

        with self.assertRaisesRegex(
            TypeError, "'trade_value' field must be of type float or int."
        ):
            Trade(
                trade_id=self.trade_id,
                leg_id=self.leg_id,
                timestamp=self.timetamp,
                instrument=self.instrument,
                quantity=self.quantity,
                avg_price=self.avg_price,
                trade_value="12345",
                trade_cost=self.trade_cost,
                action=self.action,
                fees=self.fees,
            )

        with self.assertRaisesRegex(
            TypeError, "'trade_cost' field must be of type float or int."
        ):
            Trade(
                trade_id=self.trade_id,
                leg_id=self.leg_id,
                timestamp=self.timetamp,
                instrument=self.instrument,
                quantity=self.quantity,
                avg_price=self.avg_price,
                trade_value=12345,
                trade_cost="1234",
                action=self.action,
                fees=self.fees,
            )

        with self.assertRaisesRegex(
            TypeError, "'action' field must be of type str."
        ):
            Trade(
                trade_id=self.trade_id,
                leg_id=self.leg_id,
                timestamp=self.timetamp,
                instrument=self.instrument,
                quantity=self.quantity,
                avg_price=self.avg_price,
                trade_value=self.trade_value,
                trade_cost=self.trade_cost,
                action=12234,
                fees=self.fees,
            )

        with self.assertRaisesRegex(
            TypeError, "'fees' field must be of type float or int."
        ):
            Trade(
                trade_id=self.trade_id,
                leg_id=self.leg_id,
                timestamp=self.timetamp,
                instrument=self.instrument,
                quantity=self.quantity,
                avg_price=self.avg_price,
                trade_value=self.trade_value,
                trade_cost=self.trade_cost,
                action=self.action,
                fees="90.99",
            )

    # Value validation
    def test_value_constraint(self):
        with self.assertRaises(ValueError):
            Trade(
                trade_id=self.trade_id,
                leg_id=self.leg_id,
                timestamp=self.timetamp,
                instrument=self.instrument,
                quantity=self.quantity,
                avg_price=self.avg_price,
                trade_value=self.trade_value,
                trade_cost=self.trade_cost,
                action="long",
                fees=self.fees,
            )

        with self.assertRaisesRegex(
            ValueError, "'avg_price' field must be greater than zero."
        ):
            Trade(
                trade_id=self.trade_id,
                leg_id=self.leg_id,
                timestamp=self.timetamp,
                instrument=self.instrument,
                quantity=self.quantity,
                avg_price=0.0,
                trade_value=self.trade_value,
                trade_cost=self.trade_cost,
                action=self.action,
                fees=self.fees,
            )


if __name__ == "__main__":
    unittest.main()
