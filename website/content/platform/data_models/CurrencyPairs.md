---
title: Currency Search
description: OpenBB Platform Data Model
---

<!-- markdownlint-disable MD012 MD031 MD033 -->

import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

---

## Implementation details

### Class names

| Model name | Parameters class | Data class |
| ---------- | ---------------- | ---------- |
| `CurrencyPairs` | `CurrencyPairsQueryParams` | `CurrencyPairsData` |

### Import Statement

```python
from openbb_core.provider.standard_models.currency_pairs import (
CurrencyPairsData,
CurrencyPairsQueryParams,
)
```

## Parameters

<Tabs>
<TabItem value="standard" label="Standard">

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| provider | Literal['fmp', 'intrinio', 'polygon'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'fmp' if there is no default. | fmp | True |
</TabItem>

<TabItem value='polygon' label='polygon'>

| Name | Type | Description | Default | Optional |
| ---- | ---- | ----------- | ------- | -------- |
| provider | Literal['fmp', 'intrinio', 'polygon'] | The provider to use for the query, by default None. If None, the provider specified in defaults is selected or 'fmp' if there is no default. | fmp | True |
| symbol | str | Symbol of the pair to search. | None | True |
| date | date | A specific date to get data for. | 2023-11-12 | True |
| search | str | Search for terms within the ticker and/or company name. |  | True |
| active | bool | Specify if the tickers returned should be actively traded on the queried date. | True | True |
| order | Literal['asc', 'desc'] | Order data by ascending or descending. | asc | True |
| sort | Literal['ticker', 'name', 'market', 'locale', 'currency_symbol', 'currency_name', 'base_currency_symbol', 'base_currency_name', 'last_updated_utc', 'delisted_utc'] | Sort field used for ordering. |  | True |
| limit | int | The number of data entries to return. | 1000 | True |
</TabItem>

</Tabs>

## Data

<Tabs>
<TabItem value="standard" label="Standard">

| Name | Type | Description |
| ---- | ---- | ----------- |
| name | str | Name of the currency pair. |
</TabItem>

<TabItem value='fmp' label='fmp'>

| Name | Type | Description |
| ---- | ---- | ----------- |
| name | str | Name of the currency pair. |
| symbol | str | Symbol of the currency pair. |
| currency | str | Base currency of the currency pair. |
| stock_exchange | str | Stock exchange of the currency pair. |
| exchange_short_name | str | Short name of the stock exchange of the currency pair. |
</TabItem>

<TabItem value='intrinio' label='intrinio'>

| Name | Type | Description |
| ---- | ---- | ----------- |
| name | str | Name of the currency pair. |
| code | str | Code of the currency pair. |
| base_currency | str | ISO 4217 currency code of the base currency. |
| quote_currency | str | ISO 4217 currency code of the quote currency. |
</TabItem>

<TabItem value='polygon' label='polygon'>

| Name | Type | Description |
| ---- | ---- | ----------- |
| name | str | Name of the currency pair. |
| market | str | Name of the trading market. Always 'fx'. |
| locale | str | Locale of the currency pair. |
| currency_symbol | str | The symbol of the quote currency. |
| currency_name | str | Name of the quote currency. |
| base_currency_symbol | str | The symbol of the base currency. |
| base_currency_name | str | Name of the base currency. |
| last_updated_utc | datetime | The last updated timestamp in UTC. |
| delisted_utc | datetime | The delisted timestamp in UTC. |
</TabItem>

</Tabs>
