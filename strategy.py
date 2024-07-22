# Define the interface for the strategy
class Strategy:
    def execute(self):
        pass

# Implement concrete strategies
class ConcreteStrategyA(Strategy):
    def execute(self):
        print("Executing strategy A")

class ConcreteStrategyB(Strategy):
    def execute(self):
        print("Executing strategy B")

# Context class that uses the strategy
class Context:
    def __init__(self, strategy):
        self.strategy = strategy

    def execute_strategy(self):
        self.strategy.execute()

# Usage example
if __name__ == "__main__":
    # Create strategies
    strategy_a = ConcreteStrategyA()
    strategy_b = ConcreteStrategyB()

    # Create context with strategy A
    context = Context(strategy_a)
    context.execute_strategy()  # Output: Executing strategy A

    # Change strategy to B
    context.strategy = strategy_b
    context.execute_strategy()  # Output: Executing strategy B