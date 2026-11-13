#!/usr/bin/env python3
"""AI coding agent joke - writes a one-liner to /output/entry.txt"""

import os

def main():
    joke = "AI coding agents: tapi masih bingung mana kiri mana yang disebut left."
    
    # Ensure output directory exists
    os.makedirs('/output', exist_ok=True)
    
    # Write joke to output file
    with open('/output/entry.txt', 'w', encoding='utf-8') as f:
        f.write(joke)

if __name__ == '__main__':
    main()
