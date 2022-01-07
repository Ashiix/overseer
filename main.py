#!/usr/bin/env python3

# overseer
# An open-source and self-hosted multipurpose Discord bot
# by Ashiix

from src.overseer import Overseer
import config

def main():
    print("\nstarting overseer...")
    overseer = Overseer()
    overseer.run(config.token)

if __name__ == "__main__":
    main()
