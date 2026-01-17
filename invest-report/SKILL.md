---
name: invest-report
description: Generate comprehensive investment research reports in markdown format. Use when user needs to analyze a company and create an investment research report based on annual report files in current folder. The report includes business model analysis, business segments with revenue breakdown, profit sources, ecosystem analysis, capital allocation (dividends, buybacks, investments), profit stability, balance sheet analysis, and DCF valuation. Requires access to macrotrends skill for historical financial data.
---

# Investment Research Report Generator

Generate comprehensive investment research reports from a company's annual report and financial data.

## Workflow

1. **Identify company** - Search current folder for annual report files (PDF) to determine company ticker and name
2. **Extract company info** - Read annual report to extract:
   - Company name and ticker
   - Business model
   - Business segments and revenue breakdown
   - Sources of profit
   - Ecosystem/partners
   - Recent capital allocation activities
   - Profit stability indicators
   - Balance sheet highlights
3. **Get financial data** - Use `macrotrends` skill to fetch:
   - Last 10 years: dividend per share, payout ratio
   - Last 10 years: revenue, net income, operating cash flow, capex, free cash flow
   - Share count for buyback calculations
4. **Generate report** - Create markdown file with 8 chapters as specified below

## Report Structure

Generate report named `{ticker}_investment_report.md` with:

### Chapter 1: Business Model

Analyze and describe company's core business model based on annual report.

### Chapter 2: Business Segments

List all business segments with their revenue percentages.

### Chapter 3: Sources of Profit

Identify and explain main sources of profit.

### Chapter 4: Ecosystem

Describe company's ecosystem, partnerships, and competitive positioning.

### Chapter 5: Capital Allocation

#### Dividends
- Recent year dividend yield (dividend / current stock price)
- Last 10 years dividend data table (year, dividend per share, trend)
- Recent year payout ratio (dividends / net income)

#### Buybacks
- Recent year buyback yield (shares repurchased value / market cap)
- Compare with 5 years ago: did buybacks increase or decrease relative to stock compensation dilution?

#### Important Investments
Table of major investments in last 10 years: year, description, amount, purpose.

### Chapter 6: Profit Stability

Analyze profit stability from annual report data.

### Chapter 7: Balance Sheet

Summarize key balance sheet metrics and trends.

### Chapter 8: Valuation

#### Historical Financial Data Table (last 10 years, most recent first)
| Year | Revenue | Net Income | OCF | Capex | FCF | Revenue Growth | NI Growth | FCF Growth |

#### DCF Valuation
Use discount rate of 10%. Calculate fair value for 4 scenarios:
- 0% perpetual growth
- -5% perpetual growth
- 5% perpetual growth
- Your estimated perpetual growth rate (justify based on historical trends)

For each scenario, show:
- Present value of future cash flows
- Terminal value
- Total enterprise value
- Less net debt
- Equity value
- Fair value per share

## Important Notes

- All financial data in tables should use most recent year at top
- Growth rates should be calculated year-over-year
- Justify all assumptions (growth rate, discount rate, terminal multiple)
- Use Chinese language for report content if annual report is in Chinese
