# Project Plan

Jana Brusés | janabruses@pitt.edu | Feb 11th, 2025

**Working title:**

Traces of Catalan's danger: Linguistic Markers of a Threatened Language

**Summary:**

This project aims to analyze linguistic markers of language substitution in Catalan due to Spanish dominance. By examining morphological, syntactic, lexical, and semantic changes with the goal to quantify language shift and determine key symptoms of Catalan's endangerment.

Socially, there are many proofs of Catalan's danger, as it is now spoken regularly by only 1/3 of Catalonia's population. This projects explores this threat from an empirical language data point of view. A usual misconception is that word incorporations are the most remarkable indice of a language being substituted. However, as previous Catalan-threatening situations have shown after Catalan was forbidden by Franco, vocabulary was still picked up and competence improved when the use increased. Instead, this project explores specific cases of some of the symptoms highlighted by Dr. Junyent, one of the main figures of Catalan's protection and advocates of language diversity preservation. The symptoms she proposes are going to be the pillars of the analysis, as she described them as "irreversible."

What Dr. Junyent suggests as real language-threatening losses and symptoms to diagnose Catalan as a tongue threatened by language shift are:
1. Loss of word classes absent in the dominant language. 
2. Time and space lexicon modification.
3. Syntactic restructuring

# Analysis

This analysis aims to quantify the linguistic markers of Catalan language substitution by measuring specific changes over time. The study looks at both lower-level linguistic symptoms (morphological, syntactic, lexical, and semantic) and higher-level text characteristics that could indicate increasing convergence with Spanish.

#### 1. Loss of word classes
Will explored by looking at pronoms febles. Clitic pronouns. (short explanation)
A frequency analysis of pronoms febles will be conducted on written Catalan samples across different time periods.

#### 2. Time and space lexicon modification
* 2.1 Will be explored focusing on the verbs "anar" and "venir." These have a directional difference, that is likely being lost because of its inexistence in Spanish. This point will be explored through a frequency analysis of "anar" and "venir" in a corpus of contemporary Catalan and a distribution analysis to see whether this distinction is being lost.
* 2.2 Preterit perifrastic (past tense inexistent in most romanic languages) shift into simple past. Will be explored through a frequency analysis. 
* 2.3 Pronominalization of movement verbs, mimiquing Spanish *“se’ns cauen” instead of “ens cauen”, “puja’t a la bicicleta” instead of “puja a la bicicleta”. 

#### 3. Syntactic restructuring
* 3.1 Delition of subject pronouns required in Catalan but dropped in Spanish. 
* 3.2 The use of the Spanish literal translation "Tener que" (spanish) into catalan "Tenir que," while the grammatical expression is "Haver de" 
* 3.3 Delition of "En" preposition is expressions such as "menjaré dos" because of the similar Spanish structure "Comeré dos" which is "ø menjaré dos." 
All analyzed through a frequency analysis through time. 

#### 4. Text-level analysis
Training a text classifier to differentiate Catalan and Spanish samples across different years.
Evaluating classification accuracy: If accuracy drops over time, it suggests increased linguistic convergence.

# Data

The data used for this project wll be: 

- Külebi, B. (2021). ParlamentParla - Speech corpus of Catalan Parliamentary sessions (v2.0) [Data set](https://doi.org/10.5281/zenodo.5541827). Zenodo.\
  As the catalan corpora from 2007 to 2018.
- Elena Álvarez-Mellado. 2020. A Corpus of Spanish Political Speeches from 1937 to 2019. In Proceedings of the Twelfth Language Resources and Evaluation Conference, pages 928–932, Marseille, France. European Language Resources Association [Data set](https://github.com/lirondos/discursos-de-navidad)\
  As the Spanish corpora for text-level classification section.
- Tomaž Erjavec, Matyáš Kopp, Nikola Ljubešić, Taja Kuzman, Paul Rayson, Petya Osenova, Maciej Ogrodniczuk, Çağrı Çöltekin, Danijel Koržinek, Katja Meden, Jure Skubic, Peter Rupnik, Tommaso Agnoloni, José Aires, Starkaður Barkarson, Roberto Bartolini, Núria Bel, Calzada María Pérez, Roberts Darģis, Sascha Diwersy, Maria Gavriilidou, van Ruben Heusden, Mikel Iruskieta, Neeme Kahusk, Anna Kryvenko, Noémi Ligeti-Nagy, Carmen Magariños, Martin Mölder, Costanza Navarretta, Kiril Simov, Lars Magne Tungland, Jouni Tuominen, John Vidler, Adina Ioana Vladu, Tanja Wissik, Väinö Yrjänäinen & Darja Fišer. ParlaMint II: Advancing Comparable Parliamentary Corpora Across Europe. Language Resources & Evaluation (2024). [Data set](clarin-eric.github.io/ParlaMint/)