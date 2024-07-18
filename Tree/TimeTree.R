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
TEspec <- read_csv("TEspec.csv")

#### TREE best loglik ####
tree <- phytools::read.newick('Tree50.iqtree')
tree <- read.tree('tree.txt')
treeR <- midpoint(tree)

plot(treeR, show.node.label=TRUE)

bs_tibble <- tibble(
  node=1:Nnode(treeR) + Ntip(treeR),
  bootstrap = treeR$node.label)

df <- TABLE11
tr_renamed = rename_taxa(treeR, df, key, species)

TREE <- ggtree(treeR, ladderize=TRUE) %<+% bs_tibble +
  geom_text(aes(label=bootstrap), hjust=-.25, size = 1.5) +
  geom_tiplab(geom = "text",size =1.5) +
  coord_cartesian(clip = 'off')

plot(TREE, show.node.label=TRUE)


nodes<-c(findMRCA(treeR,c("Pvins","Fgags")))
calibration<-makeChronosCalib(treeR,node=nodes,
                              age.min=27,age.max=39)

pl.tree<-chronos(treeR,calibration=calibration)

plotTree(pl.tree,direction="leftwards",
         xlim=c(40,-5),ftype="i",mar=c(4.1,1.1,0.1,1.1),
         fsize=0.8)
axis(1)
title(xlab="millions of years before present")
abline(v=seq(0,50,by=10),lty="dotted",col="grey")

is.binary.tree(pl.tree)
is.ultrametric(pl.tree)

#### Tree all ####

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
  plotTree(pl.tree,direction="leftwards",
           xlim=c(40,-5),ftype="i",mar=c(4.1,1.1,0.1,1.1),
           fsize=0.8)
  axis(1)
  title(xlab="millions of years before present")
  abline(v=seq(0,50,by=10),lty="dotted",col="grey")
  
  is.binary(pl.tree)
  is.ultrametric(pl.tree)
  file.remove('tree.txt')
  
}

thelist <- readLines("300.runtrees")

lapply(thelist, chrom_tree)


