export interface YPool {
    yPool: YPoolClass;
}

export interface YPoolClass {
    balanceOf:       BalanceProfits;
    _totalSupply:    BalanceProfits;
    _balanceToken:   BalanceProfits;
    _balanceVault:   BalanceProfits;
    _balanceProfits: BalanceProfits;
    _deposit:        BalanceProfits;
}

export interface BalanceProfits {
    constant: boolean;
    inputs:   Put[];
    name:     string;
    outputs:  Put[];
    type:     string;
}

export interface Put {
    name: string;
    type: string;
}
