import pytest
from src.agent import Agent

def test_agent_init_and_greet():
    agent = Agent(name="TestAgent")
    assert agent.name == "TestAgent"
    assert agent.greet() == "Hello, I am TestAgent!" 