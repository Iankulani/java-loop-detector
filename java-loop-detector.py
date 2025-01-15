# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:39:25 2025

@author: IAN CARTER KULANI

"""

from colorama import Fore
import pyfiglet
import os
font=pyfiglet.figlet_format("Infinite Loop Detector")
print(Fore.GREEN+font)

import re

import re

# Function to convert Java code to pseudo-assembly
def convert_to_assembly(java_code):
    assembly_code = []
    
    # Split the Java code into lines
    java_lines = java_code.splitlines()
    
    # Process each line of the Java program
    for line in java_lines:
        # Remove leading/trailing whitespaces
        stripped_line = line.strip()
        
        # Handle single-line comments (//)
        if stripped_line.startswith("//"):
            assembly_code.append(f"; {stripped_line[2:].strip()}")  # Convert to assembly comment
            
        # Handle multi-line comments (/* */)
        elif stripped_line.startswith("/*"):
            assembly_code.append(f"; {stripped_line[2:].strip()}")
            # If the comment spans multiple lines
            while not stripped_line.endswith("*/"):
                line = next(java_lines)
                stripped_line = line.strip()
                assembly_code.append(f"; {stripped_line[2:].strip()}")
            assembly_code.append(f"; {stripped_line[:-2].strip()}")
        
        # Process Java code statements and translate them to pseudo-assembly
        elif "public" in stripped_line or "private" in stripped_line or "protected" in stripped_line:
            # Skip method declarations for now
            continue
        elif "for" in stripped_line:
            assembly_code.append(f"LOOP_START: ; For loop (translated)")
        elif "while" in stripped_line:
            assembly_code.append(f"LOOP_START: ; While loop (translated)")
        elif "=" in stripped_line:
            # Simple assignment (e.g., x = 10;)
            assembly_code.append(f"MOV R1, {stripped_line.split('=')[1].strip().rstrip(';')}") 
        elif "if" in stripped_line:
            assembly_code.append(f"IF_CONDITION: ; If statement (translated)")
        elif "return" in stripped_line:
            assembly_code.append(f"RETURN: ; Return statement")
        else:
            # For other statements, we just put a comment saying "Untranslated Java statement"
            assembly_code.append(f"; {stripped_line}")
    
    return "\n".join(assembly_code)

# Function to get Java code from the user
def get_java_code():
    print("Please enter the Java program. Type 'END' on a new line to finish input")
    java_code = []
    
    while True:
        line = input()
        if line.strip() == "END":
            break
        java_code.append(line)
    
    return "\n".join(java_code)

# Main function to run the program
def main():
    # Get Java code from user
    java_code = get_java_code()
    
    # Convert Java code to pseudo-assembly
    print("\nConverting Java to pseudo-assembly...\n")
    assembly_code = convert_to_assembly(java_code)
    
    # Display the translated assembly code
    print("\nGenerated Pseudo-Assembly Code:\n")
    print(assembly_code)

if __name__ == "__main__":
    main()
