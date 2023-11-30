#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    declared_names = dir()
    for i in range(1, len(declared_names)):
        if declared_names[i][0] == '_':
            continue
        else:
            print(declared_names[i])
