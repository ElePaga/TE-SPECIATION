library(ape)
library(phytools)
library(ggtree)
library(treeio)
library(tibble)
library(ggplot2)
library(ggstance)
library(readr)

setwd("~/Desktop/TE-SPECIATION")

TABLE11 <- read_csv("TABLE11.csv")
TEspec <- read_csv("TEspec.csv")

#### Tree 
#tree <- phytools::read.newick('TreeFinal.iqtree')
#tree <- phytools::read.newick('TREE.iqtree')
tree <- phytools::read.newick('Tree50.iqtree')
tree_pruned <- drop.tip(tree, c('Fasea1', 'Isuba'))
treeR <- root.phylo(tree, "Pvins")

bs_tibble <- tibble(
  node=1:Nnode(treeR) + Ntip(treeR),
  bootstrap = treeR$node.label)

df <- TABLE11
tr_renamed = rename_taxa(treeR, df, key, species)

TREE <- ggtree(tr_renamed, ladderize=TRUE) %<+% bs_tibble +
  geom_text(aes(label=bootstrap), hjust=-.25, size = 1.5) +
  geom_tiplab(geom = "text",size =1.5) +
  coord_cartesian(clip = 'off')

plot(TREE, show.node.label=TRUE)

#### Tree + Stacked Barplot 
tree <- phytools::read.newick('TREE.iqtree')
tree <- phytools::read.newick('TreeFinal.iqtree')
tree_pruned <- drop.tip(tree, c('Fasea1', 'Isuba'))
treeR <- root.phylo(tree_pruned,"Pvins")

bs_tibble <- tibble(
  node=1:Nnode(treeR) + Ntip(treeR),
  bootstrap = treeR$node.label)

df <- TABLE11
df$speciesK <- paste(df$species, df$key)
tr_renamed = rename_taxa(treeR, df, key, speciesK)

tr_renamed$edge.length<-NULL

TREE <- ggtree(tr_renamed, ladderize=TRUE) %<+% bs_tibble +
  geom_text(aes(label=bootstrap), hjust=-.25, size = 1.5) +
  geom_tiplab(geom = "text",size =1.5, align=TRUE, linetype='dashed', linesize=.1)

plot(TREE, show.node.label=TRUE)

dfte <- TEspec
dfte$speciesK <- paste(dfte$specie, dfte$key)
dfteK <- dfte[c(4,5,6)]
dfteKO <- dfteK[, c(3,1,2)]

p <- facet_plot(TREE, panel = 'Stacked Barplot', data = dfteKO, 
                 geom = geom_barh, 
                 mapping = aes(x = `%Genome`, fill = TE), 
                 stat='identity' )

p_aligned <- facet_plot(TREE+xlim_tree(0.054), panel = 'Stacked Barplot', data = dfteKO, 
                        geom = geom_barh, 
                        mapping = aes(x = `%Genome`, fill = TE), 
                        stat='identity' )
facet_widths(p_aligned, widths = c(3, 2))

dfG <- df[c(9,12)]
dfGO <- dfG[,c(2,1)]

p2 <- facet_plot(p_aligned, panel='dot', data=dfGO, geom=geom_point, 
                 aes(x=genome_size), color='blue') 

ggplot2.dotplot(dfGO)
