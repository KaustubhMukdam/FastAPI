from pydantic_ai import Agent, RunContext
from app.finance_advisor.model import FinancialProfile, FinancialReportResult
import json

# Create agent without result_type - we'll handle response parsing manually
financial_agent = Agent(
    'cerebras:gpt-oss-120b',
    deps_type=FinancialProfile,
    system_prompt=(
        "You are a financial advisor AI. Analyze the user's financial profile and provide advice. "
        "You MUST respond ONLY with valid JSON matching this exact structure:\n"
        "{\n"
        '  "financial_advice": "detailed advice here",\n'
        '  "debt_to_income_ratio": "XX.X%",\n'
        '  "risk": 5,\n'
        '  "decrease_risk": "suggestions here"\n'
        "}\n"
        "Do not include any other text, markdown formatting, or explanations."
    )
)

@financial_agent.system_prompt
async def add_user_finance(ctx: RunContext[FinancialProfile]) -> str:
    """Inject user's financial data into the system prompt."""
    finance_data = ctx.deps
    
    # Calculate totals
    total_monthly_income = sum(inc.amount for inc in finance_data.monthly_income)
    total_monthly_expenses = sum(exp.amount for exp in finance_data.monthly_expenses)
    total_debt_amount = sum(debt.amount for debt in finance_data.debts)
    total_monthly_debt_payment = sum(debt.minimum_payment for debt in finance_data.debts)
    
    return f"""
FINANCIAL PROFILE DATA:

Monthly Income (Total: ${total_monthly_income:,.2f}):
{chr(10).join(f'  • {inc.source}: ${inc.amount:,.2f} ({inc.frequency})' for inc in finance_data.monthly_income)}

Monthly Expenses (Total: ${total_monthly_expenses:,.2f}):
{chr(10).join(f'  • {exp.category}: ${exp.amount:,.2f} ({exp.frequency}) [{"Essential" if exp.essential else "Discretionary"}]' for exp in finance_data.monthly_expenses)}

Debts (Total Owed: ${total_debt_amount:,.2f}, Monthly Payments: ${total_monthly_debt_payment:,.2f}):
{chr(10).join(f'  • {debt.type}: ${debt.amount:,.2f} @ {debt.interest_rate}% APR (Min: ${debt.minimum_payment}/mo)' for debt in finance_data.debts)}

Savings:
  • Total Savings: ${finance_data.savings:,.2f}
  • Emergency Fund: ${finance_data.emergency_fund:,.2f}
  • Retirement: ${finance_data.retirement_savings:,.2f}
  • Credit Score: {finance_data.credit_score if finance_data.credit_score else 'Not provided'}

ANALYSIS REQUIREMENTS:
1. Calculate debt-to-income ratio (total monthly debt payments / total monthly income)
2. Assess risk level (1-10): Consider debt load, savings adequacy, expense ratio
3. Provide personalized financial advice
4. Give specific suggestions to reduce risk

Remember: Respond ONLY with the JSON structure specified above.
"""

async def analyze_profile(financial_profile: FinancialProfile) -> FinancialReportResult:
    """
    Analyze financial profile and return structured results.
    """
    # Run the agent - NO result_type parameter here
    result = await financial_agent.run(
        "Analyze the financial profile and respond with the required JSON.",
        deps=financial_profile
    )
    
    # Get the response
    response_data = result.output
    
    # Handle different response types
    if isinstance(response_data, dict):
        # Already a dictionary, convert to FinancialReportResult
        return FinancialReportResult(**response_data)
    
    elif isinstance(response_data, str):
        # String response - try to parse as JSON
        try:
            # Clean up the response (remove markdown code blocks if present)
            cleaned = response_data.strip()
            if cleaned.startswith('```'):
                # Remove markdown code blocks
                lines = cleaned.split('\n')
                cleaned = '\n'.join(line for line in lines if not line.strip().startswith('```'))
            
            # Parse JSON
            data = json.loads(cleaned)
            return FinancialReportResult(**data)
            
        except (json.JSONDecodeError, ValueError) as e:
            # Fallback if parsing fails
            return FinancialReportResult(
                financial_advice=f"Analysis completed but response formatting failed. Raw response: {response_data[:500]}",
                debt_to_income_ratio="Unable to calculate",
                risk=5,
                decrease_risk="Please consult with a certified financial advisor for detailed analysis."
            )
    
    else:
        # Unexpected response type - try to convert
        try:
            return FinancialReportResult(**response_data)
        except Exception:
            return FinancialReportResult(
                financial_advice="Unable to process response",
                debt_to_income_ratio="N/A",
                risk=5,
                decrease_risk="Please try again or consult a financial advisor."
            )