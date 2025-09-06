import csv
import sys
import os
import pandas as pd

score = {}

def initNamelist():
    try:
        namelist = open("names", 'r', encoding='utf-8')
    except FileNotFoundError:
        print("Error: name list not found, please create a namelist in this folder.", file=sys.stderr)
        return 1
    line = namelist.readline()
    while line:
        score[line.strip()] = 0.0
        line = namelist.readline()

    return 0

def process(filename: str):
    with open(filename, 'r', newline='', encoding='utf-8') as inputfile:
        reader = csv.reader(inputfile)
        cnt = 0
        for row in reader:
            if row[0][0] == '-':
                continue
            print(row)
            score[row[1][1:]] += 0.01
            cnt += 1
            if cnt == 10:
                return

def main():
    if initNamelist():
        return -1
    lf = [f for f in os.listdir('./logs') if f.endswith('.log')]

    if not lf:
        print("Cannot find Yasu log files", file=sys.stderr)
        return -1

    for filename in lf:
        print(f"Processing file: {filename}")
        filename = "./logs/" + filename
        process(filename)

    df = pd.DataFrame({
        'Names': list(score.keys()),
        'Scores': list(score.values())
    })
    print(df)
    df.to_excel("result.xlsx")

    return 0


if __name__ == "__main__":
    main()