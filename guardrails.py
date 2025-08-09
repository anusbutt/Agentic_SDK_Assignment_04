from agents import input_guardrail, output_guardrail, RunContextWrapper, GuardrailFunctionOutput, Runner, Agent
from pydantic import BaseModel
from typing import List
from configuration import config

# -----------------------------
# Input Guardrail Schema
# -----------------------------
class TransferInputCheck(BaseModel):
    is_suspicious: bool
    reason: str

TransferInputGuardAgent = Agent(
    name="Transfer Input Guard Agent",
    instructions="""
    You are a security agent. Your job is to check if a user's input related to transfers is suspicious.

    A message is suspicious if:
    - It contains keywords like: hack, bypass, steal, admin access
    - It asks to transfer an amount of ₹100000 or more
    - It references another person’s account in a malicious context
    """,
    output_type=TransferInputCheck
)

@input_guardrail
async def transfer_guardrail(
    ctx: RunContextWrapper[None],
    agent: Agent,
    input: str | List
) -> GuardrailFunctionOutput:
    result = await Runner.run(TransferInputGuardAgent, input, context=ctx.context, run_config=config)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_suspicious
    )

# -----------------------------
# Output Guardrail Schema
# -----------------------------
class BankOutput(BaseModel):
    response: str

class CheckOutputResult(BaseModel):
    is_flagged: bool
    reason: str

Bank_output_guard_agent = Agent(
    name="Bank Output Guard Agent",
    instructions="""
    You check final outputs from the assistant.

    If the response contains:
    - Full account numbers (more than 4 digits in a row)
    - Internal error messages or technical details
    - Aggressive or unprofessional tone
    - Promises of instant loan approval

    Then set is_flagged = true and explain why.
    """,
    output_type=CheckOutputResult
)

@output_guardrail
async def bank_output_guardrail(
    ctx: RunContextWrapper[None],
    agent: Agent,
    output: BankOutput
) -> GuardrailFunctionOutput:
    result = await Runner.run(Bank_output_guard_agent, output.response, context=ctx.context)
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_flagged
    )
