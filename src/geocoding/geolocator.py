

import spacy
from spacy.pipeline import EntityRuler

from src.geocoding.models import Geoname, Potential_Toponym_Entitiy
from src.models import Report


def text_topo_NER(text, nlp, **kwargs):
    """
    Performs toponym NER and returns entities.
    Displays NER annotated text via displacy.
    As additioanl keyword arguments, `verbose` and
    the `report_id` is used as header for the
    displacy render if verbose = True
    """

    doc = nlp(text)
    if kwargs.get("report_id"):
        doc.user_data["title"] = kwargs.get("report_id")

    if kwargs.get("verbose"):
        displacy.render(doc, style="ent", jupyter=True)

    return doc.ents


def text_toponym_lookup(text, **kwargs):
    """
    Expects entities and performs lookup in Geonames
    table. Returns a unique set of Geoname queries
    with preference for ADM4 units. Has additioanl
    keyword arguments `singular` (defaults to False),
    which forces to return a single toponym (the
    smallest possible unit).
    Passes additioanl keyword arguments `report_id`
    and `verbose` to `text_topo_NER()`
    """

    # Geonames
    from models import Geonames, Geonames_Codes

    # Get Geoname feature_codes to filter  named entites
    # after NER process, that refer to Geonames.
    geoname_labels = Geonames_Codes.select().where(
        (Geonames_Codes.feature_class == "A") | (Geonames_Codes.feature_class == "P")
    )
    geoname_label_list = []
    for label in geoname_labels:
        geoname_label_list.append(label.code)

    # Now, lookup ents in Geonames
    if kwargs.get("base_query"):
        base_query = kwargs.get("base_query")
    else:
        base_query = (
            Geonames.select()
            .where((Geonames.feature_class == "A") | (Geonames.feature_class == "P"))
            .where(Geonames.admin4_code.startswith("08"))
            .join(Geonames_Codes)
        )
    ents = text_topo_NER(
        text, report_id=kwargs.get("report_id"), verbose=kwargs.get("verbose")
    )
    topo_list = []
    for ent in ents:
        # Only if ent is geonames-entity
        if ent.label_ in geoname_label_list:
            lookup_query = base_query.where(Geonames.name.startswith(ent))
            lookup_query = adm4_extractor(lookup_query)

            if kwargs.get("singular"):
                lookup_query_ppl = lookup_query.where(
                    Geonames.feature_code.code == "PPL"
                )
                if lookup_query_ppl.exists():
                    lookup_query = lookup_query_ppl
                else:
                    pass

            for topo in lookup_query:
                topo_list.append(topo)

    # Show results and return unique queryset
    if kwargs.get("verbose"):
        for topo in set(topo_list):
            print(
                topo.admin4_code,
                topo.name,
                topo.feature_code,
                topo.feature_code.description,
            )

    # Push to DB
    if kwargs.get("db_article"):
        for topo in set(topo_list):
            ArticleToGeoname(article=kwargs.get("db_article"), geoname=topo).save()

    return set(topo_list)


def build_ruler_pipeline(sessionmaker):
    nlp = spacy.load("de_core_news_sm")
    nlp.disable_pipes(
        [
            "tok2vec",
            "tagger",
            "morphologizer",
            "parser",
            "lemmatizer",
            "attribute_ruler",
            "ner",
        ]
    )
    ruler = EntityRuler(nlp, overwrite_ents=True)

    # Add ruler to pipe
    ruler = nlp.add_pipe("entity_ruler")

    # Get geonames for ruler
    # Only subset for populated places in Baden-Württemberg
    session = sessionmaker()
    # session = Session()
    q = (
        session.query(Geoname)
        .filter((Geoname.feature_class == "A") | (Geoname.feature_class == "P"))
        .filter(Geoname.admin4_code.like("08%"))
    )
    for e in q:
        print(e.feature_code)

    # Add patterns from Geonames to ruler
    for e in q:
        ruler.add_patterns([{"label": e.admin4_code, "pattern": e.name}])

    return nlp


def report_geolookup(report_id, nlp, geonames):
    # here
    # Get report
    session = Session()
    report = session.query(Report).filter(Report.id == report_id)

    # Apply NER on report text snippet and retrieve adm4 codes
    entities = text_topo_NER(report.scalar().text_snippet, nlp)
    topo_list = []
    geonames_labels = set(geonames["feature_code"])
    for ent in entities:
        # Only if ent is geonames-entity
        if ent.label_ in geonames_labels:
            for adm4code in geonames[geonames["name"].str.startswith(str(ent))][
                "admin4_code"
            ]:
                topo_list.append(adm4code)

    # Write to db
    potential_toponym_entity = Potential_Toponym_Entitiy(
        list_of_adm4_codes=list(set(topo_list))
    )
    potential_toponym_entity.report = report
    session.add(potential_toponym_entity)
    session.commit()
    session.close()

    return list(set(topo_list))


# engine, Session = src.db_connection(init=False)
# report_id = 683005
nlp = build_ruler_pipeline(Session)
test = report_geolookup(report_id, nlp, geonames)

text = "Test text aus Stuttgart für Neuhausen"
doc=nlp(text)
for i in doc.ents:
    print (i.char_span)