from typing import List, Optional

# Named constants to eliminate magic numbers
DISCOUNT_TYPE_STANDARD = 1
DISCOUNT_TYPE_PREMIUM = 2
DISCOUNT_RATE_STANDARD = 0.1
DISCOUNT_RATE_PREMIUM = 0.2

class Customer:
    """A data class representing customer structural attributes to lower parameter counts."""
    def __init__(self, name: str, address: str, customer_type: int, email: Optional[str], is_vip: bool):
        self.name = name
        self.address = address
        self.customer_type = customer_type
        self.email = email
        self.is_vip = is_vip


class CustomerProcessor:
    def process_customer(self, customer: Customer, orders: List[float], order_count: int) -> float:
        """
        Refactored Orchestration Routine.
        Coordinates isolated sub-routines and safely returns the computed total.
        """
        # 1. Input Validation
        self._validate_inputs(orders, order_count, customer.customer_type)

        # 2. Computations (Noun conventions for functions)
        total_sum = self._calculate_sum(orders, order_count)
        discount_rate = self._determine_discount_rate(customer.customer_type)
        absolute_total = self._calculate_total(total_sum, discount_rate)

        # 3. Side-Effects / Business Actions (Verb+Object for procedures)
        message = self._format_customer_message(customer, absolute_total)
        self._print_message(message)

        if customer.email is not None:
            self._send_email(customer.email, message)

        return absolute_total

    # --- Highly Cohesive Sub-Routines ---

    def _validate_inputs(self, orders: List[float], order_count: int, customer_type: int) -> None:
        if order_count < 0 or order_count > len(orders):
            raise ValueError("Invalid order processing count.")
        if any(order < 0 for order in orders[:order_count]):
            raise ValueError("Order profiles cannot evaluate to negative values.")
        if customer_type not in [DISCOUNT_TYPE_STANDARD, DISCOUNT_TYPE_PREMIUM]:
            raise ValueError("Unrecognized customer type.")

    def _calculate_sum(self, orders: List[float], count: int) -> float:
        return sum(orders[:count])

    def _determine_discount_rate(self, customer_type: int) -> float:
        if customer_type == DISCOUNT_TYPE_STANDARD:
            return DISCOUNT_RATE_STANDARD
        if customer_type == DISCOUNT_TYPE_PREMIUM:
            return DISCOUNT_RATE_PREMIUM
        return 0.0

    def _calculate_total(self, total_sum: float, discount_rate: float) -> float:
        return total_sum * (1.0 - discount_rate)

    def _format_customer_message(self, customer: Customer, total: float) -> str:
        msg = f"Hello {customer.name} of {customer.address}, your total is {total}"
        if customer.is_vip:
            msg += " (VIP)"
        return msg

    def _print_message(self, message: str) -> None:
        print(message)

    def _send_email(self, email: str, message: str) -> None:
        # Mocking external email module side-effect safely
        pass
