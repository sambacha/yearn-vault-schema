export declare const schemas: {
    numberSchema: {
        id: string;
        type: string;
        pattern: string;
    };
    addressSchema: {
        id: string;
        type: string;
        pattern: string;
    };
    ecSignatureSchema: {
        id: string;
        properties: {
            v: {
                type: string;
                minimum: number;
                maximum: number;
            };
            r: {
                $ref: string;
            };
            s: {
                $ref: string;
            };
        };
        required: string[];
        type: string;
    };
    ecSignatureParameterSchema: {
        id: string;
        type: string;
        pattern: string;
    };
    indexFilterValuesSchema: {
        id: string;
        additionalProperties: {
            oneOf: {
                $ref: string;
            }[];
        };
        type: string;
    };
    blockParamSchema: {
        id: string;
        oneOf: ({
            type: string;
            enum?: undefined;
        } | {
            enum: string[];
            type?: undefined;
        })[];
    };
    blockRangeSchema: {
        id: string;
        properties: {
            fromBlock: {
                $ref: string;
            };
            toBlock: {
                $ref: string;
            };
        };
        type: string;
    };
    tokenSchema: {
        id: string;
        properties: {
            name: {
                type: string;
            };
            symbol: {
                type: string;
            };
            decimals: {
                type: string;
            };
            address: {
                $ref: string;
            };
        };
        required: string[];
        type: string;
    };
    jsNumber: {
        id: string;
        type: string;
        minimum: number;
    };
    txDataSchema: {
        id: string;
        properties: {
            from: {
                $ref: string;
            };
            to: {
                $ref: string;
            };
            value: {
                oneOf: {
                    $ref: string;
                }[];
            };
            gas: {
                oneOf: {
                    $ref: string;
                }[];
            };
            gasPrice: {
                oneOf: {
                    $ref: string;
                }[];
            };
            data: {
                type: string;
                pattern: string;
            };
            nonce: {
                type: string;
                minimum: number;
            };
        };
        required: string[];
        type: string;
        additionalProperties: boolean;
    };

};
