---
name: macrotrends
description: Access and retrieve company financial data from macrotrends.net. Use when Claude needs to fetch financial statements such as income statements, cash flow statements, balance sheets, and free cash flow for publicly traded companies. Supports queries like "Get Apple's financial statements" or "Fetch the cash flow statement for TSLA" or "Get AAPL's free cash flow".
---

# Macrotrends

## Overview

Use agent-browser to access macrotrends.net and retrieve company financial data including income statements, cash flow statements, and balance sheets.

## URL Patterns

| Statement Type | URL Pattern | Example |
|----------------|-------------|---------|
| Income Statement | `https://www.macrotrends.net/stocks/charts/{TICKER}/{company-name}/financial-statements` | https://www.macrotrends.net/stocks/charts/AAPL/apple/financial-statements |
| Cash Flow Statement | `https://www.macrotrends.net/stocks/charts/{TICKER}/{company-name}/cash-flow-statement` | https://www.macrotrends.net/stocks/charts/AAPL/apple/cash-flow-statement |
| Balance Sheet | `https://www.macrotrends.net/stocks/charts/{TICKER}/{company-name}/balance-sheet` | https://www.macrotrends.net/stocks/charts/AAPL/apple/balance-sheet |
| Free Cash Flow | `https://www.macrotrends.net/stocks/charts/{TICKER}/{company-name}/free-cash-flow` | https://www.macrotrends.net/stocks/charts/AAPL/apple/free-cash-flow |

## Workflow

1. **Identify the company and statement type** from the user's request
   - Extract the stock ticker (e.g., AAPL, TSLA, MSFT)
   - Determine which statement type(s) to retrieve

2. **Construct the URL** using the appropriate pattern from the table above

3. **Use agent-browser to access the page** (use headed mode for Cloudflare):
   ```bash
   agent-browser open <URL>
   agent-browser snapshot
   ```

4. **Extract financial data** from the page:
   - Use `agent-browser get text <selector>` or `agent-browser snapshot` to capture the data tables
   - Common selectors: `.table`, `.dataTable`, or tables containing financial data

5. **Format and present the data** to the user

## Tips

- The ticker symbol is typically 1-5 uppercase letters (e.g., AAPL, MSFT, GOOGL)
- If the company name contains multiple words, use hyphens (e.g., `meta-platforms`)
- Some pages may require scrolling to view all data: `agent-browser scroll down`
- Use `screenshot` if a visual representation is needed
