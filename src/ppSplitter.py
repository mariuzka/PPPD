import copy
import os
from pathlib import Path
import pickle

import pandas as pd

import src


SEP = "#+#+#+#+#+#"

# Minimum number of characters in a text snippet
MIN_LEN = 300

# list containing names of locations
LOCATION_LIST = pickle.load(open(Path.joinpath(src.PATH, "external_data", "Orte", "DE", "location_list.p"), "rb"))
LOCATION_LIST.extend([loc.upper() for loc in LOCATION_LIST])

# load list of common endings of location names
LOCATION_INDICATORS = open(Path.joinpath(src.PATH, "external_data", "location_endings.txt"), "r", encoding='utf-8').read().split("\n")

# phrases at the end of press releases
PHRASES = [
    "Rückfragen bitte an:",
    "Medienrückfragen bitte an:",
]


def is_location(text):
    """Checks if a given string is or contains a location."""
    
    location = False

    word_list = [text]
    seps = ["/", ".", "-", " "]
    for sep in seps:
        if sep in text:
            word_list.extend(text.split(sep))
    
    for word in word_list:
        word = word.strip()
        for location_indicator in LOCATION_INDICATORS:
            if word.endswith(location_indicator):
                location = True
                break
        
        if not location:
            if word in LOCATION_LIST:
                location = True
    
    return location
        

def split_report_part0(text):
    """Entfernt den Adressanhang unten im Report."""
    
    for p in PHRASES:
        splitted_report = text.split(p)
        if len(splitted_report) > 1:
            text = splitted_report[0]
            break
    
    return text


def split_report_part6(text):

    snippets = []
    splitted_report = []
    ignore_list = []
    
    # für jede Zeile
    for i, line in enumerate(text.split("\n")):
        split = False
        
        line = line.strip()
        words = line.split()

        # wenn in der Zeile nicht mehr als 3 Worte vorkommen und darin ein Ort genannt wird
        if len(words) > 0 and not line.endswith("."):
            for i, word in enumerate(words):
                if ":" in word and not words[i-1].isdigit():
                    split = True
        # Wenn ein Split erkannt wurde
        if split:
            single_report = "\n".join(snippets)
            
            splitted_report.append(single_report)
            snippets = []
        
        snippets.append(line)
    
    single_report = "\n".join(snippets)
    splitted_report.append(single_report)
    splitted_report = SEP.join(splitted_report)
    
    return splitted_report


def split_report_part1(text):
    """Text anhand von Ortsbezeichnungen, welche vor einem ':' stehen, splitten."""
    
    snippets = []
    splitted_report = []
    words = text.split()
    
    # für jedes "Wort" im Report
    for i, word in enumerate(words):
        split = False
        
        # wenn ein ":" im Wort ist
        if ":" in word:
            
            # wenn das Wort bzw. die zwei Wörter vor dem ":" ein Ortsname ist
            if is_location(word[:-1]) or is_location(words[i-1] + " " + word[:-1]) or is_location(words[i-1] + " " + words[i-2] + " " + word[:-1]):
                split = True
            
            # wenn im :-Wort noch ein "-" ist, das Wort nochmal aufsplitten und nach passendem Ortsnamen schauen
            elif "-" in word and not " - " in word:
                for w in word.split("-"):
                    if is_location(w):
                        split = True
            
            # wenn im :-Wort noch ein "/" ist, das Wort nochmal aufsplitten und nach passendem Ortsnamen schauen
            elif "/" in word:
                for w in word.split("/"):
                    if is_location(w):
                        split = True
            
            # Wenn das Wort vor ":" eingeklammert ist
            elif word[0] == "(" and word[-2] == ")":
                split = True
            
            # Wenn eine der Bedingungen zutrifft
            if split:
                # alle bisher gesammalten Wörter zusammensetzen und als ein Report an Reportliste anhängen.
                single_report = " ".join(snippets).strip()
                splitted_report.append(single_report)
                snippets = []
        
        snippets.append(word)
    
    single_report = " ".join(snippets).strip()
    splitted_report.append(single_report)
    splitted_report = SEP.join(splitted_report)
    return splitted_report


def split_report_part3(text):
    """Anhand von Orten, die nach Zeilenumbrüchen in einer Zeile stehen, splitten."""

    snippets = []
    splitted_report = []
    ignore_list = []
    
    # für jede Zeile
    for i, line in enumerate(text.split("\n")):
        split = False
        
        line = line.strip()
        words = line.split()

        # wenn in der Zeile nicht mehr als 3 Worte vorkommen und darin ein Ort genannt wird
        if len(words) > 0 and len(words) <= 3:
            # Wenn die Zeile ein Ortsname ist
            if is_location(line.strip()):
                split = True
            
            if is_location(words[-1]): 
                split = True
        
        # wenn Zeile nicht mit Punkt endet und ein Ort darin ist
        if len(words) > 0 and not line.endswith("."):
            for word in words:
                if is_location(word):
                    split = True


        # wenn das erste Wort einer Zeile ein Ort ist
        if len(words) > 0:
            if is_location(words[0]): 
                split = True
            elif "-" in words[0]:
                for w in words[0].split("-"):
                    if is_location(w):
                        split = True
            elif len(words) > 1:
                if is_location(words[0] + " " + words[1]):
                    split = True
        
        # Wenn ein Split erkannt wurde
        if split:
            single_report = "\n".join(snippets)
            
            splitted_report.append(single_report)
            snippets = []
        
        snippets.append(line)
    
    single_report = "\n".join(snippets)
    splitted_report.append(single_report)
    splitted_report = SEP.join(splitted_report)
    return splitted_report


def split_report_part4(text):
    """Anhand von ' - ', das nach oder vor einem Ort kommt und eine neue Meldung einleitet, trennen."""
    
    snippets = []
    splitted_report = []
    ignore_list = []
    
    # für jede Zeile
    for i, line in enumerate(text.split("\n")):
        split = False
        
        if " - " in line and line.count(" - ") == 1:
            
            l = line.split(" - ")
            
            if len(l[0]) > 0 and len(l[1]) > 0:
                
                if is_location(l[0]):
                    split = True
                
                if is_location(l[1]):
                    split = True
                
        # Wenn Split gefunden
        if split:
            single_report = "\n".join(snippets)
            
            splitted_report.append(single_report)
            snippets = []
        
        snippets.append(line)
    
    single_report = "\n".join(snippets)
    splitted_report.append(single_report)
    splitted_report = SEP.join(splitted_report)
    return splitted_report


def split_report_part5(text):
    """Anhand von komplett großgeschriebenen Ortsnamen splitten."""
    
    snippets = []
    splitted_report = []
    words = text.split()
    
    # für jedes "Wort" im Report
    for i, word in enumerate(words):
        split = False
        
        if word.isupper():
            if is_location(word) or is_location(word.replace(":","").replace(".","")):
                split = True
            
            if i+2 <= len(words):
                if words[i+1].isupper():
                    if is_location(word + " " + words[i+1]) or is_location(word + " " + words[i+1].replace(":","").replace(".","")):
                        split=True
                
        # Wenn eine der Bedingungen zutrifft
        if split:
            
            # alle bisher gesammalten Wörter zusammensetzen und als ein Report an Reportliste anhängen.
            single_report = " ".join(snippets).strip()
            splitted_report.append(single_report)
            snippets = []
        
        snippets.append(word)
    single_report = " ".join(snippets).strip()
    splitted_report.append(single_report)
    splitted_report = SEP.join(splitted_report)
    return splitted_report


def split_report(text):
    """Wendet alle split_report-Funktionen auf einen eingegebenen Text an."""
    
    # Bei Adressanhang Split-Marker einfügen
    splitted_report = split_report_part0(text)
    
    # Zeilenweise durchgehen und Split-Marker einfügen
    splitted_report = split_report_part6(splitted_report)
    splitted_report = split_report_part3(splitted_report)
    splitted_report = split_report_part4(splitted_report)
    
    # Wortweise durchgehen und Split-Marker einfügen
    splitted_report = split_report_part1(splitted_report)
    splitted_report = split_report_part5(splitted_report)
    
    # Am Split-Marker splitten
    splitted_report = splitted_report.split(SEP)
    
    # noch den evtl. abgeschnittenen Teil (bis zum letzten Punkt) aus dem vorherigen Bericht holen
    if len(splitted_report) > 1:
        for i, report in enumerate(splitted_report):
            if i > 0:
                the_forgotten_part = splitted_report[i-1].split(".")[-1]
                splitted_report[i] = " ".join([the_forgotten_part, splitted_report[i]])
                splitted_report[i-1] = splitted_report[i-1][:len(splitted_report[i-1]) - len(the_forgotten_part)]
    
    # Nur Berichte mit Mindestlänge behalten
    splitted_report = [text.strip() for text in splitted_report if len(text.strip()) >= MIN_LEN]
    
    return splitted_report
        
   
def split_reports_in_df(df, report_col, drop = True):
    """Splittet alle Texte innerhalb einer Dataframe-Spalte."""
    
    df = copy.deepcopy(df)
    df = df.reset_index(drop=True)
    
    len_df = len(df)
    
    progress = 0
    
    new_df = []
    
    # für jede Zeile des DF
    for i in df.index:
        
        # Fortschritt anzeigen
        progress_temp = round((i / len_df) * 100)
        if progress_temp != progress:
            progress = progress_temp
            print(progress, "%")
        
        # Report-Text heraussuchen und splitten
        report = df.loc[i, report_col]
        if len(report) > MIN_LEN:
            splitted_report = split_report(report)
        else:
            splitted_report = [report]
        
        # Neue Zeilen/neuen DF für gesplitteten Report anlegen und Daten einfügen
        if len(splitted_report) > 0:
            df_new_rows = pd.concat([pd.DataFrame(df.loc[[i], :])] * len(splitted_report), ignore_index = True)
            df_new_rows["text_snippet"] = ""
            df_new_rows["n_snippets"] = len(splitted_report)
            df_new_rows["snippet_id"] = None

            for i in df_new_rows.index:
                df_new_rows.loc[i, "text_snippet"] = splitted_report[i]
                df_new_rows.loc[i, "snippet_id"] = i
            
            new_df.append(df_new_rows)

    # alle neuen Zeilen/Dfs zu einem Df zusammenfügen
    new_df = pd.concat(new_df, ignore_index = True)
    
    # Original-Text aus allen Zeilen löschen?
    if drop:
        new_df = new_df.drop(report_col, 1)
    
    return new_df