{ `$ref` = "#/definitions/YPool"
, `$schema` = "http://json-schema.org/draft-06/schema#"
, definitions =
  { BalanceOf =
    { additionalProperties = False
    , properties =
      { constant.type = "boolean"
      , inputs = { items.`$ref` = "#/definitions/Put", type = "array" }
      , name.type = "string"
      , outputs = { items.`$ref` = "#/definitions/Put", type = "array" }
      , type.type = "string"
      }
    , required = [ "constant", "inputs", "name", "outputs", "type" ]
    , title = "BalanceOf"
    , type = "object"
    }
  , BalanceProfits =
    { additionalProperties = False
    , properties =
      { constant.type = "boolean"
      , inputs = { items = {=}, type = "array" }
      , name.type = "string"
      , outputs = { items.`$ref` = "#/definitions/Put", type = "array" }
      , type.type = "string"
      }
    , required = [ "constant", "inputs", "name", "outputs", "type" ]
    , title = "BalanceProfits"
    , type = "object"
    }
  , BalanceToken =
    { additionalProperties = False
    , properties =
      { constant.type = "boolean"
      , inputs = { items = {=}, type = "array" }
      , name.type = "string"
      , outputs = { items.`$ref` = "#/definitions/Put", type = "array" }
      , type.type = "string"
      }
    , required = [ "constant", "inputs", "name", "outputs", "type" ]
    , title = "BalanceToken"
    , type = "object"
    }
  , BalanceVault =
    { additionalProperties = False
    , properties =
      { constant.type = "boolean"
      , inputs = { items = {=}, type = "array" }
      , name.type = "string"
      , outputs = { items.`$ref` = "#/definitions/Put", type = "array" }
      , type.type = "string"
      }
    , required = [ "constant", "inputs", "name", "outputs", "type" ]
    , title = "BalanceVault"
    , type = "object"
    }
  , Deposit =
    { additionalProperties = False
    , properties =
      { constant.type = "boolean"
      , inputs = { items.`$ref` = "#/definitions/Put", type = "array" }
      , name.type = "string"
      , outputs = { items = {=}, type = "array" }
      , type.type = "string"
      }
    , required = [ "constant", "inputs", "name", "outputs", "type" ]
    , title = "Deposit"
    , type = "object"
    }
  , Put =
    { additionalProperties = False
    , properties = { name.type = "string", type.type = "string" }
    , required = [ "name", "type" ]
    , title = "Put"
    , type = "object"
    }
  , TotalSupply =
    { additionalProperties = False
    , properties =
      { constant.type = "boolean"
      , inputs = { items = {=}, type = "array" }
      , name.type = "string"
      , outputs = { items.`$ref` = "#/definitions/Put", type = "array" }
      , type.type = "string"
      }
    , required = [ "constant", "inputs", "name", "outputs", "type" ]
    , title = "TotalSupply"
    , type = "object"
    }
  , Withdraw =
    { additionalProperties = False
    , properties =
      { constant.type = "boolean"
      , inputs = { items.`$ref` = "#/definitions/Put", type = "array" }
      , name.type = "string"
      , outputs = { items = {=}, type = "array" }
      , type.type = "string"
      }
    , required = [ "constant", "inputs", "name", "outputs", "type" ]
    , title = "Withdraw"
    , type = "object"
    }
  , YPool =
    { additionalProperties = False
    , properties.yVault.`$ref` = "#/definitions/YVault"
    , required = [ "yVault" ]
    , title = "YPool"
    , type = "object"
    }
  , YVault =
    { additionalProperties = False
    , properties =
      { _balanceProfits.`$ref` = "#/definitions/BalanceProfits"
      , _balanceToken.`$ref` = "#/definitions/BalanceToken"
      , _balanceVault.`$ref` = "#/definitions/BalanceVault"
      , _deposit.`$ref` = "#/definitions/Deposit"
      , _totalSupply.`$ref` = "#/definitions/TotalSupply"
      , _withdraw.`$ref` = "#/definitions/Withdraw"
      , balanceOf.`$ref` = "#/definitions/BalanceOf"
      }
    , required =
      [ "_balanceProfits"
      , "_balanceToken"
      , "_balanceVault"
      , "_deposit"
      , "_totalSupply"
      , "_withdraw"
      , "balanceOf"
      ]
    , title = "YVault"
    , type = "object"
    }
  }
}
