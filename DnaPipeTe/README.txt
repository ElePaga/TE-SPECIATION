#README

The library was produced using the available Formica assemblies present on NCBI (29/05/2024)

 - Formica selysi (GCA_009859135.1)
 - Formica exsecta (GCF_003651465.1)
 - Formica aquilonia x Formica polyctena (GCA_907163055.1)
 - Formica aserva (GCA_037039905.1)
 
A starting library for each species was produced with RepeatModeler2 and the LTR structure extension.
From each library, non TE-related gene fragments were removed with ProtExcluder and automatically curated and classified with MCHelper.
Curated libraries were then merged and redundancy removed at the subfamily level (95-80-98 rule).

For each consensus sequence mined from the four ants, the source genome is reported as a 4 character code:

	- FaquxFpol: Formica aquilonia x Formica polyctena
	- Fexe: Formica exsecta 
	- Fsel: Formica selysi
	- Fase: Formica aserva