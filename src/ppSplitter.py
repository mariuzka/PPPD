import pandas as pd
import os
import pickle
import copy
from pathlib import Path

import src

MIN_LEN = 200
LOCATION_LIST = pickle.load(open(
    Path.joinpath(src.PATH, "external_data", "Orte", "DE", "location_list.p"),
    "rb",
    ))
LOCATION_LIST.extend([loc.upper() for loc in LOCATION_LIST])

def is_location(text):
    if text in LOCATION_LIST:
        return True
    else:
        return False

def split_report_part0(text):
    """entfernt den Adressanhang unten im Report"""
    
    phrases = [
        "Rückfragen bitte an:",
        "Medienrückfragen bitte an:",
    ]
    
    for p in phrases:
        splitted_report = text.split(p)
        if len(splitted_report) > 1:
            text = splitted_report[0]
            break
    return text

def split_report_part1(text):
    """Text anhand von ':' splitten."""
    
    snippets = []
    splitted_report = []
    words = text.split()
    
    # für jedes "Wort" im Report
    for i, word in enumerate(words):
        split = False
        
        # wenn ein ":" im Wort ist
        if ":" in word:
            
            # wenn das Wort bzw. die zwei Wörter vor dem ":" ein Ortsname ist
            if is_location(word[:-1]) or is_location(words[i-1] + " " + word[:-1]):
                split = True
            
            # wenn im :-Wort noch ein "-" ist, das Wort nochmal aufsplitten und nach passendem Ortsnamen schauen
            elif "-" in word:
                for w in word.split("-"):
                    if is_location(w):
                        split = True
            
            # Wenn das Wort vor ":" eingeklammert ist
            elif word[0] == "(" and word[-2] == ")":
                split = True
            
            # Wenn das erste Symbol, aber nicht das letzte Symbol im Wort eine Zahl ist
            elif len(word) > 1:
                if word[-2].isdigit() and not word[-1].isdigit():
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
    splitted_report = [text for text in splitted_report if len(text) >= MIN_LEN]
    return splitted_report

def split_report_part3(text):
    snippets = []
    splitted_report = []
    ignore_list = []
    
    # für jede Zeile
    for i, line in enumerate(text.split("\n")):
        split = False
        
        # wenn in der Zeile weniger als 4 Worte vorkommen
        words = line.split()
        if len(words) <= 3:
            
            # Wenn die Zeile ein Ortsname ist
            if is_location(line.strip()):
                split = True
        
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
                
        if split:
            single_report = " ".join(snippets)
            
            splitted_report.append(single_report)
            snippets = []
        
        snippets.append(line)
    
    single_report = " ".join(snippets)
    splitted_report.append(single_report)
    splitted_report = [text for text in splitted_report if len(text) >= MIN_LEN]
    return splitted_report

def split_report_part4(text):
    snippets = []
    splitted_report = []
    ignore_list = []
    
    # für jede Zeile
    for i, line in enumerate(text.split("\n")):
        split = False
        
        if " - " in line and line.count(" - ") == 1:
            # für jede Location überprüfen, ob sie in der Zeile
            
            l = line.split(" - ")
            
            if len(l) == 2:
                if len(l[0]) > 0 and len(l[1]) > 0:
            
                    if len(l[0]) > 0:
                        if is_location(l[0][-1]):
                            split = True
                    
                    if len(l[0]) > 1:
                        if is_location(l[0][-2] + " " + l[0][-1]):
                            split = True
                    
                    if len(l[1]) > 0:
                        if is_location(l[1][0]):
                            split = True
                    
                    if len(l[1]) > 1:
                        if is_location(l[1][0] + " " + l[1][1]):
                            split = True
        
        if split:
            single_report = " ".join(snippets)
            
            splitted_report.append(single_report)
            snippets = []
        
        snippets.append(line)
    
    single_report = " ".join(snippets)
    splitted_report.append(single_report)
    splitted_report = [text for text in splitted_report if len(text) >= MIN_LEN]
    return splitted_report



def split_report_part5(text):
    """Anhand von großgeschriebenen Ortsnamen splitten."""
    
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
                    if islocation(word + " " + words[i+1]) or islocation(word + " " + words[i+1].replace(":","").replace(".","")):
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
    splitted_report = [text for text in splitted_report if len(text) >= MIN_LEN]
    return splitted_report


def split_report(text):
    """Wendet alle split_report-Funktionen auf einen eingegebenen Text an."""
    
    text = split_report_part0(text)
    
    splitted_report = split_report_part1(text)
    
    if len(splitted_report) == 1:
        splitted_report = split_report_part3(text)
    
    if len(splitted_report) == 1:
        splitted_report = split_report_part4(text)
    
    # noch den evtl. abgeschnittenen teil aus dem vorherigen Bericht holen
    if len(splitted_report) > 1:
        for i, report in enumerate(splitted_report):
            if i > 0:
                the_forgotten_part = splitted_report[i-1].split(".")[-1]
                splitted_report[i] = " ".join([the_forgotten_part, splitted_report[i]])
                splitted_report[i-1] = splitted_report[i-1][:len(splitted_report[i-1]) - len(the_forgotten_part)]
    
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
        
        progress_temp = round((i / len_df) * 100)
        if progress_temp != progress:
            progress = progress_temp
            print(progress, "%")
        
        # Report-Text heraussuchen und splitten
        report = df.loc[i, report_col]
        if len(report) > 100:
            splitted_report = split_report(report)
        else:
            splitted_report = [report]
        
        if len(splitted_report) > 0:
            df_new_rows = pd.concat([pd.DataFrame(df.loc[[i], :])] * len(splitted_report), ignore_index = True)
            df_new_rows["text_snippet"] = ""
            df_new_rows["n_snippets"] = len(splitted_report)
            df_new_rows["snippet_id"] = None
    
            for i in df_new_rows.index:
                df_new_rows.loc[i, "text_snippet"] = splitted_report[i]
                df_new_rows.loc[i, "snippet_id"] = i
            
            new_df.append(df_new_rows)
    
    new_df = pd.concat(new_df, ignore_index = True)
    
    if drop:
        new_df = new_df.drop(report_col, 1)
    return new_df
