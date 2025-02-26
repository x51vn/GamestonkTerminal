"""Tiingo provider module."""

from openbb_core.provider.abstract.provider import Provider
from openbb_tiingo.models.company_news import TiingoCompanyNewsFetcher
from openbb_tiingo.models.crypto_historical import TiingoCryptoHistoricalFetcher
from openbb_tiingo.models.currency_historical import TiingoCurrencyHistoricalFetcher
from openbb_tiingo.models.equity_historical import TiingoEquityHistoricalFetcher
from openbb_tiingo.models.trailing_dividend_yield import TiingoTrailingDivYieldFetcher
from openbb_tiingo.models.world_news import TiingoWorldNewsFetcher

tiingo_provider = Provider(
    name="tiingo",
    website="https://tiingo.com/",
    description="""""",
    credentials=["token"],
    fetcher_dict={
        "EquityHistorical": TiingoEquityHistoricalFetcher,
        "CompanyNews": TiingoCompanyNewsFetcher,
        "WorldNews": TiingoWorldNewsFetcher,
        "CryptoHistorical": TiingoCryptoHistoricalFetcher,
        "CurrencyHistorical": TiingoCurrencyHistoricalFetcher,
        "TrailingDividendYield": TiingoTrailingDivYieldFetcher,
    },
)
