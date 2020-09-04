#!/bin/usr/env bash
curl \
  --header "Authorization: Token c8ba7ebc-950c-49a5-ad5f-d69aa31a2c60" \
  --header "Content-Type: application/json" \
  --data "{
    \"values\":[
      {
        \"line\":\"a\",
        \"value\":\"1 %\"
      },
      {
        \"line\":\"b\",
        \"value\":\"2 %\"
      },
      {
        \"line\":\"c\",
        \"value\":\"3 %\"
      }
    ],
    \"sha\":\"${GITHUB_SHA}\"
  }" \
  https://seriesci.com/api/sambacha/yearn-vault-schema/:series/many
