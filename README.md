# yfiVaultSchemas

> a JSON schema for yearn vaults

The JSON schema represents the technical specification for yfi vaults - which can be used in in a RESTful API, dApp interface, etc.

## Overview

**SEE** `schema.yif.json`

## Conventions

use `camelCase`

## JSON Schema \$id

The JSON schema ID is [schema.yfi.json](schema.yfi.json))

## Validating the JSON Schema

`yarn run test`

## Authoring token lists

## Semantic versioning

The Vault Lists include a `version` field, which follows [semantic versioning](https://semver.org/).

List versions must follow the rules:

- Increment major version when vaults are removed/migrated
- Increment minor version when vaults are added
- Increment patch version when vaults already on the list have minor details changed (name, symbol, logo URL, decimals)

Changing a token address or chain ID is considered both a remove and an add, and should be a major version update.

Note that list versioning is used to improve the user experience, but not for security, i.e. list versions are not meant to provide protection against malicious updates to a token list; i.e. the list semver is used as a lossy compression of the diff of list updates. List updates may still be diffed in the client dApp.

## Contributors

Thanks to `x48` for creating the original JSON file that this utilizes which can be accessed in [`/archive`](/archive)

## License

ISC - CC0-1.0
