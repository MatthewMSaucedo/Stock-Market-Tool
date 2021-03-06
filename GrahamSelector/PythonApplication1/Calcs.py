

class Names:
	# Basics
	MARGINAL_TAX_RATE				= "Marginal Corporate Tax Rate" #(Taxable Income above $18.333 million)
	FAIR_RETURN_RATE				= "Graham's Fair Rate of Return (%)"
	REV_GROWTH_RATE 				= "Revenue Growth Rate (%)"
	EBITDA_GROWTH_RATE 				= "EBITDA Growth Rate (%)"
	EBIT_GROWTH_RATE 				= "EBIT Growth Rate (%)"
	NI_GROWTH_RATE 					= "Net Income Growth Rate (%)"
	EPS_GROWTH_RATE 				= "EPS Growth Rate (%)"
	GROWTH_RATE 					= "Generic Growth Rate (%)"
	AVG_3YEARS						= "3 Year Average"
	AVG_5YEARS						= "5 Year Average"
	COST_OF_SALES					= "Cost of Sales"
	WORKING_CAPITAL					= "Working Capital"
	CAPITAL_EMPLOYED				= "Capital Employed"
	TOTAL_INVEST					= "Total Investments"
	TOTAL_DEBT						= "Total Debt"
	EBITDA							= "Earnings Before Interst, Taxes, Depreciation, and Amortization"
	EBIAT							= "Earnings Before Interst, Amortization, and Taxes"
	EBIT							= "Earnings Before Interest and Taxes"
	CAPEX							= "Capital Expenditures"
	LEV_FCF							= "Levered Free Cash Flow" #More Important for Investors as it is what has been leftover after mandatory debt payments
	UN_LEV_FCF						= "Unlevered Free Cash Flow"
	
	# Averages
	AVG_RECEIVABLES					= "Average Accounts Receivable"
	AVG_PAYABLES_ACCRUALS			= "Average Accounts Payable & Accruals"
	AVG_WORKING_CAPITAL				= "Average Working Capital"
	AVG_INVENTORY					= "Average Inventory"
	AVG_INVEST						= "Average Investment Amount"
	AVG_LT_ASSETS					= "Average Long Term Assets"
	AVG_ASSETS						= "Average Total Assets"
	AVG_LIABILITIES					= "Average Total Liabilities"
	AVG_EQUITY						= "Average Equity"
	AVG_DEBT						= "Average Total Debt"
	
	# Solvency:
	CASH_RATIO						= "Cash Ratio"
	CASH_SERVICE_RATIO				= "Cash Service Ratio"			
	INT_SERVICE_RATIO				= "Interest Service Ratio"	
	CASH_COVERAGE_RATIO				= "Cash Coverage Ratio"
	ACID_TEST						= "Acid Test Ratio"
	QUICK_RATIO						= "Quick Ratio"
	QUICK_RATIO_2					= "Quick Ratio"	# (with Prepaid Expenses subtracted)
	CURRENT_RATIO					= "Current Ratio"
	WORKING_CAP_RATIO				= "Net Working Capital Ratio"
	DEBT_SERVICE_RATIO				= "Debt Service Ratio"			
	
	# Capital Structure
	NET_DEBT						= "Net Debt"
	DEBT_RATIO						= "Debt Ratio"
	DEBT_EQ_RATIO					= "Debt to Equity Ratio"
	DEBT_TO_NI						= "Debt to Income Ratio"
	FIXED_CHARGE_COVERAGE			= "Fixed Charge Coverage"
	DEGREE_COMBINED_LEV				= "Degree of Combined Leverage"
	DEGREE_OPERATING_LEV			= "Degree of Operating Leverage"
	DEGREE_FINANCIAL_LEV			= "Degree of Financial Leverage"
	DFL_RATIO						= "Degree of Financial Leverage Ratio"
	FINANCIAL_LEVERAGE				= "Financial Leverage"
	EQUITY_RATIO					= "Equity Ratio"
	EQUITY_MULTIPLIER_RATIO_1		= "Equity Multiplier"
	EQUITY_MULTIPLIER_RATIO_2		= "Equity Multiplier using Debt Ratio"
	NAV								= "Net Asset Value"
	EFFECTIVE_INT_RATE				= "Effective Interest Rate (%)"
	DEBT_COST_CAP					= "Debt to Cost of Capital"
	WACC							= "Weighted Average Cost of Capital"
	
	# Asset Activity
	SALES_TURNOVER					= "Sales Turnover"
	DSO								= "Days Sales Outstanding"
	ASSET_TURNOVER					= "Asset Turnover"
	ASSET_TURN_RATE					= "Asset Turnover Rate in Days"
	LT_ASSET_TURNOVER				= "Long Term Asset Turnover"
	LT_ASSET_TURN_RATE				= "Long Term Asset Turnover Rate in Days"
	INV_SALES_TURNOVER				= "Inventory Sales Turnover"
	DSI								= "Days Sales Inventory"	
	INV_COGS_TURNOVER				= "Inventory COGS Turnover"
	DIO								= "Days Inventory Outstanding "
	RECEIVABLES_ACCTS_TURNOVER		= "Accounts Receivables Turnover"
	DRO 							= "Days Receivables Outstanding"
	WORKING_CAP_TURNOVER			= "Working Capital Turnover"
	DWC								= "Days Working Capital"
	ROI_INVESTMENTS					= "Return on Investments"
	
	# Liability Activity
	CREDITORS_TURNOVER				= "Creditors Turnover"
	CDO								= "Creditors Days Outstandings"
	PAYABLES_TURNOVER_COGS			= "Payables Turnover using COGS"
	DPO_COGS						= "Days Payables Outstanding using COGS"
	PAYABLES_TURNOVER_COS			= "Payables Turnover using Cost of Sales"
	DPO_COS							= "Days Payables Outstanding using Cost of Sales"
	LIAB_TURNOVER					= "Liabilities Turnover"
	LIAB_TURN_RATE					= "Liabilities Turnover Rate in Days"		
	CHG_DEBT_REPAYMENT_REQ			= "Change in Required Short Term Debt Repayments"
	DEBTORS_PAYBACK_PERIOD			= "Pace of Debt Repayment"
	BURN_RATE						= "Burn Rate (%)"
	
	# Profitability 
	CCC								= "Cash Conversion Cycle"
	ROS								= "Return on Sales"
	ROE								= "Return on Equity"	
	ROA								= "Return on Assets"
	ROCE_NI							= "Return on Capital Employed using Net Income"
	EPS_DILUTED_NI					= "Earnings per Share on Diluted Shares"
	EPS_DILUTED_EBIT				= "EBIT per Share on Diluted Shares"
	ROCE_EBIT						= "Return on Capital Employed using EBIT"
	PE								= "Price to Earnings Ratio"
	PE_REL_3						= "3 Year Average of PE Ratio"
	PE_REL_5						= "5 Year Average of PE Ratio"
	EARNINGS_POWER 					= "Earnings Power"
	GROSS_MARGIN					= "Gross Margin"
	NOPAT_NI						= "Net Operating Profit After Tax using Net Income"
	NOPAT_EBIT						= "Net Operating Profit After Tax using Operating Income"
	ROIC							= "Return on Invested Capital"
	OPERATING_RATIO					= "Operating Ratio"
	OP_PROFIT_MARGIN				= "Operating Profit Margin"
	
	# Valuation Measures
	MV								= "Market Value"
	MV_EBIT_RATIO					= "Market Value to Cash Flow"
	ORIG_GRAHAM						= "Original Graham Equation" #TRY Net Income vs. EBIT vs EBITDA
	REVISED_GRAHAM					= "Revised Graham Equation" #TRY Net Income vs. EBIT vs EBITDA
	EV								= "Enterprise Value"
	EV_EBIT							= "Enterprise Value to Cash Flow"
	EV_NI							= "Enterprise Value to Net Income"
	BV								= "Book Value"	
	BV_PER_SHARE					= "Book Value per Share Outstanding"
	BV_NI							= "Book Value to Net Income"
	BV_EBIT							= "Book Value to Cash Flow"
	PRICE_SALES						= "Price to Sales Ratio"
	PRICE_BOOK						= "Price to Book Ratio"
	PRICE_NAV						= "Price to Net Asset Value"
	PRICE_FCF						= "Price to Free Cash Flow"
	PRICE_UN_FCF					= "Price to UnLevered Free Cash Flow"
	MV_OCF							= "Price to Operating Cash Flow"
	CASH_PRICE_RATIO				= "Cash to Price Ratio"
	INTRINSIC_VALUE_NI				= "Intrinsic Value by 3 Year Net Income Average"
	INTRINSIC_VALUE_EBIT 			= "Intrinsic Value by 3 Year EBIT Average"
	INTRINSIC_VALUE_FCF				= "Intrinsic Value by Free Cash Flow"
	MARGIN_OF_SAFETY_NI				= "Margin of Safety by 3 Year Net Income Average"
	MARGIN_OF_SAFETY_EBIT			= "Margin of Safety by 3 Year EBIT Average"
	MARGIN_OF_SAFETY_FCF			= "Margin of Safety by Free Cash Flow"
	DUPONT_SYSTEM_1					= "DuPont System of Valuation Method 1"
	DUPONT_SYSTEM_2					= "DuPont System of Valuation Method 2"
	
	# Dividend Measures:
	RETENTION_RATIO					= "Retention Ratio"
	DIV_PAYOUT_RATIO				= "Dividend Payout Ratio"
	EARNINGS_YIELD					= "Earnings Yield Ratio"
	DIVS_YIELD						= "Dividends Yield Ratio"
	SGR								= "Sustainable Growth Rate (%)"


class Formulas:
	# Basics
	MARGINAL_TAX_RATE				= "35%"
	FAIR_RETURN_RATE				= "1 / 8.5 (No Growth PE)"
	REV_GROWTH_RATE 				= "Revenue Growth Rate" "(Current Revenue - Previous Revenue) / Previous Revenue"
	EBITDA_GROWTH_RATE 				= "EBITDA Growth Rate" "(Current EBITDA - Previous EBITDA) / Previous EBITDA"
	EBIT_GROWTH_RATE 				= "EBIT Growth Rate" "(Current EBIT - Previous EBIT) / Previous EBIT"
	NI_GROWTH_RATE 					= "Net Income Growth Rate" "(Current Net Income - Previous Net Income) / Previous Net Income"
	EPS_GROWTH_RATE 				= "EPS Growth Rate" "(Current EPS - Previous EPS) / Previous EPS"
	GROWTH_RATE 					= "(Current Value - Previous Value) / Previous Value"
	AVG_3YEARS						= "(Current Value + Previous(1) + Previous(2) values) / 3"
	AVG_5YEARS						= "(Current Value + Previous(1) + Previous(2) values) / 5"
	COST_OF_SALES					= "Beginning Inventory + Purchases - Ending Inventory"
	WORKING_CAPITAL					= "Current Assets - Current Liabilities"
	CAPITAL_EMPLOYED				= "Total Assets - Current Liabilities"
	TOTAL_INVEST					= "Short Term Investments + Long Term Investments"
	TOTAL_DEBT						= "ST_Debt + LT_Debt"
	EBITDA							= "Net Income + Interest + Taxes + Depreciation + Amortization"
	EBIAT							= "Earnings + Interst + Amortization + Taxes"
	EBIT							= "Net Income + Interest + Taxes"
	CAPEX							= "Current PP&E - Previous PP&E + Accumulated Depreciation"
	LEV_FCF							= "Net Income + Depreciation + Amortization - (Change) Net Working Capital - Capital Expenditures"
	UN_LEV_FCF						= "Net Income + Non-Cash Expenses - (Change) Net Working Capital - Capital Expenditures"
	
	# Averages
	AVG_RECEIVABLES					= "1/2 (Beginning + Ending) Accounts Receivable"
	AVG_PAYABLES_ACCRUALS			= "1/2 (Beginning + Ending) Accounts Payable and Accruals"
	AVG_WORKING_CAPITAL				= "1/2 (Beginning + Ending) Working Capital"
	AVG_INVENTORY					= "1/2 (Beginning + Ending) Inventory"
	AVG_INVEST						= "1/2 (Beginning + Ending) Investments"
	AVG_LT_ASSETS					= "1/2 (Beginning + Ending) Long Term Assets"
	AVG_ASSETS						= "1/2 (Beginning + Ending) Assets"
	AVG_LIABILITIES					= "1/2 (Beginning + Ending) Liabilities"
	AVG_EQUITY						= "1/2 (Beginning + Ending) Equity"
	AVG_DEBT						= "1/2 (Beginning + Ending) Total Debt"
	
	# Solvency:
	CASH_RATIO						= "(Cash + Cash Equivalents) / Current Liabilities"
	CASH_SERVICE_RATIO				= "(Cash & Cash Equivalents) / Interest Expense"
	INT_SERVICE_RATIO				= "EBIT / Interest Expense"
	CASH_COVERAGE_RATIO				= "Cash & Cash Equivalents / Short Term Debt"
	ACID_TEST						= "(Cash + Cash Equivalents + Marketable Securities + Current Accounts Receivable) / Current Liabilities"
	QUICK_RATIO						= "(Current Assets - Inventory) / Current Liabilities"
	QUICK_RATIO_2					= "(Current Assets - Inventory - Prepaid Expenses) / Current Liabilities"
	CURRENT_RATIO					= "Current Assets / Current Liabilities"
	WORKING_CAP_RATIO				= "(Current Assets - Current Liabiities) / Total Assets"
	DEBT_SERVICE_RATIO				= "EBIT / Total Debt Payments"
	
	# Capital Structure
	NET_DEBT						= "Total Debt - Cash & Cash Equivalents"
	DEBT_RATIO						= "Total Debt / Assets"
	DEBT_EQ_RATIO					= "Total Debt / Equity"
	DEBT_TO_NI						= "Total Debt / NI"
	FIXED_CHARGE_COVERAGE			= "(EBIT + Fixed Charges Before Tax) / (Fixed Charges Before Tax * interest)"
	DEGREE_COMBINED_LEV				= "(% Change EPS) / (% Change Sales)"
	DEGREE_OPERATING_LEV			= "(% Change EBIT) / (% Change Sales)"
	DEGREE_FINANCIAL_LEV			= "(% Change EPS) / (% Change EBIT)"
	DFL_RATIO						= "EBIT / (EBIT - Interest)"
	FINANCIAL_LEVERAGE				= "Average assets / Average Equity"
	EQUITY_RATIO					= "Equity / Total Assets"
	EQUITY_MULTIPLIER_RATIO_1		= "Total Assets / Total Equity"
	EQUITY_MULTIPLIER_RATIO_2		= "1 / (1 - Debt Ratio)"
	NAV								= "(Total Assets - Total Liabilities) / Diluted Shares"
	EFFECTIVE_INT_RATE				= "Interest / Total Debt * 100"
	DEBT_COST_CAP					= "Effective Interest Rate * (1 - Marginal Tax Rate)"
	WACC							= "E / (E + D) * Cost of Equity + D / (E + D) * Cost of Debt *(1 - Tax Rate)"
	
	# Asset Activity
	SALES_TURNOVER					= "Accounts Receivable / Total Credit Sales"
	DSO								= "Sales Turnover * 365"
	ASSET_TURNOVER					= "Sales / Average Assets"
	ASSET_TURN_RATE					= "Days Asset Turnover * 365"
	LT_ASSET_TURNOVER				= "Sales / Average Net Long Term Assets"
	LT_ASSET_TURN_RATE				= "Days Long Term Asset * 365"
	INV_SALES_TURNOVER				= "Sales / Average Inventory"
	DSI								= "Days Sales Inventory * 365"
	INV_COGS_TURNOVER				= "COGS / Average Inventory"
	DIO								= "Days COGS Inventory * 365"
	RECEIVABLES_ACCTS_TURNOVER		= "Accounts Receivable / Sales"
	DRO								= "Days Accounts Receivable * 365"
	WORKING_CAP_TURNOVER			= "Sales / Average Working Capital"
	DWC								= "Days Working Capital * 365"
	ROI_INVESTMENTS					= "Cash from Investing Activities / Average (ST + LT) Investments"
	
	# Liability Activity
	CREDITORS_TURNOVER				= "Net Credit Sales / Average Accounts Receivable"
	CDO								= "Creditor's Turnover * 365"
	PAYABLES_TURNOVER_COGS			= "Accounts Payable / COGS"
	DPO_COGS						= "Cost of Goods Sold Payables Turnover * 365"
	PAYABLES_TURNOVER_COS			= "Average Accounts Payable / Cost of Sales"
	DPO_COS							= "Cost of Sales Payables Turnover * 365"
	LIAB_TURNOVER					= "Liabilities / Average Accounts Payable"
	LIAB_TURN_RATE					= "Liabilities Turnover * 365"
	CHG_DEBT_REPAYMENT_REQ			= "(Current Short Term Debt - Previous Short Term Debt) / Previous Short Term Debt * 100"
	DEBTORS_PAYBACK_PERIOD			= "Average Total Debt / Debt Payments"
	BURN_RATE						= "Cash + Cash Equivalents / (-) EBIT"
	
	# Profitability 
	CCC								= "DIO + DSO - DPO"
	ROS								= "Net Income / Sales"
	ROE								= "Net Income / Equity"	
	ROA								= "Net Income / Total Assets"
	ROCE_NI							= "Net Income / (Total Assets - Current Liabilities)"
	EPS_DILUTED_NI					= "Net Income / Diluted Shares Outstanding"
	EPS_DILUTED_EBIT				= "EBIT / Diluted Shares Outstanding"
	ROCE_EBIT						= "EBIT / (Total Assets - Current Liabilities"
	PE								= "Share Price / (Net Income / Diluted Shares)"
	PE_REL_3						= "(PE(year) + PE(year-1) + PE(year-2)) / 3"
	PE_REL_5						= "(PE(year) + PE(year-1) + PE(year-2)) + PE(year-3) + PE(year-4)) / 5"
	EARNINGS_POWER 					= "EBIT / Total Assets"
	GROSS_MARGIN					= "Gross Profit / Sales"
	NOPAT_NI						= "Net Income, Non-Operating After Tax (- Gains) (+ Losses) + Interest Expense"
	NOPAT_EBIT						= "Operating Income * (1 - Tax Rate)"
	ROIC							= "NOPAT / Invested Capital"
	OPERATING_RATIO					= "Operating Cost / Sales"
	OP_PROFIT_MARGIN				= "Operating Earnings / Sales"
	
	# Valuation Measures
	MV								= "Share Price * Diluted Shares"
	MV_EBIT_RATIO					= "Market Capitalization / EBIT"
	ORIG_GRAHAM						= "EPS * (No Growth PE + Growth Multiple * Rate of Growth)"
	REVISED_GRAHAM					= "(EPS * (No Growth PE + Growth Multiple * Rate of Growth) * Minimum Return) / AAA Bond Return"
	EV								= "Market Capitalziation + Total Debt - (Cash + Cash Equivlanets)"
	EV_EBIT							= "Enterprise Value / EBIT"
	EV_NI							= "Enterprise Value /  Net Income"
	BV								= "Total Assets - Intangible Assets - Total Liabilities"	
	BV_PER_SHARE					= "Book Value / Diluted Shares Outstanding"
	BV_NI							= "Book Value / Net Income"
	BV_EBIT							= "Book Value / EBIT"
	PRICE_SALES						= "Share Price / Sales"
	PRICE_BOOK						= "Share Price / Book Value"
	PRICE_NAV						= "Share Price / Net Asset Value"
	PRICE_FCF						= "Share Price / Free Cash Flow"
	PRICE_UN_FCF					= "Share Price / Free Cash Flow"
	MV_OCF							= "Market Value / Operating Cash Flow"
	CASH_PRICE_RATIO				= "Cash / Share Price"
	INTRINSIC_VALUE_NI				= "3 Year Net Income Average (ith year) / (1 + Discount rate) ^ (ith year)"
	INTRINSIC_VALUE_EBIT			= "3 Year EBIT Average (ith year) / (1 + Discount rate) ^ (ith year)"
	INTRINSIC_VALUE_FCF				= "Free Cash Flow Average (ith year) / (1 + Discount rate) ^ (ith year)"
	MARGIN_OF_SAFETY_NI				= "Intrinsic Value (using Net Income) / Market Capitalization"
	MARGIN_OF_SAFETY_EBIT			= "Intrinsic Value (using EBIT) / Market Capitalization"
	MARGIN_OF_SAFETY_FCF			= "Intrinsic Value (using Free Cash Flow) / Market Capitalization"
	DUPONT_SYSTEM_1					= "Net Profit Margin * Total Asset Turnover * Equity Multiplier"
	DUPONT_SYSTEM_2					= "Return on Assets * (1 + Debt to Equity Ratio)"
	
	# Dividend Measures:
	RETENTION_RATIO					= "Retained Earnings / Net Income"
	DIV_PAYOUT_RATIO				= "Dividends / Net Income"
	EARNINGS_YIELD					= "Net Income / Price"
	DIVS_YIELD						= "Dividends / Market Value"
	SGR								= "ROE * (1 - Dividend Payout Ratio)"


	
class Vars:
	# Basics
	MARGINAL_TAX_RATE				= [None] * 35
	FAIR_RETURN_RATE				= [None] * 35
	REV_GROWTH_RATE 				= [None] * 35
	EBITDA_GROWTH_RATE 				= [None] * 35
	EBIT_GROWTH_RATE 				= [None] * 35
	NI_GROWTH_RATE 					= [None] * 35
	EPS_GROWTH_RATE 				= [None] * 35
	GROWTH_RATE 					= [None] * 35
	AVG_3YEARS						= [None] * 35
	AVG_5YEARS						= [None] * 35
	COST_OF_SALES					= [None] * 35
	WORKING_CAPITAL					= [None] * 35
	CAPITAL_EMPLOYED				= [None] * 35
	TOTAL_INVEST					= [None] * 35
	TOTAL_DEBT						= [None] * 35
	EBITDA							= [None] * 35
	EBIAT							= [None] * 35
	EBIT							= [None] * 35
	CAPEX							= [None] * 35
	LEV_FCF							= [None] * 35
	UN_LEV_FCF						= [None] * 35
	# Average Functions:			  
	AVG_RECEIVABLES					= [None] * 35
	AVG_PAYABLES_ACCRUALS			= [None] * 35
	AVG_WORKING_CAPITAL				= [None] * 35
	AVG_INVENTORY					= [None] * 35
	AVG_INVEST						= [None] * 35
	AVG_LT_ASSETS					= [None] * 35
	AVG_ASSETS						= [None] * 35
	AVG_LIABILITIES					= [None] * 35
	AVG_EQUITY						= [None] * 35
	AVG_DEBT						= [None] * 35
	# Solvency:						  
	CASH_RATIO						= [None] * 35
	CASH_SERVICE_RATIO				= [None] * 35
	INT_SERVICE_RATIO				= [None] * 35
	CASH_COVERAGE_RATIO				= [None] * 35
	ACID_TEST						= [None] * 35
	QUICK_RATIO						= [None] * 35
	QUICK_RATIO_2					= [None] * 35
	CURRENT_RATIO					= [None] * 35
	WORKING_CAP_RATIO				= [None] * 35
	DEBT_SERVICE_RATIO				= [None] * 35
	# Capital Structure				
	NET_DEBT						= [None] * 35
	DEBT_RATIO						= [None] * 35
	DEBT_EQ_RATIO					= [None] * 35
	DEBT_TO_NI						= [None] * 35
	FIXED_CHARGE_COVERAGE			= [None] * 35
	DEGREE_COMBINED_LEV				= [None] * 35
	DEGREE_OPERATING_LEV			= [None] * 35
	DEGREE_FINANCIAL_LEV			= [None] * 35
	DFL_RATIO						= [None] * 35
	FINANCIAL_LEVERAGE				= [None] * 35
	EQUITY_RATIO					= [None] * 35
	EQUITY_MULTIPLIER_RATIO_1		= [None] * 35
	EQUITY_MULTIPLIER_RATIO_2		= [None] * 35
	NAV								= [None] * 35
	EFFECTIVE_INT_RATE				= [None] * 35
	DEBT_COST_CAP					= [None] * 35
	WACC							= [None] * 35
	# Asset Activity:
	SALES_TURNOVER					= [None] * 35
	DSO								= [None] * 35
	ASSET_TURNOVER					= [None] * 35
	ASSET_TURN_RATE					= [None] * 35
	LT_ASSET_TURNOVER				= [None] * 35
	LT_ASSET_TURN_RATE				= [None] * 35
	INV_SALES_TURNOVER				= [None] * 35
	DSI								= [None] * 35
	INV_COGS_TURNOVER				= [None] * 35
	DIO								= [None] * 35
	RECEIVABLES_ACCTS_TURNOVER		= [None] * 35
	DRO 							= [None] * 35
	WORKING_CAP_TURNOVER			= [None] * 35
	DWC								= [None] * 35
	ROI_INVESTMENTS					= [None] * 35
	# Liability Activity:
	CREDITORS_TURNOVER				= [None] * 35
	CDO								= [None] * 35
	PAYABLES_TURNOVER_COGS			= [None] * 35
	DPO_COGS						= [None] * 35
	PAYABLES_TURNOVER_COS			= [None] * 35
	DPO_COS							= [None] * 35
	LIAB_TURNOVER					= [None] * 35
	LIAB_TURN_RATE					= [None] * 35
	CHG_DEBT_REPAYMENT_REQ			= [None] * 35
	DEBTORS_PAYBACK_PERIOD			= [None] * 35
	BURN_RATE						= [None] * 35
	# Profitability:
	CCC								= [None] * 35
	ROS								= [None] * 35
	ROE								= [None] * 35
	ROA								= [None] * 35
	ROCE_NI							= [None] * 35
	EPS_DILUTED_NI					= [None] * 35
	EPS_DILUTED_EBIT				= [None] * 35
	ROCE_EBIT						= [None] * 35
	PE								= [None] * 35
	PE_REL_3						= [None] * 35
	PE_REL_5						= [None] * 35
	EARNINGS_POWER 					= [None] * 35
	GROSS_MARGIN					= [None] * 35
	NOPAT_NI						= [None] * 35
	NOPAT_EBIT						= [None] * 35
	ROIC							= [None] * 35
	OPERATING_RATIO					= [None] * 35
	OP_PROFIT_MARGIN				= [None] * 35
	# Valuation Measures:
	MV								= [None] * 35
	MV_EBIT_RATIO					= [None] * 35
	ORIG_GRAHAM						= [None] * 35
	REVISED_GRAHAM					= [None] * 35
	EV								= [None] * 35
	EV_EBIT							= [None] * 35
	EV_NI							= [None] * 35
	BV								= [None] * 35
	BV_PER_SHARE					= [None] * 35
	BV_NI							= [None] * 35
	BV_EBIT							= [None] * 35
	PRICE_SALES						= [None] * 35
	PRICE_BOOK						= [None] * 35
	PRICE_NAV						= [None] * 35
	PRICE_FCF						= [None] * 35
	PRICE_UN_FCF					= [None] * 35
	MV_OCF							= [None] * 35
	CASH_PRICE_RATIO				= [None] * 35
	INTRINSIC_VALUE_NI				= [None] * 35
	INTRINSIC_VALUE_EBIT 			= [None] * 35
	INTRINSIC_VALUE_FCF				= [None] * 35
	MARGIN_OF_SAFETY_NI				= [None] * 35
	MARGIN_OF_SAFETY_EBIT			= [None] * 35
	MARGIN_OF_SAFETY_FCF			= [None] * 35
	DUPONT_SYSTEM_1					= [None] * 35
	DUPONT_SYSTEM_2					= [None] * 35
	# Dividend Measures:
	RETENTION_RATIO					= [None] * 35
	DIV_PAYOUT_RATIO				= [None] * 35
	EARNINGS_YIELD					= [None] * 35
	DIVS_YIELD						= [None] * 35
	SGR								= [None] * 35

class Display:
	def GrowthRate(GROWTH_RATE):
		return round(GROWTH_RATE * 100, 2) if (GROWTH_RATE != None) else None


class Basics:
	def marginalTax():
		return 35
	def grahamFairReturnRate():
		return round(100 * (1 / 8.5), 2)
	def noGrowthPe():
		return 8.5	
	def growthMultiple():
		return 2
	def requiredReturn():
		return 4.4
	def aaaBondYield():
		return 3.04
	def growthRate(VALUE_0, VALUE_1):
		return ((VALUE_0 - VALUE_1) / VALUE_1) if (VALUE_0 != None and VALUE_1 != None and VALUE_1 != 0) else None	
	def avg(VALUE_0, VALUE_1):
		return ((VALUE_0 + VALUE_1) / 2) if (VALUE_0 != None and VALUE_1 != None) else None	
	def threeYearAvg(VALUE_0, VALUE_1, VALUE_2):
		return ((VALUE_0 + VALUE_1 + VALUE_2) / 3) if (VALUE_0 != None and VALUE_1 != None and VALUE_2 != None) else None	
	def fiveYearAvg(VALUE_0, VALUE_1, VALUE_2, VALUE_3, VALUE_4):
		return (VALUE_0 + VALUE_1 + VALUE_2 + VALUE_3 + VALUE_4) / 5 if (VALUE_0 != None and VALUE_1 != None and VALUE_2 != None and VALUE_3 != None and VALUE_4 != None) else None
	def costOfSales(INV_0, INV_1, CHG_INVENTORIES):
		return (INV_1 + CHG_INVENTORIES - INV_0) if (INV_0 != None and INV_1 != None and CHG_INVENTORIES != None) else None
	def workingCapital(TOTAL_CURR_ASSETS, TOTAL_CURR_LIAB):
		return (TOTAL_CURR_ASSETS - TOTAL_CURR_LIAB) if (TOTAL_CURR_ASSETS != None and TOTAL_CURR_LIAB != None) else None
	def capitalEmployed(TOTAL_ASSETS1, TOTAL_CURR_LIAB):
		return (TOTAL_ASSETS1 - TOTAL_CURR_LIAB) if (TOTAL_ASSETS1 != None and TOTAL_CURR_LIAB != None) else None
	def totalInvestments(ST_INVEST, LT_INVEST):
		return (ST_INVEST + LT_INVEST) if (ST_INVEST != None and LT_INVEST != None) else None
	def totalDebt(ST_DEBT, LT_DEBT):
		return (ST_DEBT + LT_DEBT) if (ST_DEBT != None and LT_DEBT != None) else None
	def ebitda(EBIT, DEPRE_AMORT):
		return (EBIT + DEPRE_AMORT) if (EBIT != None and DEPRE_AMORT != None) else None
	def ebiat(EBIT, DEPRE_AMORT, ACC_DEPREC):
		return (EBIT + DEPRE_AMORT - ACC_DEPREC) if (EBIT != None and DEPRE_AMORT != None and ACC_DEPREC != None) else None
	def ebit(NI_INC, INT_EXP, INC_TAX_EXPENSE):
		return (NI_INC + INT_EXP + INC_TAX_EXPENSE) if (NI_INC != None and INT_EXP != None) else None
	def capex(PPE_0, PPE_1, ACC_DEPREC):
		return (PPE_0 - PPE_1 + ACC_DEPREC) if (PPE_0 != None and PPE_1 != None and ACC_DEPREC != None) else None
	def leveredFreeCashFlow(NI_INC, DEPRE_AMORT, WORKING_CAPITAL_0, WORKING_CAPITAL_1, CAPEX):
		return (NI_INC + DEPRE_AMORT - (WORKING_CAPITAL_0 - WORKING_CAPITAL_1) - CAPEX) if (NI_INC != None and DEPRE_AMORT != None and WORKING_CAPITAL_0 != None and WORKING_CAPITAL_1 != None) else None
	def unleveredFreeCashFlow(NI_INC, NON_CASH_ITEMS, WORKING_CAPITAL_0, WORKING_CAPITAL_1, CAPEX):
		return (NI_INC + NON_CASH_ITEMS - (WORKING_CAPITAL_0 - WORKING_CAPITAL_1) - CAPEX) if (NI_INC != None and NON_CASH_ITEMS != None and WORKING_CAPITAL_0 != None and WORKING_CAPITAL_1 != None and CAPEX != None) else None
	
class Solvency: 
	def cashRatio(CASH_EQ, TOTAL_CURR_LIAB):
		return round((CASH_EQ / TOTAL_CURR_LIAB), 2) if (CASH_EQ != None and TOTAL_CURR_LIAB != None and TOTAL_CURR_LIAB != 0) else None
	def cashServiceRatio(CASH_EQ, INT_EXP):
		return round((CASH_EQ / INT_EXP), 2) if (CASH_EQ != None and INT_EXP != None and INT_EXP != 0) else None
	def interestServiceRatio(EBIT, INT_EXP):
		return round((EBIT / INT_EXP), 2) if (EBIT != None and INT_EXP != None and INT_EXP != 0) else None
	def cashCoverageRatio(CASH_EQ, ST_DEBT):
		return round((CASH_EQ / ST_DEBT), 2) if (CASH_EQ != None and ST_DEBT != None and ST_DEBT != 0) else None
	def acidTest(CASH_EQ_STI, ACCTS_REC, TOTAL_CURR_LIAB):
		return round(((CASH_EQ_STI + ACCTS_REC) / TOTAL_CURR_LIAB), 2) if (CASH_EQ_STI != None and ACCTS_REC != None and TOTAL_CURR_LIAB != None and TOTAL_CURR_LIAB != 0) else None
	def quickRatio(TOTAL_CURR_ASSETS, INV, TOTAL_CURR_LIAB):
		return round(((TOTAL_CURR_ASSETS - INV) / TOTAL_CURR_LIAB), 2) if (TOTAL_CURR_ASSETS != None and INV != None and TOTAL_CURR_LIAB != None and TOTAL_CURR_LIAB != 0) else None
	def quickRatio2(TOTAL_CURR_ASSETS, INV, PREPAID_EXP, TOTAL_CURR_LIAB):
		return round(((TOTAL_CURR_ASSETS - INV - PREPAID_EXP) / TOTAL_CURR_LIAB), 2) if (TOTAL_CURR_ASSETS != None and INV != None and PREPAID_EXP != None and TOTAL_CURR_LIAB != None  and TOTAL_CURR_LIAB != 0) else None
	def currentRatio(TOTAL_CURR_ASSETS, TOTAL_CURR_LIAB):
		return round((TOTAL_CURR_ASSETS / TOTAL_CURR_LIAB), 2) if (TOTAL_CURR_ASSETS != None and TOTAL_CURR_LIAB != None and TOTAL_CURR_LIAB != 0) else None
	def workingCapitalRatio(TOTAL_CURR_ASSETS, TOTAL_CURR_LIAB, TOTAL_ASSETS1):
		return round(((TOTAL_CURR_ASSETS - TOTAL_CURR_LIAB) / TOTAL_ASSETS1), 2) if (TOTAL_CURR_ASSETS != None and TOTAL_CURR_LIAB != None and TOTAL_ASSETS1 != None  and TOTAL_ASSETS1 != 0) else None
	def debtServiceCoverageRatio(EBIT, INT_EXP, ST_DEBT):
		return round((EBIT / (INT_EXP + ST_DEBT)), 2) if (EBIT != None and INT_EXP != None and ST_DEBT != None and (INT_EXP + ST_DEBT) != 0) else None


class  CapStructure:
	def netDebt(TOTAL_DEBT, CASH_EQ):
		return (TOTAL_DEBT - CASH_EQ) if(TOTAL_DEBT != None and CASH_EQ != None) else None
	def debtRatio(TOTAL_DEBT, TOTAL_ASSETS1):
		return round((TOTAL_DEBT / TOTAL_ASSETS1), 2) if (TOTAL_DEBT != None and TOTAL_ASSETS1 != None and TOTAL_ASSETS1 != 0) else None
	def debtEquityRatio(TOTAL_DEBT, TOTAL_EQUITY):
		return round((TOTAL_DEBT / TOTAL_EQUITY), 2) if (TOTAL_DEBT != None and TOTAL_EQUITY != None and TOTAL_EQUITY != 0) else None
	def debtIncomeRatio(TOTAL_DEBT, NI_INC):
		return round((TOTAL_DEBT / NI_INC), 2) if (TOTAL_DEBT != None and NI_INC != None and NI_INC != 0) else None
	def fixedChargeCoverage(EBIT, CHG_FIXED_INTANG, INT_EXP):
		return round((EBIT + CHG_FIXED_INTANG) / (CHG_FIXED_INTANG + INT_EXP), 2) if (EBIT != None and CHG_FIXED_INTANG != None and INT_EXP != None and (CHG_FIXED_INTANG + INT_EXP) != 0) else None
	def degreeCombinedLeverage(EPS_DILUTED_NI_0, EPS_DILUTED_NI_1, REV_0, REV_1):
		return round(((EPS_DILUTED_NI_0 - EPS_DILUTED_NI_1) / EPS_DILUTED_NI_1) / ((REV_0 - REV_1) / REV_1), 2) if (EPS_DILUTED_NI_0 != None and EPS_DILUTED_NI_1 != None and EPS_DILUTED_NI_1 != 0 and REV_0 != None and REV_1 != None and REV_1 != 0) else None
	def degreeOperatingLeverage(EBIT_0, EBIT_1, REV_0, REV_1):
		return round(((EBIT_0 - EBIT_1) / EBIT_1) / ((REV_0 - REV_1) / REV_1), 2) if (EBIT_0 != None and EBIT_1 != None and EBIT_1 != 0 and REV_0 != None and REV_1 != None and REV_1 != 0) else None
	def degreeFinancialLeverage(EPS_DILUTED_NI_0, EPS_DILUTED_NI_1, EBIT_0, EBIT_1):
		return round(((EPS_DILUTED_NI_0 - EPS_DILUTED_NI_1) / EPS_DILUTED_NI_1) / ((EBIT_0 - EBIT_1) / EBIT_1), 2) if (EPS_DILUTED_NI_1 != None and EPS_DILUTED_NI_1 != None and EPS_DILUTED_NI_1 != 0 and EBIT_0 != None and EBIT_1 != None and EBIT_1 != 0) else None
	def dflRatio(EBIT, INT_EXP):
		return round((EBIT / (EBIT - INT_EXP)), 2) if(EBIT != None and INT_EXP != None and (EBIT -INT_EXP) != 0) else None
	def financialLeverage(AVG_ASSETS, AVG_EQUITY):
		return round((AVG_ASSETS / AVG_EQUITY), 2) if (AVG_ASSETS != None and AVG_EQUITY != None and AVG_EQUITY != 0) else None
	def equityRatio(TOTAL_EQUITY, TOTAL_ASSETS1):
		return round((TOTAL_EQUITY / TOTAL_ASSETS1), 2) if (TOTAL_EQUITY != None and TOTAL_ASSETS1 != None and TOTAL_ASSETS1 != 0) else None
	def equityMultiplier1(TOTAL_ASSETS1, TOTAL_EQUITY):
		return round((TOTAL_ASSETS1 / TOTAL_EQUITY), 2) if (TOTAL_ASSETS1 != None and TOTAL_EQUITY != None and TOTAL_EQUITY != 0) else None
	def equityMultiplier2(DEBT_RATIO):
		return round((1 / (1 - DEBT_RATIO)), 2) if (DEBT_RATIO != None and (1 - DEBT_RATIO) != 0) else None
	def netAssetValue(TOTAL_ASSETS1, TOTAL_LIAB, EPS_DILUTED_NI):
		return round(((TOTAL_ASSETS1 - TOTAL_LIAB) / EPS_DILUTED_NI), 2) if (TOTAL_ASSETS1 != None and TOTAL_LIAB != None and EPS_DILUTED_NI != None and EPS_DILUTED_NI != 0) else None
	def effectiveInterestRate(INT_EXP, TOTAL_DEBT):
		return round((INT_EXP / TOTAL_DEBT ), 2) if (INT_EXP != None and TOTAL_DEBT != None and TOTAL_DEBT != 0) else None
	def debtCostCapital(EFFECTIVE_INT_RATE, MARGINAL_TAX_RATE):
		return round((EFFECTIVE_INT_RATE * (1 - MARGINAL_TAX_RATE) ), 2) if (EFFECTIVE_INT_RATE != None and MARGINAL_TAX_RATE != None) else None	
	def wacc(TOTAL_EQUITY, TOTAL_DEBT, FAIR_RETURN_RATE, EFFECTIVE_INT_RATE, MARGINAL_TAX_RATE ):
		return	round((TOTAL_EQUITY / (TOTAL_DEBT + TOTAL_EQUITY) * FAIR_RETURN_RATE) + (TOTAL_DEBT / (TOTAL_DEBT + TOTAL_EQUITY) * EFFECTIVE_INT_RATE * (1 - MARGINAL_TAX_RATE)), 2) if(TOTAL_EQUITY != None and TOTAL_DEBT != None and FAIR_RETURN_RATE != None and EFFECTIVE_INT_RATE != None and MARGINAL_TAX_RATE != None and (TOTAL_DEBT + TOTAL_EQUITY) != 0 ) else None

class  Asset_Activity:
	def salesTurnover(ACCTS_REC, CREDIT_SALES):
		return round((ACCTS_REC / CREDIT_SALES), 2) if (ACCTS_REC != None and CREDIT_SALES != None and CREDIT_SALES != 0) else None
	def daysSalesOutstanding(SALES_TURNOVER):
		return round((365 * SALES_TURNOVER), 2) if (SALES_TURNOVER != None) else None
	def assetTurnover(REV, AVG_ASSETS):
		return round((REV / AVG_ASSETS), 2) if (REV != None and AVG_ASSETS != None and AVG_ASSETS != 0) else None
	def assetTurnoverRate(ASSET_TURNOVER):
		return round((365 * ASSET_TURNOVER ), 2) if (ASSET_TURNOVER != None) else None
	def longTermAssetTurnover(REV, AVG_LT_ASSETS):
		return round((REV / AVG_LT_ASSETS), 2) if (REV != None and AVG_LT_ASSETS != None and AVG_LT_ASSETS != 0) else None
	def longTermAssetTurnoverRate(LT_ASSET_TURNOVER):
		return round((365 * LT_ASSET_TURNOVER), 2) if (LT_ASSET_TURNOVER != None) else None
	def inventorySalesTurnover(REV, AVG_INVENTORY):
		return round((REV / AVG_INVENTORY), 2) if (REV != None and AVG_INVENTORY != None and AVG_INVENTORY != 0) else None
	def daysSalesInventory(INV_SALES_TURNOVER):
		return round((365 * INV_SALES_TURNOVER), 2) if (INV_SALES_TURNOVER != None) else None
	def inventoryCOGSTurnover(COGS, AVG_INVENTORY):
		return round((COGS / AVG_INVENTORY), 2) if (COGS != None and AVG_INVENTORY != None and AVG_INVENTORY != 0) else None
	def daysInventoryOutstanding(INV_COGS_TURNOVER):
		return round((365 * INV_COGS_TURNOVER), 2) if (INV_COGS_TURNOVER != None) else None
	def receivablesTurnover(ACCTS_REC, REV):
		return round((ACCTS_REC / REV), 2) if (ACCTS_REC != None and REV != None and REV != 0) else None
	def daysReceivablesOutstanding(RECEIVABLES_ACCTS_TURNOVER):
		return round((365 * RECEIVABLES_ACCTS_TURNOVER), 2) if (RECEIVABLES_ACCTS_TURNOVER != None) else None
	def workingCapitalTurnover(REV, AVG_WORKING_CAPITAL):
		return round((REV / AVG_WORKING_CAPITAL), 2) if (REV != None and AVG_WORKING_CAPITAL != None and AVG_WORKING_CAPITAL != 0) else None
	def daysWorkingCapital(WORKING_CAP_TURNOVER):
		return round((365 * WORKING_CAP_TURNOVER), 2) if (WORKING_CAP_TURNOVER != None) else None
	def investmentsROI(CASH_INVEST_ACT1, AVG_INVEST):
		return round((CASH_INVEST_ACT1 / AVG_INVEST), 2) if (CASH_INVEST_ACT1 != None and AVG_INVEST != None and AVG_INVEST != 0) else None


class  Liab_Activity:
	def CreditorsTurnover(CREDIT_SALES, AVG_RECEIVABLES):
		return round((CREDIT_SALES / AVG_RECEIVABLES), 2) if (CREDIT_SALES != None and AVG_RECEIVABLES != None and AVG_RECEIVABLES != 0) else None
	def CreditorsDaysOutstanding(CREDITORS_TURNOVER):
		return round((365 * CREDITORS_TURNOVER), 2) if (CREDITORS_TURNOVER != None) else None
	def payablesTurnoverCOGS(PAYABLES, COGS):
		return round((PAYABLES / COGS), 2) if (PAYABLES != None and COGS != None and COGS != 0) else None
	def daysPayableOutstandingCOGS(PAYABLES_TURNOVER_COGS):
		return round((365 * PAYABLES_TURNOVER_COGS), 2) if (PAYABLES_TURNOVER_COGS != None) else None
	def payablesTurnoverCOS(PAYABLES, COST_OF_REV):
		return round((PAYABLES / COST_OF_REV), 2) if (PAYABLES != None and COST_OF_REV != None and COST_OF_REV != 0) else None
	def daysPayableOutstandingCOS(PAYABLES_TURNOVER_COS):
		return round((365 * PAYABLES_TURNOVER_COS), 2) if (PAYABLES_TURNOVER_COS != None) else None
	def liabitiesTurnover(TOTAL_LIAB, AVG_PAYABLES_ACCRUALS):
		return round((TOTAL_LIAB / AVG_PAYABLES_ACCRUALS), 2) if (TOTAL_LIAB != None and AVG_PAYABLES_ACCRUALS != None and AVG_PAYABLES_ACCRUALS != 0) else None
	def liabitiesTurnoverRate(LIAB_TURNOVER):
		return round((365 * LIAB_TURNOVER), 2) if (LIAB_TURNOVER != None) else None
	def changeStDebt(ST_DEBT_0, ST_DEBT_1):
		return round((ST_DEBT_0 - ST_DEBT_1) / ST_DEBT_1 * 100, 2) if (ST_DEBT_0 != None and ST_DEBT_1 != None and ST_DEBT_1 != 0) else None
	def debtorsPaybackPeriod(AVG_DEBT, CASH_REPAY_DEBT):
		return round((AVG_DEBT / CASH_REPAY_DEBT), 2) if (AVG_DEBT != None and CASH_REPAY_DEBT != None and CASH_REPAY_DEBT != 0) else None
	def burnRate(CASH_EQ, EBIT):
		return round((CASH_EQ / EBIT), 2) if (CASH_EQ != None and EBIT != None and EBIT < 0) else None


class  Profitability:
	def cashConversionCycle(DIO, DSO, DPO_COGS):
		return round((DIO + DSO - DPO_COGS), 2) if (DIO != None and DSO != None and DPO_COGS != None) else None
	def returnOnSales(NI_INC, REV):
		return round((NI_INC / REV), 2) if (NI_INC != None and REV != None and REV != 0) else None
	def returnOnEquity(NI_INC, TOTAL_EQUITY):
		return round((NI_INC / TOTAL_EQUITY), 2) if (NI_INC != None and TOTAL_EQUITY != None and TOTAL_EQUITY != 0) else None
	def returnOnAssets(NI_INC, TOTAL_ASSETS1):
		return round((NI_INC / TOTAL_ASSETS1), 2) if (NI_INC != None and TOTAL_ASSETS1 != None and TOTAL_ASSETS1 != 0) else None
	def earningsPerShare(NI_INC, DIL_WEIGHT_AVG_SHARES):
		return round((NI_INC / DIL_WEIGHT_AVG_SHARES), 2) if(NI_INC != None and DIL_WEIGHT_AVG_SHARES != None and DIL_WEIGHT_AVG_SHARES != 0) else None
	def returnOnCapitalEmployedNI(NI_INC, TOTAL_ASSETS1, TOTAL_CURR_LIAB):
		return round((NI_INC / (TOTAL_ASSETS1 - TOTAL_CURR_LIAB)), 2) if (NI_INC != None and TOTAL_ASSETS1 != None and TOTAL_CURR_LIAB != None and (TOTAL_ASSETS1 - TOTAL_CURR_LIAB) != 0) else None
	def returnOnCapitalEmployedEBIT(EBIT, TOTAL_ASSETS1, TOTAL_CURR_LIAB):
		return round((EBIT / (TOTAL_ASSETS1 - TOTAL_CURR_LIAB)), 2) if (EBIT != None and TOTAL_ASSETS1 != None and TOTAL_CURR_LIAB != None and (TOTAL_ASSETS1 - TOTAL_CURR_LIAB) != 0) else None
	def priceEarnings(PRICE, DIL_WEIGHT_AVG_SHARES, NI_INC):
		return round((PRICE * DIL_WEIGHT_AVG_SHARES / NI_INC), 2) if (PRICE != None and DIL_WEIGHT_AVG_SHARES != None and NI_INC != None and NI_INC != 0) else None
	def priceEarnings3(PE_0, PE_1, PE_2):
		return round(((PE_0 + PE_1 + PE_2) / 3), 2) if (PE_0 != None and PE_1 != None and PE_2 != None) else None
	def priceEarnings5(PE_0, PE_1, PE_2, PE_3, PE_4):
		return round(((PE_0 + PE_1 + PE_2 + PE_3 + PE_4) / 5), 2) if (PE_0 != None and PE_1 != None and PE_2 != None and PE_3 != None and PE_4 != None) else None
	def earningsPower(EBIT, TOTAL_ASSETS1):
		return round((EBIT / TOTAL_ASSETS1), 2) if (EBIT != None and TOTAL_ASSETS1 != None and TOTAL_ASSETS1 != 0) else None
	def grossMarginRatio(PROFIT, REV):
		return round((PROFIT / REV), 2) if (PROFIT != None and REV != None and REV != 0) else None
	def netOperatingProfitAfterTaxNI(NI_INC, NON_OP_INC_LOSS, INT_EXP):
		return round((NI_INC - NON_OP_INC_LOSS + INT_EXP), 2) if (NI_INC != None and NON_OP_INC_LOSS != None and INT_EXP != None) else None
	def netOperatingProfitAfterTaxEBIT(OP_INC_LOSS, MARGINAL_TAX_RATE):
		return round((OP_INC_LOSS * (1 - MARGINAL_TAX_RATE)), 2) if (OP_INC_LOSS != None and MARGINAL_TAX_RATE != None) else None
	def returnOnInvestedCapital(NOPAT, TOTAL_INVEST):
		return round((NOPAT / TOTAL_INVEST), 2) if (NOPAT != None and TOTAL_INVEST != None and TOTAL_INVEST != 0) else None
	def operatingRatio(OP_EXP, REV):
		return round((OP_EXP / REV), 2) if (OP_EXP != None and REV != None and REV != 0) else None
	def operatingProfitMargin(OP_INC_LOSS, REV):
		return round((OP_INC_LOSS / REV), 2) if (OP_INC_LOSS != None and REV != None and REV != 0) else None


class  Valuations:
	def marketCap(PRICE, DIL_WEIGHT_AVG_SHARES):
		return round((PRICE * DIL_WEIGHT_AVG_SHARES), 2) if (PRICE != None and DIL_WEIGHT_AVG_SHARES != None) else None
	#def marketCapEBITRatio(MV, EBIT):
	#	return round((MV / EBIT), 2) if (MV != None and EBIT != None and EBIT != 0) else None
	def originalGraham(EPS_DILUTED_NI, NO_GROWTH_PE, GROWTH_MULTIPLE, GROWTH_RATE):
		return round((EPS_DILUTED_NI * (NO_GROWTH_PE + GROWTH_MULTIPLE * GROWTH_RATE)), 2) if (EPS_DILUTED_NI != None and NO_GROWTH_PE != None and GROWTH_MULTIPLE != None and GROWTH_RATE != None) else None
	def revisedGraham(EPS_DILUTED_NI, NO_GROWTH_PE, GROWTH_MULTIPLE, GROWTH_RATE, REQUIRED_RETURN, AAA_BOND_YIELD):
		return round(((EPS_DILUTED_NI * (NO_GROWTH_PE + GROWTH_MULTIPLE * GROWTH_RATE) * REQUIRED_RETURN ) / AAA_BOND_YIELD), 2) if (EPS_DILUTED_NI != None and NO_GROWTH_PE != None and GROWTH_MULTIPLE != None and GROWTH_RATE != None and REQUIRED_RETURN != None and AAA_BOND_YIELD != None and AAA_BOND_YIELD != 0) else None
	def enterpriseValue(MV, TOTAL_DEBT, CASH_EQ):
		return round((MV + TOTAL_DEBT - CASH_EQ), 2) if (MV != None and TOTAL_DEBT != None and CASH_EQ != None) else None
	def enterpriseValueEBIT(MV, TOTAL_DEBT, CASH_EQ, EBIT):
		return round(((MV + TOTAL_DEBT - CASH_EQ) / EBIT), 2) if (MV != None and TOTAL_DEBT != None and CASH_EQ != None and EBIT != None and EBIT != 0) else None
	def enterpriseValueNI(MV, TOTAL_DEBT, CASH_EQ, NI_INC):
		return round(((MV + TOTAL_DEBT - CASH_EQ) / NI_INC), 2) if (MV != None and TOTAL_DEBT != None and CASH_EQ != None and NI_INC != None and NI_INC != 0) else None
	def bookValue(TOTAL_ASSETS1, TOTAL_INTANG_ASSETS, TOTAL_LIAB):
		return round((TOTAL_ASSETS1 - TOTAL_INTANG_ASSETS - TOTAL_LIAB), 2) if (TOTAL_ASSETS1 != None and TOTAL_INTANG_ASSETS != None and TOTAL_LIAB != None) else None
	#def bookValueToNI(BV, NI_INC):
	#	return round((BV / NI_INC), 2) if (BV != None and NI_INC != None and NI_INC != 0) else None
	def bookValueToEBIT(BV, EBIT):
		return round((BV / EBIT), 2) if (BV != None and EBIT != None and EBIT != 0) else None
	def bookValueEBITperShare(BV, EPS_EBIT_DILUTED):
		return round((BV / EPS_EBIT_DILUTED), 2) if (BV != None and EPS_EBIT_DILUTED != None and EPS_EBIT_DILUTED != 0) else None
	def bookValueNIperShare(BV, EPS_NI_DILUTED):
		return round((BV / EPS_NI_DILUTED), 2) if (BV != None and EPS_NI_DILUTED != None and EPS_NI_DILUTED != 0) else None	
	def priceToSales(PRICE, REV):
		return round((PRICE / REV), 2) if (PRICE != None and REV != None and REV != 0) else None
	def priceToBook(PRICE, BV):
		return round((PRICE / BV), 2) if (PRICE != None and BV != None and BV != 0) else None
	def priceToNAV(PRICE, NAV):
		return round((PRICE / NAV), 2) if (PRICE != None and NAV != None and NAV != 0) else None	
	def pricetoLeveredFreeCashFlow(PRICE, LEV_FCF):
		return round((PRICE / LEV_FCF), 2) if (PRICE != None and LEV_FCF != None and LEV_FCF != 0) else None	
	def priceToUnLeveredFreeCashFlow(PRICE, UN_LEV_FCF):
		return round((PRICE / UN_LEV_FCF), 2) if (PRICE != None and UN_LEV_FCF != None and UN_LEV_FCF != 0) else None
	def marketValueToOCF(MV, OP_INC_LOSS):
		return round((MV / OP_INC_LOSS), 2) if (MV != None and OP_INC_LOSS != None and  OP_INC_LOSS != 0) else None
	def cashPriceRatio(MV, CASH_EQ):
		return round((MV / CASH_EQ), 2) if (MV != None and CASH_EQ != None and CASH_EQ != 0) else None
	def intrinsicValueNI(VALUE, NI_3YEAR_AVG, DISC_RATE, i):
		if not ((VALUE != None and NI_3YEAR_AVG != None and DISC_RATE != None and i != None and ((1 + DISC_RATE) ** i)) != 0):
			return None 
		#print(str((i-1)) + ": " + str(VALUE))
		VALUE = (VALUE + (NI_3YEAR_AVG / ((1 + DISC_RATE) ** i)) )
		return round(VALUE, 2) if (NI_3YEAR_AVG / ((1 + DISC_RATE) ** i) < 1) else Valuations.intrinsicValueNI(VALUE, NI_3YEAR_AVG, DISC_RATE, i+1)
	def intrinsicValueEBIT(VALUE, EBIT_3YEAR_AVG, DISC_RATE, i):
		if not ((VALUE != None and EBIT_3YEAR_AVG != None and DISC_RATE != None and i != None and ((1 + DISC_RATE) ** i)) != 0):
			return None 
		#print(str((i-1)) + ": " + str(VALUE))
		VALUE = (VALUE + (EBIT_3YEAR_AVG / ((1 + DISC_RATE) ** i)) )
		return round(VALUE, 2) if (EBIT_3YEAR_AVG / ((1 + DISC_RATE) ** i) < 1) else Valuations.intrinsicValueEBIT(VALUE, EBIT_3YEAR_AVG, DISC_RATE, i+1)
	def intrinsicValueFCF(VALUE, FCF_3YEAR_AVG, DISC_RATE, i):
		if not ((VALUE != None and FCF_3YEAR_AVG != None and DISC_RATE != None and i != None and ((1 + DISC_RATE) ** i)) != 0):
			return None 
		#print(str((i-1)) + ": " + str(VALUE))
		VALUE = (VALUE + (FCF_3YEAR_AVG / ((1 + DISC_RATE) ** i)) )
		return round(VALUE, 2) if (FCF_3YEAR_AVG / ((1 + DISC_RATE) ** i) < 1) else Valuations.intrinsicValueFCF(VALUE, FCF_3YEAR_AVG, DISC_RATE, i+1)
	def marginOfSafety_NI(IVALUE_NI, MV):
		return round((1 - (IVALUE_NI / MV)) * 100, 2) if (IVALUE_NI != None and MV != None and MV != 0) else None
	def marginOfSafety_EBIT(IVALUE_EBIT, MV):
		return round((1 - (IVALUE_EBIT / MV)) * 100, 2) if (IVALUE_EBIT != None and MV != None and MV != 0) else None
	def marginOfSafety_FCF(IVALUE_FCF, MV):
		return round((1 - (IVALUE_FCF / MV)) * 100, 2) if (IVALUE_FCF != None and MV != None and MV != 0) else None
	def dupontSystem_1(ROS, ASSET_TURNOVER, EQUITY_MULTIPLIER_RATIO_1):
		return round((ROS * ASSET_TURNOVER * EQUITY_MULTIPLIER_RATIO_1), 2) if (ROS != None and ASSET_TURNOVER != None and EQUITY_MULTIPLIER_RATIO_1 != None) else None
	def dupontSystem_2(ROA, DEBT_EQ_RATIO):
		return round((ROA * (1 + DEBT_EQ_RATIO)), 2) if (ROA != None and DEBT_EQ_RATIO != None) else None


class  Dividends:
	def retentionRatio(RE, NI_INC):
			return round((RE / NI_INC), 2) if (RE != None and NI_INC != None and NI_INC != 0) else None
	def dividendPayoutRatio(DIVS_PAID, NI_INC):
			return round((DIVS_PAID / NI_INC), 2) if (DIVS_PAID != None and NI_INC != None and NI_INC != 0) else None
	def earningsYieldRatio(NI_INC, MV):
			return round((NI_INC / MV), 2) if (NI_INC != None and MV != None and MV != 0) else None
	def dividendYieldRatio(DIVS_PAID, MV):
			return round((DIVS_PAID / MV), 2) if (DIVS_PAID != None and MV != None and MV != 0) else None
	def sustainableGrowthRate(ROE, DIV_PAYOUT_RATIO):
			return round((ROE * (1 - DIV_PAYOUT_RATIO) ), 2) if (ROE != None and DIV_PAYOUT_RATIO != None) else None
