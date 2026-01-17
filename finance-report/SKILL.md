---
name: finance-report
description: Generate comprehensive financial report analysis in markdown format. Use when user needs to analyze a company's financial report and create a financial analysis report based on annual report files (PDF) and reference materials in current folder. The report includes financial performance analysis, revenue and profit trends, segment analysis, cash flow analysis, balance sheet health, risk factors, and management outlook. Unlike investment reports which focus on valuation, this skill focuses on interpreting and analyzing the financial report itself.
---

# Financial Report Analysis

Generate comprehensive financial report analysis from a company's annual report (10-K/Form 20-F) and financial statements.

## Workflow

1. **Identify report** - Search current folder for financial report files (PDF, typically 10-K, 20-F, or annual reports)
2. **Extract company information** - Read the financial report to extract:
   - Company name and ticker
   - Report period
   - Currency
3. **Analyze financial statements** - Extract and analyze data from:
   - Income statement (statement of operations)
   - Balance sheet
   - Cash flow statement
   - Notes to financial statements
4. **Generate and save analysis report** - Create markdown report content, then use Write tool to save as `{ticker}_financial_analysis.md` in the current working directory

## Report Structure

### Executive Summary

Brief overview of the company's financial performance during the reporting period, highlighting key metrics and trends.

### 1. Company Overview

- Company name and ticker
- Business description
- Report period and currency

### 2. Revenue Analysis

- Total revenue and year-over-year growth
- Revenue trends over recent years
- Segment-wise revenue breakdown
- Geographic revenue distribution
- Factors affecting revenue

### 3. Profitability Analysis

- Gross profit and gross margin trends
- Operating income and operating margin
- Net income and net margin
- Earnings per share (EPS) trends
- Key drivers of profitability changes

### 4. Expense Analysis

- Cost of goods sold (COGS) trends
- Operating expenses breakdown (R&D, SG&A, etc.)
- Expense as percentage of revenue
- Significant expense items

### 5. Cash Flow Analysis

- Operating cash flow and trends
- Investing cash flow (capital expenditures, acquisitions)
- Financing cash flow (debt, equity, dividends)
- Free cash flow calculation
- Cash position and liquidity

### 6. Balance Sheet Analysis

- Total assets composition
- Current assets and current liabilities
- Working capital position
- Debt analysis (short-term, long-term)
- Equity structure
- Key ratios: current ratio, debt-to-equity

### 7. Segment and Product Performance

- Business segment performance
- Product/service revenue breakdown
- Regional performance

### 8. Risk Factors and Challenges

- Key risks mentioned in the report
- Regulatory or market risks
- Competitive landscape

### 9. Management Discussion and Outlook

- Management's commentary on performance
- Future outlook and guidance
- Strategic initiatives

### 10. Key Financial Metrics Table

Table of key financial metrics for the current year:

| Metric | Current Year | Prior Year | Change |
|--------|--------------|------------|--------|
| Revenue | | | |
| Gross Profit | | | |
| Gross Margin (%) | | | |
| Operating Income | | | |
| Operating Margin (%) | | | |
| Net Income | | | |
| Net Margin (%) | | | |
| EPS | | | |
| Operating Cash Flow | | | |
| Free Cash Flow | | | |
| Total Assets | | | |
| Total Debt | | | |
| Current Ratio | | | |

## Important Notes

- Read the financial report PDF directly to extract data
- Focus on factual analysis rather than investment recommendations
- Include specific numbers from the financial statements
- Note any significant changes year-over-year
- Report should be written in Chinese
- Report should be saved as `{ticker}_financial_analysis.md` in the current folder
- Cite the source document for all data points: `[来源: 财报文件名]`
