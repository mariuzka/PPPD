import copy
import os
from pathlib import Path
import pickle

import pandas as pd

import src
from src import utils


SEP = " #+#+#+#+#+# "
SEP_strip = SEP.strip()

# Minimum number of characters in a text snippet
MIN_LEN = 120
TOTAL_MIN_LEN = 150

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



def ends_with_punctuation(text):
    status = False
    
    words = text.split()
    
    # eingeklammerte Worte am Ende entfernen
    if words[-1].endswith(")") and words[-1].startswith("("):
        words = words[0:-1]
        text = " ".join(words)
    
    # prüfen ob der text mit 
    for punct in [".", ",", "!", "?", ":"]:
        if text.strip().endswith(punct):
            status = True
            break
    return status



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
        
    if not location:
        for l in LOCATION_LIST:
            if l in text:
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



def split_report_part1(text):
    """Text anhand von Ortsbezeichnungen, welche vor einem ':' stehen, splitten."""
    ignore_list = ["Tel.:"]
    
    snippets = []
    splitted_report = []
    words = text.split()
    
    split_counter = 0
    
    # für jedes "Wort" im Report
    for i, word in enumerate(words):
        split = False
        
        # wenn ein ":" im Wort ist
        if ":" in word and not word[0].isnumeric() and word not in ignore_list:
            
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
                split_counter += 1
                # alle bisher gesammalten Wörter zusammensetzen und als ein Report an Reportliste anhängen.
                single_report = " ".join(snippets).strip()
                splitted_report.append(single_report)
                snippets = []
        
        snippets.append(word)
    
    single_report = " ".join(snippets).strip()
    splitted_report.append(single_report)
    splitted_report = SEP.join(splitted_report)
    return splitted_report, split_counter


def split_report_part3(text):
    """Anhand von Orten, die nach Zeilenumbrüchen in einer Zeile stehen, splitten."""

    snippets = []
    splitted_report = []
    ignore_list = []
    
    split_counter = 0
    
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
        if len(words) > 0 and not ends_with_punctuation(line):
            for word in words:
                if is_location(word):
                    split = True
                    


        # wenn das erste Wort einer Zeile ein Ort ist
        # if len(words) > 0:
        #     if is_location(words[0]): 
        #         split = True
        #     elif "-" in words[0]:
        #         for w in words[0].split("-"):
        #             if is_location(w):
        #                 split = True
        #     elif len(words) > 1:
        #         if is_location(words[0] + " " + words[1]):
        #             split = True
        
        
        
        # Wenn ein Split erkannt wurde
        if split:
            split_counter += 1
            single_report = "\n".join(snippets)
            
            splitted_report.append(single_report)
            snippets = []
        
        snippets.append(line)
    
    single_report = "\n".join(snippets)
    splitted_report.append(single_report)
    splitted_report = SEP.join(splitted_report)
    
    return splitted_report, split_counter



def split_report_part5(text):
    """Anhand von komplett großgeschriebenen Ortsnamen splitten."""
    
    snippets = []
    splitted_report = []
    words = text.split()
    
    split_counter = 0
    
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
            split_counter += 1
            
            # alle bisher gesammalten Wörter zusammensetzen und als ein Report an Reportliste anhängen.
            single_report = " ".join(snippets).strip()
            splitted_report.append(single_report)
            snippets = []
        
        snippets.append(word)
    single_report = " ".join(snippets).strip()
    splitted_report.append(single_report)
    splitted_report = SEP.join(splitted_report)
    return splitted_report, split_counter



def split_report(text):
    """Wendet alle split_report-Funktionen auf einen eingegebenen Text an."""
    
    # Bei Adressanhang Split-Marker einfügen
    splitted_report = split_report_part0(text)
    
    # Zeilenweise durchgehen und Split-Marker einfügen
    splitted_report, split_counter = split_report_part3(splitted_report)
    
    # Wortweise durchgehen und Split-Marker einfügen
    splitted_report, split_counter = split_report_part1(splitted_report)
    splitted_report, split_counter = split_report_part5(splitted_report)
    
    # Am Split-Marker splitten
    splitted_report = splitted_report.split(SEP)
   
    # noch den evtl. abgeschnittenen Teil (bis zum letzten Punkt) aus dem vorherigen Bericht holen
    if len(splitted_report) > 1:
        for i, report in enumerate(splitted_report):
            if i > 0:
                the_forgotten_part = splitted_report[i-1].split(".")[-1]
                
                if len(the_forgotten_part) < MIN_LEN:
                    splitted_report[i] = " ".join([the_forgotten_part, splitted_report[i]])
                    splitted_report[i-1] = splitted_report[i-1][:len(splitted_report[i-1]) - len(the_forgotten_part)]
    
    
    # Nur Berichte mit Mindestlänge behalten
    splitted_report = [text.strip() for text in splitted_report if len(text.strip()) >= TOTAL_MIN_LEN]
    splitted_report = [text.strip() for text in splitted_report if not (len(text.strip()) <= 200 and "Pressestelle Polizeipräsidium Karlsruhe" in text)]
    
    # Überreste von Split-Marker entfernen
    splitted_report = [text.replace(SEP_strip, "").strip() for text in splitted_report]
    
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



def eval_splits(df, df_split, doc_name, n=False, frac=False):
    """Erstellt ein Text-Dokument, mit welchem die Splits überprüft werden können."""
    
    FOLDER_NAME = "eval_split_files"
    
    assert (n and not frac) or (frac and not n)

    utils.create_folder(Path.joinpath(src.PATH, FOLDER_NAME))

    txt_file = open(Path.joinpath(src.PATH, FOLDER_NAME, doc_name+".txt"), "w", encoding="utf-8")
    df = copy.deepcopy(df)

    len_df = len(df)

    if n:
        assert n > 0
        assert n <= len(df)
        df = df.sample(n=n)
    
    elif frac:
        assert 0 < frac <= 1
        df = df.sample(frac=frac)
    
    print("Vom DF mit", len_df, "Zeilen wurde ein Sample der Größe", len(df), "gezogen.")

    text_data_dicts = []

    for i, row in enumerate(df.index):

        link = df.loc[row, "article_link"]
        original_text = df.loc[row, "text"]
        newsroom_nr = df.loc[row, "newsroom_nr"]
        newsroom = df.loc[row, "newsroom"]
        date_release = df.loc[row, "date_release"]

        txt_file = open(Path.joinpath(src.PATH, FOLDER_NAME, doc_name+".txt"), "a", encoding="utf-8")
        
        txt_file.write("\n")
        txt_file.write("\n")
        txt_file.write("###################################################################################################\n")
        txt_file.write("---------------------------------------------------------------------------------------------------\n")
        txt_file.write("###################################################################################################\n")
        txt_file.write("\n")
        txt_file.write("\n")
        txt_file.write(link)
        txt_file.write("\n")
        txt_file.write("\n")
        txt_file.write(str(i))
        txt_file.write("\n")
        txt_file.write("\n")
        txt_file.write("ORIGINAL")
        txt_file.write("\n")
        txt_file.write("\n")
        txt_file.write(original_text)
        txt_file.write("\n")
        txt_file.write("\n")
        txt_file.write("---------------------------------------------------------------------------------------------------\n")
        txt_file.write("\n")
        txt_file.write("\n")
        txt_file.write("SPLIT")
        txt_file.write("\n")
        txt_file.close()

        text_snippets = []
        for text_snippet in df_split[df_split["article_link"] == link]["text_snippet"]:

            text_snippets.append(text_snippet)
            
            txt_file = open(Path.joinpath(src.PATH, FOLDER_NAME, doc_name+".txt"), "a", encoding="utf-8")
            txt_file.write("\n")
            txt_file.write(text_snippet)
            txt_file.write("\n")
            txt_file.write("---------------------------------------------------------------------------------------------------\n")
            txt_file.close()
        
        split_text = "\n\n --------------------------------------------------------------------------------------------------- \n\n".join(text_snippets)
    
        text_data_dicts.append({
            "link": link,
            "newsroom_nr": newsroom_nr,
            "newsroom": newsroom,
            "date_release": date_release,
            "original_text": original_text,
            "split_text": split_text,
        })

    eval_df = pd.DataFrame(text_data_dicts)
    eval_df.to_excel(Path.joinpath(src.PATH, FOLDER_NAME, doc_name+".xlsx"), index=False)