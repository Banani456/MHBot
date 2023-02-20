#Disorders list: Anxiety disorders, Dissociative disorders,	Mood disorders, Trauma and stressor-related disorders, Neuro-developmental disorders, Sleep-wake disorders, Neuro-cognitive disorders, Substance-related and addictive disorders, Paraphilias, Somatic symptom related disorders, Sexual dysfunctions, Elimination disorders, Feeding and eating disorders, Disruptive impulse-control and conduct disorders,	Obsessive-compulsive and related disorders, Schizophrenia spectrum and other psychotic disorders, Personality disorders

import csv
import sys 

#inputs my data into a txt file instead of on console so I can copy it
stdoutOrigin=sys.stdout
sys.stdout = open("log.txt", "w")


from collections import defaultdict
columns = defaultdict(list)
with open('disorders.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        for (k,v) in row.items():
            columns[k].append(v)

#prints all my columns in an easy access manner
print(columns['Anxiety disorders'])
print(columns['Dissociative disorders'])
print(columns['Mood disorders'])
print(columns['Trauma and stressor-related disorders'])
print(columns['Neuro-developmental disorders'])
print(columns['Sleep-wake disorders'])
print(columns['Neuro-cognitive disorders'])
print(columns['Substance-related and addictive disorders'])
print(columns['Paraphilias'])
print(columns['Somatic symptom related disorders'])
print(columns['Sexual dysfunctions'])
print(columns['Elimination disorders'])
print(columns['Feeding and eating disorders'])
print(columns['Disruptive impulse-control, and conduct disorders'])
print(columns['Obsessive-compulsive and related disorders'])
print(columns['Schizophrenia spectrum and other psychotic disorders'])
print(columns['Personality disorders'])