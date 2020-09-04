# Development Specification

This document is intended to detail the `+dev` version of the schema. It is used to document changes between versions along with record design decisions, etc.

## +dev Changes

> `+dev` refers to the `semver` option after the patch identifier so that there is not changes in the `0.0.x` portion of versioning

### \$id

ADD: Versioning in `$id` reference at top, i.e.: `"$id": "https://yearn.finance/v0.1.0+dev/vault.schema.json",`

### Properties

ADD: `properties` field

## Vault Strategy

```json
            "vaultStrategy": {
                "type": "object",
                "description": "a strategy associated with this specific vault",
                "items": {
                    "$ref": "#/definitions/yEarnVault"
                },
                "maxLength": 18,
                "examples": ["vault", "aave"]
            }
```

### Keywords

TODO: create a list of `keywords` for vaults && strategies

### Tags

TODO: create a list of `tags` for vaults && strategies

### yipId

```json
            "yipId": {
                "type": "string",
                "description": "The associated YIP for this vault and/or strategy",
                "minLength": 5,
                "maxLength": 8,
                "pattern": "/^[a-zA-Z-][a-zA-Z0-9-]*$",
                "examples": ["YIP-40"]
            }
```

## Notes

-   il8n - translations
-   additional parameters useful for UIs
-   additional parameters or structuring to make usability easier
