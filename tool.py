from agents import function_tool, RunContextWrapper
from context import UserContext, TransferContext, LoanContext, RequestCallback

@function_tool
def check_balance(wrapper: RunContextWrapper[UserContext]):
    """Return the balance of the authenticated account"""
    ctx = wrapper.context

    if not ctx.authenticated:
        return "User not authenticated"
    if ctx.balance is None:
        return "Balance information not available"

    return f"{ctx.user_name}, your current balance is ${ctx.balance:.2f}."


@function_tool
def transfer_fund(wrapper: RunContextWrapper[TransferContext]):
    """Transfer funds between accounts in context"""
    ctx = wrapper.context

    if ctx.amount <= 0:
        return "Amount must be greater than 0"

    # For Option 1, we assume both accounts and balances are in memory
    # In reality, you'd fetch both accounts and update them in DB
    if ctx.from_account == ctx.to_account:
        return "Cannot transfer to the same account"

    return f"Transferred ${ctx.amount:.2f} from account {ctx.from_account} to {ctx.to_account}."


@function_tool
def get_loan_options() -> str:
    return (
        "Here are three loan options:\n"
        "- Personal Loan: 11% interest\n"
        "- Home Loan: 8.5% interest\n"
        "- Auto Loan: 9.5% interest\n"
    )


@function_tool
def apply_for_loan(wrapper: RunContextWrapper[LoanContext]):
    ctx = wrapper.context

    if ctx.loan_type.lower() not in ["personal loan", "home loan", "auto loan"]:
        return "Invalid loan type. Please choose personal, home, or auto."
    if ctx.amount <= 0:
        return "Amount must be greater than 0"

    return f"Loan application submitted for ${ctx.amount:.2f} ({ctx.loan_type}, {ctx.tenure_years} years)."


@function_tool
def request_callback(wrapper: RunContextWrapper[RequestCallback]):
    ctx = wrapper.context
    return f"Thanks {ctx.user_name}. A human support agent will call you shortly."
