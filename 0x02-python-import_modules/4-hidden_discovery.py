#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    phrases = dir(hidden_4)
    for phrase in phrases:
        if phrase[:2] != "__":
            print(phrase)
