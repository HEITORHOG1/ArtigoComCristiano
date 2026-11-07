# -*- coding: utf-8 -*-
"""Confere no Crossref e no OpenAlex cada referencia do artigo original (Paper Training - 15 Nov 2025).
Para DOI informado: consulta o DOI e compara o titulo. Sem DOI: busca bibliografica e compara o titulo
do melhor resultado (similaridade >= 0,80 conta como localizado)."""
import json, sys, time, difflib, urllib.parse, urllib.request

sys.stdout.reconfigure(encoding="utf-8")
UA = {"User-Agent": "ref-check/1.0 (manuscript reference verification)"}

REFS = [
 ("Airbus2024", "Airbus Human Factors Lab", "VR training efficacy in maintenance operations", "", "2024", ""),
 ("BoeingAIR2024", "Boeing AIR Lab", "NLP applications in maintenance skill gap analysis", "", "2024", ""),
 ("BoeingMRO2025", "Boeing", "Blockchain applications in competency tracking", "", "2025", ""),
 ("Boyd2015", "Boyd Stolzer", "Causes and Trends in Maintenance-Related Accidents in FAA-Certified Single Engine Piston Aircraft", "Journal of Aviation Technology and Engineering", "2015", "10.7771/2159-6670.1123"),
 ("Chen2023", "Chen", "The role of employee competency development in achieving circular economy outcomes: Evidence from the aviation MRO sector", "Journal of Cleaner Production", "2023", "10.1016/j.jclepro.2023.137521"),
 ("Dismukes2023", "Dismukes", "Cognitive dimensions of procedural deviations", "Journal of Cognitive Engineering and Decision Making", "2023", ""),
 ("FAAHERMIT2024", "FAA", "HERMIT framework: High-reliability organization practices", "", "2024", ""),
 ("FernandezDelgado2024", "Fernandez-Delgado", "Causal AI for training attribution", "IEEE Transactions on Artificial Intelligence", "2024", ""),
 ("Garcia2024", "Garcia", "Digital twins in engine maintenance training", "International Journal of Aviation Psychology", "2024", ""),
 ("IATABlockchain2025", "IATA", "Blockchain in aviation credentials", "", "2025", ""),
 ("IATAMRO2025", "IATA", "MRO economic benchmarking survey", "", "2025", ""),
 ("Iwasaki2025", "Iwasaki Schmidt", "Predictive analytics for sustainable resource allocation: Minimizing energy and material waste in service operations through data-driven competency management", "Journal of Cleaner Production", "2025", "10.1016/j.jclepro.2025.102450"),
 ("KimLee2024", "Kim Lee", "Self-reported data limitations in high-stakes training evaluation", "Human Factors", "2024", ""),
 ("Kirkpatrick2006", "Kirkpatrick", "Evaluating training programs: The four levels", "Berrett-Koehler", "2006", ""),
 ("Leveson2011", "Leveson", "Engineering a safer world: Systems thinking applied to safety", "MIT Press", "2011", ""),
 ("Nakamura2024", "Nakamura", "The compliance paradox in aviation training", "Aerospace Medicine and Human Performance", "2024", ""),
 ("NASAHFB2023", "NASA", "Neuroergonomic tools for Level 1 assessment", "", "2023", ""),
 ("OConnor2024", "O'Connor", "Safety culture as a moderator of training transfer", "Safety Science", "2024", ""),
 ("OReilly2024", "O'Reilly", "Regulatory gaps in Kirkpatrick implementation for AS9100 environments", "Journal of Aviation Technology and Engineering", "2024", ""),
 ("Oschman2017", "Oschman", "Strategic quality management in implementation of AS9100", "Quality Management Journal", "2017", ""),
 ("Patel2023", "Patel", "Isolating training effects in complex systems", "Reliability Engineering & System Safety", "2023", ""),
 ("Pereira2017", "Pereira", "Risk-based maintenance cost modeling", "International Journal of Quality and Innovation", "2017", ""),
 ("Peterson2025", "Peterson", "Predictive modeling of training ROI", "Machine Learning", "2025", ""),
 ("Phillips2021", "Phillips", "Handbook of training evaluation", "Routledge", "2021", ""),
 ("Reason1990", "Reason", "Human error", "Cambridge University Press", "1990", ""),
 ("Reason2016", "Reason", "Organizational Accidents Revisited", "", "2016", ""),
 ("SAE2025", "SAE International", "AS9100 Rev E compliance report", "", "2025", ""),
 ("Sousa2025", "Sousa", "Human capital development in high-reliability organizations: A lean-driven framework for operational sustainability and waste reduction", "Journal of Cleaner Production", "2025", "10.1016/j.jclepro.2025.102301"),
 ("YangPark2024", "Yang Park", "Integrating human factors into lean management for enhanced resource efficiency and error reduction in manufacturing systems", "Journal of Cleaner Production", "2024", "10.1016/j.jclepro.2024.139912"),
 ("YucelAyvaz2019", "Yucel Ayvaz", "AS9100 implementation challenges", "International Journal of Supply Chain Management", "2019", ""),
 ("Zhang2025", "Zhang", "Training failure costs in MRO operations", "Journal of Air Transport Management", "2025", ""),
 # citadas no texto do original, sem entrada na lista
 ("Shunko2018", "Shunko Niederhoff Rosokha", "Humans are not machines: The behavioral impact of queueing design on service time", "Management Science", "2018", ""),
 ("Jung2019", "Jung", "optimization models resource allocation high-stakes environments", "", "2019", ""),
 ("BuriakAyars2019", "Buriak Ayars", "Kirkpatrick training evaluation", "", "2019", ""),
]


def get(url):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def sim(a, b):
    a, b = a.lower().strip(" ."), b.lower().strip(" .")
    return difflib.SequenceMatcher(None, a, b).ratio()


def crossref_doi(doi):
    try:
        m = get("https://api.crossref.org/works/" + urllib.parse.quote(doi))["message"]
        return (m.get("title") or [""])[0], (m.get("container-title") or [""])[0], m.get("issued", {}).get("date-parts", [[None]])[0][0]
    except Exception as e:
        return None


def crossref_busca(q):
    try:
        it = get("https://api.crossref.org/works?rows=5&query.bibliographic=" + urllib.parse.quote(q))["message"]["items"]
        return [((i.get("title") or [""])[0], (i.get("container-title") or [""])[0],
                 i.get("issued", {}).get("date-parts", [[None]])[0][0], i.get("DOI"),
                 ", ".join(a.get("family", "") for a in i.get("author", [])[:3])) for i in it]
    except Exception as e:
        return []


def openalex_busca(q):
    try:
        it = get("https://api.openalex.org/works?per-page=5&search=" + urllib.parse.quote(q))["results"]
        return [(i.get("title") or "", ((i.get("primary_location") or {}).get("source") or {}).get("display_name", ""),
                 i.get("publication_year"), (i.get("doi") or "").replace("https://doi.org/", ""),
                 ", ".join(a["author"]["display_name"] for a in i.get("authorships", [])[:3])) for i in it]
    except Exception as e:
        return []


for key, aut, tit, ven, ano, doi in REFS:
    linha = [key]
    if doi:
        r = crossref_doi(doi)
        if r is None:
            linha.append(f"DOI {doi}: NAO EXISTE no Crossref")
        else:
            s = sim(tit, r[0])
            linha.append(f"DOI {doi} -> '{r[0][:90]}' | {r[1]} | {r[2]} | sim={s:.2f} {'OK' if s >= 0.8 else 'OUTRO ARTIGO'}")
    melhor = (0, None, "")
    for fonte, res in (("CR", crossref_busca(f"{tit} {aut} {ven}")), ("OA", openalex_busca(tit))):
        for t, v, y, d, a in res:
            s = sim(tit, t)
            if s > melhor[0]:
                melhor = (s, (t, v, y, d, a), fonte)
        time.sleep(0.3)
    s, r, fonte = melhor
    if r and s >= 0.8:
        linha.append(f"LOCALIZADO ({fonte}, sim={s:.2f}): '{r[0][:90]}' | {r[1]} | {r[2]} | {r[3]} | {r[4]}")
    elif r:
        linha.append(f"nao localizado (melhor sim={s:.2f}: '{r[0][:70]}' | {r[1]} | {r[2]} | {r[4]})")
    else:
        linha.append("nao localizado (sem resultado)")
    print(" || ".join(linha), flush=True)
