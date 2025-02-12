# Project Plan

Jana Brusés | janabruses@pitt.edu | Feb 11th, 2025

# Working title:

Traces of Catalan's danger: Linguistic Markers of a Threatened Language

# Summary:

This project analyzes linguistic markers of language substitution in Catalan due to Spanish dominance. Examining morphological, syntactic, lexical, and semantic changes to quantify language shift and determine key symptoms of Catalan’s endangerment.

Socially, there are many proofs of Catalan’s danger, as it is now spoken regularly by only one-third of Catalonia’s population. This project explores this threat from an empirical language data point of view. 

A usual misconception is that word incorporations are the most remarkable indices of a language substitution or endangerement. However, as previous Catalan-threatening situations have shown after Franco forbade Catalan, vocabulary was still picked up, and competence improved when the use increased. Instead, this project explores specific cases of some of the symptoms highlighted by Dr. Junyent, one of the leading figures of Catalan protection and advocates for language diversity preservation. The symptoms she proposes will be the pillars of the analysis, as she described them as “irreversible.”

What Dr. Junyent suggests as actual language-threatening losses and symptoms to diagnose Catalan as a tongue threatened by language shift are:
1. Loss of word classes absent in the dominant language. 
2. Time and space lexicon modification.
3. Syntactic restructuring

# Analysis

This analysis aims to quantify the linguistic markers of Catalan language substitution by measuring specific changes over time. The study looks at both lower-level linguistic symptoms (morphological, syntactic, lexical, and semantic) and higher-level text characteristics that could indicate increasing convergence with Spanish.

#### 1. Loss of word classes
It will be explored by looking at **pronoms febles**. Clitic pronouns used in Catalan that don't have an Spanish equivalent. A frequency analysis of pronoms febles will be conducted on written Catalan samples across different time periods.

#### 2. Time and space lexicon modification
* 2.1 **Directional distinction in *anar* and *venir***\
These verbs express a directional difference that is likely being lost due to its absence in Spanish. This will be analyzed through a frequency study of *anar* and *venir* in a corpus of Catalan through a decade, along with a distribution analysis to determine whether the distinction is diminishing.
* 2.2 **Shift from perifràstic past to simple past**\
The perifràstic past, a tense not present in most Romance languages, may be shifting toward the simple past. This phenomenon will be examined through a frequency analysis.
* 2.3 **Pronominalization of movement verbs**\
Influence from Spanish leading to structures like *se’ns cauen* instead of *ens cauen* and *puja’t* instead of *puja* will be analyzed. 

#### 3. Syntactic restructuring
* 3.1 **Deletion of subject pronouns**\
Subject pronouns, required in Catalan but often omitted in Spanish, will be analyzed for frequency changes over time.
* 3.2 ***Tenir que* vs *haver de***\
The Spanish construction tener que has influenced the incorrect Catalan form tenir que in place of haver de. This strength and evolution of this shift will be examined through frequency analysis.
* 3.3 **Deletion of *en* in partitive expressions**\
Omission of *en* in phrases like *menjaré dos* (mimiquing *comeré dos* in Spanish) instead of *en menjaré dos* will be analyzed for frequency changes over time.

#### 4. Text-level analysis
A text classifier will be trained to differentiate Catalan and Spanish samples across different years. Classification accuracy will be evaluated: a decline over time would suggest a clearer process of substitution.

# Data

The data used for this project wll be: 

- Külebi, B. (2021). ParlamentParla - Speech corpus of Catalan Parliamentary sessions (v2.0) [Data set](https://doi.org/10.5281/zenodo.5541827). Zenodo.\
  As the catalan corpora from 2007 to 2018.
- Elena Álvarez-Mellado. 2020. A Corpus of Spanish Political Speeches from 1937 to 2019. In Proceedings of the Twelfth Language Resources and Evaluation Conference, pages 928–932, Marseille, France. European Language Resources Association [Data set](https://github.com/lirondos/discursos-de-navidad)\
  As the Spanish corpora for text-level classification section.
- Tomaž Erjavec, Matyáš Kopp, Nikola Ljubešić, Taja Kuzman, Paul Rayson, Petya Osenova, Maciej Ogrodniczuk, Çağrı Çöltekin, Danijel Koržinek, Katja Meden, Jure Skubic, Peter Rupnik, Tommaso Agnoloni, José Aires, Starkaður Barkarson, Roberto Bartolini, Núria Bel, Calzada María Pérez, Roberts Darģis, Sascha Diwersy, Maria Gavriilidou, van Ruben Heusden, Mikel Iruskieta, Neeme Kahusk, Anna Kryvenko, Noémi Ligeti-Nagy, Carmen Magariños, Martin Mölder, Costanza Navarretta, Kiril Simov, Lars Magne Tungland, Jouni Tuominen, John Vidler, Adina Ioana Vladu, Tanja Wissik, Väinö Yrjänäinen & Darja Fišer. ParlaMint II: Advancing Comparable Parliamentary Corpora Across Europe. Language Resources & Evaluation (2024). [Data set](clarin-eric.github.io/ParlaMint/)
Containing both Spanish and Catalan corpora from the same domain and in a similar context. 