from mcp.server.fastmcp import FastMCP

from datetime import datetime

mcp = FastMCP("Calculator")
@mcp.tool()
def add(a: float, b: float) -> float:
    return a + b

@mcp.tool()
def subtract(a:float,b:float) -> float:
    return a - b

@mcp.tool()
def multiply(a:float,b:float) -> float:
    return a * b

@mcp.tool()
def divide(a:float,b:float) -> float:
    if b == 0:
        raise ValueError(ZeroDivisionError)
    return a/b

@mcp.resource("info://server")
def server_info() -> str:
    return """
Calculator MCP Server

Version: 1.0.0
Author: Joginaidu

Available Tools:
- add
- subtract
- multiply
- divide
"""


@mcp.resource("info://time")
def current_time() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@mcp.prompt()
def solve_math(expression: str) -> str:
    return f"""
You are an expert mathematician.
Solve the following expression step-by-step.
Expression:
{expression}
Explain every step and provide the final answer.
"""

@mcp.prompt()
def explain_formula(formula: str) -> str:
    return f"""Explain the following mathematical formula in simple language.
    Formula:
    {formula}

    Include:
    - Meaning
    - Example
    - Practical use
    """


if __name__ == "__main__":
    mcp.run()