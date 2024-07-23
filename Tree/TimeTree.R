library(phytools)
library(phangorn)
library(ggtree)
library(tibble)
library(readr)
library(ape)
library(treeio)
library(ggstance)
library(ggplot2)
library(magrittr)

setwd("~/Desktop/TE-SPECIATION")

TABLE11 <- read_csv("TABLE11.csv")

# Time tree best loglik ####

tree <- phytools::read.newick('Tree50.iqtree')
treeR <- midpoint(tree)

plot(treeR, show.node.label=TRUE)

bs_tibble <- tibble(
  node=1:Nnode(treeR) + Ntip(treeR),
  bootstrap = treeR$node.label)

TREE <- ggtree(treeR, ladderize=TRUE) %<+% bs_tibble +
  geom_text(aes(label=bootstrap), hjust=-.25, size = 1.5) +
  geom_tiplab(geom = "text",size =1.5) +
  coord_cartesian(clip = 'off')

plot(TREE, show.node.label=TRUE)


nodes<-c(findMRCA(treeR,c("Pvins","Fgags")))
calibration<-makeChronosCalib(treeR,node=nodes,
                              age.min=27,age.max=39)

pl.tree<-chronos(treeR,calibration=calibration)

df <- TABLE11
pl.tree_renamed = rename_taxa(pl.tree, df, key, species)

pdf("TimeTreeBestLoglik.pdf", width =10, height=7,)

plotTree(pl.tree_renamed,direction="leftwards",
         xlim=c(40,-5),ftype="i",mar=c(4.1,1.1,0.1,1.1),
         fsize=0.4, lwd = 1)  
axis(1)
title(xlab="Millions of years before present")
abline(v=seq(0,50,by=10),lty="dotted",col="grey")

dev.off()

is.binary.tree(pl.tree_renamed)
is.ultrametric(pl.tree_renamed)

# Tree all ####

chrom_tree <- function(t){
  fileConn<-file("tree.txt")
  writeLines(c(t), fileConn)
  close(fileConn)
  tree <- read.tree("tree.txt")
  treeR <- midpoint(tree)
  nodes<-c(findMRCA(treeR,c("Pvins","Fgags")))
  calibration<-makeChronosCalib(treeR,node=nodes,
                                age.min=27,age.max=39)
  pl.tree<-chronos(treeR,calibration=calibration)
  pl.tree_renamed = rename_taxa(pl.tree, df, key, species)
  plotTree(pl.tree_renamed,direction="leftwards",
           xlim=c(40,-5),ftype="i",mar=c(4.1,1.1,0.1,1.1),
           fsize=0.4, lwd = 1)
  axis(1)
  title(xlab="Millions of years before present")
  abline(v=seq(0,50,by=10),lty="dotted",col="grey")
  print(is.binary(pl.tree))
  print(is.ultrametric(pl.tree))
  file.remove('tree.txt')
  
}

df <- TABLE11
thelist <- readLines("500r.runtrees")

lapply(thelist, chrom_tree)


