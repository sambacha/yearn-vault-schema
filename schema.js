"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var basic_type_schemas_1 = require("../schemas/basic_type_schemas");
var block_range_schema_1 = require("../schemas/block_range_schema");
var ec_signature_schema_1 = require("../schemas/ec_signature_schema");
var index_filter_values_schema_1 = require("../schemas/index_filter_values_schema");
var signed_orders_schema_1 = require("../schemas/signed_orders_schema");
var token_schema_1 = require("../schemas/token_schema");
var tx_data_schema_1 = require("../schemas/tx_data_schema");
exports.schemas = {
    numberSchema: basic_type_schemas_1.numberSchema,
    addressSchema: basic_type_schemas_1.addressSchema,
    ecSignatureSchema: ec_signature_schema_1.ecSignatureSchema,
    ecSignatureParameterSchema: ec_signature_schema_1.ecSignatureParameterSchema,
    indexFilterValuesSchema: index_filter_values_schema_1.indexFilterValuesSchema,
    signedOrderSchema: order_schemas_1.signedOrderSchema,
    signedOrdersSchema: signed_orders_schema_1.signedOrdersSchema,
    blockParamSchema: block_range_schema_1.blockParamSchema,
    blockRangeSchema: block_range_schema_1.blockRangeSchema,
    tokenSchema: token_schema_1.tokenSchema,
    jsNumber: tx_data_schema_1.jsNumber,
    txDataSchema: tx_data_schema_1.txDataSchema,
};
