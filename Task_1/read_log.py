import sys
import re
from collections import Counter


def extract_user_agents(filename):
    user_agents = []
    with open(filename, 'r') as file:
        for line in file:
            match = re.search(r'\"[^\"]+\" \"([^\"]+)\"', line)
            if match:
                user_agents.append(match.group(1))
    return user_agents


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <access_log_file>")
        sys.exit(1)

    filename = sys.argv[1]
    try:
        user_agents = extract_user_agents(filename)
        user_agent_counts = Counter(user_agents)

        print(f"Total number of different User Agents: {len(user_agent_counts)}")
        print("User Agent Statistics:")
        for agent, count in user_agent_counts.items():
            print(f"{agent}: {count} requests")
    except FileNotFoundError:
        print(f"Error: File not found - {filename}")


if __name__ == "__main__":
    main()
