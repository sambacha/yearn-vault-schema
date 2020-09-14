# To use this code, make sure you
#
#     import json
#
# and then, to convert JSON from a string, do
#
#     result = y_pool_from_dict(json.loads(json_string))

from typing import Any, List, TypeVar, Callable, Type, cast


T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_list(f: Callable[[Any], T], x: Any) -> List[T]:
    assert isinstance(x, list)
    return [f(y) for y in x]


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class Put:
    name: str
    type: str

    def __init__(self, name: str, type: str) -> None:
        self.name = name
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'Put':
        assert isinstance(obj, dict)
        name = from_str(obj.get("name"))
        type = from_str(obj.get("type"))
        return Put(name, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["name"] = from_str(self.name)
        result["type"] = from_str(self.type)
        return result


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

    @staticmethod
    def from_dict(obj: Any) -> 'BalanceProfits':
        assert isinstance(obj, dict)
        constant = from_bool(obj.get("constant"))
        inputs = from_list(Put.from_dict, obj.get("inputs"))
        name = from_str(obj.get("name"))
        outputs = from_list(Put.from_dict, obj.get("outputs"))
        type = from_str(obj.get("type"))
        return BalanceProfits(constant, inputs, name, outputs, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["constant"] = from_bool(self.constant)
        result["inputs"] = from_list(lambda x: to_class(Put, x), self.inputs)
        result["name"] = from_str(self.name)
        result["outputs"] = from_list(lambda x: to_class(Put, x), self.outputs)
        result["type"] = from_str(self.type)
        return result


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

    @staticmethod
    def from_dict(obj: Any) -> 'YVault':
        assert isinstance(obj, dict)
        balance_of = BalanceProfits.from_dict(obj.get("balanceOf"))
        total_supply = BalanceProfits.from_dict(obj.get("_totalSupply"))
        balance_token = BalanceProfits.from_dict(obj.get("_balanceToken"))
        balance_vault = BalanceProfits.from_dict(obj.get("_balanceVault"))
        balance_profits = BalanceProfits.from_dict(obj.get("_balanceProfits"))
        deposit = BalanceProfits.from_dict(obj.get("_deposit"))
        withdraw = BalanceProfits.from_dict(obj.get("_withdraw"))
        return YVault(balance_of, total_supply, balance_token, balance_vault, balance_profits, deposit, withdraw)

    def to_dict(self) -> dict:
        result: dict = {}
        result["balanceOf"] = to_class(BalanceProfits, self.balance_of)
        result["_totalSupply"] = to_class(BalanceProfits, self.total_supply)
        result["_balanceToken"] = to_class(BalanceProfits, self.balance_token)
        result["_balanceVault"] = to_class(BalanceProfits, self.balance_vault)
        result["_balanceProfits"] = to_class(BalanceProfits, self.balance_profits)
        result["_deposit"] = to_class(BalanceProfits, self.deposit)
        result["_withdraw"] = to_class(BalanceProfits, self.withdraw)
        return result


class YPool:
    y_vault: YVault

    def __init__(self, y_vault: YVault) -> None:
        self.y_vault = y_vault

    @staticmethod
    def from_dict(obj: Any) -> 'YPool':
        assert isinstance(obj, dict)
        y_vault = YVault.from_dict(obj.get("yVault"))
        return YPool(y_vault)

    def to_dict(self) -> dict:
        result: dict = {}
        result["yVault"] = to_class(YVault, self.y_vault)
        return result


def y_pool_from_dict(s: Any) -> YPool:
    return YPool.from_dict(s)


def y_pool_to_dict(x: YPool) -> Any:
    return to_class(YPool, x)
