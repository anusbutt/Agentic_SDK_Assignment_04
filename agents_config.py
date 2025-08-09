from agents import Agent
from tool import check_balance, transfer_fund, get_loan_options, apply_for_loan, RequestCallback
from guardrails import bank_output_guardrail, transfer_guardrail, BankOutput

check_balance_agent: Agent = Agent(
    name="Balance Checker",
    instructions="you help users check their account balance",
    tools = [check_balance]
)

transfer_fund_agent: Agent = Agent(
    name="Fund Transfer Agent",
    instructions="you help users to trasfer fund between accounts",
    tools = [transfer_fund]
)


loan_agent: Agent = Agent(
    name="Loan Agent",
    instructions="you help users understand loan options and apply for a loan",
    tools = [get_loan_options, apply_for_loan]
)

Human_Support_Agent: Agent = Agent(
    name="Human Support Agent",
    instructions="you help customers reach human customer support",
    tools = [RequestCallback]
)

Traige_Agent: Agent = Agent(
    name="Traige Agent",
    instructions="""
    You are the central banking assistant. Based on user input, route them to the correct department:
    - Use BalanceAgent for checking balances.
    - Use TransferAgent for transferring money.
    - Use LoanAgent for loan options or applications.
    - Use AccountAgent for opening or closing accounts.
    - Use HumanSupportAgent if the user wants to speak to a human.
    """,
    handoffs=[check_balance_agent, transfer_fund_agent, loan_agent, Human_Support_Agent],
    input_guardrails = [transfer_guardrail],
    output_guardrails = [bank_output_guardrail],
    output_type=BankOutput
)