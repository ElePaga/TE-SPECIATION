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

# Tree ####

tree <- phytools::read.newick('Tree50.iqtree')
treeR <- midpoint(tree)

bs_tibble <- tibble(
  node=1:Nnode(treeR) + Ntip(treeR),
  bootstrap = treeR$node.label)

df <- TABLE11
tr_renamed = rename_taxa(treeR, df, key, species)

is.binary.tree(tr_renamed)
is.ultrametric(tr_renamed)

TREE <- ggtree(tr_renamed, ladderize=TRUE) %<+% bs_tibble +
  geom_text(aes(label=bootstrap), hjust=-.25, size = 1.5) +
  geom_tiplab(geom = "text",size =1.5) +
  coord_cartesian(clip = 'off')

plot(TREE, show.node.label=TRUE)

ggsave("BestLoglikTree.pdf")

## Tree + Stacked Barplot (aligned) ####
tree <- phytools::read.newick('Tree50.iqtree')
treeR <- midpoint(tree)

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

p_aligned <- facet_plot(TREE+xlim_tree(24.5), panel = 'Stacked Barplot', data = dfteKO, 
                        geom = geom_barh, 
                        mapping = aes(x = `%Genome`, fill = TE), 
                        stat='identity' )
facet_widths(p_aligned, widths = c(3, 2))

ggsave("TreeTEaligned.pdf")



## Tree + Stacked Barplot (dashed) ####
tree <- phytools::read.newick('Tree50.iqtree')
treeR <- midpoint(tree)

bs_tibble <- tibble(
  node=1:Nnode(treeR) + Ntip(treeR),
  bootstrap = treeR$node.label)

df <- TABLE11
df$speciesK <- paste(df$species, df$key)
tr_renamed = rename_taxa(treeR, df, key, speciesK)

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

p_aligned <- facet_plot(TREE+xlim_tree(.047), panel = 'Stacked Barplot', data = dfteKO, 
                        geom = geom_barh, 
                        mapping = aes(x = `%Genome`, fill = TE), 
                        stat='identity' )
facet_widths(p_aligned, widths = c(3, 2))

ggsave("TreeTEadashed.pdf")
