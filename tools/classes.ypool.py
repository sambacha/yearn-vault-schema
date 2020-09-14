from typing import List


class Put:
    name: str
    type: str

    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type


class BalanceProfits:
    constant: bool
    inputs: List[Put]
    name: str
    outputs: List[Put]
    type: str

    def __init__(self, constant: bool, inputs: List[Put], name: str, outputs: List[Put], type: str) -> None:
        self.constant = constant
        self.inputs = inputs
        self.name = name
        self.outputs = outputs
        self.type = type


class YVault:
    balance_of: BalanceProfits
    total_supply: BalanceProfits
    balance_token: BalanceProfits
    balance_vault: BalanceProfits
    balance_profits: BalanceProfits
    deposit: BalanceProfits
    withdraw: BalanceProfits

    def __init__(self, balance_of: BalanceProfits, total_supply: BalanceProfits, balance_token: BalanceProfits, balance_vault: BalanceProfits, balance_profits: BalanceProfits, deposit: BalanceProfits, withdraw: BalanceProfits) -> None:
        self.balance_of = balance_of
        self.total_supply = total_supply
        self.balance_token = balance_token
        self.balance_vault = balance_vault
        self.balance_profits = balance_profits
        self.deposit = deposit
        self.withdraw = withdraw


class YPool:
    y_vault: YVault

    def __init__(self, y_vault: YVault) -> None:
        self.y_vault = y_vault
