import os, sys, time, csv

with open('C:\\Users\\user\\Desktop\\data.txt', 'r', encoding='UTF-8-sig')as file:
    lines = file.readlines()
    print(lines)

with open('word.csv', 'w', newline='', encoding='utf-8-sig')as csvfile:
    writer = csv.writer(csvfile)
    for line in lines:
        word = (line.strip()).split(' ')
        writer.writerow(word)