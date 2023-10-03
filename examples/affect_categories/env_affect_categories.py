#!/usr/bin/env python

import agentspeak
import agentspeak.runtime
import agentspeak.stdlib
import agentspeak.affective_agent

import os


env = agentspeak.affective_agent.Environment()
agent = agentspeak.affective_agent.AffectiveAgent

with open(os.path.join(os.path.dirname(__file__), "agent1.asl")) as source:
    agents = env.build_agents(source, 1, agentspeak.stdlib.actions, agent)

if __name__ == "__main__":
    env.run()
