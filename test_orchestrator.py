#!/usr/bin/env python3
from orchestrator import MainAgent

def test_agent():
    """Test the agent with user input"""
    agent = MainAgent()
    
    while True:
        try:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
            
            if not user_input:
                continue
            
            # Process the query
            response = agent.process_query_sync(user_input)
            print(f"Agent: {response}")
            print()
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_agent()
